from build123d import *

# =========================================================
# FEATURE : V3 120 mm Fan Mounting Plate v7
# =========================================================
with BuildPart() as part:
    # 1. GENERATE THE MAIN PLATE BASE
    with BuildSketch(Plane.YZ) as plate_sketch:
        with BuildLine():
            # Perimeter coordinates (Global Y, Z)
            pts = [
                (-285.68, 160.84), (-305.4, 160.84), (-305.4, 160.04),
                (-306.4, 159.04), (-313.3, 159.04), (-313.3, 41.24),
                (-288.4, 41.24), (-288.4, 42.04), (-285.5, 42.04),
                (-284.5, 41.04), (-284.5, 5.0), (-279.5, 0.0),
                (-5.0, 0.0), (0.0, 5.0), (0.0, 155.04),
                (-5.0, 160.04), (-284.7, 160.04)
            ]
            Line(pts[0], pts[1])
            Line(pts[1], pts[2])
            RadiusArc(pts[2], pts[3], 1.0)
            Line(pts[3], pts[4])
            Line(pts[4], pts[5])
            Line(pts[5], pts[6])
            Line(pts[6], pts[7])
            Line(pts[7], pts[8])
            RadiusArc(pts[8], pts[9], 1.0)
            Line(pts[9], pts[10])
            RadiusArc(pts[10], pts[11], -5.0)
            Line(pts[11], pts[12])
            RadiusArc(pts[12], pts[13], -5.0)
            Line(pts[13], pts[14])
            RadiusArc(pts[14], pts[15], -5.0)
            Line(pts[15], pts[16])
            RadiusArc(pts[16], pts[0], 1.0)
        make_face()

        # --- 2D Subtractions (Slots and Fan Holes) ---
        # Top Rounded Rectangle Slot
        with Locations((-300.75, 154.19)):
            RectangleRounded(19.0, 5.4, 0.8, mode=Mode.SUBTRACT)
        
        # 8 Mounting Slots (12.95mm center-to-center length)
        slot_centers = [
            (-292.988, 125.332), (-308.663, 125.332), (-308.663, 60.715), (-292.988, 60.715),
            (-270.663, 108.975), (-252.988, 108.975), (-270.663, 41.025), (-252.988, 41.025)
        ]
        with Locations(*slot_centers):
            SlotCenterToCenter(12.95, 3.675, rotation=90, mode=Mode.SUBTRACT)

        # 4 Corner Circular Holes (3.45mm Diameter)
        with Locations((-275.45, 5.8), (-275.45, 155.04), (-9.05, 155.04), (-9.05, 5.8)):
            Circle(1.725, mode=Mode.SUBTRACT)

        # Accessory Rounded Slot
        with Locations((-194.65, 137.45)):
            RectangleRounded(13.0, 8.0, 1.0, mode=Mode.SUBTRACT)

        # 2 Large Fan Cutouts (114mm Diameter)
        with Locations((-190.5, 72.5), (-69.5, 72.5)):
            Circle(57.0, mode=Mode.SUBTRACT)

    # Extrude to 1.6mm thickness
    extrude(amount=1.6)

    # 2. TRIPLE-CIRCLE LOFT SUBTRACTIONS (Countersink Through-Holes)
    # Centers for the 8 countersink holes (Y, Z)
    hole_centers = [
        (-243.0, 125.0), (-243.0, 20.0), (-138.0, 20.0), (-122.0, 20.0),
        (-122.0, 125.0), (-138.0, 125.0), (-17.0, 125.0), (-17.0, 20.0)
    ]

    for y, z in hole_centers:
        # Create a single subtraction volume by lofting 3 sketches
        with BuildPart(mode=Mode.SUBTRACT):
            # Sketch 1: Entry face (X=0, Large Radius 3.305)
            with BuildSketch(Plane.YZ.offset(0)):
                with Locations((y, z)):
                    Circle(3.305)
            
            # Sketch 2: Taper transition point (X=0.755, Small Radius 2.55)
            with BuildSketch(Plane.YZ.offset(0.755)):
                with Locations((y, z)):
                    Circle(2.55)

            # Sketch 3: Exit face (X=1.6, Small Radius 2.55)
            with BuildSketch(Plane.YZ.offset(1.6)):
                with Locations((y, z)):
                    Circle(2.55)
            
            # Join all three circles into one continuous solid and subtract
            loft()

