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

# Part: PN-000652 v17 (with loft)

with BuildPart() as part:
    # ---------------------------------------------------------
    # Feature 1: Base Horizontal Slot
    #            (XY Plane at Z=0.0, extrude up to Z=6.628)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(0.0)):
        with Locations((-53.75, 12.3)):
            SlotCenterToCenter(center_separation=82.9, height=24.6)
    
    extrude(amount=6.628)

    # ---------------------------------------------------------
    # Feature 2: Loft to smaller slot profile
    #            (From Z=6.628 up to Z=7.628)
    # ---------------------------------------------------------
    
    # Sketch 1: Match the top face of the base extrusion exactly
    with BuildSketch(Plane.XY.offset(6.628)):
        with Locations((-53.75, 12.3)):
            SlotCenterToCenter(center_separation=82.9, height=24.6)
            
    # Sketch 2: The new, slightly smaller profile 
    with BuildSketch(Plane.XY.offset(7.628)):
        with Locations((-53.75, 12.3)):
            SlotCenterToCenter(center_separation=82.9, height=22.6)
            
    # Create the lofted solid between the two pending sketches
    loft()

    # ---------------------------------------------------------
    # Feature: Subtractive Complex Profile
    #          (XY Plane at Z=0.0, extrude to Z=6.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(0.0)):
        with BuildLine():
            # Traversal starts at (-104.4, 16.75) and loops head-to-tail
            Line((-104.4, 16.75), (-104.4, 17.25))
            ThreePointArc((-104.4, 17.25), get_mid((-104.4, 17.25), (-102.4, 19.25), (-102.4, 17.25), 2.0), (-102.4, 19.25))
            Line((-102.4, 19.25), (-98.128, 19.25))
            ThreePointArc((-98.128, 19.25), get_mid((-98.128, 19.25), (-96.264, 20.525), (-98.128, 21.25), 2.0), (-96.264, 20.525))
            ThreePointArc((-96.264, 20.525), get_mid((-96.264, 20.525), (-94.4, 21.8), (-94.4, 19.8), 2.0), (-94.4, 21.8))
            Line((-94.4, 21.8), (-35.3, 21.8))
            ThreePointArc((-35.3, 21.8), get_mid((-35.3, 21.8), (-33.436, 20.525), (-35.3, 19.8), 2.0), (-33.436, 20.525))
            ThreePointArc((-33.436, 20.525), get_mid((-33.436, 20.525), (-31.572, 19.25), (-31.572, 21.25), 2.0), (-31.572, 19.25))
            Line((-31.572, 19.25), (-26.4, 19.25))
            ThreePointArc((-26.4, 19.25), get_mid((-26.4, 19.25), (-24.4, 17.25), (-26.4, 17.25), 2.0), (-24.4, 17.25))
            Line((-24.4, 17.25), (-24.4, 16.75))
            ThreePointArc((-24.4, 16.75), get_mid((-24.4, 16.75), (-26.4, 14.75), (-26.4, 16.75), 2.0), (-26.4, 14.75))
            Line((-26.4, 14.75), (-31.3, 14.75))
            ThreePointArc((-31.3, 14.75), get_mid((-31.3, 14.75), (-33.3, 12.75), (-31.3, 12.75), 2.0), (-33.3, 12.75))
            Line((-33.3, 12.75), (-33.3, 9.6))
            ThreePointArc((-33.3, 9.6), get_mid((-33.3, 9.6), (-35.3, 7.6), (-35.3, 9.6), 2.0), (-35.3, 7.6))
            Line((-35.3, 7.6), (-94.4, 7.6))
            ThreePointArc((-94.4, 7.6), get_mid((-94.4, 7.6), (-96.4, 9.6), (-94.4, 9.6), 2.0), (-96.4, 9.6))
            Line((-96.4, 9.6), (-96.4, 12.75))
            ThreePointArc((-96.4, 12.75), get_mid((-96.4, 12.75), (-98.4, 14.75), (-98.4, 12.75), 2.0), (-98.4, 14.75))
            Line((-98.4, 14.75), (-102.4, 14.75))
            ThreePointArc((-102.4, 14.75), get_mid((-102.4, 14.75), (-104.4, 16.75), (-102.4, 16.75), 2.0), (-104.4, 16.75))
            
        make_face()
        
    # Extrude up to Z=6.0 in subtractive mode
    extrude(amount=6.0, mode=Mode.SUBTRACT)

