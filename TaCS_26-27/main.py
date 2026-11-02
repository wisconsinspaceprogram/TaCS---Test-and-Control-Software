# Imports
import math
import sys
import os
import numpy as np
# Widgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStyleFactory
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPainter, QPalette, QColor, QPixmap, QTransform, QIcon
from PyQt6 import uic
import traceback
sys.excepthook = lambda *a: traceback.print_exception(*a)
# Helper functions
from ui.antlines import AntlineAnimator
from ui.valve_state import valveButtons
from ui.buttonLists import buttonOpen, buttonClose

class tacsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TaCS.ui", self)
        
        # Saves the original pixmap of the label
        self.originalPixmap = self.labelValve.pixmap()

        # Updates the value for text browser when the value is changed
        self.dialValve.valueChanged.connect(self.readDial)
        
        # Initalizes button click event for advancing the antline
        self.antlineAnim = AntlineAnimator(self.antline_g)
        self.buttonAntline1.clicked.connect(self.antlineAnim.toggle)
        
        # Handles switching between button states
        # Runs through lists stores in buttonLists
        self.valves = []
        for open_name, close_name in zip(buttonOpen, buttonClose):
            open_btn = getattr(self, open_name)
            close_btn = getattr(self, close_name)
            valve = valveButtons(open_btn, close_btn)       
            self.valves.append(valve)      # stores every valve in a list
            open_btn.clicked.connect(lambda checked=False, v=valve: v.set_state(True))
            close_btn.clicked.connect(lambda checked=False, v=valve: v.set_state(False))

    def readDial(self):
        dialValue = self.dialValve.value()
        self.dialBrowser.setText(str(dialValue))
        self.lcdNumber.display(dialValue)
        
        self.rotateLabel()  # Call the rotateLabel method to update the label's rotation
        
    def rotateLabel(self):
        labelAngle = self.dialValve.value()

        t = QTransform()
        t.rotate(labelAngle)
        # Rotates the original pixmap
        rotatedPixmap = self.originalPixmap.transformed(t, Qt.TransformationMode.SmoothTransformation)
        self.labelValve.setPixmap(rotatedPixmap)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Sets the application theme to "Fusion"
    app.setStyle(QStyleFactory.create("Fusion"))
    
    light_palette = QPalette()
    light_palette.setColor(QPalette.ColorRole.Window, QColor(43,43,43))
    light_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    app.setPalette(light_palette)

    window = tacsApp()
    window.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")