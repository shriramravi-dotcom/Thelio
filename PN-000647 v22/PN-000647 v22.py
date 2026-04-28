from build123d import *

# Part: PN-000647 v22

with BuildPart() as part:

    with BuildSketch(Plane.YZ.offset(1.6)):

        # ── Main Profile ───────────────────────────────────────
        with BuildLine():
            Line((-368.8,   2.0),  (-368.8, 350.8))              # E6
            RadiusArc((-368.8, 350.8), (-366.8, 352.8), 2.0)    # E1
            Line((-366.8, 352.8),  (  -1.6, 352.8))              # E2rev
            Line((  -1.6, 352.8),  (  -1.6,   0.0))              # E3rev
            Line((  -1.6,   0.0),  (-366.8,   0.0))              # E4rev
            RadiusArc((-366.8,   0.0), (-368.8,   2.0), 2.0)    # E5
        make_face()

        # ── Subtract: large rounded rect ──────────────────────
        with BuildLine():
            RadiusArc(( -44.0,  325.0),  ( -40.75, 321.75), 3.25)  # E1
            Line(( -40.75, 321.75), ( -40.75, 165.41))               # E2
            RadiusArc(( -40.75, 165.41),  ( -44.0,  162.16), 3.25) # E3
            Line(( -44.0,  162.16), (-323.9,  162.16))               # E4
            RadiusArc((-323.9,  162.16), (-327.15, 165.41), 3.25)  # E5
            Line((-327.15, 165.41), (-327.15, 321.75))               # E6
            RadiusArc((-327.15, 321.75), (-323.9,  325.0),  3.25)  # E7
            Line((-323.9,  325.0),  ( -44.0,  325.0))               # E8
        make_face(mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=352.8, extrude to Z=0)
    #          Traversal: E1 → E4 → E3rev → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(352.8)):
        with BuildLine():
            Line((3.2,  1.6), (3.2,  0.0))                # E1
            RadiusArc((3.2,  0.0), (1.6, -1.6), -1.6)     # E4
            Line((1.6, -1.6), (0.0, -1.6))                 # E3rev
            RadiusArc((0.0, -1.6), (3.2,  1.6), 3.2)     # E2rev
        make_face()
    extrude(amount=-352.8)

    with BuildSketch(Plane.XZ):
        with BuildLine():
            RadiusArc(( 7.0, 352.8),   (12.0, 347.8),    5.0)
            Line((12.0, 347.8),   (12.0, 345.232))
            RadiusArc((12.0, 345.232), (17.0, 340.232),  -5.0)
            Line((17.0, 340.232), (25.6, 340.232))
            Line((25.6, 340.232), (25.6, 307.8))
            Line((25.6, 307.8),   (17.0, 307.8))
            RadiusArc((17.0, 307.8),   (12.0, 302.8),   -5.0)
            Line((12.0, 302.8),   (12.0, 187.7))
            RadiusArc((12.0, 187.7),   (10.0, 185.7),    2.0)
            Line((10.0, 185.7),   ( 8.5, 185.7))
            RadiusArc(( 8.5, 185.7),   ( 6.5, 183.7),   -2.0)
            Line(( 6.5, 183.7),   ( 6.5, 177.7))
            RadiusArc(( 6.5, 177.7),   ( 8.5, 175.7),   -2.0)
            Line(( 8.5, 175.7),   (10.0, 175.7))
            RadiusArc((10.0, 175.7),   (12.0, 173.7),    2.0)
            Line((12.0, 173.7),   (12.0,  26.965))
            RadiusArc((12.0,  26.965), (13.75, 24.98),  -2.0)
            RadiusArc((13.75,  24.98), (15.5,  22.996),  2.0)
            Line((15.5,  22.996), (15.5,  13.9))
            RadiusArc((15.5,  13.9),   (13.5,  11.9),    2.0)
            Line((13.5,  11.9),   ( 8.5,  11.9))
            RadiusArc(( 8.5,  11.9),   ( 6.5,   9.9),   -2.0)
            Line(( 6.5,   9.9),   ( 6.5,   2.0))
            RadiusArc(( 6.5,   2.0),   ( 4.5,   0.0),    2.0)
            Line(( 4.5,   0.0),   ( 3.2,   0.0))
            Line(( 3.2,   0.0),   ( 3.2, 352.8))
            Line(( 3.2, 352.8),   ( 7.0, 352.8))
        make_face()

        # ── Subtract stadium 1: centers (8.5,19.996)↔(10.0,19.996)
        #    center_separation=1.5, height=4.0, horizontal (along X)
        with Locations((9.25, 19.996)):
            SlotCenterToCenter(center_separation=1.5, height=4.0,
                               mode=Mode.SUBTRACT)

        # ── Subtract stadium 2: centers (10.0,322.3)↔(11.5,322.3)
        #    center_separation=1.5, height=4.0, horizontal (along X)
        with Locations((10.75, 322.3)):
            SlotCenterToCenter(center_separation=1.5, height=4.0,
                               mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: Arc Profile (XY Plane at Z=340.232, extrude to Z=307.8)
    #          Traversal: E1 → E4rev → E3rev → E2rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(340.232)):
        with BuildLine():
            RadiusArc((27.2, 3.2), (25.6, 1.6),  1.6)   # E1
            Line((25.6, 1.6), (25.6, 0.0))               # E4rev
            RadiusArc((25.6, 0.0), (28.8, 3.2),  -3.2)   # E3rev
            Line((28.8, 3.2), (27.2, 3.2))               # E2rev
        make_face()
    extrude(amount=-32.432)

# ---------------------------------------------------------
    # Feature: Side Profile (YZ Plane at X=28.8, extrude to X=27.2)
    #          Traversal: E1rev → E2 → E3rev → E4 → E5 → E6rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(28.8)):
        with BuildLine():
            Line(( 3.2, 340.232), ( 7.0, 340.232))               # E1rev
            RadiusArc(( 7.0, 340.232), (12.0, 335.232), 5.0)    # E2
            Line((12.0, 335.232), (12.0, 312.8))                  # E3rev
            RadiusArc((12.0, 312.8),   ( 7.0, 307.8),  5.0)    # E4
            Line(( 7.0, 307.8),   ( 3.2, 307.8))                  # E5
            Line(( 3.2, 307.8),   ( 3.2, 340.232))               # E6rev
        make_face()
    extrude(amount=-1.6)

from ocp_vscode import show
show(part)

export_stl(part.part, "output_PN-000647_v22.stl")