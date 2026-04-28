from build123d import *
from ocp_vscode import show
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
        perp = np.array([-v1[1], v1[0]])
        mid_dir = perp if not flip else -perp
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
    else:
        mid_dir = mid_dir / norm
        if flip:
            mid_dir = -mid_dir
            
    return tuple(c + mid_dir * r)

with BuildPart() as part:
    # ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = 1.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):
        
        # =========================================================
        # 1. Outer Boundary
        # =========================================================
        with BuildLine(mode=Mode.PRIVATE) as outer:
            # 32 specific boundary vertices mapped to 2D sketch plane (X, Z)
            o_p1 = (350.1, 3.2)
            o_p2 = (350.1, 9.27)
            o_p3 = (349.3, 10.25)
            o_p4 = (349.3, 14.25)
            o_p5 = (350.1, 15.23)
            o_p6 = (350.1, 142.47)
            o_p7 = (349.3, 143.45)
            o_p8 = (349.3, 147.45)
            o_p9 = (350.1, 148.43)
            o_p10 = (350.1, 154.5)
            o_p11 = (191.9, 154.5)
            o_p12 = (191.9, 153.75)
            o_p13 = (191.65, 153.5)
            o_p14 = (166.15, 153.5)
            o_p15 = (165.9, 153.75)
            o_p16 = (165.9, 154.5)
            o_p17 = (5.2, 154.5)
            o_p18 = (5.2, 148.43)
            o_p19 = (6.0, 147.45)
            o_p20 = (6.0, 143.45)
            o_p21 = (5.2, 142.47)
            o_p22 = (5.2, 15.23)
            o_p23 = (6.0, 14.25)
            o_p24 = (6.0, 10.25)
            o_p25 = (5.2, 9.27)
            o_p26 = (5.2, 3.2)
            o_p27 = (165.9, 3.2)
            o_p28 = (165.9, 3.95)
            o_p29 = (166.15, 4.2)
            o_p30 = (191.65, 4.2)
            o_p31 = (191.9, 3.95)
            o_p32 = (191.9, 3.2)

            Line(o_p1, o_p2)
            ThreePointArc(o_p2, get_mid(o_p2, o_p3, (350.3, 10.25), 1.0), o_p3)
            Line(o_p3, o_p4)
            ThreePointArc(o_p4, get_mid(o_p4, o_p5, (350.3, 14.25), 1.0), o_p5)
            Line(o_p5, o_p6)
            ThreePointArc(o_p6, get_mid(o_p6, o_p7, (350.3, 143.45), 1.0), o_p7)
            Line(o_p7, o_p8)
            ThreePointArc(o_p8, get_mid(o_p8, o_p9, (350.3, 147.45), 1.0), o_p9)
            Line(o_p9, o_p10)
            Line(o_p10, o_p11)
            Line(o_p11, o_p12)
            ThreePointArc(o_p12, get_mid(o_p12, o_p13, (191.65, 153.75), 0.25), o_p13)
            Line(o_p13, o_p14)
            ThreePointArc(o_p14, get_mid(o_p14, o_p15, (166.15, 153.75), 0.25), o_p15)
            Line(o_p15, o_p16)
            Line(o_p16, o_p17)
            Line(o_p17, o_p18)
            ThreePointArc(o_p18, get_mid(o_p18, o_p19, (5.0, 147.45), 1.0), o_p19)
            Line(o_p19, o_p20)
            ThreePointArc(o_p20, get_mid(o_p20, o_p21, (5.0, 143.45), 1.0), o_p21)
            Line(o_p21, o_p22)
            ThreePointArc(o_p22, get_mid(o_p22, o_p23, (5.0, 14.25), 1.0), o_p23)
            Line(o_p23, o_p24)
            ThreePointArc(o_p24, get_mid(o_p24, o_p25, (5.0, 10.25), 1.0), o_p25)
            Line(o_p25, o_p26)
            Line(o_p26, o_p27)
            Line(o_p27, o_p28)
            ThreePointArc(o_p28, get_mid(o_p28, o_p29, (166.15, 3.95), 0.25), o_p29)
            Line(o_p29, o_p30)
            ThreePointArc(o_p30, get_mid(o_p30, o_p31, (191.65, 3.95), 0.25), o_p31)
            Line(o_p31, o_p32)
            Line(o_p32, o_p1) # Close outer loop
        
        make_face(outer.edges())

        # =========================================================
        # 2. Inner Complex Wavy Cutout (Procedurally Generated)
        # =========================================================
        with BuildLine(mode=Mode.PRIVATE) as inner_cutout:
            p_curr = (334.8, 13.0)
            
            p_next = (337.8, 16.0)
            ThreePointArc(p_curr, get_mid(p_curr, p_next, (334.8, 16.0), 3.0), p_next)
            p_curr = p_next
            
            p_next = (337.8, 141.7)
            Line(p_curr, p_next)
            p_curr = p_next
            
            p_next = (334.8, 144.7)
            ThreePointArc(p_curr, get_mid(p_curr, p_next, (334.8, 141.7), 3.0), p_next)
            p_curr = p_next
            
            # Top Scallops (x decreases continuously)
            p_next = (330.737, 144.7)
            Line(p_curr, p_next)
            p_curr = p_next
            
            for i in range(22):
                cx = 325.9 - i * 14.0
                x1 = cx + 3.225
                x2 = cx - 3.225
                x3 = cx - 4.837
                
                p_next = (x1, 145.517)
                ThreePointArc(p_curr, get_mid(p_curr, p_next, (p_curr[0], 146.7), 2.0), p_next)
                p_curr = p_next
                
                p_next = (x2, 145.517)
                ThreePointArc(p_curr, get_mid(p_curr, p_next, (cx, 143.15), 4.0), p_next)
                p_curr = p_next
                
                p_next = (x3, 144.7)
                ThreePointArc(p_curr, get_mid(p_curr, p_next, (x3, 146.7), 2.0), p_next)
                p_curr = p_next
                
                if i < 21:
                    p_next = (x3 - 4.326, 144.7)
                    Line(p_curr, p_next)
                    p_curr = p_next
            
            # Left transition
            p_next = (23.0, 144.7)
            Line(p_curr, p_next)
            p_curr = p_next
            
            p_next = (20.0, 141.7)
            ThreePointArc(p_curr, get_mid(p_curr, p_next, (23.0, 141.7), 3.0), p_next)
            p_curr = p_next
            
            p_next = (20.0, 16.0)
            Line(p_curr, p_next)
            p_curr = p_next
            
            p_next = (23.0, 13.0)
            ThreePointArc(p_curr, get_mid(p_curr, p_next, (23.0, 16.0), 3.0), p_next)
            p_curr = p_next
            
            p_next = (27.063, 13.0)
            Line(p_curr, p_next)
            p_curr = p_next
            
            # Bottom Scallops (x increases continuously)
            for i in range(22):
                cx = 31.9 + i * 14.0
                x1 = cx - 3.225
                x2 = cx + 3.225
                x3 = cx + 4.837
                
                p_next = (x1, 12.183)
                ThreePointArc(p_curr, get_mid(p_curr, p_next, (p_curr[0], 11.0), 2.0), p_next)
                p_curr = p_next
                
                p_next = (x2, 12.183)
                ThreePointArc(p_curr, get_mid(p_curr, p_next, (cx, 14.55), 4.0), p_next)
                p_curr = p_next
                
                p_next = (x3, 13.0)
                ThreePointArc(p_curr, get_mid(p_curr, p_next, (x3, 11.0), 2.0), p_next)
                p_curr = p_next
                
                if i < 21:
                    p_next = (x3 + 4.326, 13.0)
                    Line(p_curr, p_next)
                    p_curr = p_next
                    
            p_next = (334.8, 13.0) # Close back to start
            Line(p_curr, p_next)
            
        make_face(inner_cutout.edges(), mode=Mode.SUBTRACT)

        # =========================================================
        # 3. Inner 46 Circular Cutouts (Procedurally Generated)
        # =========================================================
        x_centers = [24.9 + i * 14.0 for i in range(23)]
        y_centers = [8.0, 149.7]
        hole_locations = [(x, y) for y in y_centers for x in x_centers]
        
        with Locations(*hole_locations):
            Circle(radius=1.725, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Extrude down to target plane Y = 0.0
    # 0.0 - 1.6 = -1.6 mm
    # ---------------------------------------------------------
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Profile Sketch 
    # (YZ Plane offset to X = 350.1)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(350.1)):
        with BuildLine():
            # Mapped 3D coordinates (Y, Z) to 2D sketch plane
            p1 = (3.2, 157.7)
            p2 = (3.2, 156.1)
            p3 = (1.6, 154.5)
            p4 = (0.0, 154.5)
            
            center = (3.2, 154.5)

            # Edge 1: Line
            Line(p1, p2)
            
            # Edge 4: Inner Arc R1.6
            ThreePointArc(p2, get_mid(p2, p3, center, 1.6), p3)
            
            # Edge 3: Bottom Line
            Line(p3, p4)
            
            # Edge 2: Outer Arc R3.2 (Closing back to p1)
            ThreePointArc(p4, get_mid(p4, p1, center, 3.2), p1)
            
        make_face()

    # ---------------------------------------------------------
    # Extrude to target point X = 191.9
    # 191.9 - 350.1 = -158.2 mm
    # ---------------------------------------------------------
    extrude(amount=-158.2)

# =========================================================
    # FEATURE 3: Left Curved Lip (YZ Plane offset to X = 5.2)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(5.2)):
        with BuildLine():
            l_p1 = (3.2, 157.7)
            l_p2 = (3.2, 156.1)
            l_p3 = (1.6, 154.5)
            l_p4 = (0.0, 154.5)
            l_center = (3.2, 154.5)

            Line(l_p1, l_p2)
            ThreePointArc(l_p2, get_mid(l_p2, l_p3, l_center, 1.6), l_p3)
            Line(l_p3, l_p4)
            ThreePointArc(l_p4, get_mid(l_p4, l_p1, l_center, 3.2), l_p1)
        make_face()
    extrude(amount=160.7)

# =========================================================
    # FEATURE 4: Top Flange (XY Plane offset to Z = 156.1)
    # =========================================================
    with BuildSketch(Plane.XY.offset(156.1)):
        with BuildLine():
            f4_p1 = (3.2, 17.0)
            f4_p2 = (354.6, 17.0)
            f4_p3 = (354.6, 3.2)
            f4_p4 = (350.1, 3.2)
            f4_p5 = (191.9, 3.2)
            f4_p6 = (191.9, 3.95)
            f4_p7 = (191.65, 4.2)
            f4_p8 = (166.15, 4.2)
            f4_p9 = (165.9, 3.95)
            f4_p10 = (165.9, 3.2)
            f4_p11 = (5.2, 3.2)
            f4_p12 = (3.2, 3.2)

            Line(f4_p1, f4_p2)
            Line(f4_p2, f4_p3)
            Line(f4_p3, f4_p4)
            Line(f4_p4, f4_p5)
            Line(f4_p5, f4_p6)
            ThreePointArc(f4_p6, get_mid(f4_p6, f4_p7, (191.65, 3.95), 0.25), f4_p7)
            Line(f4_p7, f4_p8)
            ThreePointArc(f4_p8, get_mid(f4_p8, f4_p9, (166.15, 3.95), 0.25), f4_p9)
            Line(f4_p9, f4_p10)
            Line(f4_p10, f4_p11)
            Line(f4_p11, f4_p12)
            Line(f4_p12, f4_p1) # Closes the loop
            
        make_face()
        
        # --- Subtractions: 2 Circular Mounting Holes ---
        with Locations((328.9, 9.0), (28.9, 9.0)):
            Circle(radius=2.5, mode=Mode.SUBTRACT)

    extrude(amount=1.6)

# =========================================================
    # FEATURE 5 & 6: Top Left & Right Lips (XZ Plane offset to Y = 17.0)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-17.0)):
        
        # --- Top Left Lip ---
        with BuildLine():
            tl_p1 = (1.6, 159.3)
            tl_p2 = (3.2, 157.7)
            tl_p3 = (3.2, 156.1)
            tl_p4 = (0.0, 159.3)
            tl_center = (3.2, 159.3)

            ThreePointArc(tl_p1, get_mid(tl_p1, tl_p2, tl_center, 1.6), tl_p2)
            Line(tl_p2, tl_p3)
            ThreePointArc(tl_p3, get_mid(tl_p3, tl_p4, tl_center, 3.2), tl_p4)
            Line(tl_p4, tl_p1)
        make_face()

        # --- Top Right Lip ---
        with BuildLine():
            tr_p1 = (356.2, 159.3)
            tr_p2 = (354.6, 157.7)
            tr_p3 = (354.6, 156.1)
            tr_p4 = (357.8, 159.3)
            tr_center = (354.6, 159.3)

            ThreePointArc(tr_p1, get_mid(tr_p1, tr_p2, tr_center, 1.6), tr_p2)
            Line(tr_p2, tr_p3)
            ThreePointArc(tr_p3, get_mid(tr_p3, tr_p4, tr_center, 3.2), tr_p4)
            Line(tr_p4, tr_p1)
        make_face()

    extrude(amount=13.8)

# =========================================================
    # FEATURE 7: Right Side Mounting Tab (YZ Plane offset to X = 356.2)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(356.2)):
        with BuildLine():
            t_p1 = (17.0, 159.3)
            t_p2 = (17.0, 167.1)
            t_p3 = (16.0, 168.1)
            t_p4 = (4.2, 168.1)
            t_p5 = (3.2, 167.1)
            t_p6 = (3.2, 159.3)

            Line(t_p1, t_p2)
            ThreePointArc(t_p2, get_mid(t_p2, t_p3, (16.0, 167.1), 1.0), t_p3)
            Line(t_p3, t_p4)
            ThreePointArc(t_p4, get_mid(t_p4, t_p5, (4.2, 167.1), 1.0), t_p5)
            Line(t_p5, t_p6)
            Line(t_p6, t_p1)
        make_face()
        
        with Locations((10.6, 163.6)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)

    # Extrude to target point X = 357.8
    extrude(amount=1.6)

# =========================================================
    # FEATURE 8: Left Side Mounting Tab (YZ Plane offset to X = 1.6)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            lt_p1 = (17.0, 159.3)
            lt_p2 = (17.0, 167.1)
            lt_p3 = (16.0, 168.1)
            lt_p4 = (4.2, 168.1)
            lt_p5 = (3.2, 167.1)
            lt_p6 = (3.2, 159.3)

            Line(lt_p1, lt_p2)
            ThreePointArc(lt_p2, get_mid(lt_p2, lt_p3, (16.0, 167.1), 1.0), lt_p3)
            Line(lt_p3, lt_p4)
            ThreePointArc(lt_p4, get_mid(lt_p4, lt_p5, (4.2, 167.1), 1.0), lt_p5)
            Line(lt_p5, lt_p6)
            Line(lt_p6, lt_p1)
        make_face()
        
        with Locations((10.6, 163.6)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)

    # Extrude to target point X = 0.0
    extrude(amount=-1.6)

# =========================================================
    # FEATURE 9: Mirror all geometry about Z = 78.85 (XY plane)
    # =========================================================
    mirror(about=Plane.XY.offset(78.85))

# =========================================================
    # FEATURE 9: Bottom Left Inner Lip (XY Plane offset to Z = 3.2)
    # =========================================================
    with BuildSketch(Plane.XY.offset(3.2)):
        with BuildLine():
            p1 = (5.2, 0.0)
            p2 = (5.2, 1.6)
            p3 = (3.6, 3.2)
            p4 = (2.0, 3.2)
            center = (5.2, 3.2)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 1.6), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 3.2), p1)
        make_face()
    extrude(amount=6.05)

