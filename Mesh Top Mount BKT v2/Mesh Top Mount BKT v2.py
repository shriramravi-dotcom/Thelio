from build123d import *

# =========================================================
# FEATURE : Mesh Top Mount BKT v2
# =========================================================
with BuildPart() as part:
    # Sketching on the XY plane offset at Z = 1.6
    # This aligns the (X, Y) coordinates directly with your profile
    with BuildSketch(Plane.XY.offset(1.6)):
        # Main body: 14mm (X) x 45mm (Y) with 2mm rounded corners
        # Aligned so the bottom-left is at (0, 0)
        RectangleRounded(14, 45, 2.0, align=(Align.MIN, Align.MIN))
        
        # Subtract the mounting hole
        # Center: (8.5, 22.5), Diameter: 4.35mm (Radius: 2.175mm)
        with Locations((8.5, 22.5)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
            
    # Extruding from Z = 1.6 down to Z = 0.0
    # The amount is -1.6 to reach the target point
    extrude(amount=-1.6)

if __name__ == "__main__":
    # Exporting the part to STL for verification or printing
    export_stl(part.part, "output_Mesh_Top_Mount_BKT_v2.stl")
    
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass