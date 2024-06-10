from typing_extensions import Self
from PyQt6.QtWidgets import QFrame, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
from guiQt.AdvanceSlider import AdvanceSlider
from guiQt.Contrast import Contrast
from guiQt.CurveWidget import CurveWidget


class LightBlock(QFrame):
    hueChanged = pyqtSignal(float)
    saturationChanged = pyqtSignal(float)
    exposureChanged = pyqtSignal(float)
    contrastChanged = pyqtSignal(float)

    def __init__(self: Self) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)

        self.active = True

        self.topLayout = QVBoxLayout()
        self.setLayout(self.topLayout)

        self.exposure = AdvanceSlider("exposure", 0.0, (-30, +30), (-3.0, +3.0), 10)
        self.contrast = Contrast()
        self.curve = CurveWidget()

        self.topLayout.addWidget(self.exposure)
        self.topLayout.addWidget(self.contrast)
        self.topLayout.addWidget(self.curve)

        self.exposure.valueChanged.connect(
            lambda value: self.exposureChanged.emit(value)
        )
        self.contrast.valueChanged.connect(
            lambda value: self.contrastChanged.emit(value)
        )
