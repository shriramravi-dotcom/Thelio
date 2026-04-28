from build123d import *

# Part: PN-000645 v63

with BuildPart() as part:

    with BuildSketch(Plane.XZ.offset(-1.6)):
        with BuildLine():
            Line((39.9,    411.56),  (39.9,    415.8))               # E62rev
            RadiusArc((39.9,    415.8),   (34.9,    420.8),   -5.0)   # E1    cross>0 +
            Line((34.9,    420.8),   (24.9,    420.8))               # E2rev
            RadiusArc((24.9,    420.8),   (0.0,     395.9),  -24.9)   # E3rev cross>0 +
            Line((0.0,     395.9),   (0.0,     374.149))             # E4rev
            RadiusArc((0.0,     374.149),  (3.0,     371.149),  -3.0) # E5    cross>0 +
            Line((3.0,     371.149),  (24.1,    371.149))            # E6rev
            RadiusArc((24.1,    371.149),  (24.6,    370.649), 0.5) # E7    cross<0 -
            Line((24.6,    370.649),  (24.6,    369.549))            # E8rev
            Line((24.6,    369.549),  (23.8,    369.549))            # E9rev
            Line((23.8,    369.549),  (23.8,    346.349))            # E10rev
            Line((23.8,    346.349),  (24.6,    346.349))            # E11
            Line((24.6,    346.349),  (24.6,    344.649))            # E12rev
            RadiusArc((24.6,    344.649),  (24.1,    344.149), 0.5) # E13   cross<0 -
            Line((24.1,    344.149),  (10.0,    344.149))            # E14rev
            RadiusArc((10.0,    344.149),  (0.0,     334.149), -10.0) # E15   cross>0 +
            Line((0.0,     334.149),  (0.0,     225.7))              # E16rev
            RadiusArc((0.0,     225.7),    (1.0,     224.7),    -1.0) # E17   cross>0 +
            Line((1.0,     224.7),    (4.0,     224.7))              # E18rev
            Line((4.0,     224.7),    (4.0,     223.1))              # E19rev
            Line((4.0,     223.1),    (3.2,     223.1))              # E20rev
            Line((3.2,     223.1),    (3.2,     206.1))              # E21rev
            Line((3.2,     206.1),    (4.0,     206.1))              # E22rev
            Line((4.0,     206.1),    (4.0,     204.5))              # E23rev
            Line((4.0,     204.5),    (1.0,     204.5))              # E24rev
            RadiusArc((1.0,     204.5),    (0.0,     203.5),    -1.0) # E25   cross>0 +
            Line((0.0,     203.5),    (0.0,      24.9))              # E26rev
            RadiusArc((0.0,      24.9),    (22.191,    0.148),  -24.9)# E27rev cross>0 +
            RadiusArc((22.191,    0.148),  (23.3,      1.142),   -1.0)# E28   cross>0 +
            Line((23.3,      1.142),  (23.3,      4.0))              # E29rev
            Line((23.3,      4.0),    (24.9,      4.0))              # E30rev
            Line((24.9,      4.0),    (24.9,      3.2))              # E31rev
            Line((24.9,      3.2),    (224.7,     3.2))              # E32rev
            Line((224.7,     3.2),    (224.7,     4.0))              # E33rev
            Line((224.7,     4.0),    (226.3,     4.0))              # E34rev
            Line((226.3,     4.0),    (226.3,     1.142))            # E35rev
            RadiusArc((226.3,     1.142),  (227.409,   0.148),   -1.0)# E36   cross>0 +
            RadiusArc((227.409,   0.148),  (249.6,    24.9),    -24.9)# E37rev cross>0 +
            Line((249.6,    24.9),    (249.6,   203.5))              # E38rev
            RadiusArc((249.6,   203.5),    (248.6,   204.5),    -1.0) # E39   cross>0 +
            Line((248.6,   204.5),    (245.6,   204.5))              # E40rev
            Line((245.6,   204.5),    (245.6,   206.1))              # E41rev
            Line((245.6,   206.1),    (246.4,   206.1))              # E42rev
            Line((246.4,   206.1),    (246.4,   223.1))              # E43rev
            Line((246.4,   223.1),    (245.6,   223.1))              # E44rev
            Line((245.6,   223.1),    (245.6,   224.7))              # E45rev
            Line((245.6,   224.7),    (248.6,   224.7))              # E46rev
            RadiusArc((248.6,   224.7),    (249.6,   225.7),    -1.0) # E47   cross>0 +
            Line((249.6,   225.7),    (249.6,   344.186))            # E48rev
            RadiusArc((249.6,   344.186),  (248.674, 345.183),  -1.0) # E49   cross>0 +
            RadiusArc((248.674, 345.183),  (248.674, 370.114), 12.5)# E50rev cross<0 -
            RadiusArc((248.674, 370.114),  (249.6,   371.111),  -1.0) # E51   cross>0 +
            Line((249.6,   371.111),  (249.6,   395.9))              # E52rev
            RadiusArc((249.6,   395.9),    (224.7,   420.8),   -24.9) # E53rev cross>0 +
            Line((224.7,   420.8),    (214.7,   420.8))              # E54rev
            RadiusArc((214.7,   420.8),    (209.7,   415.8),    -5.0) # E55   cross>0 +
            Line((209.7,   415.8),    (209.7,   411.56))             # E56rev
            Line((209.7,   411.56),   (208.1,   411.56))             # E57rev
            Line((208.1,   411.56),   (208.1,   412.36))             # E58rev
            Line((208.1,   412.36),   (41.5,    412.36))             # E59rev
            Line((41.5,    412.36),   (41.5,    411.56))             # E60rev
            Line((41.5,    411.56),   (39.9,    411.56))             # E61rev
        make_face()
    extrude(amount=1.6)

    # ---------------------------------------------------------
    # Feature: Arc Profile (YZ Plane at X=224.7, extrude to X=24.9)
    #          Traversal: E1 → E4rev → E3rev → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(224.7)):
        with BuildLine():
            RadiusArc((3.2, 1.6), (1.6, 3.2), 1.6)   # E1
            Line((1.6, 3.2), (0.0, 3.2))               # E4rev
            RadiusArc((0.0, 3.2), (3.2, 0.0),  -3.2)   # E3rev
            Line((3.2, 0.0), (3.2, 1.6))               # E2rev
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
        with Locations((214.8, 7.0)): Circle(radius=1.59, mode=Mode.SUBTRACT)
        with Locations((124.8, 7.0)): Circle(radius=1.59, mode=Mode.SUBTRACT)
        with Locations(( 34.8, 7.0)): Circle(radius=1.59, mode=Mode.SUBTRACT)
    extrude(amount=1.6)

    # ---------------------------------------------------------
    # Feature: Arc Profile (YZ Plane at X=208.1, extrude to X=41.5)
    #          Traversal: E1 → E4 → E3 → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(208.1)):
        with BuildLine():
            RadiusArc((3.2, 413.96), (1.6, 412.36),  -1.6)   # E1
            Line((1.6, 412.36), (0.0, 412.36))               # E4
            RadiusArc((0.0, 412.36), (3.2, 415.56), 3.2)   # E3
            Line((3.2, 415.56), (3.2, 413.96))               # E2rev
        make_face()
    extrude(amount=-166.6)

    # ---------------------------------------------------------
    # Feature: Flanged slot with holes
    #          (XY Plane at Z=415.56, extrude to Z=413.96)
    #          Traversal: E2rev → E3rev → E4rev → E5 → E6rev → E1rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(415.56)):
        with BuildLine():
            RadiusArc((208.1, 10.0), (203.1, 15.0),  -5.0)   # E2rev
            Line((203.1, 15.0), ( 46.5, 15.0))               # E3rev
            RadiusArc(( 46.5, 15.0), ( 41.5, 10.0),  -5.0)   # E4rev
            Line(( 41.5, 10.0), ( 41.5,  3.2))               # E5
            Line(( 41.5,  3.2), (208.1,  3.2))               # E6rev
            Line((208.1,  3.2), (208.1, 10.0))               # E1rev
        make_face()
        with Locations((179.8, 9.7)): Circle(radius=2.175, mode=Mode.SUBTRACT)
        with Locations(( 69.8, 9.7)): Circle(radius=2.175, mode=Mode.SUBTRACT)
    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=369.549, extrude to Z=346.349)
    #          Traversal: E1 → E2 → E3 → E4
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(369.549)):
        with BuildLine():
            Line((20.6, 3.2), (22.2, 3.2))               # E1
            RadiusArc((22.2, 3.2), (23.8, 1.6),  -1.6)   # E2
            Line((23.8, 1.6), (23.8, 0.0))               # E3
            RadiusArc((23.8, 0.0), (20.6, 3.2), 3.2)   # E4
        make_face()
    extrude(amount=-23.2)

    # ---------------------------------------------------------
    # Feature: Slot with rounded rect subtraction
    #          (YZ Plane at X=22.2, extrude to X=20.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(22.2)):

        # ── Main profile ───────────────────────────────────────
        with BuildLine():
            Line(( 3.2, 369.549), (32.0, 369.549))               # E1rev
            RadiusArc((32.0, 369.549), (33.0, 368.549), 1.0)    # E2
            Line((33.0, 368.549), (33.0, 347.349))               # E3rev
            RadiusArc((33.0, 347.349), (32.0, 346.349), 1.0)    # E4
            Line((32.0, 346.349), ( 3.2, 346.349))               # E5
            Line(( 3.2, 346.349), ( 3.2, 369.549))               # E6rev
        make_face()

        # ── Circle subtraction ─────────────────────────────────
        with Locations((7.588, 362.049)): Circle(radius=2.175, mode=Mode.SUBTRACT)

        # ── Rounded rect slot subtraction ─────────────────────
        with BuildLine():
            Line((28.2, 353.1),   (28.2, 349.6))                 # E2
            RadiusArc((28.2, 349.6),  (27.4, 348.8),  0.8)     # E3
            Line((27.4, 348.8),   (10.3, 348.8))                 # E4
            RadiusArc((10.3, 348.8),  ( 9.5, 349.6),  0.8)     # E5
            Line(( 9.5, 349.6),   ( 9.5, 353.1))                 # E6
            RadiusArc(( 9.5, 353.1),  (10.3, 353.9),  0.8)     # E7
            Line((10.3, 353.9),   (27.4, 353.9))                 # E8
            RadiusArc((27.4, 353.9),  (28.2, 353.1),  0.8)     # E9
        make_face(mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

    # ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=223.1, extrude to Z=206.1)
    #          Traversal: E1 → E4 → E3rev → E2
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(223.1)):
        with BuildLine():
            RadiusArc((1.6, 3.2), (3.2, 1.6), -1.6)   # E1
            Line((3.2, 1.6), (3.2, 0.0))               # E4
            RadiusArc((3.2, 0.0), (0.0, 3.2), 3.2)   # E3rev
            Line((0.0, 3.2), (1.6, 3.2))               # E2
        make_face()
    extrude(amount=-17.0)

