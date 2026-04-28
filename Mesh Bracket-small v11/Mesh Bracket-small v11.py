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
        perp = np.array([-v1[1], v1[0]])
        mid_dir = perp if not flip else -perp
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
    else:
        mid_dir = mid_dir / norm
        if flip:
            mid_dir = -mid_dir
            
    return tuple(c + mid_dir * r)

# =========================================================
# PART: Mesh Bracket-small v11
# =========================================================
with BuildPart() as part:
    
    # ---------------------------------------------------------
    # FEATURE 1: Main Profile Sketch (YZ Plane)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ):
        with BuildLine():
            p0 = (-277.7, 41.6)
            p1 = (-282.7, 46.6)
            p2 = (-287.7, 46.6)
            p3 = (-287.7, 3.2)
            p4 = (-3.2, 3.2)
            p5 = (-3.2, 164.04)
            p6 = (-287.7, 164.04)
            p7 = (-287.7, 64.6)
            p8 = (-282.7, 64.6)
            p9 = (-277.7, 69.6)
            p10 = (-277.7, 148.64)
            p11 = (-272.7, 153.64)
            p12 = (-16.2, 153.64)
            p13 = (-11.2, 148.64)
            p14 = (-11.2, 18.6)
            p15 = (-16.2, 13.6)
            p16 = (-272.7, 13.6)
            p17 = (-277.7, 18.6)

            ThreePointArc(p0, get_mid(p0, p1, (-282.7, 41.6), 5.0), p1)
            Line(p1, p2)
            Line(p2, p3)
            Line(p3, p4)
            Line(p4, p5)
            Line(p5, p6)
            Line(p6, p7)
            Line(p7, p8)
            ThreePointArc(p8, get_mid(p8, p9, (-282.7, 69.6), 5.0), p9)
            Line(p9, p10)
            ThreePointArc(p10, get_mid(p10, p11, (-272.7, 148.64), 5.0), p11)
            Line(p11, p12)
            ThreePointArc(p12, get_mid(p12, p13, (-16.2, 148.64), 5.0), p13)
            Line(p13, p14)
            ThreePointArc(p14, get_mid(p14, p15, (-16.2, 18.6), 5.0), p15)
            Line(p15, p16)
            ThreePointArc(p16, get_mid(p16, p17, (-272.7, 18.6), 5.0), p17)
            Line(p17, p0)
            
        make_face()
        
    # ---------------------------------------------------------
    # FINAL EXTRUSION
    # ---------------------------------------------------------
    extrude(amount=1.6)

# =========================================================
    # Main Face Subtractions (4 Mounting Holes)
    # =========================================================
    with BuildSketch(Plane.YZ):
        with Locations(
            (-278.65, 9.0),
            (-278.65, 158.24),
            (-12.25, 158.24),
            (-12.25, 9.0)
        ):
            Circle(radius=2.175)
    
    # Extrude the circles to cut through the 1.6mm thickness of the main profile
    extrude(amount=1.6, mode=Mode.SUBTRACT)

# =========================================================
    # FEATURE 2: Outer Edge Hook/Lip (XY Plane offset to Z = 3.2)
    # =========================================================
    with BuildSketch(Plane.XY.offset(3.2)):
        with BuildLine():
            p1 = (0.0, -287.7)
            p2 = (1.6, -287.7)
            p3 = (-1.6, -290.9)
            p4 = (-1.6, -289.3)
            center = (-1.6, -287.7)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
    extrude(amount=43.4)

# =========================================================
    # FEATURE 3: Upper Outer Hook/Lip (XY Plane offset to Z = 164.04)
    # =========================================================
    with BuildSketch(Plane.XY.offset(164.04)):
        with BuildLine():
            p1 = (0.0, -287.7)
            p2 = (1.6, -287.7)
            p3 = (-1.6, -290.9)
            p4 = (-1.6, -289.3)
            center = (-1.6, -287.7)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
    extrude(amount=-99.44)  # Extrudes down to Z = 64.6

