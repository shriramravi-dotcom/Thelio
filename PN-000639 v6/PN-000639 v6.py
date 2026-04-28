from build123d import *
from ocp_vscode import show
import numpy as np

def get_mid(p1, p2, centre, r, flip=False):
    """Calculates the exact midpoint of an arc."""
    c = np.array(centre)
    a = np.array(p1)
    b = np.array(p2)
    v1 = a - c
    v2 = b - c
    mid_dir = v1 + v2
    norm = np.linalg.norm(mid_dir)
    if norm < 1e-10:
        perp = np.array([-v1[1], v1[0]])
        mid_dir = perp if not flip else -perp
        mid_dir = mid_dir / np.linalg.norm(mid_dir)
    else:
        mid_dir = mid_dir / norm
        if flip:
            mid_dir = -mid_dir
    return tuple(c + mid_dir * r)

with BuildPart() as part:
    # ---------------------------------------------------------
    # Profile Sketch 
    # (XY Plane offset to Z = 1.6)
    # ---------------------------------------------------------
    with BuildSketch(Plane.XY.offset(1.6)):
        
        # --- 1. Outer Boundary ---
        with BuildLine(mode=Mode.PRIVATE) as outer:
            ThreePointArc((0.0, 44.5), get_mid((0.0, 44.5), (3.0, 47.5), (3.0, 44.5), 3.0), (3.0, 47.5))
            Line((3.0, 47.5), (9.0, 47.5))
            ThreePointArc((9.0, 47.5), get_mid((9.0, 47.5), (11.99, 50.25), (9.0, 50.5), 3.0), (11.99, 50.25))
            ThreePointArc((11.99, 50.25), get_mid((11.99, 50.25), (14.979, 53.0), (14.979, 50.0), 3.0), (14.979, 53.0))
            Line((14.979, 53.0), (114.521, 53.0))
            ThreePointArc((114.521, 53.0), get_mid((114.521, 53.0), (117.51, 50.25), (114.521, 50.0), 3.0), (117.51, 50.25))
            ThreePointArc((117.51, 50.25), get_mid((117.51, 50.25), (120.5, 47.5), (120.5, 50.5), 3.0), (120.5, 47.5))
            Line((120.5, 47.5), (126.5, 47.5))
            ThreePointArc((126.5, 47.5), get_mid((126.5, 47.5), (129.5, 44.5), (126.5, 44.5), 3.0), (129.5, 44.5))
            Line((129.5, 44.5), (129.5, 25.0))
            ThreePointArc((129.5, 25.0), get_mid((129.5, 25.0), (127.0, 22.042), (126.5, 25.0), 3.0), (127.0, 22.042))
            ThreePointArc((127.0, 22.042), get_mid((127.0, 22.042), (124.5, 19.084), (127.5, 19.084), 3.0), (124.5, 19.084))
            Line((124.5, 19.084), (124.5, 3.0))
            ThreePointArc((124.5, 3.0), get_mid((124.5, 3.0), (121.5, 0.0), (121.5, 3.0), 3.0), (121.5, 0.0))
            Line((121.5, 0.0), (8.0, 0.0))
            ThreePointArc((8.0, 0.0), get_mid((8.0, 0.0), (5.0, 3.0), (8.0, 3.0), 3.0), (5.0, 3.0))
            Line((5.0, 3.0), (5.0, 19.0))
            ThreePointArc((5.0, 19.0), get_mid((5.0, 19.0), (2.5, 21.958), (2.0, 19.0), 3.0), (2.5, 21.958))
            ThreePointArc((2.5, 21.958), get_mid((2.5, 21.958), (0.0, 24.916), (3.0, 24.916), 3.0), (0.0, 24.916))
            Line((0.0, 24.916), (0.0, 44.5))
        make_face(outer.edges())
        
        # --- 2. Subtractions: Circles ---
        with Locations((5.0, 28.0), (124.5, 28.0)):
            Circle(radius=1.725, mode=Mode.SUBTRACT)

        # --- 3. Subtractions: Inner Slots and Cutouts ---
        
        # Slot 1
        with BuildLine(mode=Mode.PRIVATE) as slot1:
            ThreePointArc((20.0, 42.0), get_mid((20.0, 42.0), (22.0, 44.0), (22.0, 42.0), 2.0), (22.0, 44.0))
            Line((22.0, 44.0), (23.0, 44.0))
            ThreePointArc((23.0, 44.0), get_mid((23.0, 44.0), (25.0, 42.0), (23.0, 42.0), 2.0), (25.0, 42.0))
            Line((25.0, 42.0), (25.0, 11.0))
            ThreePointArc((25.0, 11.0), get_mid((25.0, 11.0), (23.0, 9.0), (23.0, 11.0), 2.0), (23.0, 9.0))
            Line((23.0, 9.0), (22.0, 9.0))
            ThreePointArc((22.0, 9.0), get_mid((22.0, 9.0), (20.0, 11.0), (22.0, 11.0), 2.0), (20.0, 11.0))
            Line((20.0, 11.0), (20.0, 42.0))
        make_face(slot1.edges(), mode=Mode.SUBTRACT)
        
        # Slot 2
        with BuildLine(mode=Mode.PRIVATE) as slot2:
            ThreePointArc((31.0, 42.0), get_mid((31.0, 42.0), (33.0, 44.0), (33.0, 42.0), 2.0), (33.0, 44.0))
            Line((33.0, 44.0), (34.0, 44.0))
            ThreePointArc((34.0, 44.0), get_mid((34.0, 44.0), (36.0, 42.0), (34.0, 42.0), 2.0), (36.0, 42.0))
            Line((36.0, 42.0), (36.0, 11.0))
            ThreePointArc((36.0, 11.0), get_mid((36.0, 11.0), (34.0, 9.0), (34.0, 11.0), 2.0), (34.0, 9.0))
            Line((34.0, 9.0), (33.0, 9.0))
            ThreePointArc((33.0, 9.0), get_mid((33.0, 9.0), (31.0, 11.0), (33.0, 11.0), 2.0), (31.0, 11.0))
            Line((31.0, 11.0), (31.0, 42.0))
        make_face(slot2.edges(), mode=Mode.SUBTRACT)
        
        # Profile 4: Rectangular Diamond Cutout
        pts_p4 = [
            (43.251, 46.712), (44.817, 48.262), (46.383, 46.712), 
            (46.383, 28.983), (44.817, 27.432), (43.251, 28.983)
        ]
        with BuildLine(mode=Mode.PRIVATE) as prof4:
            Polyline(pts_p4, close=True)
        make_face(prof4.edges(), mode=Mode.SUBTRACT)
        
        # Profile 5: Complex Right-Side Polygon Cutout
        pts_p5 = [
            (70.726, 37.469), (69.229, 38.749), (69.176, 39.12), (65.88, 44.506),
            (59.848, 45.966), (54.822, 42.876), (53.161, 37.866), (53.192, 37.115),
            (53.277, 36.443), (56.6, 31.125), (59.986, 29.755), (68.155, 31.686),
            (69.393, 32.374), (83.884, 40.374), (84.318, 40.517), (86.053, 39.834),
            (86.249, 39.099), (85.72, 37.972), (85.392, 37.702), (69.858, 29.2),
            (66.366, 27.623), (56.393, 27.835), (54.922, 28.723), (50.388, 35.961),
            (50.272, 36.866), (50.23, 37.866), (52.235, 44.305), (59.361, 48.849),
            (67.583, 46.887), (72.059, 39.601), (72.133, 39.099), (71.773, 37.956)
        ]
        with BuildLine(mode=Mode.PRIVATE) as prof5:
            Polyline(pts_p5, close=True)
        make_face(prof5.edges(), mode=Mode.SUBTRACT)

        # Profile 6: Complex Bottom-Right Polygon Cutout
        pts_p6 = [
            (64.731, 9.862), (65.578, 10.486), (66.599, 10.327), (70.906, 7.772),
            (70.906, 22.337), (45.484, 8.629), (44.32, 8.513), (43.394, 9.29),
            (43.214, 10.01), (44.018, 11.359), (71.34, 26.089), (73.303, 25.634),
            (73.609, 24.634), (73.609, 5.338), (72.303, 4.0), (71.535, 4.201),
            (65.139, 8.0), (64.52, 9.132)
        ]
        with BuildLine(mode=Mode.PRIVATE) as prof6:
            Polyline(pts_p6, close=True)
        make_face(prof6.edges(), mode=Mode.SUBTRACT)
        
        # Slot 3
        with BuildLine(mode=Mode.PRIVATE) as slot3:
            ThreePointArc((93.5, 42.0), get_mid((93.5, 42.0), (95.5, 44.0), (95.5, 42.0), 2.0), (95.5, 44.0))
            Line((95.5, 44.0), (96.5, 44.0))
            ThreePointArc((96.5, 44.0), get_mid((96.5, 44.0), (98.5, 42.0), (96.5, 42.0), 2.0), (98.5, 42.0))
            Line((98.5, 42.0), (98.5, 11.0))
            ThreePointArc((98.5, 11.0), get_mid((98.5, 11.0), (96.5, 9.0), (96.5, 11.0), 2.0), (96.5, 9.0))
            Line((96.5, 9.0), (95.5, 9.0))
            ThreePointArc((95.5, 9.0), get_mid((95.5, 9.0), (93.5, 11.0), (95.5, 11.0), 2.0), (93.5, 11.0))
            Line((93.5, 11.0), (93.5, 42.0))
        make_face(slot3.edges(), mode=Mode.SUBTRACT)
        
        # Slot 4
        with BuildLine(mode=Mode.PRIVATE) as slot4:
            ThreePointArc((104.5, 42.0), get_mid((104.5, 42.0), (106.5, 44.0), (106.5, 42.0), 2.0), (106.5, 44.0))
            Line((106.5, 44.0), (107.5, 44.0))
            ThreePointArc((107.5, 44.0), get_mid((107.5, 44.0), (109.5, 42.0), (107.5, 42.0), 2.0), (109.5, 42.0))
            Line((109.5, 42.0), (109.5, 11.0))
            ThreePointArc((109.5, 11.0), get_mid((109.5, 11.0), (107.5, 9.0), (107.5, 11.0), 2.0), (107.5, 9.0))
            Line((107.5, 9.0), (106.5, 9.0))
            ThreePointArc((106.5, 9.0), get_mid((106.5, 9.0), (104.5, 11.0), (106.5, 11.0), 2.0), (104.5, 11.0))
            Line((104.5, 11.0), (104.5, 42.0))
        make_face(slot4.edges(), mode=Mode.SUBTRACT)

    # ---------------------------------------------------------
    # Extrude to target point Z = 0.0
    # 0.0 - 1.6 = -1.6 mm
    # ---------------------------------------------------------
    extrude(amount=-1.6)

if __name__ == "__main__":
    show(part)

export_stl(part.part, "output_PN-000639_v6.stl") 