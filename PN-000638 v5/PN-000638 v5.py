from build123d import *
from ocp_vscode import show
import numpy as np

def get_mid(p1, p2, centre, r, flip=False):
    """Calculates the exact midpoint of a minor arc."""
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
    # (XY Plane offset to Z = 1.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(1.6)):
        
        # --- 1. Outer Boundary ---
        with BuildLine(mode=Mode.PRIVATE) as outer:
            # Traversed counter-clockwise (or sequentially based on endpoints)
            
            p_start = (-5.4, 55.0)
            p1 = (-10.4, 50.0)
            p2 = (-10.4, 48.0)
            p3 = (-6.933, 43.241)
            p4 = (0.0, 33.723)
            p5 = (0.0, 5.0)
            p6 = (5.0, 0.0)
            p7 = (6.733, 0.0)
            p8 = (11.416, 3.25)
            p9 = (16.1, 6.5)
            p10 = (93.233, 6.5)
            p11 = (97.916, 3.25)
            p12 = (102.6, 0.0)
            p13 = (103.7, 0.0)
            p14 = (108.7, 5.0)
            p15 = (108.7, 33.0)
            p16 = (115.633, 42.518)
            p17 = (119.1, 47.277)
            p18 = (119.1, 50.0)
            p19 = (114.1, 55.0)
            p20 = (100.6, 55.0)
            p21 = (97.6, 52.0)
            p22 = (97.6, 50.5)
            p23 = (94.6, 47.5)
            p24 = (14.1, 47.5)
            p25 = (11.1, 50.5)
            p26 = (11.1, 52.0)
            p27 = (8.1, 55.0)
            
            # Edge 1 to 28
            ThreePointArc(p_start, get_mid(p_start, p1, (-5.4, 50.0), 5.0), p1)
            Line(p1, p2)
            ThreePointArc(p2, get_mid(p2, p3, (-5.4, 48.0), 5.0), p3)
            ThreePointArc(p3, get_mid(p3, p4, (-10.0, 33.723), 10.0), p4)
            Line(p4, p5)
            ThreePointArc(p5, get_mid(p5, p6, (5.0, 5.0), 5.0), p6)
            Line(p6, p7)
            ThreePointArc(p7, get_mid(p7, p8, (6.733, 5.0), 5.0), p8)
            ThreePointArc(p8, get_mid(p8, p9, (16.1, 1.5), 5.0), p9)
            Line(p9, p10)
            ThreePointArc(p10, get_mid(p10, p11, (93.233, 1.5), 5.0), p11)
            ThreePointArc(p11, get_mid(p11, p12, (102.6, 5.0), 5.0), p12)
            Line(p12, p13)
            ThreePointArc(p13, get_mid(p13, p14, (103.7, 5.0), 5.0), p14)
            Line(p14, p15)
            ThreePointArc(p15, get_mid(p15, p16, (118.7, 33.0), 10.0), p16)
            ThreePointArc(p16, get_mid(p16, p17, (114.1, 47.277), 5.0), p17)
            Line(p17, p18)
            ThreePointArc(p18, get_mid(p18, p19, (114.1, 50.0), 5.0), p19)
            Line(p19, p20)
            ThreePointArc(p20, get_mid(p20, p21, (100.6, 52.0), 3.0), p21)
            Line(p21, p22)
            ThreePointArc(p22, get_mid(p22, p23, (94.6, 50.5), 3.0), p23)
            Line(p23, p24)
            ThreePointArc(p24, get_mid(p24, p25, (14.1, 50.5), 3.0), p25)
            Line(p25, p26)
            ThreePointArc(p26, get_mid(p26, p27, (8.1, 52.0), 3.0), p27)
            Line(p27, p_start)
            
        make_face(outer.edges())
        
        # --- 2. Subtraction: Central Slot ---
        with BuildLine(mode=Mode.PRIVATE) as slot:
            s_p1 = (14.1, 39.0)
            s_p2 = (11.1, 36.0)
            s_p3 = (11.1, 28.0)
            s_p4 = (14.1, 25.0)
            s_p5 = (94.6, 25.0)
            s_p6 = (97.6, 28.0)
            s_p7 = (97.6, 36.0)
            s_p8 = (94.6, 39.0)
            
            ThreePointArc(s_p1, get_mid(s_p1, s_p2, (14.1, 36.0), 3.0), s_p2)
            Line(s_p2, s_p3)
            ThreePointArc(s_p3, get_mid(s_p3, s_p4, (14.1, 28.0), 3.0), s_p4)
            Line(s_p4, s_p5)
            ThreePointArc(s_p5, get_mid(s_p5, s_p6, (94.6, 28.0), 3.0), s_p6)
            Line(s_p6, s_p7)
            ThreePointArc(s_p7, get_mid(s_p7, s_p8, (94.6, 36.0), 3.0), s_p8)
            Line(s_p8, s_p1)
            
        make_face(slot.edges(), mode=Mode.SUBTRACT)

        # --- 3. Subtractions: 6 Circular Holes ---
        hole_locations = [
            (-6.0, 50.081),
            (8.0, 43.389),
            (8.0, 13.389),
            (100.7, 13.389),
            (100.7, 43.389),
            (114.7, 50.081)
        ]
        with Locations(*hole_locations):
            Circle(radius=1.725, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Extrude to target point Z = 0.0
    # 0.0 - 1.6 = -1.6 mm
    # ---------------------------------------------------------
    extrude(amount=-1.6)

if __name__ == "__main__":
    # Export STL 
    export_stl(part.part, "output_PN-000638_v5.stl")
    
    # Visualize
    try:
        from ocp_vscode import show_all
        show_all()
    except ImportError:
        pass