from PyQt6.QtCore import QObject, QTimer
from PyQt6.QtGui import QPixmap
from ui.antlineImageLists import green_antline

# This class toggles the antline animation on and off
class AntlineAnimator(QObject):
    # images holds the list of images used for the animation
    # To make new antlines, create a new list of images in antlineImageLists.py and pass it to this class
    def __init__(self, label, images=green_antline, interval=50):
        super().__init__(label)  # parented to the label so it isn't garbage collected
        self.label = label
        self.pixmaps = [QPixmap(p) for p in images]
        self.index = 0

        for path, pm in zip(images, self.pixmaps):
            if pm.isNull():
                print(f"Failed to load image: {path}")

        # sets up a timer that will call the step function at regular intervals, set by the interval parameter (default is 50 milliseconds)
        self.timer = QTimer(self)
        self.timer.setInterval(interval)
        self.timer.timeout.connect(self.step)

    # Updates the pixmap of the label when the timer calls it
    def step(self):
        self.label.setPixmap(self.pixmaps[self.index])
        self.index = (self.index + 1) % len(self.pixmaps)

    # starts and stops the timer, therefore starting and stopping the animation
    def toggle(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()