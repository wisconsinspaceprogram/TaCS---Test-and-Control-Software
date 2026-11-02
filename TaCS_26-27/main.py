# Imports
import math
import sys
import os
import numpy as np

# The long list of PtQt6 imports
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStyleFactory
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPainter, QPalette, QColor, QPixmap, QTransform, QIcon
from PyQt6 import uic
import traceback
sys.excepthook = lambda *a: traceback.print_exception(*a)

# Helper functions
from ui.antlines import AntlineAnimator
from ui.valve_state import valveButtonState
from ui.buttonLists import buttonOpen, buttonClose
from ui import labelAnimator
from ui.valveLabelLists import labelValve, labelValveOpen


## Actual code starts here
##  |   |   |
## \|/ \|/ \|/  
class tacsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TaCS.ui", self)

        # Initalizes button click event for advancing the antline
        self.antlineAnim = AntlineAnimator(self.antline_g)
        self.buttonAntline1.clicked.connect(self.antlineAnim.toggle)
        
        # Handles switching between button states
        # Runs through lists stores in buttonLists
        self.valveButtons = []
        for valve_label, open_angle, open_name, close_name in zip(labelValve, labelValveOpen, buttonOpen, buttonClose):
            label = getattr(self, valve_label)
            open_ang = open_angle
            open_btn = getattr(self, open_name)
            close_btn = getattr(self, close_name)
            valve = valveButtonState(label, open_ang, open_btn, close_btn)
            self.valveButtons.append(valve)      # stores every valve in a list
            
            # Tells every button to change their icon and angle when clicked
            open_btn.clicked.connect(lambda checked=False, v=valve: v.set_state(True))
            close_btn.clicked.connect(lambda checked=False, v=valve: v.set_state(False))
            
            
## Handles the pallete, style, and window creation
##  |   |   |
## \|/ \|/ \|/              
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Sets the application theme to "Fusion"
    app.setStyle(QStyleFactory.create("Fusion"))
    light_palette = QPalette()
    light_palette.setColor(QPalette.ColorRole.Window, QColor(43,43,43))             # Manually sets the background color
    light_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))    # idk why this is needed but it is
    app.setPalette(light_palette)

    # Window creation
    window = tacsApp()
    window.show()
    
    try:                                # Attempts to start the window
        sys.exit(app.exec())            # Throws an error if unable to
    except SystemExit:
        print("Closing Window...")