import math
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStyleFactory
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPalette, QColor, QPixmap, QTransform
from PyQt6 import uic


class tacsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TaCS.ui", self)
        
        # Saves the original pixmap of the label
        self.originalPixmap = self.labelValve.pixmap()
        w = self.originalPixmap.width()
        h = self.originalPixmap.height()

        # Updates the value for text browser when the value is changed
        self.dialValve.valueChanged.connect(self.readDial)

    def readDial(self):
        dialValue = self.dialValve.value()
        self.dialBrowser.setText(str(dialValue))
        self.lcdNumber.display(dialValue)
        
        self.rotateLabel()  # Call the rotateLabel method to update the label's rotation
        
    def rotateLabel(self):
        labelAngle = self.dialValve.value()
        
        #Prepare the transformation centered on the image
        
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
    light_palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))
    light_palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
    app.setPalette(light_palette)

    window = tacsApp()
    window.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")