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
    # Feature 1: Main Complex Profile
    #            (YZ Plane offset to X=1.6, extrude to X=0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.6)):
        
        # --- 1. Outer Perimeter ---
        with BuildLine():
            # Continuous head-to-tail traversal
            Line((-16.4, 1.278), (-16.4, 1.0))
            ThreePointArc((-16.4, 1.0), get_mid((-16.4, 1.0), (-15.4, 0.0), (-15.4, 1.0), 1.0), (-15.4, 0.0))
            Line((-15.4, 0.0), (-5.0, 0.0))
            ThreePointArc((-5.0, 0.0), get_mid((-5.0, 0.0), (0.0, 5.0), (-5.0, 5.0), 5.0), (0.0, 5.0))
            Line((0.0, 5.0), (0.0, 10.0))
            ThreePointArc((0.0, 10.0), get_mid((0.0, 10.0), (-5.0, 15.0), (-5.0, 10.0), 5.0), (-5.0, 15.0))
            Line((-5.0, 15.0), (-17.5, 15.0))
            ThreePointArc((-17.5, 15.0), get_mid((-17.5, 15.0), (-22.5, 20.0), (-17.5, 20.0), 5.0), (-22.5, 20.0))
            Line((-22.5, 20.0), (-22.5, 35.0))
            ThreePointArc((-22.5, 35.0), get_mid((-22.5, 35.0), (-27.5, 40.0), (-27.5, 35.0), 5.0), (-27.5, 40.0))
            Line((-27.5, 40.0), (-32.5, 40.0))
            ThreePointArc((-32.5, 40.0), get_mid((-32.5, 40.0), (-37.5, 35.0), (-32.5, 35.0), 5.0), (-37.5, 35.0))
            Line((-37.5, 35.0), (-37.5, 20.0))
            ThreePointArc((-37.5, 20.0), get_mid((-37.5, 20.0), (-42.5, 15.0), (-42.5, 20.0), 5.0), (-42.5, 15.0))
            Line((-42.5, 15.0), (-55.0, 15.0))
            ThreePointArc((-55.0, 15.0), get_mid((-55.0, 15.0), (-60.0, 10.0), (-55.0, 10.0), 5.0), (-60.0, 10.0))
            Line((-60.0, 10.0), (-60.0, 5.0))
            ThreePointArc((-60.0, 5.0), get_mid((-60.0, 5.0), (-55.0, 0.0), (-55.0, 5.0), 5.0), (-55.0, 0.0))
            Line((-55.0, 0.0), (-44.6, 0.0))
            ThreePointArc((-44.6, 0.0), get_mid((-44.6, 0.0), (-43.6, 1.0), (-44.6, 1.0), 1.0), (-43.6, 1.0))
            Line((-43.6, 1.0), (-43.6, 1.278))
            Line((-43.6, 1.278), (-42.0, 1.278))
            Line((-42.0, 1.278), (-42.0, 0.478))
            Line((-42.0, 0.478), (-18.0, 0.478))
            Line((-18.0, 0.478), (-18.0, 1.278))
            Line((-18.0, 1.278), (-16.4, 1.278))  # Closes back to start
        make_face()
        
        # --- 2. Inner Subtractive Circular Hole ---
        with Locations((-30.0, 34.0)):
            Circle(radius=2.5, mode=Mode.SUBTRACT)

    # Extrude inward in the negative X direction (0.0 - 1.6 = -1.6)
    extrude(amount=-1.6)

# ---------------------------------------------------------
    # Feature 2: Added Edge Profile
    #            (XZ Plane offset to Y=-42.0, extrude to Y=-18.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(42.0)):
        with BuildLine():
            # Continuous head-to-tail traversal
            Line((1.6, 0.478), (0.0, 0.478))
            
            # Outer Arc (Radius 3.2)
            ThreePointArc((0.0, 0.478), 
                          get_mid((0.0, 0.478), (0.14, -0.457), (3.2, 0.478), 3.2), 
                          (0.14, -0.457))
            
            Line((0.14, -0.457), (1.67, 0.01))
            
            # Inner Arc (Radius 1.6)
            ThreePointArc((1.67, 0.01), 
                          get_mid((1.67, 0.01), (1.6, 0.478), (3.2, 0.478), 1.6), 
                          (1.6, 0.478))
        make_face()
        
    # Extrude outward in the positive Y direction (-18.0 - -42.0 = 24.0)
    extrude(amount=-24.0)

# ---------------------------------------------------------
    # Feature 3: Angled 3D Profile 
    #            (Constructed flawlessly using a Custom 2D Plane)
    # ---------------------------------------------------------
    
    # Calculate exact profile dimensions based on 3D vectors
    width = 24.0
    origin_pt = Vector(1.67, -18.0, 0.01)
    y_pt = Vector(4.015, -18.0, -7.661)
    
    y_vec = y_pt - origin_pt
    base_height = y_vec.length  # ~8.0214 mm
    arc_radius = 5.0
    total_height = base_height + arc_radius
    
    # Define the mathematically perfect angled local plane
    x_dir = Vector(0, -1, 0)
    
    # The plane normal (Z-direction) is the cross-product of X and Y
    z_dir = x_dir.cross(y_vec).normalized()
    
    # Create the custom plane using origin, x_dir, and z_dir
    custom_plane = Plane(origin=origin_pt, x_dir=x_dir, z_dir=z_dir)
    
    with BuildSketch(custom_plane):
        # Build the bounding rectangle
        Rectangle(width, total_height, align=(Align.MIN, Align.MIN))
        # Natively fillet the two top corners (highest Y coordinates in local sketch space)
        fillet(vertices().sort_by(Axis.Y)[-2:], radius=arc_radius)

    # Extrude normally into the body. Distance calculated from target point (-1.6mm)
    extrude(amount=-1.6)
    
if __name__ == "__main__":
    # Render the model in the OCP viewer extension
    show(part)
    
    # Export STL 
    export_stl(part.part, "output_PN_000668_v7.stl")