# =========================================================
# FEATURE : Mounting Flange / Clip Profile
# =========================================================
    # Sketching on the XZ plane offset at Y = -288.4
    # Local x maps to Global X, Local y maps to Global Z
    with BuildSketch(Plane.XZ.offset(288.4)):
        with BuildLine():
            # Define vertices (Local x, y)
            p1 = (1.6, 41.24)    # Edge 2 start / Edge 3 end
            p2 = (0.0, 41.24)    # Edge 2 end / Edge 5 start
            p3 = (-1.6, 39.64)   # Edge 5 end / Edge 4 start
            p4 = (-1.6, 38.04)   # Edge 4 end / Edge 3 start
            
            # Edge 2: Top flat
            Line(p1, p2)
            
            # Edge 5: Inner radius (1.6mm)
            # Center at (-1.6, 41.24)
            RadiusArc(p2, p3, 1.6)
            
            # Edge 4: Vertical flat
            Line(p3, p4)
            
            # Edge 3: Outer radius (3.2mm)
            # This concentric arc closes the loop back to p1
            RadiusArc(p4, p1, -3.2)
            
        make_face()
    
    # Extruding from Y = -288.4 to the target Point 1 at Y = -313.3
    # Distance = -313.3 - (-288.4) = -24.9mm
    extrude(amount=24.9)

# =========================================================
# FEATURE : L-Shaped Mounting Profile
# =========================================================
    # Sketching on the XY plane offset at Z = 39.64
    with BuildSketch(Plane.XY.offset(39.64)):
        with BuildLine():
            # Define vertices (Local x, y)
            v1 = (-1.6, -313.3)
            v2 = (-1.6, -288.4)
            v3 = (-14.2, -288.4)
            v4 = (-15.2, -289.4)
            v5 = (-15.2, -300.8)
            v6 = (-17.0, -300.8)
            v7 = (-18.0, -301.8)
            v8 = (-18.0, -313.7)
            v9 = (-17.0, -314.7)
            v10 = (-2.6, -314.7)
            v11 = (-1.6, -313.7)

            # Trace the perimeter loop
            Line(v1, v2)             # Edge 1
            Line(v2, v3)             # Edge 11
            RadiusArc(v3, v4, -1.0)   # Edge 10
            Line(v4, v5)             # Edge 9
            Line(v5, v6)             # Edge 8
            RadiusArc(v6, v7, -1.0)   # Edge 7
            Line(v7, v8)             # Edge 6
            RadiusArc(v8, v9, -1.0)   # Edge 5
            Line(v9, v10)            # Edge 4
            RadiusArc(v10, v11, -1.0) # Edge 3
            Line(v11, v1)            # Edge 2
            
        make_face()
    
    # Extrude from Z = 39.64 down to Z = 38.04
    # Distance = 38.04 - 39.64 = -1.6mm
    extrude(amount=-1.6)

# =========================================================
# FEATURE : Curved Mounting Rail Profile
# =========================================================
    # Sketching on the XY plane offset at Z = 41.24
    # Local x maps to Global X, Local y maps to Global Y
    with BuildSketch(Plane.XY.offset(41.24)):
        with BuildLine():
            # Vertices extracted from the profile (Local x, y)
            v1 = (0.0, -313.3)   # Edge 1 start / Edge 2 start
            v2 = (1.6, -313.3)   # Edge 2 end / Edge 3 end
            v3 = (-1.6, -316.5)  # Edge 3 start / Edge 4 end
            v4 = (-1.6, -314.9)  # Edge 4 start / Edge 1 end
            
            # Edge 2: Top flat horizontal line
            Line(v1, v2)
            
            # Edge 3: Outer radius (3.2mm) 
            # Concentric arc around center (-1.6, -313.3)
            RadiusArc(v2, v3, 3.2)
            
            # Edge 4: Vertical flat line
            Line(v3, v4)
            
            # Edge 1: Inner radius (1.6mm)
            # Closes the loop back to v1
            RadiusArc(v4, v1, -1.6)
            
        make_face()
    
    # Extruding from Z = 41.24 to Z = 159.04
    # Distance = 159.04 - 41.24 = 117.8mm
    extrude(amount=117.8)

# =========================================================
# FEATURE : Side Rail Bracket (XZ Plane)
# =========================================================
    # Sketching on the XZ plane offset at Y = -316.5
    # Global X maps to local x, Global Z maps to local y
    with BuildSketch(Plane.XZ.offset(316.5)):
        with BuildLine():
            # Define vertices (Local x, y) derived from global (X, Z)
            v1 = (-1.6, 159.04)
            v2 = (-3.6, 159.04)
            v3 = (-4.6, 160.04)
            v4 = (-4.6, 163.05)
            v5 = (-5.6, 164.05)
            v6 = (-17.0, 164.05)
            v7 = (-18.0, 163.05)
            v8 = (-18.0, 39.03)
            v9 = (-17.0, 38.03)
            v10 = (-2.6, 38.03)
            v11 = (-1.6, 39.03)
            v12 = (-1.6, 41.24)
            
            # Trace the perimeter loop sequentially
            Line(v1, v2)              # Edge 12
            RadiusArc(v2, v3, 1.0)    # Edge 11
            Line(v3, v4)              # Edge 10
            RadiusArc(v4, v5, -1.0)    # Edge 9
            Line(v5, v6)              # Edge 8
            RadiusArc(v6, v7, -1.0)    # Edge 7
            Line(v7, v8)              # Edge 6
            RadiusArc(v8, v9, -1.0)    # Edge 5
            Line(v9, v10)             # Edge 4
            RadiusArc(v10, v11, -1.0)  # Edge 3
            Line(v11, v12)            # Edge 2
            Line(v12, v1)             # Edge 1
            
        make_face()
        
    # Extrude from Y = -316.5 to Y = -314.9
    # Distance = -314.9 - (-316.5) = 1.6mm
    extrude(amount=-1.6)

# =========================================================
# FEATURE : Concentric Curved Support Profile
# =========================================================
    # Sketching on the XZ plane offset at Y = -305.4
    # Global X maps to local x, Global Z maps to local y
    with BuildSketch(Plane.XZ.offset(305.4)):
        with BuildLine():
            # Define vertices (Local x, y) derived from global (X, Z)
            v1 = (0.0, 160.84)    # Line 1 start / Arc 2 start
            v2 = (1.6, 160.84)    # Line 1 end / Arc 4 start
            v3 = (-1.6, 164.04)   # Arc 4 end / Line 3 end
            v4 = (-1.6, 162.44)   # Line 3 start / Arc 2 end
            
            # Edge 1: Horizontal flat transition
            Line(v1, v2)
            
            # Edge 4: Outer radius (3.2mm)
            # Sweeps from (1.6, 160.84) to (-1.6, 164.04)
            RadiusArc(v2, v3, -3.2)
            
            # Edge 3: Vertical flat connection
            Line(v3, v4)
            
            # Edge 2: Inner radius (1.6mm)
            # Sweeps back to close the loop at v1
            RadiusArc(v4, v1, 1.6)
            
        make_face()

    # Extruding from Y = -305.4 to the target Point 1 at Y = -285.68
    # Distance = -285.68 - (-305.4) = 19.72mm
    extrude(amount=-19.72)

# =========================================================
# FEATURE : Mounting Bracket (XY Plane)
# =========================================================
    # Sketching on the XY plane offset at Z = 162.44
    # Global X maps to local x, Global Y maps to local y
    with BuildSketch(Plane.XY.offset(162.44)):
        with BuildLine():
            # Define vertices (Local x, y) derived from global (X, Y)
            v1 = (-1.6, -285.7)
            v2 = (-1.6, -305.4)
            v3 = (-3.6, -305.4)
            v4 = (-4.6, -306.4)
            v5 = (-4.6, -313.7)
            v6 = (-5.6, -314.7)
            v7 = (-17.0, -314.7)
            v8 = (-18.0, -313.7)
            v9 = (-18.0, -286.7)
            v10 = (-17.0, -285.7)

            # Trace the perimeter loop sequentially
            Line(v1, v2)              # Edge 1
            Line(v2, v3)              # Line 2
            RadiusArc(v3, v4, 1.0)    # Edge 3
            Line(v4, v5)              # Edge 4
            RadiusArc(v5, v6, 1.0)    # Edge 5
            Line(v6, v7)              # Edge 6
            RadiusArc(v7, v8, 1.0)    # Edge 7
            Line(v8, v9)              # Edge 8
            RadiusArc(v9, v10, 1.0)   # Edge 9
            Line(v10, v1)             # Edge 10
            
        make_face()

        # --- Subtractions: Mounting Holes ---
        # Diameter 3.45mm (Radius 1.725mm)
        with Locations((-8.45, -305.83), (-8.45, -295.83)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)
        
    # Extrude from Z = 162.44 to Z = 164.04
    # Distance = 164.04 - 162.44 = 1.6mm
    extrude(amount=1.6)

if __name__ == "__main__":
    export_stl(part.part, "output_V3 120mm Fan Mounting Plate v7.stl")
    
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass