import math
import numpy as np
from build123d import *

# =========================================================
# FEATURE : Main Grill/Mesh Profile & Edge Hooks
# =========================================================
with BuildPart() as part:
    # --- Main Grill/Mesh Profile (XY Plane offset to Z = 0.8) ---
    with BuildSketch(Plane.XY.offset(0.8)):
        pts = []
        
        # Outer Castellated Boundary Generation
        pts.append((-159.84, 281.575)) # Start top-left
        
        # Top Edge (26 interlocking teeth)
        for i in range(26):
            x_start = -158.045 + i * 6.17
            pts.append((x_start, 281.575))
            pts.append((x_start, 283.5))
            pts.append((x_start + 2.0, 283.5))
            pts.append((x_start + 2.0, 281.575))
        pts.append((0.0, 281.575))
        
        # Right Edge (45 interlocking teeth)
        for i in range(45):
            y_top = 279.575 - i * 6.17
            pts.append((0.0, y_top))
            pts.append((-1.795, y_top))
            pts.append((-1.795, y_top - 4.17))
            pts.append((0.0, y_top - 4.17))
            
        # Final bridge half-tooth to corner
        pts.append((0.0, 1.925))
        pts.append((-1.795, 1.925))
        pts.append((-1.795, 0.0))
        
        # Bottom Edge (25 interlocking teeth)
        pts.append((-3.795, 0.0))
        for i in range(25):
            x_right = -3.795 - i * 6.17
            pts.append((x_right, 1.925))
            pts.append((x_right - 4.17, 1.925))
            pts.append((x_right - 4.17, 0.0))
            pts.append((x_right - 6.17, 0.0))
            
        # Final bridge gap to corner
        pts.append((-158.045, 1.925))
        pts.append((-159.84, 1.925))
        
        # Left Edge (45 interlocking teeth)
        for i in range(45):
            y_bot = 3.925 + i * 6.17
            pts.append((-159.84, y_bot))
            pts.append((-158.045, y_bot))
            pts.append((-158.045, y_bot + 4.17))
            pts.append((-159.84, y_bot + 4.17))

        # Build the entire boundary into a single closed face
        with BuildLine():
            Polyline(*pts, close=True)
        make_face()
        
        # --- Inner Subtractions (1,125 Square Mesh Cells) ---
        grid_locs = [
            (-156.045 + col * 6.17 + 2.085, 279.575 - row * 6.17 - 2.085)
            for row in range(45)
            for col in range(25)
        ]
        
        with Locations(*grid_locs):
            Rectangle(4.17, 4.17, mode=Mode.SUBTRACT)

    # Extrude the main mesh down to Z = 0.0
    extrude(amount=-0.8)

    # =========================================================
    # FEATURE 19: All 4 Edge Interlocking Hooks
    # =========================================================
    # We define custom planes for each edge.
    # U-axis (x_dir) = faces outward away from the mesh.
    # Normal (z_dir) = direction of the extrusion along the edge tooth.
    
    edge_planes = [
        # Top Edge (26 teeth) - Outward is +Y, Extrude is +X
        [Plane(origin=(-158.045 + i*6.17, 283.5, 0.0), x_dir=(0,1,0), z_dir=(1,0,0)) for i in range(26)],
        
        # Right Edge (46 teeth) - Outward is +X, Extrude is -Y
        [Plane(origin=(0.0, 281.575 - i*6.17, 0.0), x_dir=(1,0,0), z_dir=(0,-1,0)) for i in range(46)],
        
        # Bottom Edge (26 teeth) - Outward is -Y, Extrude is -X
        [Plane(origin=(-1.795 - i*6.17, 0.0, 0.0), x_dir=(0,-1,0), z_dir=(-1,0,0)) for i in range(26)],
        
        # Left Edge (46 teeth) - Outward is -X, Extrude is +Y
        [Plane(origin=(-159.84, 1.925 + i*6.17, 0.0), x_dir=(-1,0,0), z_dir=(0,1,0)) for i in range(46)]
    ]

    for planes in edge_planes:
        with BuildSketch(*planes):
            with BuildLine():
                # Define normalized local coordinates
                p1 = (0.8, -0.8)
                p2 = (1.6, -0.8)
                p3 = (0.0, 0.8)
                p4 = (0.0, 0.0)
                
                cx, cy = 0.0, -0.8
                
                # Calculate exact 45-degree midpoints for 1st-quadrant arcs
                mid_out = (cx + 1.6 * math.cos(math.pi/4), cy + 1.6 * math.sin(math.pi/4))
                mid_in  = (cx + 0.8 * math.cos(math.pi/4), cy + 0.8 * math.sin(math.pi/4))
                
                # Trace the closed loop profile
                Line(p1, p2)
                ThreePointArc(p2, mid_out, p3)  # Outer radius (1.6mm)
                Line(p3, p4)
                ThreePointArc(p4, mid_in, p1)   # Inner radius (0.8mm)
            make_face()
            
        # Extrude all localized profiles along their plane's normal by the 2.0mm tooth width
        extrude(amount=2.0)

    with BuildSketch(Plane.XZ.offset(-285.1)):

        # ── Dimensions ────────────────────────────────────────
        z_ot = -0.8;    z_it = -1.235    # outer/inner top Z
        z_ib = -15.575; z_ob = -16.514   # inner/outer bottom Z
        x_il = -158.045; x_ol = -159.445 # inner/outer left X
        x_ir = -1.795;   x_or = -0.395   # inner/outer right X
        tw = 2.0; gw = 4.17; ts = 6.17   # tooth width, gap, period

        # ── Build castellated frame vertices ──────────────────
        pts = []

        # TOP EDGE: going right, 26 teeth
        x = x_il
        for i in range(26):
            if i == 0:
                pts.append((x, z_ot))           # first point
            pts.append((x + tw, z_ot))          # tooth right end
            pts.append((x + tw, z_it))          # step inner
            if i < 25:
                pts.append((x + ts, z_it))      # gap end
                pts.append((x + ts, z_ot))      # step outer
            x += ts
        # now at (x_ir, z_it)

        # RIGHT EDGE: going down, 3 teeth
        z = z_it
        for i in range(3):
            pts.append((x_or, z))               # step out
            pts.append((x_or, z - tw))          # tooth down
            pts.append((x_ir, z - tw))          # step back
            z -= tw
            if i < 2:
                pts.append((x_ir, z - gw))      # gap
                z -= gw
        # now at (x_ir, z_ib)

        # BOTTOM EDGE: going left, 26 teeth
        pts.append((x_ir, z_ob))               # step to outer bottom
        x = x_ir
        for i in range(26):
            pts.append((x - tw, z_ob))          # tooth left end
            pts.append((x - tw, z_ib))          # step inner
            if i < 25:
                pts.append((x - ts, z_ib))      # gap end
                pts.append((x - ts, z_ob))      # step outer
            x -= ts
        # now at (x_il, z_ib)

        # LEFT EDGE: going up, 3 teeth
        z = z_ib
        for i in range(3):
            pts.append((x_ol, z))               # step out
            pts.append((x_ol, z + tw))          # tooth up
            pts.append((x_il, z + tw))          # step back
            z += tw
            if i < 2:
                pts.append((x_il, z + gw))      # gap
                z += gw
        pts.append((x_il, z_ot))               # close to first point
        # now at (x_il, z_ot) = first point ✓

        with BuildLine():
            Polyline(*pts, close=False)
        make_face()

        # ── Subtract 50 rectangles (25 per row) ───────────────
        # Row 1: Z centre = -11.49  (Z span -13.575 to -9.405)
        # Row 2: Z centre = -5.32   (Z span  -7.405 to -3.235)
        x_centers = [-153.96 + i * ts for i in range(25)]
        row1 = [(x, -11.49) for x in x_centers]
        row2 = [(x,  -5.32) for x in x_centers]

        with Locations(*(row1 + row2)):
            Rectangle(4.17, 4.17, mode=Mode.SUBTRACT)

    extrude(amount=0.8)

