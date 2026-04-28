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

# --- Define Tilted Custom Plane for Feature 3 ---
origin = Vector(2.209, 0.0, -18.849)
x_dir = Vector(0.0, 1.0, 0.0) 
y_vec = Vector(7.799 - 2.209, 0.0, -25.511 - (-18.849))
y_dir = y_vec.normalized()
z_dir = x_dir.cross(y_dir).normalized()
angled_plane = Plane(origin=origin, x_dir=x_dir, z_dir=z_dir)

def prj(x, y, z):
    """Maps 3D coordinates strictly to 2D (u, v) on the angled plane."""
    v = Vector(x, y, z) - origin
    return (v.dot(x_dir), v.dot(y_dir))

with BuildPart() as part:
    # ---------------------------------------------------------
    # FEATURE 1: Main Profile
    # (YZ Plane offset to X=1.79, extrude to X=0.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(1.79)):
        with BuildLine():
            Line((171.558, -18.35), (175.22, -18.35))
            Line((175.22, -18.35), (175.22, -6.35))
            Line((175.22, -6.35), (174.3, -6.35))
            ThreePointArc((174.3, -6.35), get_mid((174.3, -6.35), (173.3, -5.35), (174.3, -5.35), 1.0), (173.3, -5.35))
            Line((173.3, -5.35), (173.3, 5.35))
            ThreePointArc((173.3, 5.35), get_mid((173.3, 5.35), (172.3, 6.35), (172.3, 5.35), 1.0), (172.3, 6.35))
            Line((172.3, 6.35), (159.3, 6.35))
            ThreePointArc((159.3, 6.35), get_mid((159.3, 6.35), (156.3, 3.35), (159.3, 3.35), 3.0), (156.3, 3.35))
            Line((156.3, 3.35), (156.3, -6.6))
            ThreePointArc((156.3, -6.6), get_mid((156.3, -6.6), (153.3, -9.6), (153.3, -6.6), 3.0), (153.3, -9.6))
            Line((153.3, -9.6), (11.5, -9.6))
            ThreePointArc((11.5, -9.6), get_mid((11.5, -9.6), (8.5, -6.6), (11.5, -6.6), 3.0), (8.5, -6.6))
            Line((8.5, -6.6), (8.5, 3.35))
            ThreePointArc((8.5, 3.35), get_mid((8.5, 3.35), (5.5, 6.35), (5.5, 3.35), 3.0), (5.5, 6.35))
            Line((5.5, 6.35), (-5.5, 6.35))
            ThreePointArc((-5.5, 6.35), get_mid((-5.5, 6.35), (-8.5, 3.35), (-5.5, 3.35), 3.0), (-8.5, 3.35))
            Line((-8.5, 3.35), (-8.5, -6.6))
            ThreePointArc((-8.5, -6.6), get_mid((-8.5, -6.6), (-11.5, -9.6), (-11.5, -6.6), 3.0), (-11.5, -9.6))
            Line((-11.5, -9.6), (-153.3, -9.6))
            ThreePointArc((-153.3, -9.6), get_mid((-153.3, -9.6), (-156.3, -6.6), (-153.3, -6.6), 3.0), (-156.3, -6.6))
            Line((-156.3, -6.6), (-156.3, 3.35))
            ThreePointArc((-156.3, 3.35), get_mid((-156.3, 3.35), (-159.3, 6.35), (-159.3, 3.35), 3.0), (-159.3, 6.35))
            Line((-159.3, 6.35), (-172.3, 6.35))
            ThreePointArc((-172.3, 6.35), get_mid((-172.3, 6.35), (-173.3, 5.35), (-172.3, 5.35), 1.0), (-173.3, 5.35))
            Line((-173.3, 5.35), (-173.3, -5.35))
            ThreePointArc((-173.3, -5.35), get_mid((-173.3, -5.35), (-174.3, -6.35), (-174.3, -5.35), 1.0), (-174.3, -6.35))
            Line((-174.3, -6.35), (-175.22, -6.35))
            Line((-175.22, -6.35), (-175.22, -18.35))
            Line((-175.22, -18.35), (-171.558, -18.35))
            ThreePointArc((-171.558, -18.35), get_mid((-171.558, -18.35), (-170.575, -17.534), (-171.558, -17.35), 1.0), (-170.575, -17.534))
            ThreePointArc((-170.575, -17.534), get_mid((-170.575, -17.534), (-168.8, -17.698), (-169.695, -17.698), 0.895), (-168.8, -17.698))
            Line((-168.8, -17.698), (168.8, -17.698))
            ThreePointArc((168.8, -17.698), get_mid((168.8, -17.698), (170.575, -17.534), (169.695, -17.698), 0.895), (170.575, -17.534))
            ThreePointArc((170.575, -17.534), get_mid((170.575, -17.534), (171.558, -18.35), (171.558, -17.35), 1.0), (171.558, -18.35))
        make_face()
    extrude(amount=-1.79)

    # ---------------------------------------------------------
    # FEATURE 2: Second Profile 
    # (XZ Plane offset to Y = -168.8, extrude to Y = 168.8)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-168.8)):
        with BuildLine():
            Line((1.79, -17.698), (0.0, -17.698))
            ThreePointArc((0.0, -17.698), get_mid((0.0, -17.698), (0.838, -20.0), (3.58, -17.698), 3.58), (0.838, -20.0))
            Line((0.838, -20.0), (2.209, -18.849))
            ThreePointArc((2.209, -18.849), get_mid((2.209, -18.849), (1.79, -17.698), (3.58, -17.698), 1.79), (1.79, -17.698))
        make_face()
    extrude(amount=337.6) # Diff from Y=-168.8 to +168.8

    # ---------------------------------------------------------
    # FEATURE 3: Angled Tilted Profile with Subtractive Circles
    # (Mapped to Custom angled_plane)
    # ---------------------------------------------------------
    with BuildSketch(angled_plane):
        with BuildLine():
            Line(prj(7.799, 168.8, -25.511), prj(2.209, 168.8, -18.849))
            Line(prj(2.209, 168.8, -18.849), prj(2.209, -168.8, -18.849))
            Line(prj(2.209, -168.8, -18.849), prj(7.799, -168.8, -25.511))
            ThreePointArc(
                prj(7.799, -168.8, -25.511),
                get_mid(prj(7.799, -168.8, -25.511), prj(9.085, -166.8, -27.043), prj(7.799, -166.8, -25.511), 2.0),
                prj(9.085, -166.8, -27.043)
            )
            Line(prj(9.085, -166.8, -27.043), prj(9.085, 166.8, -27.043))
            ThreePointArc(
                prj(9.085, 166.8, -27.043),
                get_mid(prj(9.085, 166.8, -27.043), prj(7.799, 168.8, -25.511), prj(7.799, 166.8, -25.511), 2.0),
                prj(7.799, 168.8, -25.511)
            )
        make_face()
        
        with Locations(prj(5.423, 163.4, -22.679)):
            Circle(radius=2.25, mode=Mode.SUBTRACT)
            
        with Locations(prj(5.871, 157.5, -23.213), prj(5.871, 0.0, -23.213), prj(5.871, -157.5, -23.213)):
            Circle(radius=1.59, mode=Mode.SUBTRACT)

    # Dynamic target point normal calculation for the angled extrusion
    target_pt = Vector(7.713, -166.8, -28.194)
    extrude_amount = (target_pt - origin).dot(z_dir)
    extrude(amount=extrude_amount)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -18.35)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-18.35)):
        with BuildLine():
            # Continuous head-to-tail traversal in the XY plane
            
            # Edge 4: Line
            Line((1.79, -175.22), (0.0, -175.22))
            
            # Edge 3: Arc
            ThreePointArc((0.0, -175.22), 
                          get_mid((0.0, -175.22), (3.58, -178.8), (3.58, -175.22), 3.58), 
                          (3.58, -178.8))
            
            # Edge 2: Line
            Line((3.58, -178.8), (3.58, -177.01))
            
            # Edge 1: Arc
            ThreePointArc((3.58, -177.01), 
                          get_mid((3.58, -177.01), (1.79, -175.22), (3.58, -175.22), 1.79), 
                          (1.79, -175.22))
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -6.35
    # -6.35 - (-18.35) = 12.0 mm
    # ---------------------------------------------------------
    extrude(amount=12.0)

    # ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -177.01)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(177.01)):
        with BuildLine():
            # Continuous head-to-tail traversal in the XZ plane
            
            # Edge 5: Top Horizontal Line
            Line((18.0, -6.35), (3.58, -6.35))
            
            # Edge 4: Left Vertical Line
            Line((3.58, -6.35), (3.58, -18.35))
            
            # Edge 3: Bottom Horizontal Line
            Line((3.58, -18.35), (16.0, -18.35))
            
            # Edge 2: Rounded Corner Arc
            ThreePointArc((16.0, -18.35), 
                          get_mid((16.0, -18.35), (18.0, -16.35), (16.0, -16.35), 2.0), 
                          (18.0, -16.35))
            
            # Edge 1: Right Vertical Line
            Line((18.0, -16.35), (18.0, -6.35))
            
        make_face()
        
        # --- Subtraction: Edge (Circle) 1 ---
        with Locations((11.5, -12.35)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Y = -178.8
    # -178.8 - (-177.01) = -1.79 mm
    # ---------------------------------------------------------
    extrude(amount=1.79)

# ---------------------------------------------------------
    # Profile Sketch 
    # (YZ Plane offset to X = 18.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(18.0)):
        with BuildLine():
            # Continuous head-to-tail traversal in the YZ plane
            
            # Edge 4: Line
            Line((-177.01, -6.35), (-178.8, -6.35))
            
            # Edge 3: Outer Arc (Radius 3.58)
            ThreePointArc((-178.8, -6.35), 
                          get_mid((-178.8, -6.35), (-178.153, -4.297), (-175.22, -6.35), 3.58), 
                          (-178.153, -4.297))
            
            # Edge 2: Line
            Line((-178.153, -4.297), (-176.686, -5.323))
            
            # Edge 1: Inner Arc (Radius 1.79)
            ThreePointArc((-176.686, -5.323), 
                          get_mid((-176.686, -5.323), (-177.01, -6.35), (-175.22, -6.35), 1.79), 
                          (-177.01, -6.35))
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point X = 3.58
    # 3.58 - 18.0 = -14.42 mm
    # ---------------------------------------------------------
    extrude(amount=-14.42)

# ---------------------------------------------------------
    # Feature: Tilted Profile (custom Plane, extrude +1.79 mm)
    #          Normal = (0, -0.8192, 0.5737), X-dir = (1,0,0)
    #          Traversal: E1 → E6rev → E5rev → E4rev → E3 → E2rev
    # ---------------------------------------------------------
    from build123d import Plane, Vector

    _origin = Vector(3.58, -171.024, 2.763)
    _x_dir  = Vector(1.0,  0.0,      0.0)
    _normal = Vector(0.0, -39.792,   27.864)   # will be normalised internally
    _plane  = Plane(origin=_origin, x_dir=_x_dir, z_dir=_normal)

    with BuildSketch(_plane):
        with BuildLine():
            Line(( 14.42,  0.0),    (14.42, -9.872))   # E1
            Line(( 14.42, -9.872),  ( 0.0,  -9.872))   # E6rev
            Line((  0.0,  -9.872),  ( 0.0,   0.0))     # E5rev
            RadiusArc((0.0,  0.0),  (2.0,   2.0),  2.0)  # E4rev CW
            Line((  2.0,   2.0),    (12.42,  2.0))     # E3
            RadiusArc((12.42, 2.0), (14.42,  0.0), 2.0)  # E2rev CW
        make_face()
    extrude(amount=1.79)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = -18.35)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(-18.35)):
        with BuildLine():
            # Edge 1: Vertical Line
            Line((3.58, 177.01), (3.58, 178.8))
            
            # Edge 2: Outer Arc (Radius 3.58)
            ThreePointArc((3.58, 178.8), 
                          get_mid((3.58, 178.8), (0.0, 175.22), (3.58, 175.22), 3.58), 
                          (0.0, 175.22))
            
            # Edge 3: Horizontal Line
            Line((0.0, 175.22), (1.79, 175.22))
            
            # Edge 4: Inner Arc (Radius 1.79)
            ThreePointArc((1.79, 175.22), 
                          get_mid((1.79, 175.22), (3.58, 177.01), (3.58, 175.22), 1.79), 
                          (3.58, 177.01))
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -6.35
    # -6.35 - (-18.35) = 12.0 mm
    # ---------------------------------------------------------
    extrude(amount=12.0)

    # ---------------------------------------------------------
    # FEATURE 9: Positive Y XZ Mounting Profile (Updated with Circle)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-177.01)):
        with BuildLine():
            # Outer Boundary
            Line((18.0, -6.35), (3.58, -6.35))
            Line((3.58, -6.35), (3.58, -18.35))
            Line((3.58, -18.35), (16.0, -18.35))
            ThreePointArc((16.0, -18.35), 
                          get_mid((16.0, -18.35), (18.0, -16.35), (16.0, -16.35), 2.0), 
                          (18.0, -16.35))
            Line((18.0, -16.35), (18.0, -6.35))
        make_face()
        
        # --- Subtraction: Edge (Circle) 1 ---
        with Locations((11.5, -12.35)):
            Circle(radius=2.175, mode=Mode.SUBTRACT)
        
    # Extrude to target point Y = 178.8
    extrude(amount=-1.79)

