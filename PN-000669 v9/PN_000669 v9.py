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
    # Feature 1: Main Rounded Profile with Subtractive Holes
    #            (XZ Plane offset to Y=3.175, extrude to Y=0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(3.175)):
        
        # --- 1. Outer Perimeter ---
        with BuildLine():
            # Top edge (goes right)
            Line((-5.813, 16.052), (7.687, 16.052))
            # Top-right corner
            ThreePointArc((7.687, 16.052), get_mid((7.687, 16.052), (8.687, 15.052), (7.687, 15.052), 1.0), (8.687, 15.052))
            # Right edge (goes down)
            Line((8.687, 15.052), (8.687, 7.052))
            # Bottom-right corner
            ThreePointArc((8.687, 7.052), get_mid((8.687, 7.052), (7.687, 6.052), (7.687, 7.052), 1.0), (7.687, 6.052))
            # Bottom edge (goes left)
            Line((7.687, 6.052), (-5.813, 6.052))
            # Bottom-left corner
            ThreePointArc((-5.813, 6.052), get_mid((-5.813, 6.052), (-6.813, 7.052), (-5.813, 7.052), 1.0), (-6.813, 7.052))
            # Left edge (goes up)
            Line((-6.813, 7.052), (-6.813, 15.052))
            # Top-left corner
            ThreePointArc((-6.813, 15.052), get_mid((-6.813, 15.052), (-5.813, 16.052), (-5.813, 15.052), 1.0), (-5.813, 16.052))
        make_face()
        
        # --- 2. Inner Subtractive Circular Holes ---
        with Locations((4.687, 11.052), (-2.813, 11.052)):
            Circle(radius=1.59, mode=Mode.SUBTRACT)

    # Extrude inward to reach Y=0.0
    extrude(amount=-3.175)

if __name__ == "__main__":
    # Render the model in the OCP viewer extension
    show(part)
    
    # Export STL 
    export_stl(part.part, "output_PN_000669_v9.stl")