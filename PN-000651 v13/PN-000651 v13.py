from build123d import *
from ocp_vscode import show
import numpy as np

def get_mid(p1, p2, centre, r):
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
        mid_dir = perp / np.linalg.norm(perp)
    else:
        mid_dir = mid_dir / norm
    return tuple(c + mid_dir * r)

with BuildPart() as part:
    # ---------------------------------------------------------
    # Feature 1: Main Profile
    #            (YZ Plane offset to X=1.6, extrude to X=0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            # Continuous head-to-tail traversal
            Line((103.122, 119.0), (86.41, 119.0))
            ThreePointArc((86.41, 119.0), get_mid((86.41, 119.0), (81.41, 114.0), (86.41, 114.0), 5.0), (81.41, 114.0))
            Line((81.41, 114.0), (81.41, 105.0))
            ThreePointArc((81.41, 105.0), get_mid((81.41, 105.0), (76.41, 100.0), (76.41, 105.0), 5.0), (76.41, 100.0))
            Line((76.41, 100.0), (38.0, 100.0))
            ThreePointArc((38.0, 100.0), get_mid((38.0, 100.0), (33.0, 95.0), (38.0, 95.0), 5.0), (33.0, 95.0))
            Line((33.0, 95.0), (33.0, 93.0))
            ThreePointArc((33.0, 93.0), get_mid((33.0, 93.0), (28.0, 88.0), (28.0, 93.0), 5.0), (28.0, 88.0))
            Line((28.0, 88.0), (-45.0, 88.0))
            ThreePointArc((-45.0, 88.0), get_mid((-45.0, 88.0), (-50.0, 83.0), (-45.0, 83.0), 5.0), (-50.0, 83.0))
            Line((-50.0, 83.0), (-50.0, 17.0))
            ThreePointArc((-50.0, 17.0), get_mid((-50.0, 17.0), (-45.0, 12.0), (-45.0, 17.0), 5.0), (-45.0, 12.0))
            Line((-45.0, 12.0), (28.0, 12.0))
            ThreePointArc((28.0, 12.0), get_mid((28.0, 12.0), (33.0, 7.0), (28.0, 7.0), 5.0), (33.0, 7.0))
            Line((33.0, 7.0), (33.0, 5.0))
            ThreePointArc((33.0, 5.0), get_mid((33.0, 5.0), (38.0, 0.0), (38.0, 5.0), 5.0), (38.0, 0.0))
            Line((38.0, 0.0), (76.435, 0.0))
            ThreePointArc((76.435, 0.0), get_mid((76.435, 0.0), (80.611, -2.25), (76.435, -5.0), 5.0), (80.611, -2.25))
            ThreePointArc((80.611, -2.25), get_mid((80.611, -2.25), (84.787, -4.5), (84.787, 0.5), 5.0), (84.787, -4.5))
            Line((84.787, -4.5), (103.122, -4.5))
            Line((103.122, -4.5), (103.122, 3.0))
            
            # Sub-millimeter gap filler to connect Arc 22
            Line((103.122, 3.0), (103.072, 3.0))  
            
            ThreePointArc((103.072, 3.0), get_mid((103.072, 3.0), (102.322, 3.75), (103.072, 3.75), 0.75), (102.322, 3.75))
            Line((102.322, 3.75), (102.322, 96.25))
            ThreePointArc((102.322, 96.25), get_mid((102.322, 96.25), (103.072, 97.0), (103.072, 96.25), 0.75), (103.072, 97.0))
            
            # Sub-millimeter gap filler from Arc 24 to back edge
            Line((103.072, 97.0), (103.122, 97.0)) 
            
            Line((103.122, 97.0), (103.122, 119.0))
        make_face()
        
    # Extrude inward from X=1.6 down to X=0.0
    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature 1: Main Profile
    #            (XZ Plane offset to Y=104.722, extrude to Y=106.322)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-104.722)):
        with BuildLine():
            # Continuous head-to-tail traversal
            Line((3.2, 97.0), (3.2, 119.0))
            Line((3.2, 119.0), (4.0, 119.0))
            Line((4.0, 119.0), (4.0, 125.0))
            
            ThreePointArc((4.0, 125.0), get_mid((4.0, 125.0), (9.0, 130.0), (9.0, 125.0), 5.0), (9.0, 130.0))
            Line((9.0, 130.0), (60.6, 130.0))
            
            ThreePointArc((60.6, 130.0), get_mid((60.6, 130.0), (65.6, 125.0), (60.6, 125.0), 5.0), (65.6, 125.0))
            Line((65.6, 125.0), (65.6, -2.0))
            
            ThreePointArc((65.6, -2.0), get_mid((65.6, -2.0), (62.6, -5.0), (62.6, -2.0), 3.0), (62.6, -5.0))
            Line((62.6, -5.0), (48.6, -5.0))
            
            ThreePointArc((48.6, -5.0), get_mid((48.6, -5.0), (45.6, -8.0), (48.6, -8.0), 3.0), (45.6, -8.0))
            Line((45.6, -8.0), (45.6, -12.0))
            
            ThreePointArc((45.6, -12.0), get_mid((45.6, -12.0), (42.6, -15.0), (42.6, -12.0), 3.0), (42.6, -15.0))
            Line((42.6, -15.0), (16.1, -15.0))
            
            ThreePointArc((16.1, -15.0), get_mid((16.1, -15.0), (13.1, -12.0), (16.1, -12.0), 3.0), (13.1, -12.0))
            Line((13.1, -12.0), (13.1, -7.5))
            
            ThreePointArc((13.1, -7.5), get_mid((13.1, -7.5), (10.1, -4.5), (10.1, -7.5), 3.0), (10.1, -4.5))
            Line((10.1, -4.5), (3.2, -4.5))
            Line((3.2, -4.5), (3.2, 3.0))
            Line((3.2, 3.0), (55.4, 3.0))
            
            ThreePointArc((55.4, 3.0), get_mid((55.4, 3.0), (58.4, 6.0), (55.4, 6.0), 3.0), (58.4, 6.0))
            Line((58.4, 6.0), (58.4, 94.0))
            
            ThreePointArc((58.4, 94.0), get_mid((58.4, 94.0), (55.4, 97.0), (55.4, 94.0), 3.0), (55.4, 97.0))
            Line((55.4, 97.0), (3.2, 97.0))
            
        make_face()
        
    # Extrude outward in the positive Y direction (106.322 - 104.722 = 1.6)
    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature 1: Top L-Profile Arc
    #            (XY Plane offset to Z=119.0, extrude down to Z=97.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(119.0)):
        with BuildLine():
            # Continuous head-to-tail traversal
            Line((3.2, 106.322), (3.2, 104.722))
            
            # Inner arc (R=1.6)
            ThreePointArc((3.2, 104.722), 
                          get_mid((3.2, 104.722), (1.6, 103.122), (3.2, 103.122), 1.6), 
                          (1.6, 103.122))
            
            Line((1.6, 103.122), (0.0, 103.122))
            
            # Outer arc (R=3.2)
            ThreePointArc((0.0, 103.122), 
                          get_mid((0.0, 103.122), (3.2, 106.322), (3.2, 103.122), 3.2), 
                          (3.2, 106.322))
        make_face()
        
    # Extrude inward in the negative Z direction (97.0 - 119.0 = -22.0)
    extrude(amount=-22.0)

    # ---------------------------------------------------------
    # Feature 2: Bottom L-Profile Arc
    #            (XY Plane offset to Z=-4.5, extrude up to Z=3.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-4.5)):
        with BuildLine():
            # Continuous head-to-tail traversal
            Line((3.2, 104.722), (3.2, 106.322))
            
            # Outer arc (R=3.2)
            ThreePointArc((3.2, 106.322), 
                          get_mid((3.2, 106.322), (0.0, 103.122), (3.2, 103.122), 3.2), 
                          (0.0, 103.122))
            
            Line((0.0, 103.122), (1.6, 103.122))
            
            # Inner arc (R=1.6)
            ThreePointArc((1.6, 103.122), 
                          get_mid((1.6, 103.122), (3.2, 104.722), (3.2, 103.122), 1.6), 
                          (3.2, 104.722))
        make_face()
        
    # Extrude outward in the positive Z direction (3.0 - (-4.5) = 7.5)
    extrude(amount=7.5)

    with BuildSketch(Plane.YZ.offset(1.6)):
        
        # --- 1. Circular Holes ---
        with Locations(
            (87.705, 78.5),
            (87.705, 21.5),
            (40.0, 7.0),
            (5.705, 21.5),
            (5.705, 78.5),
            (40.0, 93.0)
        ):
            Circle(radius=1.725)
            
        with Locations((-17.0, 50.0)):
            Circle(radius=2.5)

        # --- 2. Profile 2 (Vertical Slot) ---
        # Arc centers: (-14.488, 68.05) and (-14.488, 81.0)
        # Midpoint: -14.4875, 74.525 | Separation: 12.95 | Height: 3.675
        with Locations((-14.4875, 74.525)):
            SlotCenterToCenter(center_separation=12.95, height=3.675, rotation=90)

        # --- 3. Profile 3 (Vertical Slot) ---
        # Arc centers: (-30.163, 68.05) and (-30.163, 81.0)
        # Midpoint: -30.1625, 74.525 | Separation: 12.95 | Height: 3.675
        with Locations((-30.1625, 74.525)):
            SlotCenterToCenter(center_separation=12.95, height=3.675, rotation=90)

        # --- 4. Profile 4 (Horizontal Slot) ---
        # Arc centers: (-30.05, 52.675) and (-43.0, 52.675)
        # Midpoint: -36.525, 52.675 | Separation: 12.95 | Height: 3.675
        with Locations((-36.525, 52.675)):
            SlotCenterToCenter(center_separation=12.95, height=3.675, rotation=0)

        # --- 5. Profile 5 (Horizontal Slot) ---
        # Arc centers: (-30.05, 37.0) and (-43.0, 37.0)
        # Midpoint: -36.525, 37.0 | Separation: 12.95 | Height: 3.675
        with Locations((-36.525, 37.0)):
            SlotCenterToCenter(center_separation=12.95, height=3.675, rotation=0)

    # Extrude inward in the negative X direction to reach X=0.0
    extrude(amount=-1.6, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Feature: Subtractive Circular Holes
    #          (XZ Plane offset to Y=-104.722, extrude to Y=106.322)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-104.722)):
        
        # Circle 1: (35.6, -9.0)
        # Circle 2: (59.6, 124.0)
        # Circle 3: (11.6, 124.0)
        with Locations(
            (35.6, -9.0),
            (59.6, 124.0),
            (11.6, 124.0)
        ):
            Circle(radius=2.175)

    # Extrude outward in the positive Y direction (106.322 - 104.722 = 1.6)
    extrude(amount=-1.6, mode=Mode.SUBTRACT)

if __name__ == "__main__":
    show(part)
    export_stl(part.part, "output_PN-000651_v13.stl")