from build123d import *

# Part: PN-000644 v54

with BuildPart() as part:

    with BuildSketch(Plane.XZ.offset(-1.6)):
        with BuildLine():
            Line((0,      388.36),  (0,      395.9))               # E2
            RadiusArc((0,      395.9),   (24.9,   420.8),   24.9)  # E1
            Line((24.9,   420.8),   (34.9,   420.8))               # E58
            RadiusArc((34.9,   420.8),   (39.9,   415.8),   5.0)  # E57rev
            Line((39.9,   415.8),   (39.9,   411.56))              # E56
            Line((39.9,   411.56),  (41.5,   411.56))              # E55
            Line((41.5,   411.56),  (41.5,   412.36))              # E54
            Line((41.5,   412.36),  (208.1,  412.36))              # E53
            Line((208.1,  412.36),  (208.1,  411.56))              # E52
            Line((208.1,  411.56),  (209.7,  411.56))              # E51
            Line((209.7,  411.56),  (209.7,  415.8))               # E50
            RadiusArc((209.7,  415.8),   (214.7,  420.8),   5.0)  # E49rev
            Line((214.7,  420.8),   (224.7,  420.8))               # E48
            RadiusArc((224.7,  420.8),   (249.6,  395.9),  24.9)  # E47
            Line((249.6,  395.9),   (249.6,  388.4))               # E46
            RadiusArc((249.6,  388.4),   (248.8,  387.42),  1.0)  # E45rev
            RadiusArc((248.8,  387.42),  (248.0,  386.44),   1.0)  # E44rev
            Line((248.0,  386.44),  (248.0,  225.7))               # E43
            RadiusArc((248.0,  225.7),   (247.0,  224.7),   1.0)  # E42rev
            Line((247.0,  224.7),   (245.6,  224.7))               # E41
            Line((245.6,  224.7),   (245.6,  223.1))               # E40
            Line((245.6,  223.1),   (246.4,  223.1))               # E39
            Line((246.4,  223.1),   (246.4,  206.1))               # E38
            Line((246.4,  206.1),   (245.6,  206.1))               # E37
            Line((245.6,  206.1),   (245.6,  204.5))               # E36
            Line((245.6,  204.5),   (247.0,  204.5))               # E35
            RadiusArc((247.0,  204.5),   (248.0,  203.5),   1.0)  # E34rev
            Line((248.0,  203.5),   (248.0,   34.2))               # E33
            RadiusArc((248.0,   34.2),   (248.8,   33.22),   -1.0)  # E32rev
            RadiusArc((248.8,   33.22),  (249.6,   32.24),  1.0)  # E31rev
            Line((249.6,   32.24),  (249.6,   24.9))               # E30
            RadiusArc((249.6,   24.9),   (227.409,  0.148), 24.9)  # E29
            RadiusArc((227.409,  0.148), (226.3,    1.142),  1.0)  # E28rev
            Line((226.3,   1.142),  (226.3,    4.0))               # E27
            Line((226.3,   4.0),    (224.7,    4.0))               # E26
            Line((224.7,   4.0),    (224.7,    3.2))               # E25
            Line((224.7,   3.2),    ( 24.9,    3.2))               # E24
            Line(( 24.9,   3.2),    ( 24.9,    4.0))               # E23
            Line(( 24.9,   4.0),    ( 23.3,    4.0))               # E22
            Line(( 23.3,   4.0),    ( 23.3,    1.142))             # E21
            RadiusArc(( 23.3,   1.142),  ( 22.191,  0.148),  1.0)  # E20rev
            RadiusArc(( 22.191,  0.148), (  0.0,   24.9),   24.9)  # E19
            Line((  0.0,  24.9),    (  0.0,   32.2))               # E18
            RadiusArc((  0.0,  32.2),    (  0.8,   33.18),  1.0)  # E17rev
            RadiusArc((  0.8,  33.18),   (  1.6,   34.16),   1.0)  # E16rev
            Line((  1.6,  34.16),   (  1.6,  172.8))               # E15
            RadiusArc((  1.6, 172.8),    (  2.6,  173.8),   1.0)  # E14rev
            Line((  2.6, 173.8),    (  4.0,  173.8))               # E13
            Line((  4.0, 173.8),    (  4.0,  175.4))               # E12
            Line((  4.0, 175.4),    (  3.2,  175.4))               # E11
            Line((  3.2, 175.4),    (  3.2,  192.4))               # E10
            Line((  3.2, 192.4),    (  4.0,  192.4))               # E9
            Line((  4.0, 192.4),    (  4.0,  194.0))               # E8
            Line((  4.0, 194.0),    (  2.6,  194.0))               # E7
            RadiusArc((  2.6, 194.0),    (  1.6,  195.0),   1.0)  # E6rev
            Line((  1.6, 195.0),    (  1.6,  386.4))               # E5
            RadiusArc((  1.6, 386.4),    (  0.8,  387.38),  -1.0)  # E4rev
            RadiusArc((  0.8, 387.38),   (  0.0,  388.36),  1.0)  # E3rev
        make_face()
    extrude(amount=1.6)

    # ---------------------------------------------------------
    # Feature: Arc Profile (YZ Plane at X=208.1, extrude to X=41.5)
    #          Traversal: E1 → E4 → E3 → E2
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(208.1)):
        with BuildLine():
            RadiusArc((3.2, 413.96), (1.6, 412.36), -1.6)   # E1
            Line((1.6, 412.36), (0.0, 412.36))               # E4
            RadiusArc((0.0, 412.36), (3.2, 415.56), 3.2)   # E3
            Line((3.2, 415.56), (3.2, 413.96))               # E2
        make_face()
    extrude(amount=-166.6)