# =========================================================
    # FEATURE 4: Left Side Rib/Flange (XZ Plane offset to Y = -289.3)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(289.3)):
        # --- Outer Boundary ---
        with BuildLine():
            p1 = (-1.6, 64.6)
            p2 = (-1.6, 164.04)
            p3 = (-1.6, 164.44)
            p4 = (-2.6, 165.44)
            p5 = (-12.2, 165.44)
            p6 = (-12.2, 1.8)
            p7 = (-2.6, 1.8)
            p8 = (-1.6, 2.8)
            p9 = (-1.6, 3.2)
            p10 = (-1.6, 46.6)
            p11 = (-4.4, 46.6)
            p12 = (-5.4, 47.6)
            p13 = (-5.4, 63.6)
            p14 = (-4.4, 64.6)

            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, (-2.6, 164.44), 1.0), p4)
            Line(p4, p5)
            Line(p5, p6)
            Line(p6, p7)
            ThreePointArc(p7, get_mid(p7, p8, (-2.6, 2.8), 1.0), p8)
            Line(p8, p9)
            Line(p9, p10)
            Line(p10, p11)
            ThreePointArc(p11, get_mid(p11, p12, (-4.4, 47.6), 1.0), p12)
            Line(p12, p13)
            ThreePointArc(p13, get_mid(p13, p14, (-4.4, 63.6), 1.0), p14)
            Line(p14, p1)
        make_face()
        
        # --- Inner Subtractions (3 Mounting Slots) ---
        # Slot 1
        with BuildLine(mode=Mode.PRIVATE) as slot1:
            Line((-4.4, 141.25), (-8.9, 141.25))
            ThreePointArc((-8.9, 141.25), get_mid((-8.9, 141.25), (-8.9, 137.05), (-8.9, 139.15), 2.1), (-8.9, 137.05))
            Line((-8.9, 137.05), (-4.4, 137.05))
            ThreePointArc((-4.4, 137.05), get_mid((-4.4, 137.05), (-4.4, 141.25), (-4.4, 139.15), 2.1), (-4.4, 141.25))
        make_face(slot1.edges(), mode=Mode.SUBTRACT)

        # Slot 2
        with BuildLine(mode=Mode.PRIVATE) as slot2:
            ThreePointArc((-3.06, 86.87), get_mid((-3.06, 86.87), (-7.26, 86.87), (-5.16, 86.87), 2.1), (-7.26, 86.87))
            Line((-7.26, 86.87), (-7.26, 80.37))
            ThreePointArc((-7.26, 80.37), get_mid((-7.26, 80.37), (-3.06, 80.37), (-5.16, 80.37), 2.1), (-3.06, 80.37))
            Line((-3.06, 80.37), (-3.06, 86.87))
        make_face(slot2.edges(), mode=Mode.SUBTRACT)

        # Slot 3
        with BuildLine(mode=Mode.PRIVATE) as slot3:
            ThreePointArc((-8.9, 30.19), get_mid((-8.9, 30.19), (-8.9, 25.99), (-8.9, 28.09), 2.1), (-8.9, 25.99))
            Line((-8.9, 25.99), (-4.4, 25.99))
            ThreePointArc((-4.4, 25.99), get_mid((-4.4, 25.99), (-4.4, 30.19), (-4.4, 28.09), 2.1), (-4.4, 30.19))
            Line((-4.4, 30.19), (-8.9, 30.19))
        make_face(slot3.edges(), mode=Mode.SUBTRACT)

    # Extrude both the outer bound and the inner subtractions together
    extrude(amount=1.6)

# =========================================================
    # FEATURE 5: Left Outer Hook/Lip (XY Plane offset to Z = 1.8)
    # =========================================================
    with BuildSketch(Plane.XY.offset(1.8)):
        with BuildLine():
            p1 = (-12.2, -290.9)
            p2 = (-12.2, -289.3)
            p3 = (-15.4, -292.5)
            p4 = (-13.8, -292.5)
            center = (-12.2, -292.5)

            Line(p1, p2)
            # Outer arc
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            # Inner arc
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
    extrude(amount=163.64)

