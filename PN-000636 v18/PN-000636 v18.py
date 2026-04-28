from build123d import *
from ocp_vscode import show
import numpy as np

def to_2d(p3d):
    """Maps a 3D coordinate on the 50-degree plane to the local 2D sketch coordinate."""
    return (np.hypot(p3d[0], p3d[2]), p3d[1])

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
        # Handles 180-degree arcs (semi-circles)
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
    # (XZ Plane offset to Y = 288.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-288.0)):
        with BuildLine():
            # Continuous traversal using (X, Z) coordinates
            
            p1 = (8.389, 8.022)
            p2 = (7.416, 8.838)
            p3 = (7.713, 9.655)
            p4 = (7.713, 32.08)
            p5 = (6.443, 33.35)
            p6 = (-57.147, 33.35)
            p7 = (-58.417, 32.08)
            p8 = (-59.687, 32.08)
            p9 = (-57.147, 34.62)
            p10 = (6.443, 34.62)
            p11 = (8.983, 32.08)
            p12 = (8.983, 9.655)

            # Edge 1 (Line)
            Line(p1, p2)
            
            # Edge 2 (Inner Arc R1.27)
            ThreePointArc(p2, get_mid(p2, p3, (6.443, 9.655), 1.27), p3)
            
            # Edge 3 (Vertical Line)
            Line(p3, p4)
            
            # Edge 4 (Inner Arc R1.27)
            ThreePointArc(p4, get_mid(p4, p5, (6.443, 32.08), 1.27), p5)
            
            # Edge 5 (Horizontal Line)
            Line(p5, p6)
            
            # Edge 6 (Inner Arc R1.27)
            ThreePointArc(p6, get_mid(p6, p7, (-57.147, 32.08), 1.27), p7)
            
            # Edge 7 (Horizontal Line offset)
            Line(p7, p8)
            
            # Edge 8 (Outer Arc R2.54)
            ThreePointArc(p8, get_mid(p8, p9, (-57.147, 32.08), 2.54), p9)
            
            # Edge 9 (Horizontal Line top)
            Line(p9, p10)
            
            # Edge 10 (Outer Arc R2.54)
            ThreePointArc(p10, get_mid(p10, p11, (6.443, 32.08), 2.54), p11)
            
            # Edge 11 (Vertical Line)
            Line(p11, p12)
            
            # Edge 12 (Outer Arc R2.54, closing back to p1)
            ThreePointArc(p12, get_mid(p12, p1, (6.443, 9.655), 2.54), p1)
            
        make_face()

    # ---------------------------------------------------------
    # Extrude to target point Y = 258.0
    # 258.0 - 288.0 = -30.0 mm
    # ---------------------------------------------------------
    extrude(amount=30.0)