# ---------------------------------------------------------
    # Feature: Flanged slot with holes
    #          (XY Plane at Z=413.96, extrude to Z=415.56)
    #          Traversal: E2 → E3rev → E4 → E5 → E6rev → E1rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(413.96)):
        with BuildLine():
            RadiusArc((208.1, 10.0), (203.1, 15.0),  -5.0)   # E2
            Line((203.1, 15.0), (46.5,  15.0))               # E3rev
            RadiusArc((46.5,  15.0), (41.5,  10.0),  -5.0)   # E4
            Line((41.5,  10.0), (41.5,   3.2))               # E5
            Line((41.5,   3.2), (208.1,  3.2))               # E6rev
            Line((208.1,  3.2), (208.1, 10.0))               # E1rev
        make_face()
        with Locations((179.8, 9.7)): Circle(radius=4.35/2, mode=Mode.SUBTRACT)
        with Locations(( 69.8, 9.7)): Circle(radius=4.35/2, mode=Mode.SUBTRACT)
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (YZ Plane at X=224.7, extrude to X=24.9)
    #          Traversal: E1 → E2 → E3rev → E4rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(224.7)):
        with BuildLine():
            RadiusArc((3.2, 1.6), (1.6, 3.2), 1.6)   # E1
            Line((1.6, 3.2), (0.0, 3.2))               # E2
            RadiusArc((0.0, 3.2), (3.2, 0.0),  -3.2)   # E3rev
            Line((3.2, 0.0), (3.2, 1.6))               # E4rev
        make_face()
    extrude(amount=-199.8)

# ---------------------------------------------------------
    # Feature: Flanged slot with holes
    #          (XY Plane at Z=0.0, extrude to Z=1.6)
    #          Traversal: E2 → E3rev → E4 → E5 → E6rev → E1rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            RadiusArc((224.7,  9.0), (221.7, 12.0),  -3.0)   # E2
            Line((221.7, 12.0), ( 27.9, 12.0))               # E3rev
            RadiusArc(( 27.9, 12.0), ( 24.9,  9.0),  -3.0)   # E4
            Line(( 24.9,  9.0), ( 24.9,  3.2))               # E5
            Line(( 24.9,  3.2), (224.7,  3.2))               # E6rev
            Line((224.7,  3.2), (224.7,  9.0))               # E1rev
        make_face()
        with Locations((214.8, 7.0)): Circle(radius=3.18/2, mode=Mode.SUBTRACT)
        with Locations((124.8, 7.0)): Circle(radius=3.18/2, mode=Mode.SUBTRACT)
        with Locations(( 34.8, 7.0)): Circle(radius=3.18/2, mode=Mode.SUBTRACT)
    extrude(amount=1.6)

    # ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=206.1, extrude to Z=223.1)
    #          Traversal: E1 → E4 → E3 → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(206.1)):
        with BuildLine():
            RadiusArc((248.0, 3.2), (246.4, 1.6), 1.6)   # E1
            Line((246.4, 1.6), (246.4, 0.0))               # E4
            RadiusArc((246.4, 0.0), (249.6, 3.2), -3.2)   # E3
            Line((249.6, 3.2), (248.0, 3.2))               # E2rev
        make_face()
    extrude(amount=17.0)