# =========================================================
    # FEATURE 6: Far Left Outer Flange/Profile (YZ Plane offset to X = -15.4)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(-15.4)):
        with BuildLine():
            p1 = (-292.5, 1.8)
            p2 = (-299.8, 1.8)
            p3 = (-303.3, 5.3)
            p4 = (-303.3, 8.06)
            p5 = (-301.8, 10.932)
            p6 = (-300.3, 13.804)
            p7 = (-300.3, 28.06)
            p8 = (-301.8, 30.932)
            p9 = (-303.3, 33.804)
            p10 = (-303.3, 161.94)
            p11 = (-299.8, 165.44)
            p12 = (-292.5, 165.44)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (-299.8, 5.3), 3.5), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (-299.8, 8.06), 3.5), p5)
            ThreePointArc(p5, get_mid(p5, p6, (-303.8, 13.804), 3.5), p6)
            Line(p6, p7)
            ThreePointArc(p7, get_mid(p7, p8, (-303.8, 28.06), 3.5), p8)
            ThreePointArc(p8, get_mid(p8, p9, (-299.8, 33.804), 3.5), p9)
            Line(p9, p10)
            ThreePointArc(p10, get_mid(p10, p11, (-299.8, 161.94), 3.5), p11)
            Line(p11, p12)
            Line(p12, p1)
        make_face()
    extrude(amount=1.6)  # Extrudes from X = -15.4 to X = -13.8

# =========================================================
    # FEATURE 8: Bottom Inner Hook/Lip (XZ Plane offset to Y = -287.7)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(287.7)):
        with BuildLine():
            p1 = (0.0, 3.2)
            p2 = (-1.6, 1.6)
            p3 = (-1.6, 0.0)
            p4 = (1.6, 3.2)
            center = (-1.6, 3.2)

            ThreePointArc(p1, get_mid(p1, p2, center, 1.6), p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, center, 3.2), p4)
            Line(p4, p1)
        make_face()
    extrude(amount=-284.5)  # Extrudes from Y = -287.7 to Y = -3.2

# =========================================================
    # FEATURE 9: Left Inner Flange & Slots (XY Plane)
    # =========================================================
    with BuildSketch(Plane.XY):
        # --- Outer Boundary ---
        with BuildLine():
            p1 = (-12.2, 0.01)
            p2 = (-2.6, 0.01)
            p3 = (-1.6, -0.99)
            p4 = (-1.6, -3.2)
            p5 = (-1.6, -287.7)
            p6 = (-1.6, -289.91)
            p7 = (-2.6, -290.91)
            p8 = (-12.2, -290.91)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (-2.6, -0.99), 1.0), p3)
            Line(p3, p4)
            Line(p4, p5)
            Line(p5, p6)
            ThreePointArc(p6, get_mid(p6, p7, (-2.6, -289.91), 1.0), p7)
            Line(p7, p8)
            Line(p8, p1)
        make_face()

        # --- Inner Subtractions (3 Stadium Slots) ---
        # Slot 1
        with BuildLine(mode=Mode.PRIVATE) as slot1:
            s1_1 = (-4.4, -44.63)
            s1_2 = (-8.9, -44.63)
            s1_3 = (-8.9, -48.83)
            s1_4 = (-4.4, -48.83)
            
            Line(s1_1, s1_2)
            ThreePointArc(s1_2, get_mid(s1_2, s1_3, (-8.9, -46.73), 2.1), s1_3)
            Line(s1_3, s1_4)
            ThreePointArc(s1_4, get_mid(s1_4, s1_1, (-4.4, -46.73), 2.1), s1_1)
        make_face(slot1.edges(), mode=Mode.SUBTRACT)

        # Slot 2
        with BuildLine(mode=Mode.PRIVATE) as slot2:
            s2_1 = (-3.68, -142.2)
            s2_2 = (-7.88, -142.2)
            s2_3 = (-7.88, -148.7)
            s2_4 = (-3.68, -148.7)
            
            ThreePointArc(s2_1, get_mid(s2_1, s2_2, (-5.78, -142.2), 2.1), s2_2)
            Line(s2_2, s2_3)
            ThreePointArc(s2_3, get_mid(s2_3, s2_4, (-5.78, -148.7), 2.1), s2_4)
            Line(s2_4, s2_1)
        make_face(slot2.edges(), mode=Mode.SUBTRACT)

        # Slot 3
        with BuildLine(mode=Mode.PRIVATE) as slot3:
            s3_1 = (-8.9, -242.07)
            s3_2 = (-8.9, -246.27)
            s3_3 = (-4.4, -246.27)
            s3_4 = (-4.4, -242.07)
            
            ThreePointArc(s3_1, get_mid(s3_1, s3_2, (-8.9, -244.17), 2.1), s3_2)
            Line(s3_2, s3_3)
            ThreePointArc(s3_3, get_mid(s3_3, s3_4, (-4.4, -244.17), 2.1), s3_4)
            Line(s3_4, s3_1)
        make_face(slot3.edges(), mode=Mode.SUBTRACT)

    # Final extrusion up to Z=1.6
    extrude(amount=1.6)

