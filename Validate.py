"""
validate_thelio.py — Volumetric & Symmetric-Difference Comparison
Compares original STEP files against rebuilt output STL files for Thelio parts.

INSTALL (run once):
    pip3 install trimesh manifold3d numpy build123d

RUN:
    python3 validate_thelio.py
"""

import os
import sys
import struct
import tempfile
import numpy as np

# ─── trimesh ──────────────────────────────────────────────────
try:
    import trimesh
    HAS_TRIMESH = True
except ImportError:
    HAS_TRIMESH = False
    print("[WARNING] trimesh not found. Run: pip3 install trimesh manifold3d")

# ─── STEP loader: try cadquery first, then build123d ──────────
HAS_CQ = HAS_B123 = False
try:
    import cadquery as cq
    HAS_CQ = True
except ImportError:
    pass

if not HAS_CQ:
    try:
        import build123d as b123
        HAS_B123 = True
    except ImportError:
        pass

if not HAS_CQ and not HAS_B123:
    print("[WARNING] No STEP loader found.")
    print("  Install one:  pip3 install cadquery   OR   pip3 install build123d")


# ══════════════════════════════════════════════════════════════
#  STEP → temp STL conversion
# ══════════════════════════════════════════════════════════════

def step_to_temp_stl(step_path: str) -> str | None:
    tmp = tempfile.NamedTemporaryFile(suffix=".stl", delete=False)
    tmp.close()
    tmp_path = tmp.name

    if HAS_CQ:
        try:
            shape = cq.importers.importStep(step_path)
            cq.exporters.export(shape, tmp_path)
            return tmp_path
        except Exception as e:
            print(f"    [cadquery error] {e}")

    if HAS_B123:
        try:
            from build123d import import_step, export_stl, Mesher
            shape = import_step(step_path)
            try:
                export_stl(shape, tmp_path)
            except TypeError:
                m = Mesher()
                m.add_shape(shape)
                m.write(tmp_path)
            return tmp_path
        except Exception as e:
            print(f"    [build123d error] {e}")

    os.unlink(tmp_path)
    return None


# ══════════════════════════════════════════════════════════════
#  Raw STL helpers
# ══════════════════════════════════════════════════════════════

def _is_binary_stl(path):
    with open(path, 'rb') as f:
        hdr = f.read(80)
    return not (hdr[:5] == b'solid' and hdr[5:6] in (b' ', b'\n', b'\r'))

def _get_triangles(path):
    tris = []
    if _is_binary_stl(path):
        with open(path, 'rb') as f:
            f.read(80)
            n = struct.unpack('<I', f.read(4))[0]
            for _ in range(n):
                d = struct.unpack('<12fH', f.read(50))
                tris.append([d[3:6], d[6:9], d[9:12]])
    else:
        verts = []
        with open(path, 'r', errors='ignore') as f:
            for line in f:
                s = line.strip()
                if s.startswith('vertex'):
                    p = s.split()
                    verts.append([float(p[1]), float(p[2]), float(p[3])])
        for i in range(0, len(verts) - 2, 3):
            tris.append([verts[i], verts[i+1], verts[i+2]])
    return np.array(tris, dtype=np.float64)

def volume_from_stl(path):
    total = 0.0
    for tri in _get_triangles(path):
        v1, v2, v3 = tri
        total += np.dot(v1, np.cross(v2, v3)) / 6.0
    return abs(total)


# ══════════════════════════════════════════════════════════════
#  Orientation search  (all 24 proper axis-aligned rotations)
# ══════════════════════════════════════════════════════════════

def _all_24_rotations():
    from itertools import permutations, product
    rots = []
    for perm in permutations([0, 1, 2]):
        for signs in product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i, j in enumerate(perm):
                R[i, j] = signs[i]
            if round(np.linalg.det(R)) == 1:
                rots.append(R)
    return rots

ALL_24 = _all_24_rotations()

def _centre(pts):
    return pts - (pts.min(axis=0) + pts.max(axis=0)) / 2.0

