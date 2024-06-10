# uHDR: HDR image editing software
#   Copyright (C) 2022  remi cozot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, ou
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be utile,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
# hdrCore project 2020-2022
# author: remi.cozot@univ-littoral.fr

# import
# ------------------------------------------------------------------------------------------
from typing_extensions import Self
from numpy import ndarray

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QSplitter
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtCore import Qt, pyqtSignal, QLocale

from guiQt.Editor import Editor
from guiQt.ImageWidget import ImageWidget


# ------------------------------------------------------------------------------------------
# --- class EditorBlock (QSplitter) ------------------------------------------------------
# ------------------------------------------------------------------------------------------
class EditorBlock(QSplitter):
    # class attributes
    imageChanged = pyqtSignal(int, ndarray)

    # constructor
    def __init__(self: Self) -> None:
        super().__init__(Qt.Orientation.Vertical)

        # attributes
        self.imageWidget: ImageWidget = ImageWidget()
        self.edit: Editor = Editor()

        # adding widgets to self (QSplitter)
        self.addWidget(self.imageWidget)
        self.addWidget(self.edit)
        self.setSizes([20, 80])

        # Connection to changes
        self.edit.updateRequested.connect(self.setImage)

    # methods
    ## setImage
    def setImage(self: Self, image: ndarray | None):
        if image is not None:
            self.imageWidget.setPixmap(image)
        else:
            # Handle the case where there is no image
            pass

    def onColorChanged(self, colorType: str, value: float):
        print(f"EditorBlock received color change: {colorType} -> {value}")
        # Assuming we have a method to update the image based on color changes
        updated_image = self.updateImage(self.imageWidget.imagePixmap, colorType, value)
        # Emit signal with updated image
        index = 0  # Assuming we are working with a single image for simplicity
        self.imageChanged.emit(index, updated_image)

    def updateImage(
        self, currentImage: ndarray, colorType: str, value: float
    ) -> ndarray:
        # Implement the logic to update the image based on the color change
        # This is a placeholder and should be replaced with actual image processing code
        # For example, apply contrast, hue, saturation changes, etc.
        new_image = currentImage.copy()
        if colorType == "contrast":
            new_image = self.applyContrast(new_image, value)
        elif colorType == "hue":
            new_image = self.applyHue(new_image, value)
        elif colorType == "saturation":
            new_image = self.applySaturation(new_image, value)
        elif colorType == "exposure":
            new_image = self.applyExposure(new_image, value)
        return new_image

    def applyContrast(self, image: ndarray, value: float) -> ndarray:
        # Example contrast adjustment (placeholder)
        return image * (1 + value)

    def applyHue(self, image: ndarray, value: float) -> ndarray:
        # Example hue adjustment (placeholder)
        return image

    def applySaturation(self, image: ndarray, value: float) -> ndarray:
        # Example saturation adjustment (placeholder)
        return image

    def applyExposure(self, image: ndarray, value: float) -> ndarray:
        # Example exposure adjustment (placeholder)
        return image * (1 + value)