# =========================================================
    # FEATURE 10: Left Inner Middle Lip (XY Plane offset to Z = 15.23)
    # =========================================================
    with BuildSketch(Plane.XY.offset(15.23)):
        with BuildLine():
            p1 = (5.2, 1.6)
            p2 = (5.2, 0.0)
            p3 = (5.0, 0.006)
            p4 = (2.0, 3.2)
            p5 = (3.6, 3.2)
            p6 = (5.0, 1.613)
            center = (5.2, 3.2)

            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, center, 3.2), p4)
            Line(p4, p5)
            ThreePointArc(p5, get_mid(p5, p6, center, 1.6), p6)
            Line(p6, p1)
        make_face()
    extrude(amount=127.22)

# =========================================================
    # FEATURE 11: Left Inner Top Lip (XY Plane offset to Z = 154.5)
    # =========================================================
    with BuildSketch(Plane.XY.offset(154.5)):
        with BuildLine():
            p1 = (5.2, 1.6)
            p2 = (5.2, 0.0)
            p3 = (2.0, 3.2)
            p4 = (3.6, 3.2)
            center = (5.2, 3.2)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
    extrude(amount=-6.05)

# =========================================================
    # FEATURE 12: Left Inner Side Panel (YZ Plane offset to X = 3.6)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(3.6)):
        with BuildLine():
            # Boundary Vertices (Y, Z)
            p1  = (3.2, 154.5)
            p2  = (3.2, 148.45)
            p3  = (11.6, 148.45)
            p4  = (12.6, 147.45)
            p5  = (12.6, 143.45)
            p6  = (11.6, 142.45)
            p7  = (3.2, 142.45)
            p8  = (3.2, 15.25)
            p9  = (11.6, 15.25)
            p10 = (12.6, 14.25)
            p11 = (12.6, 10.25)
            p12 = (11.6, 9.25)
            p13 = (3.2, 9.25)
            p14 = (3.2, 3.2)
            p15 = (14.0, 3.2)
            p16 = (17.0, 6.2)
            p17 = (17.0, 151.5)
            p18 = (14.0, 154.5)

            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, (11.6, 147.45), 1.0), p4)
            Line(p4, p5)
            ThreePointArc(p5, get_mid(p5, p6, (11.6, 143.45), 1.0), p6)
            Line(p6, p7)
            Line(p7, p8)
            Line(p8, p9)
            ThreePointArc(p9, get_mid(p9, p10, (11.6, 14.25), 1.0), p10)
            Line(p10, p11)
            ThreePointArc(p11, get_mid(p11, p12, (11.6, 10.25), 1.0), p12)
            Line(p12, p13)
            Line(p13, p14)
            Line(p14, p15)
            ThreePointArc(p15, get_mid(p15, p16, (14.0, 6.2), 3.0), p16)
            Line(p16, p17)
            ThreePointArc(p17, get_mid(p17, p18, (14.0, 151.5), 3.0), p18)
            Line(p18, p1)
        make_face()
        
        # --- Subtractions: Circular Mounting Holes ---
        with Locations((9.5, 128.85), (9.5, 28.85)):
            Circle(radius=2.5, mode=Mode.SUBTRACT)
            
    extrude(amount=-1.6)

