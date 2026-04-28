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
    #            (YZ Plane offset to X=1.79, extrude to X=0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.79)):
        
        # --- Outer Perimeter ---
        with BuildLine():
            # 1. Top inner arc
            ThreePointArc((-4.956, 4.206), get_mid((-4.956, 4.206), (4.956, 4.206), (0.0, 0.0), 6.5), (4.956, 4.206))
            
            # 2. Top right transition arc
            ThreePointArc((4.956, 4.206), get_mid((4.956, 4.206), (6.481, 3.5), (6.481, 5.5), 2.0), (6.481, 3.5))
            
            # 3. Top right straight edge
            Line((6.481, 3.5), (10.0, 3.5))
            
            # 4. Right 180-degree lobe (Explicit outer midpoint to ensure correct bulge)
            ThreePointArc((10.0, 3.5), (13.5, 0.0), (10.0, -3.5))
            
            # 5. Bottom right straight edge
            Line((10.0, -3.5), (6.481, -3.5))
            
            # 6. Bottom right transition arc
            ThreePointArc((6.481, -3.5), get_mid((6.481, -3.5), (4.956, -4.206), (6.481, -5.5), 2.0), (4.956, -4.206))
            
            # 7. Bottom inner arc
            ThreePointArc((4.956, -4.206), get_mid((4.956, -4.206), (-4.956, -4.206), (0.0, 0.0), 6.5), (-4.956, -4.206))
            
            # 8. Bottom left transition arc
            ThreePointArc((-4.956, -4.206), get_mid((-4.956, -4.206), (-6.481, -3.5), (-6.481, -5.5), 2.0), (-6.481, -3.5))
            
            # 9. Bottom left straight edge
            Line((-6.481, -3.5), (-10.0, -3.5))
            
            # 10. Left 180-degree lobe (Explicit outer midpoint to ensure correct bulge)
            ThreePointArc((-10.0, -3.5), (-13.5, 0.0), (-10.0, 3.5))
            
            # 11. Top left straight edge
            Line((-10.0, 3.5), (-6.481, 3.5))
            
            # 12. Top left transition arc (closes the loop)
            ThreePointArc((-6.481, 3.5), get_mid((-6.481, 3.5), (-4.956, 4.206), (-6.481, 5.5), 2.0), (-4.956, 4.206))
        
        make_face()
        
        # --- Subtractive Circular Holes ---
        with Locations((10.0, 0.0), (-10.0, 0.0)):
            Circle(radius=1.59, mode=Mode.SUBTRACT)

    # Extrude inward in the negative X direction to reach X=0.0 (0.0 - 1.79 = -1.79)
    extrude(amount=-1.79)

if __name__ == "__main__":
    # Render the model in the OCP viewer extension
    show(part)
    
    # Export STL 
    export_stl(part.part, "output_PN-000666_v7.stl")