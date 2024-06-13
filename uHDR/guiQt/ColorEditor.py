# uHDR: HDR image editing software
#   Copyright (C) 2022  remi cozot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
# hdrCore project 2020-2022
# author: remi.cozot@univ-littoral.fr

# import
# ------------------------------------------------------------------------------------------
from typing_extensions import Self
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QSlider,
    QCheckBox,
)
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtCore import Qt, pyqtSignal, QLocale
from guiQt.AdvanceSliderLine import AdvanceSliderLine


# ------------------------------------------------------------------------------------------
# --- class ColorEditor (QFrame) ------------------------------------------------------
# ------------------------------------------------------------------------------------------
class ColorEditor(QFrame):
    # class attributes
    ## signal
    hue_changed = pyqtSignal(float)
    saturation_changed = pyqtSignal(float)
    exposure_changed = pyqtSignal(float)
    contrast_changed = pyqtSignal(float)

    # constructor
    def __init__(self: Self) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)

        # attributes

        ## layout and widget
        self.topLayout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.topLayout)

        self.hueShift: AdvanceSliderLine = AdvanceSliderLine(
            "hue shift", 0.0, (-180, 180)
        )
        self.saturation: AdvanceSliderLine = AdvanceSliderLine(
            "saturation", 0.0, (-100, 100)
        )
        self.exposure: AdvanceSliderLine = AdvanceSliderLine(
            "exposure", 0, (-300, 300), (-3, +3)
        )  # -3,+3 0.01
        self.contrast: AdvanceSliderLine = AdvanceSliderLine(
            "contrast", 0.0, (-100, 100)
        )

        ## add widget to layout
        self.topLayout.addWidget(self.hueShift)
        self.topLayout.addWidget(self.saturation)
        self.topLayout.addWidget(self.exposure)
        self.topLayout.addWidget(self.contrast)

        # connect signals
        self.hueShift.valueChanged.connect(self.on_hue_changed)
        self.saturation.valueChanged.connect(self.on_saturation_changed)
        self.exposure.valueChanged.connect(self.on_exposure_changed)
        self.contrast.valueChanged.connect(self.on_contrast_changed)

    def on_hue_changed(self, name: str, value: float):
        self.hue_changed.emit(value)

    def on_saturation_changed(self, name: str, value: float):
        self.saturation_changed.emit(value)

    def on_exposure_changed(self, name: str, value: float):
        self.exposure_changed.emit(value)

    def on_contrast_changed(self, name: str, value: float):
        self.contrast_changed.emit(value)


# ------------------------------------------------------------------------------------------
