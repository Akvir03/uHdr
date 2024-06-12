# uHDR: HDR image editing software
#   Copyright (C) 2022  remi cozot
#
#    This program is free software: vous pouvez le redistribuer et/ou le modifier
#    selon les termes de la licence GNU General Public License telle que publiée par
#    la Free Software Foundation, soit la version 3 de la licence, soit
#    (à votre choix) toute version ultérieure.
#
#    Ce programme est distribué dans l'espoir qu'il sera utile,
#    mais SANS AUCUNE GARANTIE; sans même la garantie implicite de
#    QUALITÉ MARCHANDE ou D'ADÉQUATION À UN USAGE PARTICULIER. Voir la
#    GNU General Public License pour plus de détails.
#
# projet hdrCore 2020-2022
# auteur: remi.cozot@univ-littoral.fr

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
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import Qt, pyqtSignal, QLocale


# ------------------------------------------------------------------------------------------
# --- class AdvanceSlider(QFrame) ----------------------------------------------------------
# ------------------------------------------------------------------------------------------
class AdvanceSlider(QFrame):
    valueChanged: pyqtSignal = pyqtSignal(float, bool)
    autoClicked: pyqtSignal = pyqtSignal()
    activeToggled: pyqtSignal = pyqtSignal(bool)

    # constructeur
    def __init__(
        self: Self,
        name: str,
        defaultValue: float,
        rangeGUI: tuple[int, int],
        rangeData: tuple[float, float] | None = None,
        precision=1000,
    ) -> None:
        super().__init__()

        self.active: bool = True
        self.guiRange: tuple[int, int] = rangeGUI
        self.dataRange: tuple[float, float] = (
            rangeData
            if rangeData
            else (float(self.guiRange[0]), float(self.guiRange[1]))
        )
        self.defaultValue: float = defaultValue
        self.precision: int = precision

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstrow: QFrame = QFrame()

        self.vbox: QVBoxLayout = QVBoxLayout()
        self.hboxTop: QHBoxLayout = QHBoxLayout()
        self.hbox: QHBoxLayout = QHBoxLayout()

        self.firstrow.setLayout(self.hbox)

        self.checkBoxActive: QCheckBox = QCheckBox("active")
        self.checkBoxActive.setChecked(True)

        self.label: QLabel = QLabel(name)
        self.auto: QPushButton = QPushButton("auto")
        self.editValue: QLineEdit = QLineEdit()
        validator: QDoubleValidator = QDoubleValidator()
        locale: QLocale = QLocale(
            QLocale.Language.English, QLocale.Country.UnitedStates
        )
        validator.setLocale(locale)

        self.editValue.setValidator(validator)

        self.editValue.setText(str(self.defaultValue))
        self.reset: QPushButton = QPushButton("reset")

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.auto)
        self.hbox.addWidget(self.editValue)
        self.hbox.addWidget(self.reset)
        self.hbox.addWidget(self.checkBoxActive)

        self.slider: QSlider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(self.guiRange[0], self.guiRange[1])
        self.slider.setValue(self.toGui(self.defaultValue))
        self.slider.setSingleStep(1)

        self.vbox.addWidget(self.firstrow)
        self.vbox.addWidget(self.slider)

        self.setLayout(self.vbox)

        # connexion aux signaux : slider/reset/auto
        self.slider.valueChanged.connect(self.sliderChanged)
        self.editValue.editingFinished.connect(self.valueEdited)
        self.reset.clicked.connect(self.resetClicked)
        self.auto.clicked.connect(self.autoClickedCB)
        self.checkBoxActive.toggled.connect(self.activeChanged)

    # méthodes
    # --------------------------------------------------
    def toGui(self, data: float) -> int:
        u: float = (data - self.dataRange[0]) / (self.dataRange[1] - self.dataRange[0])
        guiValue: float = self.guiRange[0] * (1 - u) + self.guiRange[1] * u
        return int(guiValue)

    # --------------------------------------------------
    def toValue(self, data: int) -> float:
        u: float = (data - self.guiRange[0]) / (self.guiRange[1] - self.guiRange[0])
        value: float = self.dataRange[0] * (1 - u) + self.dataRange[1] * u
        return value

    # callback
    # --------------------------------------------------
    def activeChanged(self):
        self.activeToggled.emit(self.checkBoxActive.isChecked())

    # --------------------------------------------------
    def sliderChanged(self: Self):
        guiData: int = self.slider.value()
        value: float = round(self.toValue(guiData) * self.precision) / self.precision
        if self.active:
            self.active = False
            self.editValue.setText(str(value))
            self.active = True
            self.valueChanged.emit(value, self.checkBoxActive.isChecked())
        else:
            self.editValue.setText(str(value))

    # -------------------------------------------------
    def valueEdited(self: Self) -> None:
        value: float = (
            round(float(self.editValue.text()) * self.precision) / self.precision
        )
        if self.active:
            self.active = False
            self.editValue.setText(str(value))
            self.slider.setValue(self.toGui(value))
            self.active = True
            self.valueChanged.emit(value, self.checkBoxActive.isChecked())
        else:
            self.slider.setValue(self.toGui(value))

    # -------------------------------------------------
    def resetClicked(self: Self) -> None:
        if self.active:
            self.active = False
            self.editValue.setText(str(self.defaultValue))
            self.slider.setValue(self.toGui(self.defaultValue))
            self.active = True
            self.valueChanged.emit(self.defaultValue, self.checkBoxActive.isChecked())
        else:
            self.editValue.setText(str(self.defaultValue))
            self.slider.setValue(self.toGui(self.defaultValue))

    # -------------------------------------------------
    def autoClickedCB(self: Self) -> None:
        self.autoClicked.emit()