# =========================================================
    # FEATURE 13 (mirror of F9): Bottom Right Inner Lip
    # XY@3.2 — mirror X: 5.2→350.1, 3.6→351.7, 2.0→353.3
    # =========================================================
    with BuildSketch(Plane.XY.offset(3.2)):
        with BuildLine():
            p1 = (350.1, 0.0)
            p2 = (350.1, 1.6)
            p3 = (351.7, 3.2)
            p4 = (353.3, 3.2)
            center = (350.1, 3.2)
            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 1.6), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 3.2), p1)
        make_face()
    extrude(amount=6.05)

    # =========================================================
    # FEATURE 14 (mirror of F10): Right Inner Middle Lip
    # XY@15.23 — mirror X: 5.2→350.1, 5.0→350.3, 2.0→353.3, 3.6→351.7
    # =========================================================
    with BuildSketch(Plane.XY.offset(15.23)):
        with BuildLine():
            p1 = (350.1, 1.6)
            p2 = (350.1, 0.0)
            p3 = (350.3, 0.006)
            p4 = (353.3, 3.2)
            p5 = (351.7, 3.2)
            p6 = (350.3, 1.613)
            center = (350.1, 3.2)
            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, center, 3.2), p4)
            Line(p4, p5)
            ThreePointArc(p5, get_mid(p5, p6, center, 1.6), p6)
            Line(p6, p1)
        make_face()
    extrude(amount=127.22)

    # =========================================================
    # FEATURE 15 (mirror of F11): Right Inner Top Lip
    # XY@154.5 — mirror X: 5.2→350.1, 2.0→353.3, 3.6→351.7
    # =========================================================
    with BuildSketch(Plane.XY.offset(154.5)):
        with BuildLine():
            p1 = (350.1, 1.6)
            p2 = (350.1, 0.0)
            p3 = (353.3, 3.2)
            p4 = (351.7, 3.2)
            center = (350.1, 3.2)
            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
    extrude(amount=-6.05)

    # =========================================================
    # FEATURE 16 (mirror of F12): Right Inner Side Panel
    # YZ plane: 3.6 → 351.7, extrude flips: -1.6 → +1.6
    # Sketch (Y,Z) coordinates unchanged
    # =========================================================
    with BuildSketch(Plane.YZ.offset(351.7)):
        with BuildLine():
            p1  = (3.2,  154.5)
            p2  = (3.2,  148.45)
            p3  = (11.6, 148.45)
            p4  = (12.6, 147.45)
            p5  = (12.6, 143.45)
            p6  = (11.6, 142.45)
            p7  = (3.2,  142.45)
            p8  = (3.2,   15.25)
            p9  = (11.6,  15.25)
            p10 = (12.6,  14.25)
            p11 = (12.6,  10.25)
            p12 = (11.6,   9.25)
            p13 = (3.2,    9.25)
            p14 = (3.2,    3.2)
            p15 = (14.0,   3.2)
            p16 = (17.0,   6.2)
            p17 = (17.0,  151.5)
            p18 = (14.0,  154.5)
            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3,  get_mid(p3,  p4,  (11.6, 147.45), 1.0), p4)
            Line(p4, p5)
            ThreePointArc(p5,  get_mid(p5,  p6,  (11.6, 143.45), 1.0), p6)
            Line(p6, p7)
            Line(p7, p8)
            Line(p8, p9)
            ThreePointArc(p9,  get_mid(p9,  p10, (11.6,  14.25), 1.0), p10)
            Line(p10, p11)
            ThreePointArc(p11, get_mid(p11, p12, (11.6,  10.25), 1.0), p12)
            Line(p12, p13)
            Line(p13, p14)
            Line(p14, p15)
            ThreePointArc(p15, get_mid(p15, p16, (14.0,   6.2),  3.0), p16)
            Line(p16, p17)
            ThreePointArc(p17, get_mid(p17, p18, (14.0, 151.5),  3.0), p18)
            Line(p18, p1)
        make_face()
    extrude(amount=+1.6)
  
if __name__ == "__main__":
    export_stl(part.part, "output_PN-000635_v20.stl")
    
    try:
        from ocp_vscode import show_all
        show_all()
    except ImportError:
        pass