# ---------------------------------------------------------
    # Feature: Channel Profile (YZ Plane at X=249.6, extrude to X=248.0)
    #          Gaps fixed: E3rev start snapped to (13.2, 207.1)
    #                      E6rev start snapped to (13.2, 222.083)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(249.6)):
        with BuildLine():
            Line((3.2,   206.1),   (12.2,  206.1))                   # E1
            RadiusArc((12.2,   206.1),   (13.2,   207.1),    -1.0)    # E2rev
            RadiusArc((13.2,   207.1),   (12.332, 208.108),  -1.0)    # E3rev — snapped
            RadiusArc((12.332, 208.108), (12.332, 221.092), 6.55)   # E4
            RadiusArc((12.332, 221.092), (13.2,   222.083),  -1.0)    # E5rev
            RadiusArc((13.2,   222.083), (12.2,   223.1),    -1.0)    # E6rev — snapped
            Line((12.2,  223.1),   (3.2,   223.1))                   # E7
            Line(( 3.2,  223.1),   (3.2,   206.1))                   # E8
        make_face()
    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=175.4, extrude to Z=192.4)
    #          Traversal: E1 → E2 → E3rev → E4rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(175.4)):
        with BuildLine():
            RadiusArc((1.6, 3.2), (3.2, 1.6), -1.6)   # E1
            Line((3.2, 1.6), (3.2, 0.0))               # E2
            RadiusArc((3.2, 0.0), (0.0, 3.2),  3.2)   # E3rev
            Line((0.0, 3.2), (1.6, 3.2))               # E4rev
        make_face()
    extrude(amount=17.0)

