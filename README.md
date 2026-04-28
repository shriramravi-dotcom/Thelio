# Thelio Parts Reconstruction & Validation

Methodology
Original parts were imported into Fusion.
Data for edges, arcs, and lines were extracted to create profiles.
These profiles were added or subtracted to generate the final 3D part designs.

Validation
A validation script (validate.py) compares the rebuilt output models to the original parts using cadquery and trimesh. It calculates Volumetric Difference (mm³ and %) and Symmetric Difference (mm³ and %).
Validation Output: 

╔══════════════════════════════════════════════════════════════════════════════════╗
║  Thelio Parts — Validation Report (Volume & Symmetric Difference)               ║
╚══════════════════════════════════════════════════════════════════════════════════╝
  Originals   : /Users/softage/Desktop/Thelio/Original
  Outputs     : /Users/softage/Desktop/Thelio
  Parts       : 30
  STEP loader : cadquery
  trimesh     : ✓

  [OK                                          ] Mesh Bracket-small v11
  [OK                                          ] Mesh Side Mount BKT v2
  [OK                                          ] Mesh Update v9
  [OK                                          ] PN-000518 v27
  [OK                                          ] PN-000634 v11
  [OK                                          ] PN-000635 v20
  [OK                                          ] PN-000636 v18
  [OK                                          ] PN-000637 v8
  [OK                                          ] PN-000638 v5
  [OK                                          ] PN-000639 v6
  [OK                                          ] PN-000640 v21
  [OK                                          ] PN-000641 v10
  [OK                                          ] PN-000643 v36
  [OK                                          ] PN-000644 v54
  [OK                                          ] PN-000645 v63
  [OK                                          ] PN-000646 v10
  [OK                                          ] PN-000647 v22
  [OK                                          ] PN-000648 v17
  [OK                                          ] PN-000650 v12
  [OK                                          ] PN-000651 v13
  [OK                                          ] PN-000652 v17
  [OK                                          ] PN-000662 v14
  [OK                                          ] PN-000663 v14
  [OK                                          ] PN-000664 v2
  [OK                                          ] PN-000665 v6
  [OK                                          ] PN-000666 v7
  [OK                                          ] PN-000668 v7
  [OK                                          ] PN-000669 v9
  [OK                                          ] Top BKT Mag Guide Slim v6
  [OK                                          ] V3 120mm Fan Plate v7

┌──────────────────────────────────────────────────────────────────────────────────────┐
│  Part Name                   Vol Diff (mm³)     Vol (%)    Sym Diff (mm³)     Sym (%)  │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Mesh Bracket-small v11               0.000        0.00%             0.247        0.00%  │
│  Mesh Side Mount BKT v2               0.000        0.00%             0.000        0.00%  │
│  Mesh Update v9                       9.062        0.03%           127.797        0.48%  │
│  PN-000518 v27                        0.028        0.00%             0.073        0.00%  │
│  PN-000634 v11                      118.360        0.08%          1282.454        0.91%  │
│  PN-000635 v20                       22.300        0.05%           103.739        0.24%  │
│  PN-000636 v18                        0.078        0.00%                 —           —  │
│  PN-000637 v8                         0.022        0.00%             0.038        0.00%  │
│  PN-000638 v5                         0.002        0.00%             0.026        0.00%  │
│  PN-000639 v6                        30.463        0.36%            81.737        0.96%  │
│  PN-000640 v21                       31.824        0.06%            37.857        0.07%  │
│  PN-000641 v10                        0.016        0.00%             0.018        0.00%  │
│  PN-000643 v36                       49.135        0.03%            49.541        0.03%  │
│  PN-000644 v54                       24.244        0.02%            24.363        0.02%  │
│  PN-000645 v63                       97.207        0.06%            97.463        0.06%  │
│  PN-000646 v10                       14.597        0.01%            15.844        0.01%  │
│  PN-000647 v22                        0.010        0.00%             0.010        0.00%  │
│  PN-000648 v17                        0.727        0.00%             1.699        0.00%  │
│  PN-000650 v12                        7.065        0.00%            32.887        0.01%  │
│  PN-000651 v13                        0.001        0.00%             0.001        0.00%  │
│  PN-000652 v17                        0.528        0.00%                 —           —  │
│  PN-000662 v14                        0.186        0.00%             1.115        0.01%  │
│  PN-000663 v14                        1.522        0.01%             2.101        0.01%  │
│  PN-000664 v2                         2.665        0.03%             9.614        0.12%  │
│  PN-000665 v6                         0.077        0.00%                 —           —  │
│  PN-000666 v7                         0.207        0.06%             0.219        0.06%  │
│  PN-000668 v7                         0.006        0.00%                 —           —  │
│  PN-000669 v9                         0.000        0.00%             0.000        0.00%  │
│  Top BKT Mag Guide Slim v            18.251        0.30%            21.876        0.37%  │
│  V3 120mm Fan Plate v7               17.822        0.04%            18.062        0.04%  │
└──────────────────────────────────────────────────────────────────────────────────────┘

  Summary : 30/30 parts processed, 0 skipped

  Notes:
  • Vol Diff  = |volume(original) − volume(output)|  in mm³
  • Vol (%)   = Vol Diff as % of original volume
  • Sym Diff  = (A−B) ∪ (B−A) boolean volume in mm³  [requires watertight meshes]
  • Sym (%)   = Sym Diff as % of original volume
  • '—' in Sym columns = open-shell mesh or trimesh unavailable

Time Taken: 54 hours 
