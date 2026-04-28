from build123d import *
import numpy as np

def get_mid(p1, p2, centre, r, flip=False):
    """Calculates the exact midpoint of a minor arc given start, end, center, and radius."""
    c = np.array(centre)
    a = np.array(p1)
    b = np.array(p2)
    v1 = a - c
    v2 = b - c
    mid_dir = v1 + v2
    norm = np.linalg.norm(mid_dir)
    
    if norm < 1e-10:
        # Handling 180-degree arcs where vectors cancel out
        perp = np.array([-v1[1], v1[0]])
        mid_dir = perp if not flip else -perp
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
    else:
        mid_dir = mid_dir / norm
        if flip:
            mid_dir = -mid_dir
            
    return tuple(c + mid_dir * r)

# =========================================================
# PART: PN-000518 v27
# =========================================================
with BuildPart() as part:
    
    # ---------------------------------------------------------
    # FEATURE 1: Main Profile Sketch (XY Plane)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY) as main_sketch:
        
        # --- Outer Boundary ---
        with BuildLine() as outer:
            p1  = (-37.5, 193.35)
            p2  = (36.0, 193.35)
            p3  = (36.8, 193.35)
            p4  = (36.8, 4.0)
            p5  = (36.8, 3.2)
            p6  = (0.0, 3.2)
            p7  = (0.0, 4.6)
            p8  = (3.0, 7.6)
            p9  = (4.0, 7.6)
            p10 = (4.0, 9.2)
            p11 = (3.2, 9.2)
            p12 = (3.2, 171.55)
            p13 = (4.0, 171.55)
            p14 = (4.0, 173.15)
            p15 = (2.159, 173.15)
            p16 = (-0.647, 175.088)
            p17 = (-10.0, 181.55)
            p18 = (-27.5, 181.55)
            p19 = (-37.5, 191.55)

            Line(p1, p2)
            Line(p2, p3)
            Line(p3, p4)
            Line(p4, p5)
            Line(p5, p6)
            Line(p6, p7)
            ThreePointArc(p7, get_mid(p7, p8, (3.0, 4.6), 3.0), p8)
            Line(p8, p9)
            Line(p9, p10)
            Line(p10, p11)
            Line(p11, p12)
            Line(p12, p13)
            Line(p13, p14)
            Line(p14, p15)
            ThreePointArc(p15, get_mid(p15, p16, (2.159, 176.15), 3.0), p16)
            ThreePointArc(p16, get_mid(p16, p17, (-10.0, 171.55), 10.0), p17)
            Line(p17, p18)
            ThreePointArc(p18, get_mid(p18, p19, (-27.5, 191.55), 10.0), p19)
            Line(p19, p1)
        make_face()

        # --- Inner Subtraction Profile ---
        with BuildLine(mode=Mode.PRIVATE) as inner:
            s1 = (22.718, 171.69)
            s2 = (14.082, 171.69)
            s3 = (15.45, 169.173)
            s4 = (15.45, 86.357)
            s5 = (21.35, 86.357)
            s6 = (21.35, 169.173)

            ThreePointArc(s1, get_mid(s1, s2, (18.4, 178.35), 7.937, flip=True), s2)
            ThreePointArc(s2, get_mid(s2, s3, (12.45, 169.173), 3.0), s3)
            Line(s3, s4)
            ThreePointArc(s4, get_mid(s4, s5, (18.4, 86.357), 2.95), s5)
            Line(s5, s6)
            ThreePointArc(s6, get_mid(s6, s1, (24.35, 169.173), 3.0), s1)
        make_face(inner.edges(), mode=Mode.SUBTRACT)

    extrude(amount=1.6)
# =========================================================
    # FEATURE 2: Inner Lip (XZ Plane offset to Y = 9.2)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-9.2)):
        with BuildLine():
            p1 = (1.6, -1.6)
            p2 = (3.2, 0.0)
            p3 = (3.2, 1.6)
            p4 = (0.0, -1.6)
            center = (3.2, -1.6)

            ThreePointArc(p1, get_mid(p1, p2, center, 1.6), p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, center, 3.2), p4)
            Line(p4, p1)
        make_face()
    extrude(amount=-162.35)

# =========================================================
    # FEATURE 3: Left Inner Side Rib (YZ Plane offset to X = 1.6)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            p1 = (171.55, -1.6)
            p2 = (9.2, -1.6)
            p3 = (9.2, -6.8)
            p4 = (14.2, -11.8)
            p5 = (166.55, -11.8)
            p6 = (171.55, -6.8)

            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, (14.2, -6.8), 5.0), p4)
            Line(p4, p5)
            ThreePointArc(p5, get_mid(p5, p6, (166.55, -6.8), 5.0), p6)
            Line(p6, p1)
        make_face()
    extrude(amount=-1.6)

# =========================================================
    # FEATURE 4: Top Rear Mounting Lip (YZ Plane offset to X = -37.5)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(-37.5)):
        with BuildLine():
            p1 = (194.95, -1.6)
            p2 = (193.35, 0.0)
            p3 = (193.35, 1.6)
            p4 = (196.55, -1.6)
            center = (193.35, -1.6)

            Line(p1, p4)
            ThreePointArc(p4, get_mid(p4, p3, center, 3.2), p3)
            Line(p3, p2)
            ThreePointArc(p2, get_mid(p2, p1, center, 1.6), p1)
        make_face()
    extrude(amount=73.5)

# =========================================================
    # FEATURE 5: Rear Vertical Rib (XZ Plane offset to Y = 194.95)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-194.95)):
        with BuildLine():
            p1 = (36.0, -1.6)
            p2 = (36.0, -14.4)
            p3 = (31.0, -19.4)
            p4 = (-32.5, -19.4)
            p5 = (-37.5, -14.4)
            p6 = (-37.5, -1.6)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (31.0, -14.4), 5.0), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (-32.5, -14.4), 5.0), p5)
            Line(p5, p6)
            Line(p6, p1)
        make_face()
        
        with Locations((23.25, -16.113), (-33.75, -16.113)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)
    extrude(amount=-1.6)

# =========================================================
    # FEATURE 6: Right Inner Side Rib (XZ Plane offset to Y = 4.0)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-4.0)):
        with BuildLine():
            p1 = (36.8, 0.0)
            p2 = (36.8, 1.6)
            p3 = (40.0, -1.6)
            p4 = (38.4, -1.6)
            center = (36.8, -1.6)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
    extrude(amount=-189.35)

# =========================================================
    # FEATURE 7: Right Side Internal Rib (YZ Plane offset to X = 38.4)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(38.4)):
        with BuildLine():
            p1 = (193.35, -1.6)
            p2 = (193.35, -15.4)
            p3 = (190.35, -18.4)
            p4 = (7.0, -18.4)
            p5 = (4.0, -15.4)
            p6 = (4.0, -1.6)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (190.35, -15.4), 3.0), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (7.0, -15.4), 3.0), p5)
            Line(p5, p6)
            Line(p6, p1)
        make_face()
        
        with Locations((155.049, -7.337), (167.049, -7.337)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
    extrude(amount=1.6)

# =========================================================
    # FEATURE 8: Bottom Forward Mounting Lip (YZ Plane offset to X = 0.0)
    # =========================================================
    with BuildSketch(Plane.YZ):
        with BuildLine():
            p1 = (0.0, -1.6)
            p2 = (1.6, -1.6)
            p3 = (3.2, 0.0)
            p4 = (3.2, 1.6)
            center = (3.2, -1.6)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 1.6), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 3.2), p1)
        make_face()
    extrude(amount=36.8)

# =========================================================
    # FEATURE 9: Bottom Forward Internal Rib (XZ Plane offset to Y = 1.6)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-1.6)):
        with BuildLine():
            p1 = (36.8, -1.6)
            p2 = (36.8, -13.4)
            p3 = (31.8, -18.4)
            p4 = (5.0, -18.4)
            p5 = (0.0, -13.4)
            p6 = (0.0, -1.6)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (31.8, -13.4), 5.0), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (5.0, -13.4), 5.0), p5)
            Line(p5, p6)
            Line(p6, p1)
        make_face()
        
        # --- Internal Subtractions ---
        with Locations((5.9, -10.5), (30.9, -10.5)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
        with Locations((18.4, -10.5)):
            Circle(radius=2.39, mode=Mode.SUBTRACT)
            
    extrude(amount=1.6)

if __name__ == "__main__":
    export_stl(part.part, "output_PN-000518_v27.stl")
    
    try:
        from ocp_vscode import show_all
        show_all()
    except ImportError:
        pass