# ---------------------------------------------------------
    # Feature: Channel Profile (YZ Plane at X=0.0, extrude to X=1.6)
    #          Traversal: E1→E8→E7rev→E6rev→E5→E4rev→E3rev→E2
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(0.0)):
        with BuildLine():
            Line((3.2,   175.4),   (3.2,   192.4))                   # E1
            Line((3.2,   192.4),   (12.2,  192.4))                   # E8
            RadiusArc((12.2,  192.4),   (13.2,  191.4),    1.0)      # E7rev
            RadiusArc((13.2,  191.4),   (12.332, 190.392), 1.0)      # E6rev — snapped
            RadiusArc((12.332, 190.392), (12.332, 177.408), -6.55)   # E5
            RadiusArc((12.332, 177.408), (13.2,  176.4),   1.0)      # E4rev — snapped
            RadiusArc((13.2,  176.4),   (12.2,  175.4),   1.0)       # E3rev
            Line((12.2,  175.4),   (3.2,   175.4))                   # E2
        make_face()
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Feature: 4 Subtractive Profiles (XZ Plane at Y=1.6, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):

        # ── Profile 1: complex slot with r=2.5 arcs ───────────
        with BuildLine():
            Line((212.02,  36.55),  (212.02, 175.07))               # E1
            RadiusArc((212.02, 175.07),  (209.52, 177.57),  -2.5)    # E2rev
            Line((209.52, 177.57),  (189.042,177.57))               # E3rev
            RadiusArc((189.042,177.57),  (186.938,176.42),  -2.5)    # E4rev
            RadiusArc((186.938,176.42),  (184.834,175.27), 2.5)    # E5rev
            Line((184.834,175.27),  ( 89.36, 175.27))               # E6rev
            RadiusArc(( 89.36, 175.27),  ( 86.86, 172.77),  -2.5)   # E7rev
            Line(( 86.86, 172.77),  ( 86.86,  37.75))               # E8rev
            RadiusArc(( 86.86,  37.75),  ( 89.36,  35.25),  -2.5)   # E9rev
            Line(( 89.36,  35.25),  (184.415, 35.25))               # E10rev
            RadiusArc((184.415, 35.25),  (186.039, 34.65), 2.5)    # E11rev
            RadiusArc((186.039, 34.65),  (187.664, 34.05),  -2.5)    # E12rev
            Line((187.664, 34.05),  (209.52,  34.05))               # E13rev
            RadiusArc((209.52,  34.05),  (212.02,  36.55),  -2.5)    # E14rev
        make_face()

        # ── Profile 2: rectangle ───────────────────────────────
        with BuildLine():
            Polyline([(78.325, 178.491), (122.825, 178.491),
                      (122.825, 337.491), (78.325,  337.491)], close=True)
        make_face()

        # ── Profile 3: rounded rect r=3.0 ─────────────────────
        with BuildLine():
            RadiusArc(( 64.0, 194.7),   ( 67.0, 197.7),   -3.0)     # E1
            Line(( 67.0, 197.7),   ( 67.0, 313.2))                  # E2
            RadiusArc(( 67.0, 313.2),   ( 64.0, 316.2),   -3.0)     # E3
            Line(( 64.0, 316.2),   ( 14.0, 316.2))                  # E4
            RadiusArc(( 14.0, 316.2),   ( 11.0, 313.2),   -3.0)     # E5
            Line(( 11.0, 313.2),   ( 11.0, 197.7))                  # E6
            RadiusArc(( 11.0, 197.7),   ( 14.0, 194.7),   -3.0)     # E7
            Line(( 14.0, 194.7),   ( 64.0, 194.7))                  # E8
        make_face()

        # ── Profile 4: complex notched slot ───────────────────
        with BuildLine():
            Line(( 62.7,  61.098), ( 62.7, 163.302))                # E1
            RadiusArc(( 62.7, 163.302), ( 61.562, 164.292),  -1.0)   # E2rev
            RadiusArc(( 61.562, 164.292), ( 58.868, 164.767), 4.45) # E3
            RadiusArc(( 58.868, 164.767), ( 58.401, 164.883), -1.0) # E4rev
            Line(( 58.401, 164.883), ( 37.749, 164.883))             # E5
            RadiusArc(( 37.749, 164.883), ( 37.282, 164.767), -1.0) # E6rev
            RadiusArc(( 37.282, 164.767), ( 33.118, 164.767),  4.45) # E7
            RadiusArc(( 33.118, 164.767), ( 32.651, 164.883), -1.0) # E8rev
            Line(( 32.651, 164.883), ( 19.8,  164.883))              # E9
            RadiusArc(( 19.8,  164.883), ( 18.8,  163.883),   -1.0)  # E10rev
            Line(( 18.8,  163.883), ( 18.8,  105.2))                 # E11
            RadiusArc(( 18.8,  105.2),   ( 17.8,  104.2),    1.0)  # E12rev
            Line(( 17.8,  104.2),  ( 13.05, 104.2))                  # E13
            RadiusArc(( 13.05, 104.2),   ( 12.05, 103.2),     -1.0)  # E14rev
            Line(( 12.05, 103.2),  ( 12.05,  60.2))                  # E15
            RadiusArc(( 12.05,  60.2),   ( 13.05,  59.2),     -1.0)  # E16rev
            Line(( 13.05,  59.2),  ( 32.126,  59.2))                 # E17
            RadiusArc(( 32.126,  59.2),  ( 32.69,   59.374),  -1.0)  # E18rev
            RadiusArc(( 32.69,   59.374), ( 37.71,   59.374), 4.45) # E19
            RadiusArc(( 37.71,   59.374), ( 38.274,  59.2),   -1.0)  # E20rev
            Line(( 38.274,  59.2),  ( 57.876,  59.2))                # E21
            RadiusArc(( 57.876,  59.2),  ( 58.44,   59.374),  -1.0)  # E22rev
            RadiusArc(( 58.44,   59.374), ( 61.562,  60.108), 4.45) # E23
            RadiusArc(( 61.562,  60.108), ( 62.7,    61.098),  -1.0)  # E24rev
        make_face()

    extrude(amount=1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Feature: 6 Subtractive Profiles (XZ Plane at Y=1.6, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):

        with BuildLine():
            RadiusArc((233.5, 21.6),  (233.5, 25.0),  -1.838)  # P1
            Line((233.5, 25.0),  (198.3, 25.0))
            RadiusArc((198.3, 25.0),  (198.3, 21.6),  -1.838)
            Line((198.3, 21.6),  (233.5, 21.6))
        make_face()

        with BuildLine():
            RadiusArc((176.5, 21.6),  (176.5, 25.0),  -1.838)  # P2
            Line((176.5, 25.0),  (151.3, 25.0))
            RadiusArc((151.3, 25.0),  (151.3, 21.6),  -1.838)
            Line((151.3, 21.6),  (176.5, 21.6))
        make_face()

        with BuildLine():
            RadiusArc((233.5, 191.1), (233.5, 194.5), -1.838)  # P3
            Line((233.5, 194.5), (198.3, 194.5))
            RadiusArc((198.3, 194.5), (198.3, 191.1), -1.838)
            Line((198.3, 191.1), (233.5, 191.1))
        make_face()

        with BuildLine():
            RadiusArc((176.5, 191.1), (176.5, 194.5), -1.838)  # P4
            Line((176.5, 194.5), (151.3, 194.5))
            RadiusArc((151.3, 194.5), (151.3, 191.1), -1.838)
            Line((151.3, 191.1), (176.5, 191.1))
        make_face()

        with BuildLine():
            RadiusArc((147.162, 238.2),  (150.838, 238.2),  -1.838)  # P5
            Line((150.838, 238.2),  (150.838, 251.15))
            RadiusArc((150.838, 251.15), (147.162, 251.15), -1.838)
            Line((147.162, 251.15), (147.162, 238.2))
        make_face()

        with BuildLine():
            RadiusArc((129.488, 238.2),  (133.162, 238.2),  -1.838)  # P6
            Line((133.162, 238.2),  (133.162, 251.15))
            RadiusArc((133.162, 251.15), (129.488, 251.15), -1.838)
            Line((129.488, 251.15), (129.488, 238.2))
        make_face()

    extrude(amount=1.6, mode=Mode.SUBTRACT)

# ---------------------------------------------------------
    # Feature: 34 Subtractive Circles (XZ Plane at Y=1.6, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):
        with Locations((241.20,  40.850)): Circle(radius=3.45/2)   # 1
        with Locations((234.60,  40.850)): Circle(radius=3.45/2)   # 2
        with Locations((242.70,  53.996)): Circle(radius=4.35/2)   # 3
        with Locations((241.00, 214.600)): Circle(radius=3.45/2)   # 4
        with Locations((232.50, 214.600)): Circle(radius=3.45/2)   # 5
        with Locations((241.20, 356.300)): Circle(radius=4.35/2)   # 6
        with Locations((236.50, 389.149)): Circle(radius=4.50/2)   # 7
        with Locations((233.22, 106.264)): Circle(radius=3.18/2)   # 8
        with Locations((225.72, 106.264)): Circle(radius=3.18/2)   # 9
        with Locations((218.72,  66.264)): Circle(radius=4.35/2)   # 10
        with Locations((218.72, 146.264)): Circle(radius=4.35/2)   # 11
        with Locations((189.774, 30.750)): Circle(radius=3.45/2)   # 12
        with Locations((189.774,181.750)): Circle(radius=3.45/2)   # 13
        with Locations((151.55, 385.800)): Circle(radius=4.35/2)   # 14
        with Locations(( 98.05, 385.800)): Circle(radius=4.35/2)   # 15
        with Locations(( 62.20, 384.550)): Circle(radius=3.18/2)   # 16
        with Locations(( 13.10, 389.149)): Circle(radius=4.50/2)   # 17
        with Locations((  8.40, 356.300)): Circle(radius=4.35/2)   # 18
        with Locations(( 62.20, 339.150)): Circle(radius=3.18/2)   # 19
        with Locations(( 57.40, 322.000)): Circle(radius=3.45/2)   # 20
        with Locations((  9.40, 322.000)): Circle(radius=3.45/2)   # 21
        with Locations(( 71.95, 255.500)): Circle(radius=3.45/2)   # 22
        with Locations(( 62.20, 184.025)): Circle(radius=3.18/2)   # 23
        with Locations(( 60.95, 168.700)): Circle(radius=3.90/2)   # 24
        with Locations(( 35.20, 168.700)): Circle(radius=3.90/2)   # 25
        with Locations(( 33.40, 189.000)): Circle(radius=3.45/2)   # 26
        with Locations(( 17.10, 183.900)): Circle(radius=3.18/2)   # 27
        with Locations((  8.60, 183.900)): Circle(radius=3.18/2)   # 28
        with Locations(( 60.95,  55.700)): Circle(radius=3.90/2)   # 29
        with Locations(( 62.20,  23.695)): Circle(radius=3.18/2)   # 30
        with Locations(( 35.20,  55.700)): Circle(radius=3.90/2)   # 31
        with Locations(( 15.00,  40.850)): Circle(radius=3.45/2)   # 32
        with Locations(( 12.40,  47.696)): Circle(radius=4.35/2)   # 33
        with Locations((  8.40,  40.850)): Circle(radius=3.45/2)   # 34
    extrude(amount=1.6, mode=Mode.SUBTRACT)

from ocp_vscode import show
show(part)

export_step(part.part, "output_PN-000644_v54.step")