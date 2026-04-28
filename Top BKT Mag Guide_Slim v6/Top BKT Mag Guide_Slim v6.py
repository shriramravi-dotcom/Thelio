import math
from build123d import *

# =========================================================
# FEATURE : Top BKT Mag Guide_Slim v6
# =========================================================
with BuildPart() as part:
    # 1. Define the tilted plane
    # Normal oriented in XZ plane (-0.766, 0, -0.643)
    bracket_plane = Plane(
        origin=(0.676, 0.0, 26.514), 
        x_dir=(-0.643, 0, 0.766), 
        z_dir=(-0.766, 0, -0.643)
    )

    with BuildSketch(bracket_plane):
        with BuildLine():
            # Local 2D Coordinates: u (width), v (length/Y)
            p_br = (0, 0)
            p_tr = (0, 356.8)
            p_tm = (9.538, 356.8)
            p_to = (11.538, 354.8)
            p_bo = (11.538, 2.0)
            p_bm = (9.538, 0.0)
            
            # Start at bottom-right and move up the inside edge with cutouts
            Line(p_br, (0, 22.1)) # Edge 6
            
            # First Cutout
            Line((0, 22.1), (1.038, 22.1)) # Edge 7
            RadiusArc((1.038, 22.1), (1.538, 22.6), -0.5) # Edge 8 (Fixed)
            Line((1.538, 22.6), (1.538, 169.4)) # Edge 9
            RadiusArc((1.538, 169.4), (1.038, 169.9), -0.5) # Edge 10 (Fixed)
            Line((1.038, 169.9), (0, 169.9)) # Edge 11
            
            Line((0, 169.9), (0, 186.9)) # Edge 12
            
            # Second Cutout
            Line((0, 186.9), (1.038, 186.9)) # Edge 13
            RadiusArc((1.038, 186.9), (1.538, 187.4), -0.5) # Edge 14 (Fixed)
            Line((1.538, 187.4), (1.538, 334.2)) # Edge 15
            RadiusArc((1.538, 334.2), (1.038, 334.7), -0.5) # Edge 16 (Fixed)
            Line((1.038, 334.7), (0, 334.7)) # Edge 17
            
            Line((0, 334.7), p_tr) # Edge 18
            Line(p_tr, p_tm) # Edge 1
            
            # Outer Rounded Perimeter
            RadiusArc(p_tm, p_to, 2.0) # Edge 2 (Fixed)
            Line(p_to, p_bo) # Edge 3
            RadiusArc(p_bo, p_bm, 2.0) # Edge 4 (Fixed)
            Line(p_bm, p_br) # Edge 5
            
        make_face()

        # 2. Subtract Mounting Holes
        # Calculated local u positions for holes: 5.841 and 6.538
        with Locations((5.841, 341.8)):
            Circle(2.25, mode=Mode.SUBTRACT) # Hole 1
        with Locations((6.538, 335.9), (6.538, 178.4), (6.538, 20.9)):
            Circle(1.59, mode=Mode.SUBTRACT) # Holes 2, 3, 4

    # 3. Extrude to target thickness
    extrude(amount=1.265)

# =========================================================
# FEATURE: Curved Bracket Profile
# =========================================================
    # Sketching on the XZ plane (Global X and Z map to local x and y)
    with BuildSketch(Plane.XZ):
        with BuildLine():
            # Coordinates extracted from the profile points (Global X, Global Z)
            p1 = (-0.297, 25.698)
            p2 = (0.676, 26.514)
            p3 = (0.0, 24.881)
            p4 = (1.27, 24.881)
            
            # Edge 1: Outer flat connection
            Line(p1, p2)
            
            # Edge 2: Inner radius curve (r = 1.27mm)
            RadiusArc(p1, p3, 1.27)
            
            # Edge 3: Inner flat connection
            Line(p3, p4)
            
            # Edge 4: Outer radius curve (r = 2.54mm)
            # This concentric arc closes the profile
            RadiusArc(p2, p4, 2.54)
            
        make_face()
    
    # Extruding from Y=0.0 up to the target Point 1 at Y=22.1
    extrude(amount=-22.1)

# =========================================================
# FEATURE : Side Bracket Profile
# =========================================================
    # Sketching on the YZ plane offset at X = 1.27
    with BuildSketch(Plane.YZ.offset(1.27)):
        with BuildLine():
            # Local coordinates: x = Global Y, y = Global Z
            p1 = (0.0, 2.0)
            p1_end = (0.0, 24.881)
            p11_end = (22.1, 24.881)
            p10_end = (22.1, 6.9)
            p9_end = (21.25, 6.05)
            p8_end = (20.992, 6.05)
            p7_end = (20.143, 6.86)
            p6_end = (7.05, 6.55)
            p5_end = (7.05, 0.85)
            p4_end = (6.2, 0.0)
            p3_end = (2.0, 0.0)
            
            # Trace the loop in sequence (1 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2)
            Line(p1, p1_end)                      # Edge 1
            Line(p1_end, p11_end)                # Edge 11
            Line(p11_end, p10_end)               # Edge 10
            RadiusArc(p10_end, p9_end, 0.85)     # Edge 9
            Line(p9_end, p8_end)                 # Edge 8
            RadiusArc(p8_end, p7_end, 0.85)      # Edge 7
            RadiusArc(p7_end, p6_end, -6.55)      # Edge 6
            Line(p6_end, p5_end)                 # Edge 5
            RadiusArc(p5_end, p4_end, 0.85)      # Edge 4
            Line(p4_end, p3_end)                 # Edge 3
            RadiusArc(p3_end, p1, 2.0)           # Edge 2
            
        make_face()
    
    # Extrude from X = 1.27 to X = 0.0
    extrude(amount=-1.27)

# =========================================================
# FEATURE : Curved Profile Section (Y=169.9)
# =========================================================
    # Sketching on the XZ plane offset at Y = 169.9
    # Global X -> local x, Global Z -> local y
    with BuildSketch(Plane.XZ.offset(-169.9)):
        with BuildLine():
            # Local coordinates from your profile data
            p1 = (0.676, 26.514)
            p2 = (-0.297, 25.698)
            p3 = (0.0, 24.881)
            p4 = (1.27, 24.881)
            
            # Edge 1: Flat transition
            Line(p1, p2)
            
            # Edge 2: Inner curve (r = 1.27mm)
            RadiusArc(p2, p3, 1.27)
            
            # Edge 3: Base flat
            Line(p3, p4)
            
            # Edge 4: Outer curve (r = 2.54mm)
            # This completes the concentric loop
            RadiusArc(p4, p1, -2.54)
            
        make_face()
    
    # Extruding from Y=169.9 to the target Point 1 at Y=186.9
    # Distance = 17.0mm
    extrude(amount=-17.0)

# =========================================================
# FEATURE : Side Bracket Section (Y=169.9 to 186.9)
# =========================================================
    # Sketching on the YZ plane offset at X = 1.27
    # Local x maps to Global Y, Local y maps to Global Z
    with BuildSketch(Plane.YZ.offset(1.27)):
        with BuildLine():
            # Define vertices based on profile data (Local x, y)
            v1 = (169.9, 6.9)
            v2 = (169.9, 24.881)
            v3 = (186.9, 24.881)
            v4 = (186.9, 6.9)
            v5 = (186.05, 6.05)
            v6 = (185.792, 6.05)
            v7 = (184.943, 6.86)
            v8 = (171.857, 6.86)
            v9 = (171.008, 6.05)
            v10 = (170.75, 6.05)
            
            # Trace the loop
            Line(v1, v2)                          # Line 1
            Line(v2, v3)                          # Line 10
            Line(v3, v4)                          # Line 9
            RadiusArc(v4, v5, 0.85)               # Arc 8
            Line(v5, v6)                          # Line 7
            RadiusArc(v6, v7, 0.85)               # Arc 6
            # Arc 5: Large central curve (Radius 6.55)
            # Center is at (178.4, 6.55), arc peaks at z=13.1
            ThreePointArc(v7, (178.4, 13.1), v8)  
            RadiusArc(v8, v9, 0.85)               # Arc 4
            Line(v9, v10)                         # Line 3
            RadiusArc(v10, v1, 0.85)              # Arc 2
            
        make_face()
    
    # Extrude from X = 1.27 back to X = 0.0
    extrude(amount=-1.27)

# =========================================================
# FEATURE : Curved Profile Section (Y=356.8)
# =========================================================
    # Sketching on the XZ plane offset at Y = 356.8
    # Global X maps to local x, Global Z maps to local y
    with BuildSketch(Plane.XZ.offset(-356.8)):
        with BuildLine():
            # Define local coordinates (x, y) based on provided points
            p1 = (-0.297, 25.698) # Edge 1 Start / Edge 4 End
            p2 = (0.676, 26.514)  # Edge 1 End / Edge 2 End
            p3 = (1.27, 24.881)   # Edge 2 Start / Edge 3 End
            p4 = (0.0, 24.881)    # Edge 3 Start / Edge 4 Start
            
            # Edge 1: Flat outer transition
            Line(p1, p2)
            
            # Edge 2: Outer curve (Radius 2.54mm)
            # Center is at x=-1.27, y=24.881
            RadiusArc(p2, p3, 2.54)
            
            # Edge 3: Base flat
            Line(p3, p4)
            
            # Edge 4: Inner curve (Radius 1.27mm)
            RadiusArc(p4, p1, -1.27)
            
        make_face()
    
    # Extruding from Y=356.8 back to the target Point 1 at Y=334.7
    # Distance = 334.7 - 356.8 = -22.1mm
    extrude(amount=22.1)

# =========================================================
# FEATURE : Side Bracket Section (Y=334.7 to 356.8)
# =========================================================
    # Sketching on the YZ plane offset at X = 1.27
    # Local x maps to Global Y, Local y maps to Global Z
    with BuildSketch(Plane.YZ.offset(1.27)):
        with BuildLine():
            # Define vertices based on profile data (Local x, y)
            v1 = (356.8, 24.881)
            v2 = (356.8, 2.0)
            v3 = (354.8, 0.0)
            v4 = (350.6, 0.0)
            v5 = (349.75, 0.85)
            v6 = (349.75, 6.55)
            v7 = (336.657, 6.86)
            v8 = (335.808, 6.05)
            v9 = (335.55, 6.05)
            v10 = (334.7, 6.9)
            v11 = (334.7, 24.881)
            
            # Trace the loop
            Line(v1, v2)                          # Edge 1
            RadiusArc(v2, v3, 2.0)                # Edge 2
            Line(v3, v4)                          # Edge 3
            RadiusArc(v4, v5, 0.85)               # Edge 4
            Line(v5, v6)                          # Edge 5
            # Edge 6: Large central curve (Radius 6.55)
            # Center at (343.2, 6.55), arc peaks at z=13.1
            ThreePointArc(v6, (343.2, 13.1), v7)  
            RadiusArc(v7, v8, 0.85)               # Edge 7
            Line(v8, v9)                          # Edge 8
            RadiusArc(v9, v10, 0.85)              # Edge 9
            Line(v10, v11)                        # Edge 10
            Line(v11, v1)                         # Edge 11
            
        make_face()
    
    # Extrude from X = 1.27 back to X = 0.0
    extrude(amount=-1.27)

if __name__ == "__main__":
    export_stl(part.part, "output_Top BKT Mag Guide_Slim v6.stl")
    
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass