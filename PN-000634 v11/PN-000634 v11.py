from build123d import *
import numpy as np

# Part: PN-000634 v11

def get_mid(p1, p2, centre, r, flip=False):
    c = np.array(centre); a = np.array(p1); b = np.array(p2)
    v1 = a - c; v2 = b - c
    md = v1 + v2; n = np.linalg.norm(md)
    if n < 1e-10:
        perp = np.array([-v1[1], v1[0]])
        md = (-perp if flip else perp) / np.linalg.norm(perp)
    else:
        md = md / n
        if flip: md = -md
    return tuple(c + md * r)

with BuildPart() as part:

    with BuildSketch(Plane.XY.offset(1.6)):

        # ── Main Rectangle ────────────────────────────────────
        with BuildLine():
            Polyline([(26.6, 0.0), (226.4, 0.0),
                      (226.4, 368.4), (26.6, 368.4)], close=True)
        make_face()

        # ── Lightning-bolt subtract 1 (Y~267) ─────────────────
        with BuildLine():
            Line((94.63, 267.423), (99.07, 267.423))
            Line((99.07, 267.423), (97.993, 264.665))
            Line((97.993, 264.665), (98.605, 262.571))
            Line((98.605, 262.571), (99.439, 262.439))
            ThreePointArc((99.439, 262.439),
                get_mid((99.439,262.439),(99.963,262.705),(99.518,262.932),0.5),
                (99.963, 262.705))
            Line((99.963, 262.705), (101.793, 266.29))
            ThreePointArc((101.793, 266.29),
                get_mid((101.793,266.29),(102.543,266.039),(102.149,266.109),0.4),
                (102.543, 266.039))
            Line((102.543, 266.039), (101.569, 260.497))
            ThreePointArc((101.569, 260.497),
                get_mid((101.569,260.497),(101.367,260.104),(100.83,260.627),0.75),
                (101.367, 260.104))
            Line((101.367, 260.104), (99.465, 258.15))
            Line((99.465, 258.15), (97.091, 248.486))
            ThreePointArc((97.091, 248.486),
                get_mid((97.091,248.486),(96.609,248.486),(96.85,248.664),0.3),
                (96.609, 248.486))
            Line((96.609, 248.486), (94.235, 258.15))
            Line((94.235, 258.15), (92.333, 260.104))
            ThreePointArc((92.333, 260.104),
                get_mid((92.333,260.104),(92.131,260.497),(92.87,260.627),0.75),
                (92.131, 260.497))
            Line((92.131, 260.497), (91.157, 266.039))
            ThreePointArc((91.157, 266.039),
                get_mid((91.157,266.039),(91.907,266.29),(91.551,266.109),0.4),
                (91.907, 266.29))
            Line((91.907, 266.29), (93.737, 262.705))
            ThreePointArc((93.737, 262.705),
                get_mid((93.737,262.705),(94.261,262.439),(94.182,262.932),0.5),
                (94.261, 262.439))
            Line((94.261, 262.439), (95.095, 262.571))
            Line((95.095, 262.571), (95.707, 264.665))
            Line((95.707, 264.665), (94.63, 267.423))
        make_face(mode=Mode.SUBTRACT)

        # ── Lightning-bolt subtract 2 (Y~121.923) ─────────────
        with BuildLine():
            Line((94.63, 121.923), (99.07, 121.923))
            Line((99.07, 121.923), (97.993, 119.165))
            Line((97.993, 119.165), (98.605, 117.071))
            Line((98.605, 117.071), (99.439, 116.939))
            ThreePointArc((99.439, 116.939),
                get_mid((99.439,116.939),(99.963,117.205),(99.518,117.432),0.5),
                (99.963, 117.205))
            Line((99.963, 117.205), (101.793, 120.79))
            ThreePointArc((101.793, 120.79),
                get_mid((101.793,120.79),(102.543,120.539),(102.149,120.609),0.4),
                (102.543, 120.539))
            Line((102.543, 120.539), (101.569, 114.997))
            ThreePointArc((101.569, 114.997),
                get_mid((101.569,114.997),(101.367,114.604),(100.83,115.127),0.75),
                (101.367, 114.604))
            Line((101.367, 114.604), (99.465, 112.65))
            Line((99.465, 112.65), (97.091, 102.986))
            ThreePointArc((97.091, 102.986),
                get_mid((97.091,102.986),(96.609,102.986),(96.85,103.164),0.3),
                (96.609, 102.986))
            Line((96.609, 102.986), (94.235, 112.65))
            Line((94.235, 112.65), (92.333, 114.604))
            ThreePointArc((92.333, 114.604),
                get_mid((92.333,114.604),(92.131,114.997),(92.87,115.127),0.75),
                (92.131, 114.997))
            Line((92.131, 114.997), (91.157, 120.539))
            ThreePointArc((91.157, 120.539),
                get_mid((91.157,120.539),(91.907,120.79),(91.551,120.609),0.4),
                (91.907, 120.79))
            Line((91.907, 120.79), (93.737, 117.205))
            ThreePointArc((93.737, 117.205),
                get_mid((93.737,117.205),(94.261,116.939),(94.182,117.432),0.5),
                (94.261, 116.939))
            Line((94.261, 116.939), (95.095, 117.071))
            Line((95.095, 117.071), (95.707, 119.165))
            Line((95.707, 119.165), (94.63, 121.923))
        make_face(mode=Mode.SUBTRACT)

      # ── Gear around C1=(96.85, 259.25): 6 teeth + 6 ring segments ──
        C1 = (96.85, 259.25)

        # Tooth 1
        with BuildLine():
            Line((98.049, 279.214), (90.399, 303.785))
            ThreePointArc((90.399,303.785), get_mid((90.399,303.785),(127.922,291.8),C1,45), (127.922,291.8))
            Line((127.922,291.8), (111.626,272.728))
            ThreePointArc((111.626,272.728), get_mid((111.626,272.728),(98.049,279.214),C1,20), (98.049,279.214))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 2
        with BuildLine():
            Line((114.739,268.194), (132.193,287.104))
            ThreePointArc((132.193,287.104), get_mid((132.193,287.104),(140.576,248.616),C1,45), (140.576,248.616))
            Line((140.576,248.616), (115.911,253.192))
            ThreePointArc((115.911,253.192), get_mid((115.911,253.192),(114.739,268.194),C1,20), (114.739,268.194))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 3
        with BuildLine():
            Line((113.54,248.23), (138.644,242.569))
            ThreePointArc((138.644,242.569), get_mid((138.644,242.569),(109.503,216.066),C1,45), (109.503,216.066))
            Line((109.503,216.066), (101.134,239.714))
            ThreePointArc((101.134,239.714), get_mid((101.134,239.714),(113.54,248.23),C1,20), (113.54,248.23))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 4
        with BuildLine():
            Line((95.651,239.286), (103.301,214.715))
            ThreePointArc((103.301,214.715), get_mid((103.301,214.715),(65.778,226.7),C1,45), (65.778,226.7))
            Line((65.778,226.7), (82.074,245.772))
            ThreePointArc((82.074,245.772), get_mid((82.074,245.772),(95.651,239.286),C1,20), (95.651,239.286))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 5
        with BuildLine():
            Line((78.961,250.306), (61.507,231.396))
            ThreePointArc((61.507,231.396), get_mid((61.507,231.396),(53.124,269.884),C1,45), (53.124,269.884))
            Line((53.124,269.884), (77.789,265.308))
            ThreePointArc((77.789,265.308), get_mid((77.789,265.308),(78.961,250.306),C1,20), (78.961,250.306))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 6
        with BuildLine():
            Line((80.16,270.27), (55.056,275.931))
            ThreePointArc((55.056,275.931), get_mid((55.056,275.931),(84.197,302.434),C1,45), (84.197,302.434))
            Line((84.197,302.434), (92.566,278.786))
            ThreePointArc((92.566,278.786), get_mid((92.566,278.786),(80.16,270.27),C1,20), (80.16,270.27))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 1
        with BuildLine():
            ThreePointArc((130.081,296.609), get_mid((130.081,296.609),(87.484,308.365),C1,50), (87.484,308.365))
            Line((87.484,308.365), (71.152,324.362))
            ThreePointArc((71.152,324.362), get_mid((71.152,324.362),(135.29,317.751),C1,70), (135.29,317.751))
            Line((135.29,317.751), (130.081,296.609))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 2
        with BuildLine():
            ThreePointArc((145.819,249.151), get_mid((145.819,249.151),(134.702,291.919),C1,50), (134.702,291.919))
            Line((134.702,291.919), (140.39,314.061))
            ThreePointArc((140.39,314.061), get_mid((140.39,314.061),(166.733,255.21),C1,70), (166.733,255.21))
            Line((166.733,255.21), (145.819,249.151))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 3
        with BuildLine():
            ThreePointArc((112.589,211.792), get_mid((112.589,211.792),(144.068,242.804),C1,50), (144.068,242.804))
            Line((144.068,242.804), (166.088,248.949))
            ThreePointArc((166.088,248.949), get_mid((166.088,248.949),(128.293,196.709),C1,70), (128.293,196.709))
            Line((128.293,196.709), (112.589,211.792))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 4
        with BuildLine():
            ThreePointArc((63.619,221.891), get_mid((63.619,221.891),(106.216,210.135),C1,50), (106.216,210.135))
            Line((106.216,210.135), (122.548,194.138))
            ThreePointArc((122.548,194.138), get_mid((122.548,194.138),(58.41,200.749),C1,70), (58.41,200.749))
            Line((58.41,200.749), (63.619,221.891))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 5 — FIXED (gap between arc end and line start)
        with BuildLine():
            ThreePointArc((47.881,269.349), get_mid((47.881,269.349),(58.998,226.581),C1,50), (58.998,226.581))
            Line((58.998,226.581), (53.31,204.439))
            ThreePointArc((53.31,204.439), get_mid((53.31,204.439),(34.712,227.018),C1,70), (34.712,227.018))
            Line((34.712,227.018), (34.6,227.478))   # ← gap-closing connector
            Line((34.6,227.478), (34.6,266.2))
            Line((34.6,266.2), (47.881,269.349))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 6  (has two straight lines closing at X=34.6)
        with BuildLine():
            ThreePointArc((81.111,306.708), get_mid((81.111,306.708),(49.632,275.696),C1,50), (49.632,275.696))
            Line((49.632,275.696), (34.6,272.359))
            Line((34.6,272.359), (34.6,291.265))
            ThreePointArc((34.6,291.265), get_mid((34.6,291.265),(65.407,321.791),C1,70), (65.407,321.791))
            Line((65.407,321.791), (81.111,306.708))
        make_face(mode=Mode.SUBTRACT)

        # ── Gear around C2=(96.85, 114.75): 6 teeth + 6 ring segments ──
        C2 = (96.85, 114.75)

        # Tooth 1
        with BuildLine():
            ThreePointArc((111.038,128.846), get_mid((111.038,128.846),(98.84,134.651),C2,20), (98.84,134.651))
            Line((98.84,134.651), (97.948,135.516))
            Line((97.948,135.516), (91.103,158.009))
            Line((91.103,158.009), (91.874,159.474))
            ThreePointArc((91.874,159.474), get_mid((91.874,159.474),(127.369,147.82),C2,45), (127.369,147.82))
            Line((127.369,147.82), (127.579,146.626))
            Line((127.579,146.626), (112.341,128.746))
            Line((112.341,128.746), (111.038,128.846))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 2
        with BuildLine():
            ThreePointArc((91.736,134.085), get_mid((91.736,134.085),(80.61,126.423),C2,20), (80.61,126.423))
            Line((80.61,126.423), (79.415,126.083))
            Line((79.415,126.083), (56.513,131.402))
            Line((56.513,131.402), (55.63,132.803))
            ThreePointArc((55.63,132.803), get_mid((55.63,132.803),(83.47,157.715),C2,45), (83.47,157.715))
            Line((83.47,157.715), (84.609,157.3))
            Line((84.609,157.3), (92.474,135.164))
            Line((92.474,135.164), (91.736,134.085))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 3
        with BuildLine():
            ThreePointArc((77.548,119.989), get_mid((77.548,119.989),(78.621,106.523),C2,20), (78.621,106.523))
            Line((78.621,106.523), (78.318,105.318))
            Line((78.318,105.318), (62.26,88.143))
            Line((62.26,88.143), (60.606,88.079))
            ThreePointArc((60.606,88.079), get_mid((60.606,88.079),(52.951,124.645),C2,45), (52.951,124.645))
            Line((52.951,124.645), (53.88,125.424))
            Line((53.88,125.424), (76.983,121.167))
            Line((76.983,121.167), (77.548,119.989))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 4
        with BuildLine():
            ThreePointArc((82.662,100.654), get_mid((82.662,100.654),(94.86,94.849),C2,20), (94.86,94.849))
            Line((94.86,94.849), (95.752,93.984))
            Line((95.752,93.984), (102.597,71.491))
            Line((102.597,71.491), (101.826,70.026))
            ThreePointArc((101.826,70.026), get_mid((101.826,70.026),(66.331,81.68),C2,45), (66.331,81.68))
            Line((66.331,81.68), (66.121,82.874))
            Line((66.121,82.874), (81.359,100.754))
            Line((81.359,100.754), (82.662,100.654))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 5
        with BuildLine():
            ThreePointArc((101.964,95.415), get_mid((101.964,95.415),(113.09,103.077),C2,20), (113.09,103.077))
            Line((113.09,103.077), (114.285,103.417))
            Line((114.285,103.417), (137.187,98.098))
            Line((137.187,98.098), (138.07,96.697))
            ThreePointArc((138.07,96.697), get_mid((138.07,96.697),(110.23,71.785),C2,45), (110.23,71.785))
            Line((110.23,71.785), (109.091,72.2))
            Line((109.091,72.2), (101.226,94.336))
            Line((101.226,94.336), (101.964,95.415))
        make_face(mode=Mode.SUBTRACT)

        # Tooth 6
        with BuildLine():
            ThreePointArc((116.152,109.511), get_mid((116.152,109.511),(115.079,122.977),C2,20), (115.079,122.977))
            Line((115.079,122.977), (115.382,124.182))
            Line((115.382,124.182), (131.44,141.357))
            Line((131.44,141.357), (133.094,141.421))
            ThreePointArc((133.094,141.421), get_mid((133.094,141.421),(140.749,104.855),C2,45), (140.749,104.855))
            Line((140.749,104.855), (139.82,104.076))
            Line((139.82,104.076), (116.717,108.333))
            Line((116.717,108.333), (116.152,109.511))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 1
        with BuildLine():
            ThreePointArc((146.084,106.029), get_mid((146.084,106.029),(135.11,146.94),C2,50), (135.11,146.94))
            Line((135.11,146.94), (134.962,147.992))
            Line((134.962,147.992), (140.196,167.735))
            Line((140.196,167.735), (141.832,168.384))
            ThreePointArc((141.832,168.384), get_mid((141.832,168.384),(166.767,111.334),C2,70), (166.767,111.334))
            Line((166.767,111.334), (166.161,110.463))
            Line((166.161,110.463), (147.23,104.867))
            Line((147.23,104.867), (146.084,106.029))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 2
        with BuildLine():
            ThreePointArc((129.02,153.027), get_mid((129.02,153.027),(88.103,163.979),C2,50), (88.103,163.979))
            Line((88.103,163.979), (87.118,164.377))
            Line((87.118,164.377), (72.636,178.781))
            Line((72.636,178.781), (72.892,180.522))
            ThreePointArc((72.892,180.522), get_mid((72.892,180.522),(134.767,173.591),C2,70), (134.767,173.591))
            Line((134.767,173.591), (135.218,172.632))
            Line((135.218,172.632), (130.599,153.439))
            Line((130.599,153.439), (129.02,153.027))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 3  (has Line closing at X=34.6)
        with BuildLine():
            ThreePointArc((79.786,161.748), get_mid((79.786,161.748),(49.843,131.789),C2,50), (49.843,131.789))
            Line((49.843,131.789), (49.006,131.135))
            Line((49.006,131.135), (34.6,127.859))
            Line((34.6,127.859), (34.6,146.765))
            ThreePointArc((34.6,146.765), get_mid((34.6,146.765),(65.407,177.291),C2,70), (65.407,177.291))
            Line((65.407,177.291), (80.219,163.322))
            Line((80.219,163.322), (79.786,161.748))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 4  (has small r=1 arc at X=34.6 boundary)
        with BuildLine():
            ThreePointArc((47.616,123.471), get_mid((47.616,123.471),(58.59,82.56),C2,50), (58.59,82.56))
            Line((58.59,82.56), (58.738,81.508))
            Line((58.738,81.508), (53.504,61.765))
            Line((53.504,61.765), (51.868,61.116))
            ThreePointArc((51.868,61.116), get_mid((51.868,61.116),(34.712,82.518),C2,70), (34.712,82.518))
            ThreePointArc((34.712,82.518), get_mid((34.712,82.518),(34.6,82.978),(35.6,82.978),1.0), (34.6,82.978))
            Line((34.6,82.978), (34.6,121.7))
            Line((34.6,121.7), (46.47,124.633))
            Line((46.47,124.633), (47.616,123.471))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 5
        with BuildLine():
            ThreePointArc((64.68,76.473), get_mid((64.68,76.473),(105.597,65.521),C2,50), (105.597,65.521))
            Line((105.597,65.521), (106.582,65.123))
            Line((106.582,65.123), (121.064,50.719))
            Line((121.064,50.719), (120.808,48.978))
            ThreePointArc((120.808,48.978), get_mid((120.808,48.978),(58.933,55.909),C2,70), (58.933,55.909))
            Line((58.933,55.909), (58.482,56.868))
            Line((58.482,56.868), (63.101,76.061))
            Line((63.101,76.061), (64.68,76.473))
        make_face(mode=Mode.SUBTRACT)

        # Ring segment 6
        with BuildLine():
            ThreePointArc((113.914,67.752), get_mid((113.914,67.752),(143.857,97.711),C2,50), (143.857,97.711))
            Line((143.857,97.711), (144.694,98.365))
            Line((144.694,98.365), (164.409,103.704))
            Line((164.409,103.704), (165.79,102.612))
            ThreePointArc((165.79,102.612), get_mid((165.79,102.612),(128.85,52.492),C2,70), (128.85,52.492))
            Line((128.85,52.492), (127.793,52.581))
            Line((127.793,52.581), (113.481,66.178))
            Line((113.481,66.178), (113.914,67.752))
        make_face(mode=Mode.SUBTRACT)

        # ── 6 Stadium slots (vertical, sep=12.95, h=3.675) ────
        for cx, cy_bot in [
            (198.888, 220.45), (217.563, 220.45),
            (198.888, 135.45), (217.563, 135.45),
            (198.888,  50.45), (217.563,  50.45),
        ]:
            cy_mid = cy_bot + 12.95 / 2
            with Locations((cx, cy_mid)):
                SlotCenterToCenter(center_separation=12.95,
                                   height=3.675,
                                   rotation=90,
                                   mode=Mode.SUBTRACT)

        # ── 26 Circles ────────────────────────────────────────
        with Locations((216.5, 14.2)):   Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations((220.4, 40.2)):   Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations((204.4, 24.2)):   Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations((173.5, 42.8)):   Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations((159.1, 52.5)):   Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations((126.5, 14.2)):   Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations(( 48.6, 24.2)):   Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations(( 36.5, 14.2)):   Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations(( 32.6, 40.2)):   Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations(( 34.6, 52.5)):   Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations((173.5, 139.467)):Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations((159.1, 177.0)):  Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations((159.1, 197.0)):  Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations(( 34.6, 177.0)):  Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations(( 34.6, 197.0)):  Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations((173.5, 236.133)):Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations((220.4, 335.4)):  Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations((216.5, 361.4)):  Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations((204.4, 351.4)):  Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations((173.5, 332.8)):  Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations((159.1, 321.5)):  Circle(radius=2.55,  mode=Mode.SUBTRACT)
        with Locations((126.5, 361.4)):  Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations(( 48.6, 351.4)):  Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations(( 36.5, 361.4)):  Circle(radius=1.59,  mode=Mode.SUBTRACT)
        with Locations(( 32.6, 335.4)):  Circle(radius=2.25,  mode=Mode.SUBTRACT)
        with Locations(( 34.6, 321.5)):  Circle(radius=2.55,  mode=Mode.SUBTRACT)

    extrude(amount=-1.6)

# =========================================================
    # FEATURE 7: Top Left & Right Curved Lips (XZ Plane offset to Y = 368.4)
    # =========================================================
    with BuildSketch(Plane.XZ.offset(-368.4)):
        # --- Right Curved Lip ---
        with BuildLine():
            r_p1 = (226.4, 0.0)
            r_p2 = (253.0, 26.6)
            r_p3 = (251.4, 26.6)
            r_p4 = (226.4, 1.6)
            r_center = (226.4, 26.6)

            ThreePointArc(r_p1, get_mid(r_p1, r_p2, r_center, 26.6), r_p2)
            Line(r_p2, r_p3)
            ThreePointArc(r_p3, get_mid(r_p3, r_p4, r_center, 25.0), r_p4)
            Line(r_p4, r_p1)
        make_face()

        # --- Left Curved Lip ---
        with BuildLine():
            l_p1 = (1.6, 26.6)
            l_p2 = (26.6, 1.6)
            l_p3 = (26.6, 0.0)
            l_p4 = (0.0, 26.6)
            l_center = (26.6, 26.6)

            ThreePointArc(l_p1, get_mid(l_p1, l_p2, l_center, 25.0), l_p2)
            Line(l_p2, l_p3)
            ThreePointArc(l_p3, get_mid(l_p3, l_p4, l_center, 26.6), l_p4)
            Line(l_p4, l_p1)
        make_face()

    extrude(amount=368.4)

# =========================================================
    # FEATURE 8: Left Mounting Flange (YZ Plane offset to X = 1.6)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(1.6)):
        with BuildLine():
            p1 = (0.0, 26.6)
            p2 = (368.4, 26.6)
            p3 = (368.4, 34.0)
            p4 = (366.4, 36.0)
            p5 = (2.0, 36.0)
            p6 = (0.0, 34.0)

            Line(p1, p2)
            Line(p2, p3)
            ThreePointArc(p3, get_mid(p3, p4, (366.4, 34.0), 2.0), p4)
            Line(p4, p5)
            ThreePointArc(p5, get_mid(p5, p6, (2.0, 34.0), 2.0), p6)
            Line(p6, p1)
        make_face()
    extrude(amount=-1.6)

# =========================================================
    # FEATURE 9: Right Mounting Flange (YZ Plane offset to X = 251.4)
    # =========================================================
    with BuildSketch(Plane.YZ.offset(251.4)):
        with BuildLine():
            p1 = (0.0, 34.0)
            p2 = (0.0, 26.6)
            p3 = (368.4, 26.6)
            p4 = (368.4, 34.0)
            p5 = (366.4, 36.0)
            p6 = (2.0, 36.0)

            Line(p1, p2)
            Line(p2, p3)
            Line(p3, p4)
            ThreePointArc(p4, get_mid(p4, p5, (366.4, 34.0), 2.0), p5)
            Line(p5, p6)
            ThreePointArc(p6, get_mid(p6, p1, (2.0, 34.0), 2.0), p1)
        make_face()
    extrude(amount=1.6)

from ocp_vscode import show
show(part)
export_stl(part.part, "output_PN-000634_v11.stl")