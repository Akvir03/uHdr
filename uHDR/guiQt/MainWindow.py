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
from __future__ import annotations
from typing_extensions import Self
from typing import Tuple
from PyQt6.QtWidgets import QFileDialog, QDockWidget, QMainWindow
from PyQt6.QtCore import pyqtSignal, Qt, QBuffer, QIODevice
from PyQt6.QtGui import QAction
from PIL import Image as PILImage
from numpy import ndarray
import numpy as np
from app.Tags import Tags
import preferences.Prefs, io
from guiQt.AdvanceImageGallery import AdvanceImageGallery
from guiQt.EditorBlock import EditorBlock
from guiQt.InfoSelPrefBlock import InfoSelPrefBlock
import colour
import imageio
from hdrCore.image import Image as HDRImage, imageType, ColorSpace
from hdrCore.metadata import metadata

# ------------------------------------------------------------------------------------------
# --- class MainWindow(QMainWindow) --------------------------------------------------------
# ------------------------------------------------------------------------------------------
debug = True


class MainWindow(QMainWindow):
    # class attributes

    ## signals
    ## -------
    dirSelected: pyqtSignal = pyqtSignal(str)
    requestImages: pyqtSignal = pyqtSignal(int, int)
    imageSelected: pyqtSignal = pyqtSignal(int)
    tagChanged: pyqtSignal = pyqtSignal(tuple, bool)
    scoreChanged: pyqtSignal = pyqtSignal(int)
    scoreSelectionChanged: pyqtSignal = pyqtSignal(list)

    # constructor
    # -------------------------------------------------------------------------------------------
    def __init__(
        self: MainWindow, nbImages: int = 0, tags: dict[Tuple[str, str], bool] = {}
    ) -> None:
        super().__init__()

        # attributes
        ## widgets
        self.metaBlock: InfoSelPrefBlock = InfoSelPrefBlock(tags)

        self.editBlock: EditorBlock = EditorBlock()
        self.imageGallery: AdvanceImageGallery = AdvanceImageGallery(nbImages)

        self.metaDock: QDockWidget = QDockWidget("INFO. - SELECTION - PREFERENCES")
        self.metaDock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.metaDock.setWidget(self.metaBlock)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.metaDock)

        self.editDock: QDockWidget = QDockWidget("EDIT")
        self.editDock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.editDock.setWidget(self.editBlock)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.editDock)

        self.setCentralWidget(self.imageGallery)

        ## menu
        self.buildFileMenu()

        ## callbacks
        ### from AdvanceImageGallery
        self.imageGallery.requestImages.connect(self.CBrequestImages)
        self.imageGallery.imageSelected.connect(self.CBimageSelected)
        self.metaBlock.tagChanged.connect(self.CBtagChanged)
        self.metaBlock.scoreChanged.connect(self.CBscoreChanged)
        self.metaBlock.scoreSelectionChanged.connect(self.CBscoreSelectionChanged)

    # methods
    # -------------------------------------------------------------------
    ## reset
    def resetGallery(self: MainWindow):
        """resetGallery"""

        if debug:
            print(f"MainWindows.resetGallery()")

        self.imageGallery.gallery.resetImages()

    ## firstPage
    def firstPage(self: MainWindow):
        """go to first page."""

        if debug:
            print(f"MainWindows.firstPage()")

        self.imageGallery.firstPage()

    ## image
    def setGalleryImage(self: Self, index: int, image: ndarray | None) -> None:
        """send the image of global index to image gallery"""
        if debug:
            print(f"MainWindows.setGalleryImage(index={index}, image= ...)")
        self.imageGallery.setImage(index, image)

    def setNumberImages(self: Self, nbImages: int) -> None:
        self.imageGallery.setNbImages(nbImages)

    def setEditorImage(self: Self, image: ndarray) -> None:
        self.editBlock.setImage(image)

    ## tags
    def setTagsImage(self: Self, tags: dict[Tuple[str, str], bool]) -> None:
        self.metaBlock.setTags(tags)

    def resetTags(self: Self) -> None:
        self.metaBlock.resetTags()

    ## info
    def setInfo(
        self: Self,
        name: str,
        path: str,
        size: tuple[int, int] = (-1, -1),
        colorSpace: str = "...",
        type: str = "...",
        bps: int = -1,
    ) -> None:
        self.metaBlock.setInfo(name, path, size, colorSpace, type, bps)

    ## score
    def setScore(self: Self, score: int) -> None:
        self.metaBlock.setScore(score)

    ## prefs
    def setPrefs(self: Self) -> None:
        self.imageGallery.setSize(preferences.Prefs.Prefs.gallerySize)

    ## menu
    def buildFileMenu(self):
        menubar = self.menuBar()  # get menubar
        fileMenu = menubar.addMenu("&File")  # file menu

        selectDir = QAction("&Select directory", self)
        selectDir.setShortcut("Ctrl+O")
        selectDir.setStatusTip("[File] select a directory")
        selectDir.triggered.connect(self.CBSelectDir)
        fileMenu.addAction(selectDir)

        selectSave = QAction("&Save", self)
        selectSave.setShortcut("Ctrl+S")
        selectSave.setStatusTip("[File] saving processpipe metadata")
        selectSave.triggered.connect(self.CBSave)
        fileMenu.addAction(selectSave)

        quit = QAction("&Quit", self)
        quit.setShortcut("Ctrl+Q")
        quit.setStatusTip("[File] saving updates and quit")
        quit.triggered.connect(lambda x: print("quit"))
        fileMenu.addAction(quit)

    ## callbacks
    ## -------------------------------------------------------------------
    ### select dir
    def CBSelectDir(self):
        dirName = QFileDialog.getExistingDirectory(None, "Select Directory")
        if dirName != "":
            self.dirSelected.emit(dirName)

    ## -------------------------------------------------------------------
    ### requestImages
    def CBrequestImages(self: Self, minIdx: int, maxIdx: int) -> None:
        if debug:
            print(f"MainWindow.CBrequestImages({minIdx},{maxIdx})")
        self.requestImages.emit(minIdx, maxIdx)

    ## -------------------------------------------------------------------
    ### image selected
    def CBimageSelected(self: Self, idx: int) -> None:
        if debug:
            print(f"MainWindow.CBimageSelected({idx})")
        self.imageSelected.emit(idx)

    # -----------------------------------------------------------------
    def CBtagChanged(self, key: tuple[str, str], value: bool) -> None:
        if debug:
            print(f"guiQt.MainWindow.CBtagChanged({key},{value}) > emit !")
        self.tagChanged.emit(key, value)

    # -----------------------------------------------------------------
    def CBscoreChanged(self, value: int) -> None:
        if debug:
            print(f"guiQt.MainWindow.CBscoreChanged({value}) > emit !")
        self.scoreChanged.emit(value)

    # -----------------------------------------------------------------
    def CBscoreSelectionChanged(self: Self, scoreSelection: list) -> None:
        if debug:
            print(f"guiQt.MainWindow.CBscoreSelectionChanged({scoreSelection})")
        self.scoreSelectionChanged.emit(scoreSelection)

    # -----------------------------------------------------------------
    ### Save modified img

    def CBSave(self: QMainWindow) -> None:
        """Callback to save the current image displayed in the editor."""
        if self.editBlock.imageWidget.imagePixmap is not None:
            # Open a file dialog to select the save location and file type
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Image",
                "",
                "Images (*.jpg *.hdr);;JPG Files (*.jpg);;HDR Files (*.hdr)",
            )

            if save_path:
                # Convert QPixmap to QImage
                pixmap = self.editBlock.imageWidget.imagePixmap
                image = pixmap.toImage()

                if save_path.lower().endswith(".jpg"):
                    # Save as JPG
                    buffer = QBuffer()
                    buffer.open(QIODevice.OpenModeFlag.ReadWrite)
                    image.save(buffer, "JPG")

                    # Convert the buffer to a PIL image
                    pil_image = PILImage.open(io.BytesIO(buffer.data()))
                    pil_image.save(save_path, "JPEG")
                elif save_path.lower().endswith(".hdr"):
                    # Save as HDR
                    # Convert QImage to numpy array
                    ptr = image.bits()
                    ptr.setsize(
                        image.width() * image.height() * 4
                    )  # Assuming 4 bytes per pixel (RGBA)
                    arr = np.array(ptr).reshape((image.height(), image.width(), 4))
                    arr = arr[..., :3]  # Remove alpha channel

                    # Normalize the array to 0-1 range
                    arr = arr / 255.0

                    # Create an instance of the HDRImage class
                    hdr_image = HDRImage(
                        path="",
                        name="",
                        colorData=arr.astype(np.float32),
                        type=imageType.HDR,
                        linear=True,
                        colorspace=ColorSpace.sRGB(),
                    )

                    # Initialize metadata
                    hdr_image.metadata = metadata.build(hdr_image)

                    # Save the image using the HDRImage write method
                    hdr_image.write(save_path)


# ------------------------------------------------------------------------------------------
