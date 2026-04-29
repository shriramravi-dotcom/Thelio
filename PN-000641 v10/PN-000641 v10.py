from build123d import *

# Part: PN-000641 v10

with BuildPart() as part:

    # ---------------------------------------------------------
    # 1. Main Profile (XY Plane at Z=165.2, extrude to Z=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(165.2)):
        with BuildLine():
            RadiusArc((1.6, 3.2),  (3.2, 1.6),  -1.6)
            Line((3.2,  1.6), (54.1, 1.6))
            Line((54.1, 1.6), (54.1, 0.0))
            Line((54.1, 0.0), (3.2,  0.0))
            RadiusArc((3.2, 0.0),  (0.0, 3.2),  3.2)
            Line((0.0,  3.2), (1.6,  3.2))
        make_face()
    extrude(amount=-165.2)

    # ---------------------------------------------------------
    # 2. Fillet edges at X=54.1 by 1mm
    # ---------------------------------------------------------
    try:
        fillet_edges = (
            part.edges().sort_by_distance((54.1, 0.8, 165.2))[0:1] +
            part.edges().sort_by_distance((54.1, 0.8,   0.0))[0:1]
        )
        fillet(fillet_edges, radius=1.0)
    except Exception as e:
        print(f"Fillet failed: {e}")

    # ---------------------------------------------------------
    # 3. Side Profile (YZ Plane at X=1.6, extrude to X=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            Line((3.2,  165.2),    (10.6, 165.2))
            RadiusArc((10.6, 165.2),   (15.6, 160.2),   5.0)
            Line((15.6, 160.2),    (15.6, 156.084))
            RadiusArc((15.6, 156.084), (13.8, 152.242),  5.0)
            RadiusArc((13.8, 152.242), (12.0, 148.4),     -5.0)
            Line((12.0, 148.4),    (12.0, 17.0))
            RadiusArc((12.0, 17.0),    (17.0, 12.0),      -5.0)
            Line((17.0, 12.0),     (24.1, 12.0))
            RadiusArc((24.1, 12.0),    (29.1,  7.0),     5.0)
            Line((29.1,  7.0),     (29.1,  5.0))
            RadiusArc((29.1,  5.0),    (24.1,  0.0),     5.0)
            Line((24.1,  0.0),     (3.2,   0.0))
            Line((3.2,   0.0),     (3.2,  165.2))
        make_face()
    extrude(amount=-1.6)

    # ---------------------------------------------------------
    # 4. Subtractive Circles (YZ Plane at X=1.6, extrude to X=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        with Locations((9.60,  159.20)): Circle(radius=4.35 / 2)
        with Locations((10.70,   6.00)): Circle(radius=5.50 / 2)
        with Locations((23.60,   6.00)): Circle(radius=4.35 / 2)
    extrude(amount=-1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 5. Subtractive Profiles
    #    Plane.XZ normal = (0,-1,0)
    #    offset(-1.6) → plane at Y=+1.6  ✓
    #    extrude(amount=1.6) → moves along normal (-Y) → reaches Y=0  ✓
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):

        # ── Profile 1 ──────────────────────────────────────────
        with BuildLine():
            Line((11.418, 123.075), (12.832, 121.661))
            RadiusArc((12.832, 121.661), (13.539, 121.368),  -1.0)
            Line((13.539, 121.368), (17.825, 121.368))
            RadiusArc((17.825, 121.368), (18.825, 122.368),  -1.0)
            Line((18.825, 122.368), (18.825, 137.368))
            RadiusArc((18.825, 137.368), (17.825, 138.368),  -1.0)
            Line((17.825, 138.368), (13.464, 138.368))
            RadiusArc((13.464, 138.368), (12.757, 138.075),  -1.0)
            Line((12.757, 138.075), (11.418, 136.736))
            RadiusArc((11.418, 136.736), (11.125, 136.029),  -1.0)
            Line((11.125, 136.029), (11.125, 123.782))
            RadiusArc((11.125, 123.782), (11.418, 123.075),  -1.0)
        make_face()

        # ── Profiles 2–11, 13, 14: RectangleRounded ───────────
        with Locations((14.875, 108.568)): RectangleRounded( 9.5, 15.5, 1.0)  # P2
        with Locations((24.525, 108.568)): RectangleRounded( 7.0, 15.0, 1.0)  # P3
        with Locations((14.875,  86.643)): RectangleRounded( 9.5, 15.5, 1.0)  # P4
        with Locations((24.525,  86.643)): RectangleRounded( 7.0, 15.0, 1.0)  # P5
        with Locations((15.625,  66.493)): RectangleRounded( 7.0, 15.0, 1.0)  # P6
        with Locations((24.025,  66.493)): RectangleRounded( 7.0, 15.0, 1.0)  # P7
        with Locations((32.425,  66.493)): RectangleRounded( 7.0, 15.0, 1.0)  # P8
        with Locations((40.825,  66.493)): RectangleRounded( 7.0, 15.0, 1.0)  # P9
        with Locations((15.625,  46.643)): RectangleRounded( 7.0, 15.0, 1.0)  # P10
        with Locations((24.025,  46.643)): RectangleRounded( 7.0, 15.0, 1.0)  # P11
        with Locations((15.625,  26.643)): RectangleRounded( 7.0, 15.0, 1.0)  # P13
        with Locations((24.025,  26.643)): RectangleRounded( 7.0, 15.0, 1.0)  # P14

        # ── Profile 12: stepped slot ───────────────────────────
        with BuildLine():
            Line((30.925, 38.393), (39.443, 38.393))
            RadiusArc((39.443, 38.393), (40.443, 39.393),  -1.0)
            Line((40.443, 39.393), (40.443, 43.173))
            RadiusArc((40.443, 43.173), (40.943, 43.673), 0.5)
            Line((40.943, 43.673), (41.243, 43.673))
            RadiusArc((41.243, 43.673), (41.743, 44.173),  -0.5)
            Line((41.743, 44.173), (41.743, 49.113))
            RadiusArc((41.743, 49.113), (41.243, 49.613),  -0.5)
            Line((41.243, 49.613), (40.943, 49.613))
            RadiusArc((40.943, 49.613), (40.443, 50.113), 0.5)
            Line((40.443, 50.113), (40.443, 53.893))
            RadiusArc((40.443, 53.893), (39.443, 54.893),  -1.0)
            Line((39.443, 54.893), (30.925, 54.893))
            RadiusArc((30.925, 54.893), (29.925, 53.893),  -1.0)
            Line((29.925, 53.893), (29.925, 39.393))
            RadiusArc((29.925, 39.393), (30.925, 38.393),  -1.0)
        make_face()

        # ── Profile 15 ─────────────────────────────────────────
        with BuildLine():
            Line((12.740,  6.375), (13.655,  5.461))
            RadiusArc((13.655,  5.461), (14.362,  5.168),  -1.0)
            Line((14.362,  5.168), (22.203,  5.168))
            RadiusArc((22.203,  5.168), (23.203,  6.168),  -1.0)
            Line((23.203,  6.168), (23.203, 15.168))
            RadiusArc((23.203, 15.168), (22.203, 16.168),  -1.0)
            Line((22.203, 16.168), (14.362, 16.168))
            RadiusArc((14.362, 16.168), (13.655, 15.875),  -1.0)
            Line((13.655, 15.875), (12.740, 14.961))
            RadiusArc((12.740, 14.961), (12.447, 14.254),  -1.0)
            Line((12.447, 14.254), (12.447,  7.082))
            RadiusArc((12.447,  7.082), (12.740,  6.375),  -1.0)
        make_face()

    extrude(amount=1.6, mode=Mode.SUBTRACT)

 # ---------------------------------------------------------
    # 6. Subtractive Circles (XZ Plane at Y=1.6, extrude to Y=0)
    #    All centres: Y=1.6 → Plane.XZ.offset(-1.6), coords (X, Z)
    #    1) (29.445, 10.668) dia=8.74  r=4.370
    #    2) (40.305, 10.668) dia=8.74  r=4.370
    #    3) (43.875, 129.868) dia=6.62  r=3.310
    #    4) (27.875, 129.868) dia=6.62  r=3.310
    #    5) (15.775, 149.668) dia=6.20  r=3.100
    #    6) (13.375, 143.768) dia=3.00  r=1.500
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):
        with Locations((29.445,  10.668)): Circle(radius=8.74 / 2)
        with Locations((40.305,  10.668)): Circle(radius=8.74 / 2)
        with Locations((43.875, 129.868)): Circle(radius=6.62 / 2)
        with Locations((27.875, 129.868)): Circle(radius=6.62 / 2)
        with Locations((15.775, 149.668)): Circle(radius=6.20 / 2)
        with Locations((13.375, 143.768)): Circle(radius=3.00 / 2)
    extrude(amount=1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 7. Subtractive Profile (XY Plane at Z=68.777, extrude +20.0)
    #    All edges have Z=68.777 → Plane.XY.offset(68.777)
    #    Sketch coords (X, Y). Extrude to Z=88.777 → amount=+20.0
    #    Arc 3: (1.6,3.2)→(3.2,1.6) center LEFT  → r=+1.6
    #    Arc 7: (3.2,0.0)→(0.0,3.2) center RIGHT → r=-3.2
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(68.777)):
        with BuildLine():
            # Line 1: (0.0,7.0) → (1.6,7.0)
            Line((0.0, 7.0), (1.6, 7.0))
            # Line 2: (1.6,7.0) → (1.6,3.2)
            Line((1.6, 7.0), (1.6, 3.2))
            # Arc 3: (1.6,3.2) → (3.2,1.6), center=(3.2,3.2), r=+1.6
            RadiusArc((1.6, 3.2), (3.2, 1.6),  1.6)
            # Line 4: (3.2,1.6) → (6.2,1.6)
            Line((3.2, 1.6), (6.2, 1.6))
            # Line 5: (6.2,1.6) → (6.2,0.0)
            Line((6.2, 1.6), (6.2, 0.0))
            # Line 6: (6.2,0.0) → (3.2,0.0)
            Line((6.2, 0.0), (3.2, 0.0))
            # Arc 7: (3.2,0.0) → (0.0,3.2), center=(3.2,3.2), r=-3.2
            RadiusArc((3.2, 0.0), (0.0, 3.2), 3.2)
            # Line 8: (0.0,3.2) → (0.0,7.0)
            Line((0.0, 3.2), (0.0, 7.0))
        make_face()
    extrude(amount=20.0, mode=Mode.SUBTRACT) 

    # ---------------------------------------------------------
    # 8. Subtractive Profile (YZ Plane at X=1.6, extrude to X=0)
    #    Arc 1: (7.0,68.777)→(8.0,69.777) center=(7.0,69.777) LEFT  → r=+1.0
    #    Line 2: (8.0,69.777)→(8.0,87.777)
    #    Arc 3: (8.0,87.777)→(7.0,88.777) center=(7.0,87.777) LEFT  → r=+1.0
    #    Closing line: (7.0,88.777)→(7.0,68.777)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            RadiusArc((7.0, 68.777), (8.0, 69.777),  -1.0)
            Line((8.0, 69.777), (8.0, 87.777))
            RadiusArc((8.0, 87.777), (7.0, 88.777),  -1.0)
            Line((7.0, 88.777), (7.0, 68.777))
        make_face()
    extrude(amount=-1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # 9. Subtractive Slot (XZ Plane at Y=1.6, extrude to Y=0)
    #    Traversal: Line2 → Arc3rev → Closing line → Arc1rev
    #    Arc 1 rev: (6.2,68.777)→(7.2,69.777) center=(6.2,69.777) LEFT → r=+1.0
    #    Arc 3 rev: (7.2,87.777)→(6.2,88.777) center=(6.2,87.777) LEFT → r=+1.0
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):
        with BuildLine():
            Line((7.2, 69.777), (7.2, 87.777))             # Line 2
            RadiusArc((7.2, 87.777), (6.2, 88.777),  -1.0)  # Arc 3 rev
            Line((6.2, 88.777), (6.2, 68.777))             # Closing line
            RadiusArc((6.2, 68.777), (7.2, 69.777),  -1.0)  # Arc 1 rev
        make_face()
    extrude(amount=1.6, mode=Mode.SUBTRACT)

from ocp_vscode import show
show(part)

export_step(part.part, "output_PN-000641_v10.step")