# =========================================================
    # FEATURE 10: Left Outer Lower Hook/Lip (XZ Plane offset to Y = -290.91)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(290.91)):
        with BuildLine():
            p1 = (-12.2, 1.6)
            p2 = (-12.2, 0.0)
            p3 = (-13.8, -1.6)
            p4 = (-15.4, -1.6)
            center = (-12.2, -1.6)

            Line(p1, p2)
            # Inner arc
            ThreePointArc(p2, get_mid(p2, p3, center, 1.6), p3)
            Line(p3, p4)
            # Outer arc
            ThreePointArc(p4, get_mid(p4, p1, center, 3.2), p1)
        make_face()
        
    extrude(amount=-290.92)  # Extrudes from Y = -290.91 up to Y = 0.01

# =========================================================
    # FEATURE 11: Left Outer Lower Profile/Flange (YZ Plane offset to X = -15.4)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(-15.4)):
        with BuildLine():
            p1 = (0.01, -1.6)
            p2 = (0.01, -8.9)
            p3 = (-3.49, -12.4)
            p4 = (-287.41, -12.4)
            p5 = (-290.91, -8.9)
            p6 = (-290.91, -1.6)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (-3.49, -8.9), 3.5), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (-287.41, -8.9), 3.5), p5)
            Line(p5, p6)
            Line(p6, p1)
        make_face()
    extrude(amount=1.6)  # Extrudes from X = -15.4 to X = -13.8

# =========================================================
    # FEATURE 12: Top Inner Hook/Lip (XY Plane offset to Z = 3.2)
    # =========================================================
    with BuildSketch(Plane.XY.offset(3.2)):
        with BuildLine():
            p1 = (0.0, -3.2)
            p4 = (1.6, -3.2)
            p3 = (-1.6, 0.0)
            p2 = (-1.6, -1.6)
            center = (-1.6, -3.2)

            Line(p1, p4)
            ThreePointArc(p4, get_mid(p4, p3, center, 3.2), p3)
            Line(p3, p2)
            ThreePointArc(p2, get_mid(p2, p1, center, 1.6), p1)
        make_face()
    extrude(amount=160.84)
    
    # ---------------------------------------------------------
    # Feature: Side panel with 3 subtractive slots
    #          (XZ Plane at Y=-1.6, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(1.6)):

        # ── Main Profile ───────────────────────────────────────
        with BuildLine():
            Line((-2.6,   1.8),  (-12.2,   1.8))             # E1
            Line((-12.2,  1.8),  (-12.2, 165.44))            # E8rev
            Line((-12.2, 165.44), (-2.6,  165.44))            # E7rev
            RadiusArc((-2.6, 165.44), (-1.6, 164.44), 1.0)  # E6rev
            Line((-1.6, 164.44), (-1.6, 164.04))              # E5rev
            Line((-1.6, 164.04), (-1.6,   3.2))               # E4rev
            Line((-1.6,   3.2),  (-1.6,   2.8))               # E3
            RadiusArc((-1.6,   2.8),  (-2.6,   1.8),  +1.0)  # E2
        make_face()

        # ── P1: horizontal stadium Z≈28.09 ────────────────────
        with Locations((-6.65, 28.09)):
            SlotCenterToCenter(center_separation=4.5, height=4.2,
                               mode=Mode.SUBTRACT)

        # ── P2: vertical stadium Z≈83.62 ──────────────────────
        with Locations((-5.16, 83.62)):
            SlotCenterToCenter(center_separation=6.5, height=4.2,
                               rotation=90, mode=Mode.SUBTRACT)

        # ── P3: horizontal stadium Z≈139.15 ───────────────────
        with Locations((-6.65, 139.15)):
            SlotCenterToCenter(center_separation=4.5, height=4.2,
                               mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=165.44, extrude to Z=1.8)
    #          Traversal: E1 → E2 → E3 → E4
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(165.44)):
        with BuildLine():
            RadiusArc((-13.8, 1.6), (-12.2, 0.0),  -1.6)   # E1
            Line((-12.2, 0.0), (-12.2, -1.6))              # E2
            RadiusArc((-12.2, -1.6), (-15.4, 1.6), 3.2)  # E3
            Line((-15.4, 1.6), (-13.8, 1.6))               # E4
        make_face()
    extrude(amount=-163.64)