# ---------------------------------------------------------
    # Feature: Channel Profile (YZ Plane at X=1.6, extrude to X=0)
    #          Traversal: E1rev → E8rev → E7rev → E6rev → E5rev → E4 → E3rev → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            Line(( 3.2,  223.1),   (12.2,  223.1))                   # E1rev
            RadiusArc((12.2,  223.1),   (13.2,  222.1),    1.0)      # E2rev
            RadiusArc((13.2,  222.1),   (12.332, 221.092), 1.0)      # E3rev — snapped
            RadiusArc((12.332, 221.092), (12.332, 208.108), -6.55)   # E4
            RadiusArc((12.332, 208.108), (13.2,  207.117),  1.0)     # E5rev
            RadiusArc((13.2,  207.117),  (12.2,  206.1),    1.0)     # E6rev — snapped
            Line((12.2,  206.1),   ( 3.2,  206.1))                   # E7rev
            Line(( 3.2,  206.1),   ( 3.2,  223.1))                   # E8rev
        make_face()
    extrude(amount=-1.6)

    # ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=223.1, extrude to Z=206.1)
    #          Traversal: E1 → E4 → E3rev → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(223.1)):
        with BuildLine():
            RadiusArc((248.0, 3.2), (246.4, 1.6), 1.6)   # E1
            Line((246.4, 1.6), (246.4, 0.0))               # E4
            RadiusArc((246.4, 0.0), (249.6, 3.2), -3.2)   # E3rev
            Line((249.6, 3.2), (248.0, 3.2))               # E2rev
        make_face()
    extrude(amount=-17.0)

    # ---------------------------------------------------------
    # Feature: Channel Profile (YZ Plane at X=249.6, extrude to X=248.0)
    #          Traversal: E1rev→E2rev→E3rev→E4→E5rev→E6rev→E7→E8rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(249.6)):
        with BuildLine():
            Line(( 3.2,  223.1),   (12.2,  223.1))                   # E1rev
            RadiusArc((12.2,  223.1),   (13.2,  222.1),    1.0)      # E2rev
            RadiusArc((13.2,  222.1),   (12.332, 221.092), 1.0)      # E3rev — snapped
            RadiusArc((12.332, 221.092), (12.332, 208.108), -6.55)   # E4
            RadiusArc((12.332, 208.108), (13.2,  207.117),  1.0)     # E5rev
            RadiusArc((13.2,  207.117),  (12.2,  206.1),    1.0)     # E6rev — snapped
            Line((12.2,  206.1),   ( 3.2,  206.1))                   # E7
            Line(( 3.2,  206.1),   ( 3.2,  223.1))                   # E8rev
        make_face()
    extrude(amount=-1.6)

    # ---------------------------------------------------------
    # Feature: 10 Subtractive Profiles (XZ Plane at Y=1.6, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):

        for _ in range(2):
            with BuildLine():
                Line((31.15, 356.05), (31.15, 347.65))
                RadiusArc((31.15, 347.65), (31.4,  347.4),  -0.25)
                Line((31.4,  347.4),  (33.2,  347.4))
                RadiusArc((33.2,  347.4),  (33.45, 347.65), -0.25)
                Line((33.45, 347.65), (33.45, 356.05))
                RadiusArc((33.45, 356.05), (33.2,  356.3),  -0.25)
                Line((33.2,  356.3),  (31.4,  356.3))
                RadiusArc((31.4,  356.3),  (31.15, 356.05), -0.25)
            make_face()

        with BuildLine():                                          # P3
            RadiusArc(( 78.8, 391.685), ( 78.8, 388.01),  -1.838)
            Line(( 78.8, 388.01),  ( 91.75, 388.01))
            RadiusArc(( 91.75, 388.01),  ( 91.75, 391.685), -1.838)
            Line(( 91.75, 391.685), ( 78.8,  391.685))
        make_face()

        with BuildLine():                                          # P4 — chord=3.4 → r=1.701
            RadiusArc(( 16.1, 194.5), ( 16.1, 191.1), -1.701)
            Line(( 16.1, 191.1), ( 51.3, 191.1))
            RadiusArc(( 51.3, 191.1), ( 51.3, 194.5), -1.701)
            Line(( 51.3, 194.5), ( 16.1, 194.5))
        make_face()

        with BuildLine():                                          # P5
            RadiusArc(( 73.1, 194.5), ( 73.1, 191.1), -1.701)
            Line(( 73.1, 191.1), ( 98.3, 191.1))
            RadiusArc(( 98.3, 191.1), ( 98.3, 194.5), -1.701)
            Line(( 98.3, 194.5), ( 73.1, 194.5))
        make_face()

        with BuildLine():                                          # P6
            RadiusArc(( 16.1,  25.0), ( 16.1,  21.6), -1.701)
            Line(( 16.1,  21.6), ( 51.3,  21.6))
            RadiusArc(( 51.3,  21.6), ( 51.3,  25.0), -1.701)
            Line(( 51.3,  25.0), ( 16.1,  25.0))
        make_face()

        with BuildLine():                                          # P7
            RadiusArc(( 73.1,  25.0), ( 73.1,  21.6), -1.701)
            Line(( 73.1,  21.6), ( 98.3,  21.6))
            RadiusArc(( 98.3,  21.6), ( 98.3,  25.0), -1.701)
            Line(( 98.3,  25.0), ( 73.1,  25.0))
        make_face()

        with BuildLine():                                          # P8
            RadiusArc((161.75, 405.36),  (161.75, 401.685), -1.838)
            Line((161.75, 401.685), (174.7,  401.685))
            RadiusArc((174.7,  401.685), (174.7,  405.36),  -1.838)
            Line((174.7,  405.36),  (161.75, 405.36))
        make_face()

        with BuildLine():                                          # P9
            RadiusArc((161.75, 391.685), (161.75, 388.01),  -1.838)
            Line((161.75, 388.01),  (174.7,  388.01))
            RadiusArc((174.7,  388.01),  (174.7,  391.685), -1.838)
            Line((174.7,  391.685), (161.75, 391.685))
        make_face()

        with BuildLine():                                          # P10
            Line((188.175, 353.8),   (186.425, 353.8))
            RadiusArc((186.425, 353.8),   (185.425, 352.8),  -1.0)
            Line((185.425, 352.8),   (185.425, 345.8))
            RadiusArc((185.425, 345.8),   (184.425, 344.8),  +1.0)
            Line((184.425, 344.8),   (183.825, 344.8))
            RadiusArc((183.825, 344.8),   (182.825, 343.8),  -1.0)
            Line((182.825, 343.8),   (182.825, 282.8))
            RadiusArc((182.825, 282.8),   (183.825, 281.8),  -1.0)
            Line((183.825, 281.8),   (184.425, 281.8))
            RadiusArc((184.425, 281.8),   (185.425, 280.8),  +1.0)
            Line((185.425, 280.8),   (185.425, 274.3))
            RadiusArc((185.425, 274.3),   (186.425, 273.3),  -1.0)
            Line((186.425, 273.3),   (188.175, 273.3))
            RadiusArc((188.175, 273.3),   (189.175, 274.3),  -1.0)
            Line((189.175, 274.3),   (189.175, 280.8))
            RadiusArc((189.175, 280.8),   (190.175, 281.8),  +1.0)
            Line((190.175, 281.8),   (196.175, 281.8))
            RadiusArc((196.175, 281.8),   (197.175, 282.8),  -1.0)
            Line((197.175, 282.8),   (197.175, 343.8))
            RadiusArc((197.175, 343.8),   (196.175, 344.8),  -1.0)
            Line((196.175, 344.8),   (190.175, 344.8))
            RadiusArc((190.175, 344.8),   (189.175, 345.8),  +1.0)
            Line((189.175, 345.8),   (189.175, 352.8))
            RadiusArc((189.175, 352.8),   (188.175, 353.8),  -1.0)
        make_face()

    extrude(amount=1.6, mode=Mode.SUBTRACT)

# ---------------------------------------------------------
    # Feature: 36 Subtractive Circles (XZ Plane at Y=1.6, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-1.6)):
        with Locations(( 13.1,   389.149)): Circle(radius=2.25)    # 1
        with Locations(( 23.0,   392.36)):  Circle(radius=1.59)    # 2
        with Locations(( 43.0,   392.36)):  Circle(radius=1.59)    # 3
        with Locations(( 27.2,   351.85)):  Circle(radius=1.59)    # 4
        with Locations(( 41.6,   342.7)):   Circle(radius=1.725)   # 5
        with Locations(( 75.819, 294.2)):   Circle(radius=1.725)   # 6
        with Locations(( 75.819, 237.2)):   Circle(radius=1.725)   # 7
        with Locations(( 41.6,   222.2)):   Circle(radius=1.725)   # 8
        with Locations(( 17.1,   214.6)):   Circle(radius=1.59)    # 9
        with Locations((  8.6,   214.6)):   Circle(radius=1.59)    # 10
        with Locations((  8.4,    40.85)):  Circle(radius=1.725)   # 11
        with Locations(( 15.0,    40.85)):  Circle(radius=1.725)   # 12
        with Locations(( 23.0,    13.2)):   Circle(radius=1.59)    # 13
        with Locations(( 43.0,    13.2)):   Circle(radius=1.59)    # 14
        with Locations((114.8,   208.2)):   Circle(radius=1.59)    # 15
        with Locations((134.8,   208.2)):   Circle(radius=1.59)    # 16
        with Locations((166.1,   222.2)):   Circle(radius=1.725)   # 17
        with Locations((157.819, 237.2)):   Circle(radius=1.725)   # 18
        with Locations((157.819, 294.2)):   Circle(radius=1.725)   # 19
        with Locations((166.1,   342.7)):   Circle(radius=1.725)   # 20
        with Locations((187.4,   387.1)):   Circle(radius=1.59)    # 21
        with Locations((194.992, 348.8)):   Circle(radius=1.725)   # 22
        with Locations((194.992, 277.8)):   Circle(radius=1.725)   # 23
        with Locations((187.4,   262.55)):  Circle(radius=1.59)    # 24
        with Locations((206.6,   392.36)):  Circle(radius=1.59)    # 25
        with Locations((226.6,   392.36)):  Circle(radius=1.59)    # 26
        with Locations((236.5,   389.149)): Circle(radius=2.25)    # 27
        with Locations((192.392, 365.8)):   Circle(radius=9.75)    # 28
        with Locations((232.5,   214.6)):   Circle(radius=1.59)    # 29
        with Locations((241.0,   214.6)):   Circle(radius=1.59)    # 30
        with Locations((187.4,   143.175)): Circle(radius=1.59)    # 31
        with Locations((187.4,    23.8)):   Circle(radius=1.59)    # 32
        with Locations((206.6,    13.2)):   Circle(radius=1.59)    # 33
        with Locations((226.6,    13.2)):   Circle(radius=1.59)    # 34
        with Locations((234.6,    40.85)):  Circle(radius=1.725)   # 35
        with Locations((241.2,    40.85)):  Circle(radius=1.725)   # 36
    extrude(amount=1.6, mode=Mode.SUBTRACT)

from ocp_vscode import show
show(part)

export_stl(part.part, "output_PN-000645_v63.stl")