# ---------------------------------------------------------
    # Profile Sketch 
    # (YZ Plane offset to X = 18.0)
    # ---------------------------------------------------------
    with BuildSketch(Plane.YZ.offset(18.0)):
        with BuildLine():
            # Continuous head-to-tail traversal in the YZ plane
            
            # Edge 4: Line
            Line((176.686, -5.323), (178.153, -4.297))
            
            # Edge 1: Outer Arc (Radius 3.58)
            ThreePointArc((178.153, -4.297), 
                          get_mid((178.153, -4.297), (178.8, -6.35), (175.22, -6.35), 3.58), 
                          (178.8, -6.35))
            
            # Edge 2 (Reversed): Line
            Line((178.8, -6.35), (177.01, -6.35))
            
            # Edge 3 (Reversed): Inner Arc (Radius 1.79)
            ThreePointArc((177.01, -6.35), 
                          get_mid((177.01, -6.35), (176.686, -5.323), (175.22, -6.35), 1.79), 
                          (176.686, -5.323))
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point X = 3.58
    # 3.58 - 18.0 = -14.42 mm
    # ---------------------------------------------------------
    extrude(amount=-14.42)

# ---------------------------------------------------------
    # Feature: Tilted Positive Y Bracket (Corrected Angle)
    # ---------------------------------------------------------
    from build123d import Plane, Vector

    # Origin at the Start of Edge 1
    _origin = Vector(3.58, 171.024, 2.763)
    _x_dir  = Vector(1.0,  0.0,      0.0)
    # Corrected normal: Y is positive to tilt toward the extrusion target
    _normal = Vector(0.0, 39.792, 27.864)  
    _plane  = Plane(origin=_origin, x_dir=_x_dir, z_dir=_normal)

    with BuildSketch(_plane):
        with BuildLine():
            # Traversal based on local V-axis pointing toward (3.58, 176.686, -5.323)
            # Edge 1: Start to End (Height = 9.871)
            Line((0.0, 0.0), (0.0, 9.871))
            
            # Edge 6rev: Across the top (Width = 14.42)
            Line((0.0, 9.871), (14.42, 9.871))
            
            # Edge 5rev: Down the other side
            Line((14.42, 9.871), (14.42, 0.0))
            
            # Edge 4rev: Arc from (14.42, 0.0) down to (12.42, -2.0)
            RadiusArc((14.42, 0.0), (12.42, -2.0), 2.0)
            
            # Edge 3: Bottom horizontal line
            Line((12.42, -2.0), (2.0, -2.0))
            
            # Edge 2rev: Arc back to the origin
            RadiusArc((2.0, -2.0), (0.0, 0.0), 2.0)
            
        make_face()
        
    # Extrude along the positive Z-normal of the tilted plane
    extrude(amount=1.79)
if __name__ == "__main__":
    show(part)
    export_stl(part.part, "output_PN-000663_v14.stl")