def _best_rotation(pts_a_raw, pts_b_raw, subsample=1000):
    rng = np.random.default_rng(0)
    pa  = _centre(pts_a_raw)
    pb  = _centre(pts_b_raw)
    ia  = rng.choice(len(pa), min(subsample, len(pa)),  replace=False)
    ib  = rng.choice(len(pb), min(subsample, len(pb)),  replace=False)
    pa_s, pb_s = pa[ia], pb[ib]
    best_d, best_R = np.inf, np.eye(3)
    for R in ALL_24:
        pb_rot = (R @ pb_s.T).T
        diff   = pa_s[:, None, :] - pb_rot[None, :, :]
        d      = np.sqrt((diff**2).sum(axis=2)).min(axis=1).mean()
        if d < best_d:
            best_d, best_R = d, R
    return best_R


# ══════════════════════════════════════════════════════════════
#  Symmetric difference
# ══════════════════════════════════════════════════════════════

def symmetric_difference(stl_a: str, stl_b: str):
    if not HAS_TRIMESH:
        return None, None, "trimesh not installed"
    try:
        a = trimesh.load(stl_a, force='mesh')
        b = trimesh.load(stl_b, force='mesh')

        a.apply_translation(-a.bounding_box.center_mass)
        b.apply_translation(-b.bounding_box.center_mass)

        best_R = _best_rotation(np.array(a.vertices), np.array(b.vertices))
        T = np.eye(4); T[:3, :3] = best_R
        b.apply_transform(T)

        trimesh.repair.fill_holes(a)
        trimesh.repair.fill_holes(b)

        if not a.is_watertight or not b.is_watertight:
            return None, None, "open-shell mesh (boolean ops unavailable)"

        a_minus_b = trimesh.boolean.difference([a, b], engine='manifold')
        b_minus_a = trimesh.boolean.difference([b, a], engine='manifold')

        v_amb = abs(a_minus_b.volume) if a_minus_b is not None and len(a_minus_b.faces) > 0 else 0.0
        v_bma = abs(b_minus_a.volume) if b_minus_a is not None and len(b_minus_a.faces) > 0 else 0.0

        return v_amb + v_bma, abs(a.volume), None
    except Exception as e:
        return None, None, str(e)


# ══════════════════════════════════════════════════════════════
#  Core comparison
# ══════════════════════════════════════════════════════════════

def compare(part_name: str, orig_step: str, output_stl: str, results: list):
    rec = {"name": part_name, "vol_diff": None, "vol_pct": None,
           "sym_diff": None, "sym_pct": None, "note": ""}

    if not os.path.exists(output_stl):
        rec["note"] = "output STL not found"
        results.append(rec)
        return

    if not os.path.exists(orig_step):
        rec["note"] = "original STEP not found"
        results.append(rec)
        return

    tmp_stl = step_to_temp_stl(orig_step)
    if tmp_stl is None:
        rec["note"] = "STEP conversion failed"
        results.append(rec)
        return

    try:
        v_orig    = volume_from_stl(tmp_stl)
        v_out     = volume_from_stl(output_stl)
        vol_diff  = abs(v_orig - v_out)
        vol_pct   = vol_diff / v_orig * 100 if v_orig > 0 else 0.0

        rec["vol_diff"] = vol_diff
        rec["vol_pct"]  = vol_pct

        sym_diff, orig_vol, err = symmetric_difference(tmp_stl, output_stl)
        if sym_diff is not None:
            sym_pct = sym_diff / orig_vol * 100 if orig_vol and orig_vol > 0 else 0.0
            rec["sym_diff"] = sym_diff
            rec["sym_pct"]  = sym_pct
        else:
            rec["note"] = err or "sym-diff unavailable"

    finally:
        try:
            os.unlink(tmp_stl)
        except OSError:
            pass

    results.append(rec)


# ══════════════════════════════════════════════════════════════
#  PARTS REGISTRY  (30 parts)
# ══════════════════════════════════════════════════════════════

BASE_ORIG  = "/Users/softage/Desktop/Thelio/Original"
OUTPUT_DIR = "/Users/softage/Desktop/Thelio"

# (display_name, original_step_filename, output_stl_filename)
PARTS = [
    # ── Mesh / bracket parts ──────────────────────────────────
    ("Mesh Bracket-small v11",
     "Mesh Bracket-small v11.step",
     "output_Mesh Bracket-small_v11.stl"),

    ("Mesh Side Mount BKT v2",
     "Mesh Side Mount BKT v2.step",
     "output_Mesh Side Mount BKT v2.stl"),

    ("Mesh Update v9",
     "Mesh Update v9.step",
     "output_Mesh Update v9.stl"),

    # ── PN-000518 ─────────────────────────────────────────────
    ("PN-000518 v27",
     "PN-000518 v27.step",
     "output_PN-000518_v27.stl"),

    # ── PN-000634 … PN-000640 ─────────────────────────────────
    ("PN-000634 v11",
     "PN-000634 v11.step",
     "output_PN-000634_v11.stl"),

    ("PN-000635 v20",
     "PN-000635 v20.step",
     "output_PN-000635_v20.stl"),

    ("PN-000636 v18",
     "PN-000636 v18.step",
     "output_PN-000636_v18.stl"),

    ("PN-000637 v8",
     "PN-000637 v8.step",
     "output_PN-000637_v8.stl"),

    ("PN-000638 v5",
     "PN-000638 v5.step",
     "output_PN-000638_v5.stl"),

    ("PN-000639 v6",
     "PN-000639 v6.step",
     "output_PN-000639_v6.stl"),

    ("PN-000640 v21",
     "PN-000640 v21.step",
     "output_PN-000640_v21.stl"),

    # ── PN-000641 … PN-000652 ─────────────────────────────────
    ("PN-000641 v10",
     "PN-000641 v10.step",
     "output_PN-000641_v10.stl"),

    ("PN-000643 v36",
     "PN-000643 v36.step",
     "output_PN-000643_v36.stl"),

    ("PN-000644 v54",
     "PN-000644 v54.step",
     "output_PN-000644_v54.stl"),

    ("PN-000645 v63",
     "PN-000645 v63.step",
     "output_PN-000645_v63.stl"),

    ("PN-000646 v10",
     "PN-000646 v10.step",
     "output_PN-000646_v10.stl"),

    ("PN-000647 v22",
     "PN-000647 v22.step",
     "output_PN-000647_v22.stl"),

    ("PN-000648 v17",
     "PN-000648 v17.step",
     "output_PN-000648_v17.stl"),

    ("PN-000650 v12",
     "PN-000650 v12.step",
     "output_PN-000650_v12.stl"),

    ("PN-000651 v13",
     "PN-000651 v13.step",
     "output_PN-000651_v13.stl"),

    ("PN-000652 v17",
     "PN-000652 v17.step",
     "output_PN-000652_v17.stl"),

    # ── PN-000662 … PN-000666 ─────────────────────────────────
    ("PN-000662 v14",
     "PN-000662 v14.step",
     "output_PN-000662_v14.stl"),

    ("PN-000663 v14",
     "PN-000663 v14.step",
     "output_PN-000663_v14.stl"),

    ("PN-000664 v2",
     "PN-000664 v2.step",
     "output_PN-000664_v2.stl"),

    ("PN-000665 v6",
     "PN-000665 v6.step",
     "output_PN-000665_v6.stl"),

    ("PN-000666 v7",
     "PN-000666 v7.step",
     "output_PN-000666_v7.stl"),

    # ── PN-000668 / PN-000669 ─────────────────────────────────
    ("PN-000668 v7",
     "PN_000668 v7.step",
     "output_PN_000668_v7.stl"),

    ("PN-000669 v9",
     "PN_000669 v9.step",
     "output_PN_000669_v9.stl"),

    # ── Miscellaneous ─────────────────────────────────────────
    ("Top BKT Mag Guide Slim v6",
     "Top BKT Mag Guide_Slim v6.step",
     "output_Top BKT Mag Guide_Slim v6.stl"),

    ("V3 120mm Fan Plate v7",
     "V3 120 mm Fan Mounting Plate v7.step",
     "output_V3 120mm Fan Mounting Plate v7.stl"),
]


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print()
    print("╔" + "═"*82 + "╗")
    print("║  Thelio Parts — Validation Report (Volume & Symmetric Difference)" + " "*15 + "║")
    print("╚" + "═"*82 + "╝")
    print(f"  Originals   : {BASE_ORIG}")
    print(f"  Outputs     : {OUTPUT_DIR}")
    print(f"  Parts       : {len(PARTS)}")
    print(f"  STEP loader : {'cadquery' if HAS_CQ else 'build123d' if HAS_B123 else '✗ NONE'}")
    print(f"  trimesh     : {'✓' if HAS_TRIMESH else '✗ not installed'}")
    print()

    results = []

    for display_name, orig_filename, output_filename in PARTS:
        orig_step  = os.path.join(BASE_ORIG,  orig_filename)
        output_stl = os.path.join(OUTPUT_DIR, output_filename)

        print(f"  Processing: {display_name} ...", end="", flush=True)
        compare(display_name, orig_step, output_stl, results)
        last   = results[-1]
        status = "OK" if last["vol_diff"] is not None else f"SKIP ({last['note']})"
        print(f"\r  [{status:<44}] {display_name}")

    # ── results table ─────────────────────────────────────────
    COL = [24, 16, 10, 16, 10]
    W   = sum(COL) + 4 * 2 + 2   # total inner width

    print()
    print("┌" + "─"*W + "┐")
    print(f"│  {'Part Name':<{COL[0]}}  {'Vol Diff (mm³)':>{COL[1]}}  "
          f"{'Vol (%)':>{COL[2]}}  {'Sym Diff (mm³)':>{COL[3]}}  {'Sym (%)':>{COL[4]}}  │")
    print("├" + "─"*W + "┤")

    all_ok = True
    for r in results:
        name = r["name"][:COL[0]]

        if r["vol_diff"] is not None:
            vd = f"{r['vol_diff']:>{COL[1]}.3f}"
            vp = f"{r['vol_pct']:>{COL[2]}.2f}%"
        else:
            vd = f"{'N/A':>{COL[1]}}"
            vp = f"{'N/A':>{COL[2]}}"
            all_ok = False

        if r["sym_diff"] is not None:
            sd = f"{r['sym_diff']:>{COL[3]}.3f}"
            sp = f"{r['sym_pct']:>{COL[4]}.2f}%"
        else:
            sd = f"{'—':>{COL[3]}}"
            sp = f"{'—':>{COL[4]}}"

        note_str = f"  [{r['note']}]" if r["note"] and r["vol_diff"] is None else ""
        print(f"│  {name:<{COL[0]}}  {vd}  {vp}  {sd}  {sp}  │{note_str}")

    print("└" + "─"*W + "┘")

    # ── summary ───────────────────────────────────────────────
    print()
    processed = sum(1 for r in results if r["vol_diff"] is not None)
    skipped   = len(results) - processed
    print(f"  Summary : {processed}/{len(results)} parts processed, {skipped} skipped")
    print()
    print("  Notes:")
    print("  • Vol Diff  = |volume(original) − volume(output)|  in mm³")
    print("  • Vol (%)   = Vol Diff as % of original volume")
    print("  • Sym Diff  = (A−B) ∪ (B−A) boolean volume in mm³  [requires watertight meshes]")
    print("  • Sym (%)   = Sym Diff as % of original volume")
    print("  • '—' in Sym columns = open-shell mesh or trimesh unavailable")
    print()
    print(f"  {'Part Name':<24}  {'Original STEP':<36}  {'Output STL'}")
    print(f"  {'─'*24}  {'─'*36}  {'─'*36}")
    for display_name, orig_filename, output_filename in PARTS:
        print(f"  {display_name:<24}  {orig_filename:<36}  {output_filename}")
    print()