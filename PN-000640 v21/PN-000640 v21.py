from build123d import *
import numpy as np

def get_mid(p1, p2, centre, r, flip=False):
    """Calculates the midpoint of an arc. Set flip=True to reverse concavity."""
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

# Constants based on provided coordinates
plane_y = 111.685
target_y = 113.285
extrude_amount = target_y - plane_y  # -1.6 mm

# Dimensions for internal slits
slit_width = 3.175
slit_height = 73.66
slit_z_center = -76.0  # Midpoint of -112.83 and -39.17

# List of starting X coordinates for the 11 slits
slit_x_starts = [
    117.723, 109.549, 101.374, 93.198, 85.023, 
    76.849, 68.674, 60.499, 52.324, 44.149, 35.974
]

with BuildPart() as part:
    # Sketch on the XZ plane at Y = 111.685
    with BuildSketch(Plane.XZ.offset(plane_y)):
        # Main rectangular boundary
        with BuildLine():
            p1 = (129.586, -147.37)
            p2 = (27.286, -147.37)
            p3 = (27.286, -4.63)
            p4 = (129.586, -4.63)
            Polyline([p1, p2, p3, p4, p1])
        make_face()
        
        # Subtraction of the 11 rectangular slits
        for x in slit_x_starts:
            # Calculate the center for build123d's Rectangle placement
            x_center = x + (slit_width / 2)
            with Locations((x_center, slit_z_center)):
                Rectangle(slit_width, slit_height, mode=Mode.SUBTRACT)
                
    # Extrude the sketched face to the target coordinate
    extrude(amount=extrude_amount)
# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -147.37)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-147.37)):
        with BuildLine():
            # Edge 1: Inner Arc (Radius 1.6)
            ThreePointArc((25.686, -110.085), 
                          get_mid((25.686, -110.085), (27.286, -111.685), (27.286, -110.085), 1.6), 
                          (27.286, -111.685))
            
            # Edge 4: Vertical Line
            Line((27.286, -111.685), (27.286, -113.285))
            
            # Edge 3: Outer Arc (Radius 3.2)
            ThreePointArc((27.286, -113.285), 
                          get_mid((27.286, -113.285), (24.086, -110.085), (27.286, -110.085), 3.2), 
                          (24.086, -110.085))
            
            # Edge 2: Horizontal Line
            Line((24.086, -110.085), (25.686, -110.085))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -4.63
    # -4.63 - (-147.37) = 142.74 mm
    # ---------------------------------------------------------
    extrude(amount=142.74)

    # ---------------------------------------------------------
    # Profile Sketch 
    # (YZ Plane offset to X = 25.686)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(25.686)):
        with BuildLine():
            # Traversal using (Y, Z) coordinates
            
            # Bottom Section
            Line((-110.085, -147.37), (-104.185, -147.37)) # Edge 1
            Line((-104.185, -147.37), (-104.085, -147.37)) # Edge 2
            
            # Edge 3: Bottom Corner Arc
            ThreePointArc((-104.085, -147.37), 
                          get_mid((-104.085, -147.37), (-102.085, -145.37), (-104.085, -145.37), 2.0), 
                          (-102.085, -145.37))
            
            Line((-102.085, -145.37), (-102.085, -30.74))  # Edge 4
            
            # --- Edge 5: TOP ARC (Flipped to curve Outward) ---
            ThreePointArc((-102.085, -30.74), 
                          get_mid((-102.085, -30.74), (-95.285, -30.74), (-98.685, -30.74), 3.4, flip=True), 
                          (-95.285, -30.74))
            
            Line((-95.285, -30.74), (-95.285, -145.37))    # Edge 6
            
            # Edge 7: Bottom Corner Arc
            ThreePointArc((-95.285, -145.37), 
                          get_mid((-95.285, -145.37), (-93.285, -147.37), (-93.285, -145.37), 2.0), 
                          (-93.285, -147.37))
            
            Line((-93.285, -147.37), (-93.185, -147.37))   # Edge 8
            Line((-93.185, -147.37), (-72.385, -147.37))   # Edge 9
            Line((-72.385, -147.37), (-72.285, -147.37))   # Edge 10
            
            # Edge 11: Bottom Corner Arc
            ThreePointArc((-72.285, -147.37), 
                          get_mid((-72.285, -147.37), (-70.285, -145.37), (-72.285, -145.37), 2.0), 
                          (-70.285, -145.37))
            
            Line((-70.285, -145.37), (-70.285, -30.74))    # Edge 12
            
            # --- Edge 13: TOP ARC (Flipped to curve Outward) ---
            ThreePointArc((-70.285, -30.74), 
                          get_mid((-70.285, -30.74), (-63.485, -30.74), (-66.885, -30.74), 3.4, flip=True), 
                          (-63.485, -30.74))
            
            Line((-63.485, -30.74), (-63.485, -145.37))    # Edge 14
            
            # Edge 15: Bottom Corner Arc
            ThreePointArc((-63.485, -145.37), 
                          get_mid((-63.485, -145.37), (-61.485, -147.37), (-61.485, -145.37), 2.0), 
                          (-61.485, -147.37))
            
            # Closing the profile
            Line((-61.485, -147.37), (-61.385, -147.37))   # Edge 16
            Line((-61.385, -147.37), (-50.8, -147.37))     # Edge 17
            Line((-50.8, -147.37), (-50.8, -147.17))       # Edge 18
            Line((-50.8, -147.17), (-50.0, -147.17))       # Edge 19
            Line((-50.0, -147.17), (-50.0, -145.57))       # Edge 20
            Line((-50.0, -145.57), (-50.0, -3.55))         # Edge 21
            Line((-50.0, -3.55), (-101.985, -3.55))        # Edge 22
            Line((-101.985, -3.55), (-101.985, -4.63))     # Edge 23
            Line((-101.985, -4.63), (-110.085, -4.63))     # Edge 24
            Line((-110.085, -4.63), (-110.085, -147.37))   # Edge 25
        make_face()
        
    extrude(amount=-1.6)

    # ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -50.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(50.0)):
        with BuildLine():
            # Traversal using (X, Z) coordinates
            
            # Edge 1: Horizontal Line
            Line((24.086, -3.55), (25.686, -3.55))
            
            # Edge 2: Inner Arc (Radius 1.6)
            ThreePointArc((25.686, -3.55), 
                          get_mid((25.686, -3.55), (27.286, -1.95), (27.286, -3.55), 1.6), 
                          (27.286, -1.95))
            
            # Edge 3: Vertical Line
            Line((27.286, -1.95), (27.286, -0.35))
            
            # Edge 4: Outer Arc (Radius 3.2)
            ThreePointArc((27.286, -0.35), 
                          get_mid((27.286, -0.35), (24.086, -3.55), (27.286, -3.55), 3.2), 
                          (24.086, -3.55))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Y = -101.985
    # -101.985 - (-50.0) = -51.985 mm
    # ---------------------------------------------------------
    extrude(amount=51.985)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -1.95)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-1.95)):
        with BuildLine():
            # Continuous traversal in the XY plane
            
            # Edge 1: Bottom horizontal line
            Line((34.686, -101.985), (27.286, -101.985))
            
            # Edge 6: Left vertical line
            Line((27.286, -101.985), (27.286, -50.0))
            
            # Edge 5: Top horizontal line
            Line((27.286, -50.0), (34.686, -50.0))
            
            # Edge 4: Top-right corner arc (Radius 3.0)
            ThreePointArc((34.686, -50.0), 
                          get_mid((34.686, -50.0), (37.686, -53.0), (34.686, -53.0), 3.0), 
                          (37.686, -53.0))
            
            # Edge 3: Right vertical line
            Line((37.686, -53.0), (37.686, -98.985))
            
            # Edge 2: Bottom-right corner arc (Radius 3.0)
            ThreePointArc((37.686, -98.985), 
                          get_mid((37.686, -98.985), (34.686, -101.985), (34.686, -98.985), 3.0), 
                          (34.686, -101.985))
            
        make_face()
        # --- Subtractions: Circles ---
        with Locations((32.086, -90.992), (32.086, -60.992)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)
    # ---------------------------------------------------------
    # Extrude to target point Z = -0.35
    # -0.35 - (-1.95) = 1.6 mm
    # ---------------------------------------------------------
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -145.57)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-145.57)):
        with BuildLine():
            # Traversal using (X, Y) coordinates
            
            # Edge 1: Inner Arc (Radius 1.6)
            ThreePointArc((22.486, -48.4), 
                          get_mid((22.486, -48.4), (24.086, -50.0), (22.486, -50.0), 1.6), 
                          (24.086, -50.0))
            
            # Edge 2: Horizontal Line
            Line((24.086, -50.0), (25.686, -50.0))
            
            # Edge 3: Outer Arc (Radius 3.2)
            ThreePointArc((25.686, -50.0), 
                          get_mid((25.686, -50.0), (22.486, -46.8), (22.486, -50.0), 3.2), 
                          (22.486, -46.8))
            
            # Edge 4: Vertical Line
            Line((22.486, -46.8), (22.486, -48.4))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -3.55
    # -3.55 - (-145.57) = 142.02 mm
    # ---------------------------------------------------------
    extrude(amount=142.02)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -46.8)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(46.8)):
        with BuildLine():
            # Define the rectangular boundary based on X and Z coordinates
            # X: 13.686 to 22.486 | Z: -145.57 to -3.55
            p1 = (13.686, -3.55)
            p2 = (22.486, -3.55)
            p3 = (22.486, -145.57)
            p4 = (13.686, -145.57)
            Polyline([p1, p2, p3, p4, p1])
        make_face()
        
        # --- Subtractions: Circular Mounting Holes ---
        # Map 3D (X, Z) centers to 2D sketch coordinates
        with Locations((18.186, -134.26), (18.186, -9.76)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Y = -48.4
    # ---------------------------------------------------------
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Profile 1: Top Corner Rail
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(13.686)) as sketch1:
        with BuildLine():
            # Traversal (Y, Z)
            p1_start = (-48.4, -3.55)
            p1_e1_end = (-46.8, -3.55)
            p1_e2_end = (-50.0, -0.35)
            p1_e3_end = (-50.0, -1.95)
            
            Line(p1_start, p1_e1_end) # Edge 1 (Line)
            ThreePointArc(p1_e1_end, 
                          get_mid(p1_e1_end, p1_e2_end, (-50.0, -3.55), 3.2), 
                          p1_e2_end) # Edge 2 (Arc R3.2)
            Line(p1_e2_end, p1_e3_end) # Edge 3 (Line)
            ThreePointArc(p1_e3_end, 
                          get_mid(p1_e3_end, p1_start, (-50.0, -3.55), 1.6), 
                          p1_start)  # Edge 4 (Arc R1.6)
        make_face()
    extrude(amount=8.8)

    # ---------------------------------------------------------
    # Profile 2: Bottom Corner Rail
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(13.686)) as sketch2:
        with BuildLine():
            # Traversal (Y, Z)
            p2_start = (-46.8, -145.57)
            p2_e1_end = (-48.4, -145.57)
            p2_e4_end = (-50.0, -147.17)
            p2_e3_end = (-50.0, -148.77)
            
            Line(p2_start, p2_e1_end) # Edge 1 (Line)
            ThreePointArc(p2_e1_end, 
                          get_mid(p2_e1_end, p2_e4_end, (-50.0, -145.57), 1.6), 
                          p2_e4_end) # Edge 4 (Arc R1.6)
            Line(p2_e4_end, p2_e3_end) # Edge 3 (Line)
            ThreePointArc(p2_e3_end, 
                          get_mid(p2_e3_end, p2_start, (-50.0, -145.57), 3.2), 
                          p2_start)  # Edge 2 (Arc R3.2)
        make_face()
    extrude(amount=8.8)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -1.95)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-1.95)):
        with BuildLine():
            # Traversal (X, Y)
            # Start at top-left of the tab
            p_tl = (13.686, -55.8)
            p_tr = (13.686, -50.0)
            p_br = (22.486, -50.0)
            p_bl = (22.486, -55.8)
            
            # Edge 1: Top vertical line
            Line(p_tl, p_tr)
            
            # Edge 6: Horizontal closure
            Line(p_tr, p_br)
            
            # Edge 5: Bottom vertical line
            Line(p_br, p_bl)
            
            # Edge 4: Bottom-right corner arc (Radius 3.0)
            # Center: (19.486, -55.8)
            ThreePointArc(p_bl, 
                          get_mid(p_bl, (19.486, -58.8), (19.486, -55.8), 3.0), 
                          (19.486, -58.8))
            
            # Edge 3: Bottom horizontal line
            Line((19.486, -58.8), (16.686, -58.8))
            
            # Edge 2: Bottom-left corner arc (Radius 3.0)
            # Center: (16.686, -55.8)
            ThreePointArc((16.686, -58.8), 
                          get_mid((16.686, -58.8), p_tl, (16.686, -55.8), 3.0), 
                          p_tl)
            
        make_face()
        
        # --- Subtraction: Mounting Hole ---
        with Locations((18.086, -54.3)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -0.35
    # ---------------------------------------------------------
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -147.17)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-147.17)):
        with BuildLine():
            # Traversal (X, Y)
            p_start = (13.686, -57.8)
            p_top_left = (13.686, -50.0)
            p_top_right = (22.486, -50.0)
            p_bottom_right = (22.486, -57.8)
            p_arc1_end = (19.486, -60.8)
            p_arc2_start = (16.686, -60.8)

            # Edge 1: Left vertical line
            Line(p_start, p_top_left)
            
            # Edge 6: Top horizontal closure
            Line(p_top_left, p_top_right)
            
            # Edge 5: Right vertical line
            Line(p_top_right, p_bottom_right)
            
            # Edge 4: Bottom-right corner arc (Radius 3.0)
            ThreePointArc(p_bottom_right, 
                          get_mid(p_bottom_right, p_arc1_end, (19.486, -57.8), 3.0), 
                          p_arc1_end)
            
            # Edge 3: Bottom horizontal line
            Line(p_arc1_end, p_arc2_start)
            
            # Edge 2: Bottom-left corner arc (Radius 3.0)
            ThreePointArc(p_arc2_start, 
                          get_mid(p_arc2_start, p_start, (16.686, -57.8), 3.0), 
                          p_start)
            
        make_face()
        
        # --- Subtraction: Mounting Hole ---
        with Locations((18.086, -55.8)):
            Circle(radius=1.59, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -148.77
    # ---------------------------------------------------------
    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -50.8)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(50.8)):
        with BuildLine():
            # Traversal using (X, Z) coordinates
            
            # Edge 1: Horizontal Line
            Line((24.086, -147.37), (25.686, -147.37))
            
            # Edge 4: Outer Arc (Radius 3.2)
            # Reordered to close the loop from Edge 1 end to Edge 3 start
            ThreePointArc((25.686, -147.37), 
                          get_mid((25.686, -147.37), (22.486, -150.57), (22.486, -147.37), 3.2), 
                          (22.486, -150.57))
            
            # Edge 3: Vertical Line
            Line((22.486, -150.57), (22.486, -148.97))
            
            # Edge 2: Inner Arc (Radius 1.6)
            ThreePointArc((22.486, -148.97), 
                          get_mid((22.486, -148.97), (24.086, -147.37), (22.486, -147.37), 1.6), 
                          (24.086, -147.37))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Y = -60.885
    # -60.885 - (-50.8) = -10.085 mm
    # ---------------------------------------------------------
    extrude(amount=10.085)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -72.885)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(72.885)):
        with BuildLine():
            # Traversal using (X, Z) coordinates
            
            # Edge 1: Inner Arc (Radius 1.6)
            ThreePointArc((24.006, -147.87), 
                          get_mid((24.006, -147.87), (22.486, -148.97), (22.486, -147.37), 1.6), 
                          (22.486, -148.97))
            
            # Edge 2: Vertical Line (Reversed to maintain continuity)
            Line((22.486, -148.97), (22.486, -150.57))
            
            # Edge 3: Outer Arc (Radius 3.2)
            ThreePointArc((22.486, -150.57), 
                          get_mid((22.486, -150.57), (25.647, -147.87), (22.486, -147.37), 3.2), 
                          (25.647, -147.87))
            
            # Edge 4: Horizontal Line closing the loop
            Line((25.647, -147.87), (24.006, -147.87))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Y = -92.685
    # -92.685 - (-72.885) = -19.8 mm
    # ---------------------------------------------------------
    extrude(amount=19.8)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -110.085)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(110.085)):
        with BuildLine():
            # Traversal using (X, Z) coordinates
            
            # Edge 1: Inner Arc (Radius 1.6)
            ThreePointArc((22.486, -148.97), 
                          get_mid((22.486, -148.97), (24.086, -147.37), (22.486, -147.37), 1.6), 
                          (24.086, -147.37))
            
            # Edge 2: Horizontal Line
            Line((24.086, -147.37), (25.686, -147.37))
            
            # Edge 3: Outer Arc (Radius 3.2)
            ThreePointArc((25.686, -147.37), 
                          get_mid((25.686, -147.37), (22.486, -150.57), (22.486, -147.37), 3.2), 
                          (22.486, -150.57))
            
            # Edge 4: Vertical Line
            Line((22.486, -150.57), (22.486, -148.97))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Y = -104.685
    # -104.685 - (-110.085) = 5.4 mm
    # ---------------------------------------------------------
    extrude(amount=-5.4)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -150.57)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-150.57)):
        with BuildLine():
            # Continuous traversal mapping the 18 edges (X, Y)
            
            p1_start = (22.486, -110.085)
            p1_end   = (16.686, -110.085)
            p2_end   = (13.686, -107.085)
            p3_end   = (13.686, -53.8)
            p4_end   = (16.686, -50.8)
            p5_end   = (22.486, -50.8)
            p6_end   = (22.486, -60.885)
            p7_end   = (20.336, -60.885)
            p8_end   = (18.336, -62.885)
            p9_end   = (18.336, -70.885)
            p10_end  = (20.336, -72.885)
            p11_end  = (22.486, -72.885)
            p12_end  = (22.486, -92.685)
            p13_end  = (20.336, -92.685)
            p14_end  = (18.336, -94.685)
            p15_end  = (18.336, -102.685)
            p16_end  = (20.336, -104.685)
            p17_end  = (22.486, -104.685)
            
            Line(p1_start, p1_end) # Edge 1
            
            ThreePointArc(p1_end, 
                          get_mid(p1_end, p2_end, (16.686, -107.085), 3.0), 
                          p2_end) # Edge 2
                          
            Line(p2_end, p3_end) # Edge 3
            
            ThreePointArc(p3_end, 
                          get_mid(p3_end, p4_end, (16.686, -53.8), 3.0), 
                          p4_end) # Edge 4
                          
            Line(p4_end, p5_end) # Edge 5
            Line(p5_end, p6_end) # Edge 6
            Line(p6_end, p7_end) # Edge 7
            
            ThreePointArc(p7_end, 
                          get_mid(p7_end, p8_end, (20.336, -62.885), 2.0), 
                          p8_end) # Edge 8
                          
            Line(p8_end, p9_end) # Edge 9
            
            ThreePointArc(p9_end, 
                          get_mid(p9_end, p10_end, (20.336, -70.885), 2.0), 
                          p10_end) # Edge 10
                          
            Line(p10_end, p11_end) # Edge 11
            Line(p11_end, p12_end) # Edge 12
            Line(p12_end, p13_end) # Edge 13
            
            ThreePointArc(p13_end, 
                          get_mid(p13_end, p14_end, (20.336, -94.685), 2.0), 
                          p14_end) # Edge 14
                          
            Line(p14_end, p15_end) # Edge 15
            
            ThreePointArc(p15_end, 
                          get_mid(p15_end, p16_end, (20.336, -102.685), 2.0), 
                          p16_end) # Edge 16
                          
            Line(p16_end, p17_end) # Edge 17
            Line(p17_end, p1_start) # Edge 18 (Closing back to start)
            
        make_face()
        
        # --- Subtraction 1: Original Circular Hole ---
        with Locations((18.686, -80.442)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
            
        # --- Subtraction 2: New Circular Hole ---
        with Locations((18.086, -55.8)):
            Circle(radius=1.59, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -148.97
    # -148.97 - (-150.57) = 1.6 mm
    # ---------------------------------------------------------
    extrude(amount=1.6)

# ---------------------------------------------------------
    # Mirror the entire part about the YZ plane offset to X = 78.436
    # ---------------------------------------------------------
    mirror(about=Plane.YZ.offset(78.436))

if __name__ == "__main__":
        from ocp_vscode import show_all
        show_all()
    # Export STL 
export_stl(part.part, "output_PN-000640_v21.stl")  