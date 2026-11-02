import os
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QObject

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
BUTTONS_DIR = os.path.join(ASSETS_DIR, "buttons")

icon_null = os.path.join(BUTTONS_DIR, "buttonValveNull.png")
icon_on = os.path.join(BUTTONS_DIR, "buttonValveOpen.png")
icon_off = os.path.join(BUTTONS_DIR, "buttonValveClosed.png")

class valveButtons:
    def __init__(self,open_btn, close_btn):
        self.open_btn = open_btn
        self.close_btn = close_btn
        
        # Starts the buttons in the null state
        self.set_state(None)
        self.open_btn.setIcon(QIcon(icon_null))
        self.close_btn.setIcon(QIcon(icon_null))
        
    def set_state(self, is_open):
        self.is_open = is_open
        # icon for each button depends only on the one shared state
        self.open_btn.setIcon(QIcon(icon_on if is_open is True else icon_off))
        self.close_btn.setIcon(QIcon(icon_on if is_open is False else icon_off))
        
        