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

# --- Define the Angled Plane ---
origin_pt = Vector(2.209, -178.5, -12.499)
x_dir = Vector(0.0, 1.0, 0.0) # Long axis (Y)
# The Tilt vector from (2.209, -12.499) to (7.156, -18.395)
tilt_vec = Vector(7.156 - 2.209, 0, -18.395 - (-12.499))
y_dir = tilt_vec.normalized()
z_dir = x_dir.cross(y_dir).normalized() # Normal for extrusion
plane = Plane(origin=origin_pt, x_dir=x_dir, z_dir=z_dir)

def prj(x, y, z):
    """Projects 3D points onto the local 2D sketch plane."""
    v = Vector(x, y, z) - origin_pt
    return (v.dot(x_dir), v.dot(y_dir))

with BuildPart() as part:
    # Sketch on the YZ Plane offset to the provided X coordinate
    with BuildSketch(Plane.YZ.offset(1.79)):
        with BuildLine():
            # Continuous traversal using (Y, Z) coordinates
            Line((-178.5, -11.348), (178.5, -11.348)) # E1
            Line((178.5, -11.348), (178.5, -9.138))  # E2
            
            # E3
            ThreePointArc((178.5, -9.138), 
                          get_mid((178.5, -9.138), (175.5, -6.138), (175.5, -9.138), 3.0), 
                          (175.5, -6.138))
            
            Line((175.5, -6.138), (174.425, -6.138)) # E4
            Line((174.425, -6.138), (174.425, -4.348)) # E5
            Line((174.425, -4.348), (175.32, -4.348))  # E6
            Line((175.32, -4.348), (175.32, 12.7))     # E7
            Line((175.32, 12.7), (162.0, 12.7))        # E8
            
            # E9
            ThreePointArc((162.0, 12.7), 
                          get_mid((162.0, 12.7), (159.0, 9.7), (162.0, 9.7), 3.0), 
                          (159.0, 9.7))
            
            Line((159.0, 9.7), (159.0, 0.626))         # E10
            
            # E11
            ThreePointArc((159.0, 0.626), 
                          get_mid((159.0, 0.626), (156.0, -2.374), (156.0, 0.626), 3.0), 
                          (156.0, -2.374))
            
            Line((156.0, -2.374), (53.25, -2.374))     # E12
            
            # E13
            ThreePointArc((53.25, -2.374), 
                          get_mid((53.25, -2.374), (52.25, -1.374), (53.25, -1.374), 1.0), 
                          (52.25, -1.374))
            
            Line((52.25, -1.374), (52.25, -0.374))     # E14
            
            # E15
            ThreePointArc((52.25, -0.374), 
                          get_mid((52.25, -0.374), (51.25, 0.626), (51.25, -0.374), 1.0), 
                          (51.25, 0.626))
            
            Line((51.25, 0.626), (46.75, 0.626))       # E16
            
            # E17
            ThreePointArc((46.75, 0.626), 
                          get_mid((46.75, 0.626), (45.75, -0.374), (46.75, -0.374), 1.0), 
                          (45.75, -0.374))
            
            Line((45.75, -0.374), (45.75, -1.374))     # E18
            
            # E19
            ThreePointArc((45.75, -1.374), 
                          get_mid((45.75, -1.374), (44.75, -2.374), (44.75, -1.374), 1.0), 
                          (44.75, -2.374))
            
            Line((44.75, -2.374), (-44.75, -2.374))    # E20
            
            # E21
            ThreePointArc((-44.75, -2.374), 
                          get_mid((-44.75, -2.374), (-45.75, -1.374), (-44.75, -1.374), 1.0), 
                          (-45.75, -1.374))
            
            Line((-45.75, -1.374), (-45.75, -0.374))   # E22
            
            # E23
            ThreePointArc((-45.75, -0.374), 
                          get_mid((-45.75, -0.374), (-46.75, 0.626), (-46.75, -0.374), 1.0), 
                          (-46.75, 0.626))
            
            Line((-46.75, 0.626), (-51.25, 0.626))     # E24
            
            # E25
            ThreePointArc((-51.25, 0.626), 
                          get_mid((-51.25, 0.626), (-52.25, -0.374), (-51.25, -0.374), 1.0), 
                          (-52.25, -0.374))
            
            Line((-52.25, -0.374), (-52.25, -1.374))   # E26
            
            # E27
            ThreePointArc((-52.25, -1.374), 
                          get_mid((-52.25, -1.374), (-53.25, -2.374), (-53.25, -1.374), 1.0), 
                          (-53.25, -2.374))
            
            Line((-53.25, -2.374), (-156.0, -2.374))   # E28
            
            # E29
            ThreePointArc((-156.0, -2.374), 
                          get_mid((-156.0, -2.374), (-159.0, 0.626), (-156.0, 0.626), 3.0), 
                          (-159.0, 0.626))
            
            Line((-159.0, 0.626), (-159.0, 9.7))       # E30
            
            # E31
            ThreePointArc((-159.0, 9.7), 
                          get_mid((-159.0, 9.7), (-162.0, 12.7), (-162.0, 9.7), 3.0), 
                          (-162.0, 12.7))
            
            Line((-162.0, 12.7), (-175.32, 12.7))      # E32
            Line((-175.32, 12.7), (-175.32, -4.348))   # E33
            Line((-175.32, -4.348), (-174.425, -4.348))# E34
            Line((-174.425, -4.348), (-174.425, -6.138))# E35
            Line((-174.425, -6.138), (-175.5, -6.138)) # E36
            
            # E37
            ThreePointArc((-175.5, -6.138), 
                          get_mid((-175.5, -6.138), (-178.5, -9.138), (-175.5, -9.138), 3.0), 
                          (-178.5, -9.138))
            
            Line((-178.5, -9.138), (-178.5, -11.348))  # E38
        make_face()
        
        # Subtractive Circular Cutout
        with Locations((168.75, -6.374)):
            Circle(radius=2.5, mode=Mode.SUBTRACT)

    # Extrude from X=1.79 to X=0.0
    extrude(amount=-1.79)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = -178.5)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-178.5)):
        with BuildLine():
            # Continuous head-to-tail traversal in the XZ plane
            
            # Edge 1: Inner Arc (Radius 1.79)
            ThreePointArc((1.79, -11.348), 
                          get_mid((1.79, -11.348), (2.209, -12.499), (3.58, -11.348), 1.79), 
                          (2.209, -12.499))
            
            # Edge 2: Connecting Line
            Line((2.209, -12.499), (0.838, -13.65))
            
            # Edge 3: Outer Arc (Radius 3.58)
            ThreePointArc((0.838, -13.65), 
                          get_mid((0.838, -13.65), (0.0, -11.348), (3.58, -11.348), 3.58), 
                          (0.0, -11.348))
            
            # Edge 4: Closure Line
            Line((0.0, -11.348), (1.79, -11.348))
            
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Y = 178.5
    # 178.5 - (-178.5) = 357.0 mm
    # ---------------------------------------------------------
    extrude(amount=357.0)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = 12.7)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(12.7)):
        with BuildLine():
            # Edge 4: Line
            Line((1.79, 175.32), (0.0, 175.32))
            
            # Edge 3: Outer Arc (Radius 3.58)
            ThreePointArc((0.0, 175.32), 
                          get_mid((0.0, 175.32), (3.58, 178.9), (3.58, 175.32), 3.58), 
                          (3.58, 178.9))
            
            # Edge 2: Line
            Line((3.58, 178.9), (3.58, 177.11))
            
            # Edge 1: Inner Arc (Radius 1.79)
            ThreePointArc((3.58, 177.11), 
                          get_mid((3.58, 177.11), (1.79, 175.32), (3.58, 175.32), 1.79), 
                          (1.79, 175.32))
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -4.348
    # -4.348 - 12.7 = -17.048 mm
    # ---------------------------------------------------------
    extrude(amount=-17.048)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = 177.11)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(-177.11)):
        with BuildLine():
            # Edge 10: Right Vertical side
            Line((3.58, 12.7), (3.58, -4.348))
            
            # Edge 1: Bottom Horizontal side
            Line((3.58, -4.348), (17.0, -4.348))
            
            # Edge 2: Bottom Corner Arc (Radius 3.0)
            ThreePointArc((17.0, -4.348), 
                          get_mid((17.0, -4.348), (20.0, -1.348), (17.0, -1.348), 3.0), 
                          (20.0, -1.348))
            
            # Edge 3: Left Vertical side
            Line((20.0, -1.348), (20.0, 8.2))
            
            # Edge 4: Left Top Arc (Radius 1.0)
            ThreePointArc((20.0, 8.2), 
                          get_mid((20.0, 8.2), (19.0, 9.2), (19.0, 8.2), 1.0), 
                          (19.0, 9.2))
            
            # Edge 5: Top Horizontal step
            Line((19.0, 9.2), (10.0, 9.2))
            
            # Edge 6: Inner Corner Arc (Radius 1.0)
            ThreePointArc((10.0, 9.2), 
                          get_mid((10.0, 9.2), (9.0, 10.2), (10.0, 10.2), 1.0), 
                          (9.0, 10.2))
            
            # Edge 7: Short Vertical step
            Line((9.0, 10.2), (9.0, 11.7))
            
            # Edge 8: Final Top Corner Arc (Radius 1.0)
            ThreePointArc((9.0, 11.7), 
                          get_mid((9.0, 11.7), (8.0, 12.7), (8.0, 11.7), 1.0), 
                          (8.0, 12.7))
            
            # Edge 9: Top Horizontal closure
            Line((8.0, 12.7), (3.58, 12.7))
            
        make_face()
        
        # --- Subtractions: Circles ---
        with Locations((6.8, 4.176), (13.4, 4.176)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Y = 178.9
    # 178.9 - 177.11 = 1.79 mm
    # ---------------------------------------------------------
    extrude(amount=-1.79)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XZ Plane offset to Y = 177.11)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XZ.offset(177.11)):
        with BuildLine():
            # Edge 10: Right Vertical side
            Line((3.58, 12.7), (3.58, -4.348))
            
            # Edge 1: Bottom Horizontal side
            Line((3.58, -4.348), (17.0, -4.348))
            
            # Edge 2: Bottom Corner Arc (Radius 3.0)
            ThreePointArc((17.0, -4.348), 
                          get_mid((17.0, -4.348), (20.0, -1.348), (17.0, -1.348), 3.0), 
                          (20.0, -1.348))
            
            # Edge 3: Left Vertical side
            Line((20.0, -1.348), (20.0, 8.2))
            
            # Edge 4: Left Top Arc (Radius 1.0)
            ThreePointArc((20.0, 8.2), 
                          get_mid((20.0, 8.2), (19.0, 9.2), (19.0, 8.2), 1.0), 
                          (19.0, 9.2))
            
            # Edge 5: Top Horizontal step
            Line((19.0, 9.2), (10.0, 9.2))
            
            # Edge 6: Inner Corner Arc (Radius 1.0)
            ThreePointArc((10.0, 9.2), 
                          get_mid((10.0, 9.2), (9.0, 10.2), (10.0, 10.2), 1.0), 
                          (9.0, 10.2))
            
            # Edge 7: Short Vertical step
            Line((9.0, 10.2), (9.0, 11.7))
            
            # Edge 8: Final Top Corner Arc (Radius 1.0)
            ThreePointArc((9.0, 11.7), 
                          get_mid((9.0, 11.7), (8.0, 12.7), (8.0, 11.7), 1.0), 
                          (8.0, 12.7))
            
            # Edge 9: Top Horizontal closure
            Line((8.0, 12.7), (3.58, 12.7))
            
        make_face()
        
        # --- Subtractions: Circles ---
        with Locations((6.8, 4.176), (13.4, 4.176)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point Y = 178.9
    # 178.9 - 177.11 = 1.79 mm
    # ---------------------------------------------------------
    extrude(amount=1.79)

# ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = 12.7)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(12.7)):
        with BuildLine():
            # Edge 4: Vertical Line
            Line((3.58, -177.11), (3.58, -178.9))
            
            # Edge 3: Outer Arc (Radius 3.58)
            ThreePointArc((3.58, -178.9), 
                          get_mid((3.58, -178.9), (0.0, -175.32), (3.58, -175.32), 3.58), 
                          (0.0, -175.32))
            
            # Edge 2: Horizontal Line
            Line((0.0, -175.32), (1.79, -175.32))
            
            # Edge 1: Inner Arc (Radius 1.79)
            ThreePointArc((1.79, -175.32), 
                          get_mid((1.79, -175.32), (3.58, -177.11), (3.58, -175.32), 1.79), 
                          (3.58, -177.11))
        make_face()
        
    # ---------------------------------------------------------
    # Extrude to target point Z = -4.348
    # -4.348 - 12.7 = -17.048 mm
    # ---------------------------------------------------------
    extrude(amount=-17.048)

# ---------------------------------------------------------
    # Profile Sketch (Indented inside BuildPart)
    # ---------------------------------------------------------
    with BuildSketch(plane):
        with BuildLine():
            # Continuous traversal through the 18 Edges
            # Edge 1: Angled Slope
            Line(prj(2.209, -178.5, -12.499), prj(7.156, -178.5, -18.395))
            
            # Edge 2: Arc (R=3.0)
            ThreePointArc(prj(7.156, -178.5, -18.395),
                          prj(*get_mid((7.156, -178.5, -18.395), (9.085, -175.5, -20.693), (7.156, -175.5, -18.395), 3.0)),
                          prj(9.085, -175.5, -20.693))
            
            # Edge 3: Vertical side
            Line(prj(9.085, -175.5, -20.693), prj(9.085, -161.124, -20.693))
            
            # Edge 4: Transition Arc (R=3.0)
            ThreePointArc(prj(9.085, -161.124, -20.693),
                          prj(*get_mid((9.085, -161.124, -20.693), (8.218, -158.62, -19.66), (7.156, -161.124, -18.395), 3.0)),
                          prj(8.218, -158.62, -19.66))
            
            # Edge 5: Reverse transition Arc (R=3.0)
            ThreePointArc(prj(8.218, -158.62, -19.66),
                          prj(*get_mid((8.218, -158.62, -19.66), (7.351, -156.115, -18.627), (9.279, -156.115, -20.926), 3.0)),
                          prj(7.351, -156.115, -18.627))
            
            # Edge 6: Main length
            Line(prj(7.351, -156.115, -18.627), prj(7.351, -9.985, -18.627))
            
            # Edge 7 & 8: Notch Arcs
            ThreePointArc(prj(7.351, -9.985, -18.627),
                          prj(*get_mid((7.351, -9.985, -18.627), (8.218, -7.48, -19.66), (9.279, -9.985, -20.926), 3.0)),
                          prj(8.218, -7.48, -19.66))
            ThreePointArc(prj(8.218, -7.48, -19.66),
                          prj(*get_mid((8.218, -7.48, -19.66), (9.085, -4.976, -20.693), (7.156, -4.976, -18.395), 3.0)),
                          prj(9.085, -4.976, -20.693))
            
            # Edge 9: Middle side
            Line(prj(9.085, -4.976, -20.693), prj(9.085, 4.015, -20.693))
            
            # Edge 10 & 11: Transition Arcs
            ThreePointArc(prj(9.085, 4.015, -20.693),
                          prj(*get_mid((9.085, 4.015, -20.693), (8.218, 6.52, -19.66), (7.156, 4.015, -18.395), 3.0)),
                          prj(8.218, 6.52, -19.66))
            ThreePointArc(prj(8.218, 6.52, -19.66),
                          prj(*get_mid((8.218, 6.52, -19.66), (7.351, 9.024, -18.627), (9.279, 9.024, -20.926), 3.0)),
                          prj(7.351, 9.024, -18.627))
            
            # Edge 12: Second main length
            Line(prj(7.351, 9.024, -18.627), prj(7.351, 157.076, -18.627))
            
            # Edge 13 & 14: Notch Arcs
            ThreePointArc(prj(7.351, 157.076, -18.627),
                          prj(*get_mid((7.351, 157.076, -18.627), (8.218, 159.58, -19.66), (9.279, 157.076, -20.926), 3.0)),
                          prj(8.218, 159.58, -19.66))
            ThreePointArc(prj(8.218, 159.58, -19.66),
                          prj(*get_mid((8.218, 159.58, -19.66), (9.085, 162.085, -20.693), (7.156, 162.085, -18.395), 3.0)),
                          prj(9.085, 162.085, -20.693))
            
            # Edge 15: Far Vertical side
            Line(prj(9.085, 162.085, -20.693), prj(9.085, 175.5, -20.693))
            
            # Edge 16: Closing Arc
            ThreePointArc(prj(9.085, 175.5, -20.693),
                          prj(*get_mid((9.085, 175.5, -20.693), (7.156, 178.5, -18.395), (7.156, 175.5, -18.395), 3.0)),
                          prj(7.156, 178.5, -18.395))
            
            # Edge 17: Closing top slope
            Line(prj(7.156, 178.5, -18.395), prj(2.209, 178.5, -12.499))
            
            # Edge 18: Bottom long closure
            Line(prj(2.209, 178.5, -12.499), prj(2.209, -178.5, -12.499))
        make_face()
        
        # Subtractions: Circles (Holes along the rail)
        hole_locs = [
            prj(6.128, -172.5, -17.17),
            prj(6.128, -165.0, -17.17),
            prj(6.128, 172.5, -17.17),
            prj(6.128, 165.0, -17.17),
            prj(6.128, 0.0, -17.17)
        ]
        with Locations(*hole_locs):
            Circle(radius=1.59, mode=Mode.SUBTRACT)
        
    # ---------------------------------------------------------
    # Extrude to target point
    # Distance is calculated based on projection along the normal
    # ---------------------------------------------------------
    extrude(amount=1.79)

if __name__ == "__main__":
    show(part)
    export_stl(part.part, "output_PN-000662_v14.stl")