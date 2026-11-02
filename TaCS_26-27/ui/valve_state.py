import os
from PyQt6.QtGui import QPixmap, QIcon, QTransform
from PyQt6.QtCore import QObject, Qt
from ui import labelAnimator
from ui.valveLabelLists import labelValve, labelValveOpen

#
# Boring directory stuff
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
BUTTONS_DIR = os.path.join(ASSETS_DIR, "buttons")

icon_null = os.path.join(BUTTONS_DIR, "buttonValveNull.png")
icon_on = os.path.join(BUTTONS_DIR, "buttonValveOpen.png")
icon_off = os.path.join(BUTTONS_DIR, "buttonValveClosed.png")
#
# 

class valveButtonState:
    def __init__(self, label, open_ang, open_btn, close_btn):
        self.label = label
        self.open_angle = open_ang
        self.open_btn = open_btn
        self.close_btn = close_btn
        
        # Starts in the null state
        self.set_state(None)
        # Defines the null state for buttons and labels
        labelAnimator.rotate_label(label=self.label, angle=45)
        self.open_btn.setIcon(QIcon(icon_null))
        self.close_btn.setIcon(QIcon(icon_null))
        
        
    def set_state(self, is_open):
        self.is_open = is_open
        # icon for each button depends only on the one shared state
        self.open_btn.setIcon(QIcon(icon_on if is_open is True else icon_off))
        self.close_btn.setIcon(QIcon(icon_on if is_open is False else icon_off))
        
        if is_open is None:
            labelAnimator.rotate_label(label=self.label, angle=0)
        elif is_open is True:
            labelAnimator.rotate_label(label=self.label, angle=self.open_angle)
        elif is_open is False:
            labelAnimator.rotate_label(label=self.label, angle=(self.open_angle - 90))
        else:
            print("Error: Invalid state for valve. Must be True, False, or None.")
        
        