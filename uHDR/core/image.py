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

from core.colourSpace import ColorSpace
from copy import deepcopy
import numpy as np
import os
import colour
import skimage.transform
import rawpy
from imageio import imwrite

# ------------------------------------------------------------------------------------------

debug: bool = True


# -----------------------------------------------------------------------------
def filenamesplit(filename: str) -> tuple[str, str, str]:
    """Retrieve path, name and extension from a filename.

    Args:
        filename (str): Filename

    Returns:
        tuple[str, str, str]: (path, name, ext)

    Example:
        filenamesplit("./dir0/dir1/name.ext") returns ("./dir0/dir1/", "name", "ext")
    """
    path, nameWithExt = os.path.split(filename)
    splits = nameWithExt.split(".")
    ext = splits[-1].lower()
    name = ".".join(splits[:-1])
    return path, name, ext


# ------------------------------------------------------------------------------------------
# --- class Image -----------------------------------------------------------
# ------------------------------------------------------------------------------------------
class Image:
    """Color data + color space + HDR"""

    # constructor
    # -----------------------------------------------------------------
    def __init__(
        self, data: np.ndarray, space: ColorSpace = ColorSpace.sRGB, isHdr: bool = False
    ):
        self.cSpace: ColorSpace = space
        self.cData: np.ndarray = data
        self.hdr: bool = isHdr

    # methods
    # -----------------------------------------------------------------
    def __repr__(self) -> str:
        y, x, c = self.cData.shape
        res: str = "-------------------    Image   -------------------------------"
        res += f"\n size: {x} x {y} x {c} "
        res += f"\n colourspace: {self.cSpace.name}"
        res += f"\n hdr: {self.hdr}"
        res += "\n-------------------  Image End -------------------------------"
        return res

    # -----------------------------------------------------------------
    def write(self, fileName: str):
        """Write image to system."""
        # Infer file extension
        ext = os.path.splitext(fileName)[-1].lower()

        # Convert image data to uint8 if saving as jpg/jpeg
        if ext in [".jpg", ".jpeg"]:
            img_data_to_save = (self.cData * 255).astype(np.uint8)
        else:
            img_data_to_save = self.cData

        # Write image using imageio
        imwrite(fileName, img_data_to_save)

    # -----------------------------------------------------------------
    def buildThumbnail(self, maxSize: int = 800) -> Image:
        """Build a thumbnail image."""
        y, x, _ = self.cData.shape
        factor: float = maxSize / max(y, x)
        if factor < 1:
            thumbcData = skimage.transform.resize(
                self.cData, (int(y * factor), int(x * factor))
            )
            return Image(thumbcData, self.cSpace, self.hdr)
        else:
            return deepcopy(self)

    # static methods
    # -----------------------------------------------------------------
    @staticmethod
    def read(fileName: str) -> Image:
        """Read an image from system with advanced processing based on file type."""
        path, name, ext = filenamesplit(fileName)
        if not os.path.exists(fileName):
            # Return a default gray image if file does not exist
            return Image(np.ones((600, 800, 3)) * 0.50, ColorSpace.sRGB, False)

        imgData = None
        if ext in ["jpg", "jpeg"]:
            imgData = colour.read_image(fileName, bit_depth="float32", method="Imageio")
            img = Image(imgData, ColorSpace.sRGB, False)

        # Handling RAW files (assuming similar to 'arw' handling needed)
        elif ext == "arw":
            raw = rawpy.imread(fileName)
            ppParams = rawpy.Params(
                use_camera_wb=True, output_color=rawpy.ColorSpace.sRGB, output_bps=16
            )
            imgData = colour.utilities.as_float_array(raw.postprocess(ppParams)) / (
                2**16 - 1
            )
            raw.close()
            img = Image(imgData, ColorSpace.sRGB, True)  # Assuming RAW files are linear

        # Handling HDR files with thumbnail capability
        elif ext == "hdr":
            hdr_file_path = os.path.join(path, fileName)
            if not os.path.exists(hdr_file_path):
                # If the HDR file doesn't exist at the path, handle accordingly (optional)
                pass

            imgData = colour.read_image(fileName, bit_depth="float32", method="Imageio")
            img = Image(imgData, ColorSpace.sRGB, True)  # Assuming HDR files are linear

        # Finalize and return the image object
        if imgData is not None:
            return img

        # Return a default image if no conditions are met (fallback)
        return Image(np.ones((600, 800, 3)) * 0.50, ColorSpace.sRGB, False)


# Ensure the image is loaded correctly
class ImageManagement:
    def __init__(self):
        self.images = {}

    def addImage(self, fileName: str):
        image = Image.read(fileName)
        path, name, ext = filenamesplit(fileName)
        self.images[name + "." + ext] = image

    def getImage(self, name: str) -> Image:
        if name not in self.images:
            raise KeyError(f"Image '{name}' not found in images dictionary.")
        return self.images[name]


# Example usage
imagesManagement = ImageManagement()
imagesManagement.addImage("/mnt/data/0216_HDR.hdr")
image = imagesManagement.getImage("0216_HDR.hdr")
print(image)
