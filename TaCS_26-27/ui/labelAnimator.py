from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QObject, Qt
from PyQt6.QtGui import QPixmap, QTransform, QPainter

BASE_ANGLE = 0

_originals = {}  # label -> original pixmap, saved once

# Function to rotate a label's pixmap based off an absolute value, rather than offset from the current angle
def rotate_label(label, angle):
    """Make the label appear at an absolute angle (degrees clockwise)."""
    if label not in _originals:
        pixmap = label.pixmap()
        if pixmap.isNull():
            print("Error: Label has no pixmap to rotate.")
            return
        _originals[label] = pixmap.copy()

    original = _originals[label]
    w, h = original.width(), original.height()

    result = QPixmap(original.size())
    result.fill(Qt.GlobalColor.transparent)

    painter = QPainter(result)
    painter.setRenderHints(
        QPainter.RenderHint.SmoothPixmapTransform | QPainter.RenderHint.Antialiasing
    )
    painter.translate(w / 2, h / 2)
    painter.rotate(angle - BASE_ANGLE)
    painter.translate(-w / 2, -h / 2)
    painter.drawPixmap(0, 0, original)
    painter.end()

    label.setPixmap(result)