from build123d import *

# Part: PN-000648 v17

with BuildPart() as part:

    with BuildSketch(Plane.YZ.offset(0.0)):
        with BuildLine():
            Line((   0.0,   0.0),  (   0.0, 352.8))              # E1
            Line((   0.0, 352.8),  (-365.2, 352.8))              # E2rev
            RadiusArc((-365.2, 352.8), (-367.2, 350.8),  -2.0)   # E3
            Line((-367.2, 350.8),  (-367.2,   2.0))              # E4rev
            RadiusArc((-367.2,   2.0), (-365.2,   0.0),  -2.0)   # E5
            Line((-365.2,   0.0),  (   0.0,   0.0))              # E6
        make_face()
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=352.8, extrude to Z=0)
    #          Traversal: E1 → E2 → E3rev → E4rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(352.8)):
        with BuildLine():
            Line((-1.6, 1.6), (-1.6, 3.2))               # E1
            RadiusArc((-1.6, 3.2), (1.6, 0.0),  3.2)   # E2
            Line(( 1.6, 0.0), (0.0, 0.0))                 # E3rev
            RadiusArc(( 0.0, 0.0), (-1.6, 1.6), -1.6)   # E4rev
        make_face()
    extrude(amount=-352.8)

    # ---------------------------------------------------------
    #  Side profile (XZ Plane at Y=1.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):
        with BuildLine():
            Line((-1.6,   0.0),  (-1.6, 352.8))                  # E36
            Line((-1.6, 352.8),  (-8.4, 352.8))                  # E35rev
            RadiusArc((-8.4,  352.8), (-10.4, 350.8),  -2.0)    # E34rev
            Line((-10.4, 350.8),  (-10.4, 345.232))              # E33rev
            RadiusArc((-10.4, 345.232), (-15.4, 340.232), +5.0)  # E32rev
            Line((-15.4, 340.232), (-24.0, 340.232))             # E31rev
            Line((-24.0, 340.232), (-24.0, 307.8))               # E30rev
            Line((-24.0, 307.8),  (-15.4, 307.8))                # E29rev
            RadiusArc((-15.4, 307.8),  (-10.4, 302.8),  +5.0)   # E28rev
            Line((-10.4, 302.8),  (-10.4, 295.5))                # E27rev
            RadiusArc((-10.4, 295.5),  ( -8.4, 293.5),  -2.0)   # E26rev
            Line(( -8.4, 293.5),  ( -6.9, 293.5))                # E25rev
            RadiusArc(( -6.9, 293.5),  ( -4.9, 291.5),  +2.0)   # E24rev
            Line(( -4.9, 291.5),  ( -4.9, 285.5))                # E23rev
            RadiusArc(( -4.9, 285.5),  ( -6.9, 283.5),  +2.0)   # E22rev
            Line(( -6.9, 283.5),  ( -8.4, 283.5))                # E21rev
            RadiusArc(( -8.4, 283.5),  (-10.4, 281.5),  -2.0)   # E20rev
            Line((-10.4, 281.5),  (-10.4, 156.8))                # E19rev
            RadiusArc((-10.4, 156.8),  ( -8.4, 154.8),  -2.0)   # E18rev
            Line(( -8.4, 154.8),  ( -6.9, 154.8))                # E17rev
            RadiusArc(( -6.9, 154.8),  ( -4.9, 152.8),  +2.0)   # E16rev
            Line(( -4.9, 152.8),  ( -4.9, 146.8))                # E15rev
            RadiusArc(( -4.9, 146.8),  ( -6.9, 144.8),  +2.0)   # E14rev
            Line(( -6.9, 144.8),  ( -8.4, 144.8))                # E13rev
            RadiusArc(( -8.4, 144.8),  (-10.4, 142.8),  -2.0)   # E12rev
            Line((-10.4, 142.8),  (-10.4,  20.696))              # E11rev
            RadiusArc((-10.4,  20.696), (-12.4,  18.696), +2.0)  # E10rev
            Line((-12.4,  18.696), (-15.9,  18.696))             # E9rev
            RadiusArc((-15.9,  18.696), (-17.9,  16.696), -2.0)  # E8rev
            Line((-17.9,  16.696), (-17.9,  12.2))               # E7rev
            RadiusArc((-17.9,  12.2),  (-15.9,  10.2),  -2.0)   # E6rev
            Line((-15.9,  10.2),  ( -7.9,  10.2))                # E5rev
            RadiusArc(( -7.9,  10.2),  ( -4.9,   7.2),  +3.0)   # E4rev
            Line(( -4.9,   7.2),  ( -4.9,   2.0))                # E3rev
            RadiusArc(( -4.9,   2.0),  ( -2.9,   0.0),  -2.0)   # E2rev
            Line(( -2.9,   0.0),  ( -1.6,   0.0))                # E1
        make_face()

        # ── Subtract stadium 1: Z≈13.696 ──────────────────────
        with Locations((-13.15, 13.696)):
            SlotCenterToCenter(center_separation=1.5, height=4.0,
                               mode=Mode.SUBTRACT)

        # ── Subtract stadium 2: Z≈322.3 ───────────────────────
        with Locations((-9.15, 322.3)):
            SlotCenterToCenter(center_separation=1.5, height=4.0,
                               mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=307.8, extrude to Z=340.232)
    #          Traversal: E1 → E4 → E3rev → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(307.8)):
        with BuildLine():
            RadiusArc((-25.6, 4.8), (-24.0, 3.2),  -1.6)   # E1
            Line((-24.0, 3.2), (-24.0, 1.6))               # E4
            RadiusArc((-24.0, 1.6), (-27.2, 4.8), 3.2)   # E3rev
            Line((-27.2, 4.8), (-25.6, 4.8))               # E2rev
        make_face()
    extrude(amount=32.432)

# ---------------------------------------------------------
    # Feature: Side Profile (YZ Plane at X=-27.2, extrude to X=-25.6)
    #          Traversal: E2 → E3rev → E4 → E5rev → E6rev → E1rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(-27.2)):
        with BuildLine():
            RadiusArc((11.6, 307.8),  (16.6, 312.8),   -5.0)    # E2
            Line((16.6, 312.8),  (16.6, 335.232))               # E3rev
            RadiusArc((16.6, 335.232), (11.6, 340.232), -5.0)   # E4
            Line((11.6, 340.232), ( 4.8, 340.232))              # E5rev
            Line(( 4.8, 340.232), ( 4.8, 307.8))                # E6rev
            Line(( 4.8, 307.8),  (11.6, 307.8))                 # E1rev
        make_face()
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Feature: Array of 102 Angled Subtractive Slots
    #          (YZ Plane at X=0.0, extrude to X=1.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(0.0)):
        
        def rot_slot(cy, cz, sep, angle_deg):
            """Place a SlotCenterToCenter at (cy,cz), rotated by angle_deg."""
            with Locations(Location((cy, cz), (0, 0, 1), angle_deg)):
                SlotCenterToCenter(center_separation=sep,
                                   height=3.675,
                                   mode=Mode.ADD)

        import math
        def a(cy1, cz1, cy2, cz2):
            cy = (cy1+cy2)/2
            cz = (cz1+cz2)/2
            sep = math.dist([cy1, cz1], [cy2, cz2])
            ang = math.degrees(math.atan2(cz2-cz1, cy2-cy1))
            rot_slot(cy, cz, sep, ang)

        # The 102 points follow a strict grid pattern based on your coordinates:
        # Y columns: -111.162, -76.162, -41.162 (Step of 35.0)
        # Z rows: 23.495 up to 254.495 (Step of 7.0, 34 total rows)
        y_cols = [-111.162, -76.162, -41.162]
        z_rows = [23.495 + i * 7.0 for i in range(34)]
        
        for y_bl in y_cols:
            for z_bl in z_rows:
                # Calculate the two arc centers for the slot relative to each bottom-left point.
                # These offsets are derived exactly from the base profile's Arc centers.
                c1_y = y_bl - 1.054
                c1_z = z_bl + 1.505
                
                c2_y = y_bl + 9.554
                c2_z = z_bl + 8.933
                
                # Draw the angled slot
                a(c1_y, c1_z, c2_y, c2_z)
                
    # Extrude the array of 102 slots into the main body in subtract mode
    extrude(amount=1.6, mode=Mode.SUBTRACT)

# ---------------------------------------------------------
    # Feature: 98 Array Slots + 3 Custom Curved Profiles
    #          (YZ Plane at X=0.0, extrude to X=1.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(0.0)):
        
        # --- 1. Array of 98 Slots ---
        def rot_slot(cy, cz, sep, angle_deg):
            with Locations(Location((cy, cz), (0, 0, 1), angle_deg)):
                SlotCenterToCenter(center_separation=sep,
                                   height=3.675,
                                   mode=Mode.ADD)

        import math
        def a(cy1, cz1, cy2, cz2):
            cy = (cy1+cy2)/2
            cz = (cz1+cz2)/2
            sep = math.dist([cy1, cz1], [cy2, cz2])
            ang = math.degrees(math.atan2(cz2-cz1, cy2-cy1))
            rot_slot(cy, cz, sep, ang)

        pts_c1 = [( -95.662, 30.923 + i*7.0 ) for i in range(34)]
        pts_c2 = [( -60.662, 30.923 + i*7.0 ) for i in range(34)]
        pts_c3_a = [( -25.662, 30.923 + i*7.0 ) for i in range(17)] # Up to 142.923
        pts_c3_b = [( -25.662, 170.923 + i*7.0 ) for i in range(14)] # Up to 261.923
        
        all_grid_pts = pts_c1 + pts_c2 + pts_c3_a + pts_c3_b

        for y_bl, z_bl in all_grid_pts:
            c1_y = y_bl + 1.054
            c1_z = z_bl + 1.505
            c2_y = y_bl + 11.662
            c2_z = z_bl - 5.923
            a(c1_y, c1_z, c2_y, c2_z)

        # --- 2. Custom Curved Profile 1 ---
        with BuildLine():
            RadiusArc((-15.054, 142.495), (-13.294, 142.303), -1.838)
            # Flipped to -0.5 because coordinates are reversed from original list
            RadiusArc((-13.294, 142.303), (-13.398, 143.257), -0.5) 
            RadiusArc((-13.398, 143.257), (-18.936, 149.47), 6.75)
            # Flipped to -0.5
            RadiusArc((-18.936, 149.47), (-19.149, 149.848), -0.5) 
            Line((-19.149, 149.848), (-23.554, 152.933))
            RadiusArc((-23.554, 152.933), (-25.662, 149.923), -1.838)
            Line((-25.662, 149.923), (-15.054, 142.495))
        make_face(mode=Mode.ADD)

        # --- 3. Custom Curved Profile 2 ---
        with BuildLine():
            # Flipped to -0.5
            RadiusArc((-19.145, 152.359), (-18.399, 152.571), -0.5) 
            RadiusArc((-18.399, 152.571), (-17.008, 154.638), 6.75)
            # Flipped to -0.5
            RadiusArc((-17.008, 154.638), (-17.077, 155.398), -0.5) 
            Line((-17.077, 155.398), (-23.554, 159.933))
            RadiusArc((-23.554, 159.933), (-25.662, 156.923), -1.838)
            Line((-25.662, 156.923), (-19.145, 152.359))
        make_face(mode=Mode.ADD)

        # --- 4. Custom Curved Profile 3 ---
        with BuildLine():
            RadiusArc((-15.054, 156.495), (-14.522, 156.238), -1.838)
            RadiusArc((-14.522, 156.238), (-12.95, 156.608), 6.75)
            # Flipped to -0.5
            RadiusArc((-12.95, 156.608), (-12.634, 156.77), -0.5) 
            RadiusArc((-12.634, 156.77), (-12.946, 159.505), -1.838)
            Line((-12.946, 159.505), (-23.554, 166.933))
            RadiusArc((-23.554, 166.933), (-25.662, 163.923), -1.838)
            Line((-25.662, 163.923), (-15.054, 156.495))
        make_face(mode=Mode.ADD)
        
    # Extrude all profiles into the main body in subtract mode
    extrude(amount=1.6, mode=Mode.SUBTRACT)
from ocp_vscode import show
show(part)

export_stl(part.part, "output_PN-000648_v17.stl")