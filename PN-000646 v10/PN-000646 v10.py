from build123d import *

# Part: PN-000646 v10

with BuildPart() as part:

    with BuildSketch(Plane.XY.offset(1.6)):

        # ── Main rectangular body ──────────────────────────────
        with BuildLine():
            Polyline([(26.6, 0.0), (226.4, 0.0), (226.4, 368.4),
                      (218.8, 368.4), (218.8, 368.9),
                      (218.0, 368.9), (218.0, 368.4),
                      ( 35.0, 368.4), ( 35.0, 368.9),
                      ( 34.2, 368.9), ( 34.2, 368.4),
                      ( 26.6, 368.4)], close=True)
        make_face()

        # ── Left circular boss (349.2° arc + closing chord) ───
        with BuildLine():
            CenterArc(center=(34.6, 373.131), radius=4.25,
                      start_angle=275.4, arc_size=349.2)
            Line((34.2, 368.9), (35.0, 368.9))
        make_face()

        # ── Right circular boss (349.2° arc + closing chord) ──
        with BuildLine():
            CenterArc(center=(218.4, 373.131), radius=4.25,
                      start_angle=275.4, arc_size=349.2)
            Line((218.0, 368.9), (218.8, 368.9))
        make_face()

        # ── Subtract rectangles (41 rows × 2 groups) ──────────
        y_values = [43, 50, 57, 64, 71, 78, 85, 92, 99, 106,
                    113, 120, 127, 134, 141, 148, 155, 162, 169,
                    176, 183, 190, 197, 204, 211, 218, 225, 232,
                    239, 246, 253, 260, 267, 274, 281, 288, 295,
                    302, 309, 316, 323]
        h = 3.175
        for y in y_values:
            with BuildLine():
                Polyline([( 63.74, y), (137.4,  y),
                           (137.4,  y+h), ( 63.74, y+h)], close=True)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Polyline([(143.74, y), (217.4,  y),
                           (217.4,  y+h), (143.74, y+h)], close=True)
            make_face(mode=Mode.SUBTRACT)

        # ── Subtract inner circles ─────────────────────────────
        with Locations(( 34.6, 373.131)): Circle(radius=2.25, mode=Mode.SUBTRACT)
        with Locations((218.4, 373.131)): Circle(radius=2.25, mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature: 2 Corner Arc Profiles (XZ Plane at Y=368.4, extrude to Y=0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-368.4)):

        # ── Profile 1: right corner ────────────────────────────
        # Traversal: E1 → E2 → E3 → E4
        with BuildLine():
            Line((226.4,  1.6), (226.4,  0.0))                  # E1
            RadiusArc((226.4,  0.0), (253.0, 26.6), -26.6)      # E2
            Line((253.0, 26.6), (251.4, 26.6))                   # E3
            RadiusArc((251.4, 26.6), (226.4,  1.6),  25.0)      # E4
        make_face()

        # ── Profile 2: left corner ─────────────────────────────
        # Traversal: E1 → E4rev → E3 → E2rev
        with BuildLine():
            Line(( 26.6,  0.0), ( 26.6,  1.6))                  # E1
            RadiusArc(( 26.6,  1.6), (  1.6, 26.6),  25.0)      # E4rev
            Line((  1.6, 26.6), (  0.0, 26.6))                   # E3
            RadiusArc((  0.0, 26.6), ( 26.6,  0.0), -26.6)      # E2rev
        make_face()

    extrude(amount=368.4)

# ---------------------------------------------------------
    # Feature: Profile 1 (YZ Plane at X=251.4, extrude to X=253.0)
    #          Traversal: E1rev → E2 → E3rev → E4 → E5 → E6rev
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(251.4)):
        with BuildLine():
            Line((368.4, 26.6), (368.4, 34.0))               # E1rev
            RadiusArc((368.4, 34.0), (366.4, 36.0),  2.0)    # E2
            Line((366.4, 36.0), (  2.0, 36.0))               # E3rev
            RadiusArc((  2.0, 36.0), (  0.0, 34.0),  2.0)    # E4
            Line((  0.0, 34.0), (  0.0, 26.6))               # E5
            Line((  0.0, 26.6), (368.4, 26.6))               # E6rev
        make_face()
    extrude(amount=1.6)

    # ---------------------------------------------------------
    # Feature: Profile 2 (YZ Plane at X=1.6, extrude to X=0.0)
    #          Traversal: E1rev → E2rev → E3 → E4rev → E5 → E6
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            Line((368.4, 26.6), (368.4, 34.0))               # E1rev
            RadiusArc((368.4, 34.0), (366.4, 36.0),  2.0)    # E2rev
            Line((366.4, 36.0), (  2.0, 36.0))               # E3
            RadiusArc((  2.0, 36.0), (  0.0, 34.0),  2.0)    # E4rev
            Line((  0.0, 34.0), (  0.0, 26.6))               # E5
            Line((  0.0, 26.6), (368.4, 26.6))               # E6
        make_face()
    extrude(amount=-1.6)

from ocp_vscode import show
show(part)

export_stl(part.part, "output_PN-000646_v10.stl")