# ---------------------------------------------------------
    # Profile Sketch 
    # (YZ Plane offset to X = -59.687)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(-59.687)):
        with BuildLine():
            # Continuous traversal using (Y, Z) coordinates
            p1 = (288.0, 32.08)
            p2 = (288.0, 25.62)
            p3 = (285.0, 22.62)
            p4 = (261.0, 22.62)
            p5 = (258.0, 25.62)
            p6 = (258.0, 32.08)
            
            # Edge 1 (Vertical Line)
            Line(p1, p2)
            
            # Edge 2 (Arc R3.0)
            ThreePointArc(p2, get_mid(p2, p3, (285.0, 25.62), 3.0), p3)
            
            # Edge 3 (Horizontal Line)
            Line(p3, p4)
            
            # Edge 4 (Arc R3.0)
            ThreePointArc(p4, get_mid(p4, p5, (261.0, 25.62), 3.0), p5)
            
            # Edge 5 (Vertical Line)
            Line(p5, p6)
            
            # Edge 6 (Top Horizontal Line, closing the loop)
            Line(p6, p1)
            
        make_face()
        
        # --- Subtractions: Circular Mounting Holes ---
        # Mapped to (Y, Z) coordinates
        with Locations((282.0, 26.85), (264.0, 26.85)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Extrude to target point X = -58.417
    # -58.417 - (-59.687) = 1.27 mm
    # ---------------------------------------------------------
    extrude(amount=1.27)

    # ---------------------------------------------------------
    # Profile Sketch 
    # (Plane rotated -50 degrees around Y-axis)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.rotated((0, -50, 0))):
        with BuildLine():
            # Continuous traversal mapping 3D coordinates to the 2D plane
            p1  = to_2d((7.416, 357.0, 8.838))
            p2  = to_2d((1.928, 357.0, 2.298))
            p3  = to_2d((0.0, 354.0, 0.0))
            c2  = to_2d((1.928, 354.0, 2.298))
            p4  = to_2d((0.0, 3.0, 0.0))
            p5  = to_2d((1.928, 0.0, 2.298))
            c4  = to_2d((1.928, 3.0, 2.298))
            p6  = to_2d((7.416, 0.0, 8.838))
            p7  = to_2d((7.416, 19.5, 8.838))
            p8  = to_2d((7.135, 19.5, 8.503))
            p9  = to_2d((6.492, 20.5, 7.737))
            c8  = to_2d((7.135, 20.5, 8.503))
            p10 = to_2d((6.492, 257.0, 7.737))
            p11 = to_2d((7.135, 258.0, 8.503))
            c10 = to_2d((7.135, 257.0, 8.503))
            p12 = to_2d((7.416, 258.0, 8.838))
            p13 = to_2d((7.416, 288.0, 8.838))
            p14 = to_2d((7.135, 288.0, 8.503))
            p15 = to_2d((6.492, 289.0, 7.737))
            c14 = to_2d((7.135, 289.0, 8.503))
            p16 = to_2d((6.492, 336.5, 7.737))
            p17 = to_2d((7.135, 337.5, 8.503))
            c16 = to_2d((7.135, 336.5, 8.503))
            p18 = to_2d((7.416, 337.5, 8.838))
            p19 = to_2d((7.416, 357.0, 8.838))

            # Draw the 18 edges to form a closed continuous loop
            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, c2, 3.0), p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, c4, 3.0), p5)
            Line(p5, p6)
            Line(p6, p7)
            Line(p7, p8)
            ThreePointArc(p8, get_mid(p8, p9, c8, 1.0), p9)
            Line(p9, p10)
            ThreePointArc(p10, get_mid(p10, p11, c10, 1.0), p11)
            Line(p11, p12)
            Line(p12, p13)
            Line(p13, p14)
            ThreePointArc(p14, get_mid(p14, p15, c14, 1.0), p15)
            Line(p15, p16)
            ThreePointArc(p16, get_mid(p16, p17, c16, 1.0), p17)
            Line(p17, p18)
            Line(p18, p19)  # Closes exactly back to p1
            
        make_face()
        
        # --- Subtractions: 5 Circular Mounting Holes ---
        hole_centers = [
            to_2d((2.957, 351.0, 3.524)),
            to_2d((2.957, 343.5, 3.524)),
            to_2d((2.957, 178.5, 3.524)),
            to_2d((2.957, 13.5, 3.524)),
            to_2d((2.957, 6.0, 3.524))
        ]
        
        with Locations(*hole_centers):
            Circle(radius=1.59, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Extrude to target point along the local normal
    # Distance to (0.973, 3.0, -0.816) = -1.27 mm
    # ---------------------------------------------------------
    extrude(amount=-1.27)

# =========================================================
    # FEATURE 4: XZ End-Cap Profile
    # =========================================================
    with BuildSketch(Plane.XZ.offset(0.0)):
        with BuildLine():
            ec_pA = (7.713, 9.655)
            ec_pB = (7.416, 8.838)
            ec_pC = (8.389, 8.022)
            ec_pD = (8.983, 9.655)

            ThreePointArc(ec_pA, get_mid(ec_pA, ec_pB, (6.443, 9.655), 1.27), ec_pB)
            Line(ec_pB, ec_pC)
            ThreePointArc(ec_pC, get_mid(ec_pC, ec_pD, (6.443, 9.655), 2.54), ec_pD)
            Line(ec_pD, ec_pA)
        make_face()
    
    # 19.5 - 0.0 = 19.5 mm
    extrude(amount=-19.5)
# =========================================================
    # FEATURE 5: YZ Scalloped End-Cap Profile
    # =========================================================
    with BuildSketch(Plane.YZ.offset(7.713)):
        with BuildLine():
            s_p1 = (0.0, 9.655)
            s_p2 = (0.0, 27.044)
            s_p3 = (1.0, 28.044)
            s_p4 = (2.267, 28.044)
            s_p5 = (3.258, 27.176)
            s_p6 = (16.242, 27.176)
            s_p7 = (17.233, 28.044)
            s_p8 = (18.5, 28.044)
            s_p9 = (19.5, 27.044)
            s_p10 = (19.5, 9.655)

            Line(s_p1, s_p2)
            ThreePointArc(s_p2, get_mid(s_p2, s_p3, (1.0, 27.044), 1.0), s_p3)
            Line(s_p3, s_p4)
            ThreePointArc(s_p4, get_mid(s_p4, s_p5, (2.267, 27.044), 1.0), s_p5)
            ThreePointArc(s_p5, get_mid(s_p5, s_p6, (9.75, 28.044), 6.55), s_p6)
            ThreePointArc(s_p6, get_mid(s_p6, s_p7, (17.233, 27.044), 1.0), s_p7)
            Line(s_p7, s_p8)
            ThreePointArc(s_p8, get_mid(s_p8, s_p9, (18.5, 27.044), 1.0), s_p9)
            Line(s_p9, s_p10)
            Line(s_p10, s_p1) # Closes the loop
        make_face()
    extrude(amount=1.27)

    # =========================================================
    # FEATURE 6: XZ End-Cap Profile (Top)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-357.0)):
        with BuildLine():
            ec2_pA = (7.713, 9.655)
            ec2_pB = (7.416, 8.838)
            ec2_pC = (8.389, 8.022)
            ec2_pD = (8.983, 9.655)

            ThreePointArc(ec2_pA, get_mid(ec2_pA, ec2_pB, (6.443, 9.655), 1.27), ec2_pB)
            Line(ec2_pB, ec2_pC)
            ThreePointArc(ec2_pC, get_mid(ec2_pC, ec2_pD, (6.443, 9.655), 2.54), ec2_pD)
            Line(ec2_pD, ec2_pA)
        make_face()
    extrude(amount=19.5)

# =========================================================
    # FEATURE 7: YZ Scalloped End-Cap Profile (Top)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(7.713)):
        with BuildLine():
            s2_p1 = (337.5, 9.655)
            s2_p2 = (337.5, 27.044)
            s2_p3 = (338.5, 28.044)
            s2_p4 = (339.767, 28.044)
            s2_p5 = (340.758, 27.176)
            s2_p6 = (353.742, 27.176)
            s2_p7 = (354.733, 28.044)
            s2_p8 = (356.0, 28.044)
            s2_p9 = (357.0, 27.044)
            s2_p10 = (357.0, 9.655)

            Line(s2_p1, s2_p2)
            ThreePointArc(s2_p2, get_mid(s2_p2, s2_p3, (338.5, 27.044), 1.0), s2_p3)
            Line(s2_p3, s2_p4)
            ThreePointArc(s2_p4, get_mid(s2_p4, s2_p5, (339.767, 27.044), 1.0), s2_p5)
            ThreePointArc(s2_p5, get_mid(s2_p5, s2_p6, (347.25, 28.044), 6.55), s2_p6)
            ThreePointArc(s2_p6, get_mid(s2_p6, s2_p7, (354.733, 27.044), 1.0), s2_p7)
            Line(s2_p7, s2_p8)
            ThreePointArc(s2_p8, get_mid(s2_p8, s2_p9, (356.0, 27.044), 1.0), s2_p9)
            Line(s2_p9, s2_p10)
            Line(s2_p10, s2_p1) 
        make_face()
    extrude(amount=1.27)
    
if __name__ == "__main__":
    export_stl(part.part, "output_PN-000636_v18.stl")
    show(part)