# ---------------------------------------------------------
    # Feature: Subtractive Circles and Slots
    #          (XY Plane at Z=7.628, extrude to Z=0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(7.628)):
# --- 1. Circular Holes ---
        with Locations((-12.3, 12.3)):
            Circle(radius=9.0)
            
        with Locations((-75.3, 12.772)):
            Circle(radius=3.65)

        # --- 2. Rounded Rectangle Slot 1 ---
        with BuildLine():
            ThreePointArc((-33.95, 10.843), get_mid((-33.95, 10.843), (-35.601, 9.192), (-35.601, 10.843), 1.651), (-35.601, 9.192))
            Line((-35.601, 9.192), (-46.799, 9.192))
            ThreePointArc((-46.799, 9.192), get_mid((-46.799, 9.192), (-48.45, 10.843), (-46.799, 10.843), 1.651), (-48.45, 10.843))
            Line((-48.45, 10.843), (-48.45, 14.061))
            ThreePointArc((-48.45, 14.061), get_mid((-48.45, 14.061), (-46.799, 15.712), (-46.799, 14.061), 1.651), (-46.799, 15.712))
            Line((-46.799, 15.712), (-35.601, 15.712))
            ThreePointArc((-35.601, 15.712), get_mid((-35.601, 15.712), (-33.95, 14.061), (-35.601, 14.061), 1.651), (-33.95, 14.061))
            Line((-33.95, 14.061), (-33.95, 10.843))
        make_face()

        # --- 3. Rounded Rectangle Slot 2 ---
        with BuildLine():
            ThreePointArc((-52.25, 10.843), get_mid((-52.25, 10.843), (-53.901, 9.192), (-53.901, 10.843), 1.651), (-53.901, 9.192))
            Line((-53.901, 9.192), (-65.099, 9.192))
            ThreePointArc((-65.099, 9.192), get_mid((-65.099, 9.192), (-66.75, 10.843), (-65.099, 10.843), 1.651), (-66.75, 10.843))
            Line((-66.75, 10.843), (-66.75, 14.061))
            ThreePointArc((-66.75, 14.061), get_mid((-66.75, 14.061), (-65.099, 15.712), (-65.099, 14.061), 1.651), (-65.099, 15.712))
            Line((-65.099, 15.712), (-53.901, 15.712))
            ThreePointArc((-53.901, 15.712), get_mid((-53.901, 15.712), (-52.25, 14.061), (-53.901, 14.061), 1.651), (-52.25, 14.061))
            Line((-52.25, 14.061), (-52.25, 10.843))
        make_face()

        # --- 4. Elongated Split-Arc Slot 3 ---
        with BuildLine():
            Line((-86.25, 10.792), (-92.35, 10.792))
            ThreePointArc((-92.35, 10.792), get_mid((-92.35, 10.792), (-94.3, 12.742), (-92.35, 12.742), 1.95), (-94.3, 12.742))
            Line((-94.3, 12.742), (-94.3, 12.802))
            ThreePointArc((-94.3, 12.802), get_mid((-94.3, 12.802), (-92.35, 14.752), (-92.35, 12.802), 1.95), (-92.35, 14.752))
            Line((-92.35, 14.752), (-86.25, 14.752))
            ThreePointArc((-86.25, 14.752), get_mid((-86.25, 14.752), (-84.3, 12.802), (-86.25, 12.802), 1.95), (-84.3, 12.802))
            Line((-84.3, 12.802), (-84.3, 12.742))
            ThreePointArc((-84.3, 12.742), get_mid((-84.3, 12.742), (-86.25, 10.792), (-86.25, 12.742), 1.95), (-86.25, 10.792))
        make_face()

    # Extrude down to Z=0.0 (-7.628 distance) in subtract mode
    extrude(amount=-7.628, mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Feature: Subtractive Circular Holes
    #          (XY Plane at Z=0.0, extrude +4mm towards +Z)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY):
        # Circle 1: (-29.3, 9.7)
        # Circle 2: (-100.3, 9.7)
        with Locations(
            (-29.3, 9.7),
            (-100.3, 9.7)
        ):
            Circle(radius=1.264)

    # Extrude upward in the positive Z direction by 4.0 mm
    extrude(amount=4.0, mode=Mode.SUBTRACT)

if __name__ == "__main__":
    # Render the model in the OCP viewer extension
    show(part)
    
    # Export STL 
    export_stl(part.part, "output_PN-000652_v17.stl")