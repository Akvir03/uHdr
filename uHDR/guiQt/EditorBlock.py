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

import numpy
from numpy import ndarray

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QSplitter
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal, QLocale

from guiQt.Editor import Editor
from guiQt.ImageWidget import ImageWidget


# ------------------------------------------------------------------------------------------
# --- class EditorBlock (QSplitter) ------------------------------------------------------
# ------------------------------------------------------------------------------------------
class EditorBlock(QSplitter):
    # class attributes
    imageChanged = pyqtSignal(int, ndarray)  # Ajoutez le signal ici

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
        self.edit.updateRequested.connect(self.onColorChanged)

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
        # Exemple de traitement de l'image
        pixmap = self.imageWidget.imagePixmap
        updated_image = self.applyColorChange(pixmap, colorType, value)
        # Conversion de QPixmap à ndarray
        updated_image_array = self.qpixmap_to_array(updated_image)
        # Émission du signal
        self.imageChanged.emit(0, updated_image_array)

    def applyColorChange(self, pixmap, colorType, value):
        # Placeholder for actual color change logic
        return pixmap

    ## setImage
    def qpixmap_to_array(self, pixmap: QPixmap) -> ndarray:
        size = pixmap.size()
        h = size.height()
        w = size.width()
        qimg = pixmap.toImage()
        byte_str = qimg.bits().asstring(h * w * 4)
        img = numpy.frombuffer(byte_str, dtype=numpy.uint8).reshape((h, w, 4))
        return img[:, :, :3]