# ── Helper: generates pts only (no build123d context) ─────
    def get_hook_pts():
        y_or = 282.975; y_ir = 281.575
        y_il = 1.925;   y_ol = 0.525
        z_ot = -0.8;    z_it = -1.365
        z_ib = -15.705; z_ob = -16.514
        tw = 2.0; gw = 4.17; ts = 6.17

        pts = []
        pts.append((y_il, z_ob))          # start — close=True will add closing step back here

        y = y_il                           # BOTTOM going right
        for i in range(46):
            pts += [(y+tw, z_ob), (y+tw, z_ib)]
            if i < 45:
                pts += [(y+ts, z_ib), (y+ts, z_ob)]
            y += ts

        pts.append((y_or, z_ib))          # BOTTOM→RIGHT

        z = z_ib                           # RIGHT going up
        for i in range(3):
            pts += [(y_or, z+tw), (y_ir, z+tw)]
            z += tw
            if i < 2:
                pts.append((y_ir, z+gw));  z += gw

        pts.append((y_ir, z_ot))          # RIGHT→TOP

        y = y_ir                           # TOP going left
        for i in range(46):
            pts += [(y-tw, z_ot), (y-tw, z_it)]
            if i < 45:
                pts += [(y-ts, z_it), (y-ts, z_ot)]
            y -= ts

        pts.append((y_ol, z_it))          # TOP→LEFT

        z = z_it                           # LEFT going down
        for i in range(3):
            pts += [(y_ol, z-tw), (y_il, z-tw)]
            z -= tw
            if i < 2:
                pts.append((y_il, z-gw));  z -= gw
        # ends at (y_il, z_ib) → close=True adds step back to (y_il, z_ob) ✓

        return pts

    def get_rect_locs():
        ts = 6.17
        y_cents = [279.575 - i*ts - 2.085 for i in range(45)]
        return [(yc, -11.62) for yc in y_cents] + [(yc, -5.45) for yc in y_cents]

    _hook_pts  = get_hook_pts()
    _rect_locs = get_rect_locs()

    # ── Hook frame 1: X=1.6 → X=0 ─────────────────────────────
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            Polyline(*_hook_pts, close=True)   # close=True avoids duplicate-point issue
        make_face()
        with Locations(*_rect_locs):
            Rectangle(4.17, 4.17, mode=Mode.SUBTRACT)
    extrude(amount=-0.8)

    # ── Hook frame 2: X=−161.44 → X=−160 (mirror of frame 1) ──
    with BuildSketch(Plane.YZ.offset(-161.44)):
        with BuildLine():
            Polyline(*_hook_pts, close=True)
        make_face()
        with Locations(*_rect_locs):
            Rectangle(4.17, 4.17, mode=Mode.SUBTRACT)
    extrude(amount=0.8)

    with BuildSketch(Plane.XZ.offset(0.8)):

        z_ot=-0.8; z_it=-1.235; z_ib=-15.575; z_ob=-16.514
        x_il=-158.045; x_ol=-159.445; x_ir=-1.795; x_or=-0.395
        tw=2.0; gw=4.17; ts=6.17

        pts = []

        # ── TOP EDGE: going right, 26 teeth (0.435mm deep) ────
        x = x_il
        for i in range(26):
            if i == 0: pts.append((x, z_ot))
            pts.append((x+tw, z_ot))
            pts.append((x+tw, z_it))
            if i < 25:
                pts.append((x+ts, z_it))
                pts.append((x+ts, z_ot))
            x += ts
        # ends at (x_ir=-1.795, z_it=-1.235)

        # ── RIGHT EDGE: going down, 3 teeth (1.4mm deep) ──────
        z = z_it
        for i in range(3):
            pts.append((x_or, z))
            pts.append((x_or, z-tw))
            pts.append((x_ir, z-tw))
            z -= tw
            if i < 2:
                pts.append((x_ir, z-gw)); z -= gw
        # ends at (x_ir=-1.795, z_ib=-15.575)

        # ── BOTTOM EDGE ────────────────────────────────────────
        # Step to outer bottom
        pts.append((x_ir, z_ob))                  # (-1.795,-16.514)

        # 16 regular teeth going left (-1.795 → -96.345, 0.939mm deep)
        x = x_ir
        for i in range(16):
            pts.append((x-tw, z_ob))               # tooth left end
            pts.append((x-tw, z_ib))               # step inner
            if i < 15:
                pts.append((x-ts, z_ib))           # gap
                pts.append((x-ts, z_ob))           # step outer
            x -= ts
        # ends at (-96.345, z_ib=-15.575)

        # Notch RIGHT WALL (1mm wide, 2mm tall, going left then up)
        pts.append((-97.345, z_ib))                # step 1mm left to outer
        pts.append((-97.345, z_ib+tw))             # tooth UP 2mm → (-97.345,-13.575)
        pts.append((-96.345, z_ib+tw))             # step 1mm right back
        pts.append((-96.345, -9.405))              # gap UP 4.17mm

        # 3 inner notch teeth going left (0.859mm deep, at Z=-9.405)
        notch_tw = 2.0; notch_d = 0.859
        for x_start in [-96.345, -102.515, -108.685]:
            pts.append((x_start - gw, -9.405))           # gap left 4.17mm
            pts.append((x_start - gw, -9.405-notch_d))   # step outer (down)
            pts.append((x_start - gw - notch_tw, -9.405-notch_d))  # tooth left
            pts.append((x_start - gw - notch_tw, -9.405))          # step inner (up)
        # last: arrives at (-114.855,-9.405). Gap to left wall:
        pts.append((-119.025, -9.405))             # gap left 4.17mm to left wall

        # Notch LEFT WALL (1mm wide, 2mm tall, going down then right)
        pts.append((-119.025, -13.575))            # gap DOWN 4.17mm (inner left wall)
        pts.append((-118.025, -13.575))            # step 1mm right to outer
        pts.append((-118.025, z_ib))               # tooth DOWN 2mm → (-118.025,-15.575)
        pts.append((-119.025, z_ib))               # step 1mm left back to inner
        pts.append((-119.025, z_ob))               # step DOWN to outer bottom

        # 7 regular teeth going left (-119.025 → -158.045, 0.939mm deep)
        x = -119.025
        for i in range(7):
            pts.append((x-tw, z_ob))
            pts.append((x-tw, z_ib))
            if i < 6:
                pts.append((x-ts, z_ib))
                pts.append((x-ts, z_ob))
            x -= ts
        # ends at (-158.045, z_ib=-15.575)

        # ── LEFT EDGE: going up, 3 teeth (1.4mm deep) ─────────
        z = z_ib
        for i in range(3):
            pts.append((x_ol, z))
            pts.append((x_ol, z+tw))
            pts.append((x_il, z+tw))
            z += tw
            if i < 2:
                pts.append((x_il, z+gw)); z += gw
        pts.append((x_il, z_ot))                  # close to first point

        with BuildLine():
            Polyline(*pts, close=False)
        make_face()

        x_all = [-153.96 + i*ts for i in range(25)]
        row1 = [(x, -11.49) for i,x in enumerate(x_all) if i not in (6,7,8,9)]
        row2 = [(x, -5.32) for x in x_all]
        with Locations(*(row1+row2)):
            Rectangle(4.17, 4.17, mode=Mode.SUBTRACT)
    extrude(amount=0.8)

if __name__ == "__main__":
    export_stl(part.part, "output_Mesh Update v9.stl")
    export_step(part.part, "output_Mesh Update v9.step")
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass
