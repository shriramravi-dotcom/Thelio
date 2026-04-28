from build123d import *

# =========================================================
# FEATURE : Mesh Side Mount BKT v2
# =========================================================
with BuildPart() as part:
    # Sketching on the XZ plane offset at Y = 1.6
    # This aligns the profile coordinates (X, Z) with the global coordinate system
    with BuildSketch(Plane.XZ.offset(1.6)):
        # Main body: 14mm wide x 131.06mm high with 2mm rounded corners
        # Aligned so the bottom-left corner is at (0, 0) in the XZ plane
        RectangleRounded(14, 131.06, 2.0, align=(Align.MIN, Align.MIN))
        
        # Subtracting the two circular mounting holes
        # Diameter 4.35mm (Radius 2.175mm)
        with Locations((8.5, 121.06), (8.5, 10.0)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
            
    # Extruding the part from Y = 1.6 down to Y = 0.0
    # The amount is -1.6 to reach the target plane
    extrude(amount=-1.6)

if __name__ == "__main__":
    export_stl(part.part, "output_Mesh Side Mount BKT v2.stl")
    
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass