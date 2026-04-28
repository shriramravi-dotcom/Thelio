from build123d import *

# =========================================================
# FEATURE : PN-000653 v9 (Mounting Plate)
# =========================================================
with BuildPart() as part:
    # Sketching on the XZ plane offset at Y = 3.175
    # Global X maps to local x, Global Z maps to local y
    with BuildSketch(Plane.XZ.offset(3.175)):
        
        # 1. Main Plate Profile
        # A 38.5mm x 152.5mm rectangle with 2.0mm radius corners.
        # Align.MIN places the bottom-left corner exactly at (0, 0).
        RectangleRounded(38.5, 152.5, 2.0, align=(Align.MIN, Align.MIN))

        # --- SUBTRACTIONS ---

        # 2. Central Slots (Profile 1 & Profile 2)
        # Slot 1: Centers at Z=5.5 and Z=72.125 (Distance = 66.625, Midpoint Z = 38.8125)
        with Locations((19.25, 38.8125)):
            SlotCenterToCenter(center_separation=66.625, height=4.5, rotation=90, mode=Mode.SUBTRACT)
            
        # Slot 2: Centers at Z=80.375 and Z=147.0 (Distance = 66.625, Midpoint Z = 113.6875)
        with Locations((19.25, 113.6875)):
            SlotCenterToCenter(center_separation=66.625, height=4.5, rotation=90, mode=Mode.SUBTRACT)

        # 3. Circular Holes (Radius = 2.175mm / Dia = 4.35mm)
        # 8 standard mounting holes scattered across the plate
        std_holes = [
            (12.25, 5.2), (26.25, 5.2),
            (5.0, 22.0), (33.5, 22.0),
            (5.0, 130.5), (33.5, 130.5),
            (12.25, 147.3), (26.25, 147.3)
        ]
        with Locations(*std_holes):
            Circle(radius=2.175, mode=Mode.SUBTRACT)

        # 4. Asymmetric Circular Hole (Radius = 2.5mm / Dia = 5.0mm)
        # 1 slightly larger hole at the top right
        with Locations((33.5, 147.0)):
            Circle(radius=2.5, mode=Mode.SUBTRACT)

    # Extrude from Y = 3.175 down to Y = 0.0
    # Distance = 0.0 - 3.175 = -3.175 mm
    extrude(amount=-3.175)

if __name__ == "__main__":
    # Export the model for fabrication or assembly
    export_stl(part.part, "PN-000653_v9.stl")
    
    try:
        from ocp_vscode import show
        show(part)
    except ImportError:
        pass