import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

GREEN = os.path.join(ASSETS_DIR, "antlines")
green_antline = [
    os.path.join(GREEN, "G1.png"),
    os.path.join(GREEN, "G2.png"),
    os.path.join(GREEN, "G3.png"),
    os.path.join(GREEN, "G4.png"),
    os.path.join(GREEN, "G5.png"),
    os.path.join(GREEN, "G6.png"),
]