# ---------------------------------------------------------
    # Feature: Side panel (YZ Plane at X=-15.4, extrude to X=-13.8)
    #          Traversal: E1 → E2rev → E3 → E4rev → E5 → E6rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(-15.4)):
        with BuildLine():
            Line(( 1.6, 165.44), ( 8.9, 165.44))              # E1
            RadiusArc(( 8.9, 165.44), (12.4, 161.94), 3.5)   # E2rev
            Line((12.4, 161.94), (12.4,   5.3))               # E3
            RadiusArc((12.4,   5.3),  ( 8.9,   1.8), 3.5)   # E4rev
            Line(( 8.9,   1.8),  ( 1.6,   1.8))               # E5
            Line(( 1.6,   1.8),  ( 1.6, 165.44))              # E6rev
        make_face()
        with Locations((6.9, 133.62)): Circle(radius=2.5, mode=Mode.SUBTRACT)
        with Locations((6.9,  33.62)): Circle(radius=2.5, mode=Mode.SUBTRACT)
    extrude(amount=1.6)

# =========================================================
    # FEATURE 14: Top Outer Hook/Lip (XZ Plane offset to Y = -3.2)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(3.2)):
        with BuildLine():
            p1 = (0.0, 164.04)
            p2 = (-1.6, 165.64)
            p3 = (-1.6, 167.24)
            p4 = (1.6, 164.04)
            center = (-1.6, 164.04)

            ThreePointArc(p1, get_mid(p1, p2, center, 1.6), p2)
            Line(p2, p3)
            # Reversing Edge 3 to maintain a continuous closed loop
            ThreePointArc(p3, get_mid(p3, p4, center, 3.2), p4)
            Line(p4, p1)
        make_face()
        
    extrude(amount=284.5)  # Extrudes from Y = -3.2 to Y = -287.7

# =========================================================
    # FEATURE 15: Top Flange Profile & Slots (XY Plane offset to Z = 167.24)
    # =========================================================
    with BuildSketch(Plane.XY.offset(167.24)):
        # --- Outer Boundary ---
        with BuildLine():
            p1 = (-1.6, -287.7)
            p2 = (-1.6, -0.99)
            p3 = (-2.6, 0.01)
            p4 = (-12.2, 0.01)
            p5 = (-12.2, -288.2)
            p6 = (-2.466, -288.2)

            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (-2.6, -0.99), 1.0), p3)
            Line(p3, p4)
            Line(p4, p5)
            Line(p5, p6)
            ThreePointArc(p6, get_mid(p6, p1, (-2.466, -287.2), 1.0), p1)
        make_face()

        # --- Inner Subtractions (3 Stadium Slots) ---
        # Slot 1
        with BuildLine(mode=Mode.PRIVATE) as slot1:
            Line((-4.4, -246.27), (-8.9, -246.27))
            # Left arc: bulges outward to the left (X: -8.9 - 2.1 = -11.0)
            ThreePointArc((-8.9, -246.27), (-11.0, -244.17), (-8.9, -242.07))
            Line((-8.9, -242.07), (-4.4, -242.07))
            # Right arc: bulges outward to the right (X: -4.4 + 2.1 = -2.3)
            ThreePointArc((-4.4, -242.07), (-2.3, -244.17), (-4.4, -246.27))
        make_face(slot1.edges(), mode=Mode.SUBTRACT)

        # Slot 2 (Horizontal orientation)
        with BuildLine(mode=Mode.PRIVATE) as slot2:
            # Bottom arc: bulges outward downwards (Y: -148.7 - 2.1 = -150.8)
            ThreePointArc((-3.68, -148.7), (-5.78, -150.8), (-7.88, -148.7))
            Line((-7.88, -148.7), (-7.88, -142.2))
            # Top arc: bulges outward upwards (Y: -142.2 + 2.1 = -140.1)
            ThreePointArc((-7.88, -142.2), (-5.78, -140.1), (-3.68, -142.2))
            Line((-3.68, -142.2), (-3.68, -148.7))
        make_face(slot2.edges(), mode=Mode.SUBTRACT)

        # Slot 3
        with BuildLine(mode=Mode.PRIVATE) as slot3:
            Line((-4.4, -48.83), (-8.9, -48.83))
            # Left arc: bulges outward to the left (X: -8.9 - 2.1 = -11.0)
            ThreePointArc((-8.9, -48.83), (-11.0, -46.73), (-8.9, -44.63))
            Line((-8.9, -44.63), (-4.4, -44.63))
            # Right arc: bulges outward to the right (X: -4.4 + 2.1 = -2.3)
            ThreePointArc((-4.4, -44.63), (-2.3, -46.73), (-4.4, -48.83))
        make_face(slot3.edges(), mode=Mode.SUBTRACT)

    # Extrude both the outer bound and the inner subtractions together downwards
    extrude(amount=-1.6)

# =========================================================
    # FEATURE 16: Top Left Outer Hook/Lip (XZ Plane offset to Y = 0.01)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(0.01)):
        with BuildLine():
            p1 = (-13.8, 168.84)
            p2 = (-15.4, 168.84)
            p3 = (-12.2, 165.64)
            p4 = (-12.2, 167.24)
            center = (-12.2, 168.84)

            Line(p1, p2)
            # Outer arc
            ThreePointArc(p2, get_mid(p2, p3, center, 3.2), p3)
            Line(p3, p4)
            # Inner arc
            ThreePointArc(p4, get_mid(p4, p1, center, 1.6), p1)
        make_face()
        
    extrude(amount=288.21)  # Extrudes from Y = 0.01 to Y = -288.2

# =========================================================
    # FEATURE 17: Top Left Outer Profile/Flange (YZ Plane offset to X = -13.8)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(-13.8)):
        with BuildLine():
            p1 = (0.01, 168.84)
            p2 = (0.01, 176.14)
            p3 = (-3.49, 179.64)
            p4 = (-127.563, 179.64)
            p5 = (-130.981, 176.89)
            p6 = (-134.4, 174.14)
            p7 = (-149.563, 174.14)
            p8 = (-152.981, 176.89)
            p9 = (-156.4, 179.64)
            p10 = (-284.7, 179.64)
            p11 = (-288.2, 176.14)
            p12 = (-288.2, 168.84)

            # Trace the loop chronologically
            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (-3.49, 176.14), 3.5), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (-127.563, 176.14), 3.5), p5)
            ThreePointArc(p5, get_mid(p5, p6, (-134.4, 177.64), 3.5), p6)
            Line(p6, p7)
            ThreePointArc(p7, get_mid(p7, p8, (-149.563, 177.64), 3.5), p8)
            ThreePointArc(p8, get_mid(p8, p9, (-156.4, 176.14), 3.5), p9)
            Line(p9, p10)
            ThreePointArc(p10, get_mid(p10, p11, (-284.7, 176.14), 3.5), p11)
            Line(p11, p12)
            Line(p12, p1)
        make_face()
        
    extrude(amount=-1.6)  # Extrudes from X = -13.8 to X = -15.4

if __name__ == "__main__":
    export_stl(part.part, "output_Mesh Bracket-small_v11.stl")
    
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass