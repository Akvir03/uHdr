# Documentation des composants applicatifs

## Table des Matières
- [AdvanceSliderLine.py](#AdvanceSliderLinepy)
- [AdvanceSlider.py](#AdvanceSliderpy)
- [AdvanceLineEditGroup.py](#AdvanceLineEditGrouppy)
- [AdvanceImageGallery.py](#AdvanceImageGallerypy)
- [AdvanceFormLineEdit.py](#AdvanceFormLineEditpy)
- [AdvanceFormCheckBox.py](#AdvanceFormCheckBoxpy)
- [AdvanceCheckBoxGroup.py](#AdvanceCheckBoxGrouppy)
- [MainWindow.py](#MainWindowpy)
- [ImageFiles.py](#ImageFilespy)
- [Jexif.py](#Jexifpy)
- [Score.py](#Scorepy)
- [SelectionMap.py](#SelectionMappy)
- [Tags.py](#Tagspy)
- [App.py](#Apppy)
- [colourData.py](#colourDatapy)
- [colourSpace.py](#colourSpacepy)
- [Exif.py](#Exifpy)
- [metadata.py](#metadatapy)
- [net.py](#netpy)
- [numbafun.py](#numbafunpy)
- [quality.py](#qualitypy)
- [srgb.py](#srgbpy)
- [utils.py](#utilspy)
- [processing.py](#processingpy)
- [Prefs.py](#Prefspy)

## AdvanceSliderLine.py

### Classes

#### Classe `AdvanceSliderLine`
- **Description**: La classe `AdvanceSliderLine` est une interface utilisateur pour ajuster une valeur numérique à l'aide d'un curseur, d'un champ de texte et d'un bouton de réinitialisation. Elle hérite de `QFrame` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `valueChanged`: Un signal PyQt qui émet un nom et une valeur flottante lorsque la valeur change.
  - `name`: Un string représentant le nom de l'attribut.
  - `active`: Un booléen indiquant si le widget est actif ou non.
  - `default`: Un flottant représentant la valeur par défaut.
  - `guiRange`: Un tuple d'entiers représentant la plage de valeurs pour le curseur.
  - `dataRange`: Un tuple de flottants représentant la plage de valeurs réelles.
  - `precision`: Un entier représentant la précision d'affichage et de saisie.
  - `hbox`: Un `QHBoxLayout` utilisé pour organiser les widgets horizontalement.
  - `label`: Un `QLabel` pour afficher le nom de l'attribut.
  - `slider`: Un `QSlider` pour ajuster la valeur.
  - `edit`: Un `QLineEdit` pour afficher et modifier la valeur.
  - `reset`: Un `QPushButton` pour réinitialiser la valeur.

- **Méthodes**:
  - `__init__(self: Self, name: str, default: float, guiRange: tuple[int, int], dataRange: tuple[float, float], precision: int = 1000) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `toGui(self, data: float) -> int`: Convertit une valeur réelle en valeur de curseur.
  - `toValue(self, data: int) -> float`: Convertit une valeur de curseur en valeur réelle.
  - `sliderChanged(self: Self) -> None`: Méthode de rappel appelée lors du changement de la valeur du curseur. Met à jour la valeur et émet le signal `valueChanged`.
  - `valueEdited(self: Self) -> None`: Méthode de rappel appelée lors de la modification de la valeur dans le champ de texte. Met à jour la valeur et émet le signal `valueChanged`.
  - `resetClicked(self: Self) -> None`: Méthode de rappel appelée lors de la réinitialisation de la valeur. Réinitialise la valeur à la valeur par défaut et émet le signal `valueChanged`.

## AdvanceSlider.py

### Classes

#### Classe `AdvanceSlider`
- **Description**: La classe `AdvanceSlider` est une interface utilisateur pour ajuster une valeur numérique avec des options supplémentaires telles que l'auto-ajustement et l'activation. Elle hérite de `QFrame` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `valueChanged`: Un signal PyQt qui émet une valeur flottante et un booléen lorsque la valeur change.
  - `autoClicked`: Un signal PyQt qui émet un signal lorsque le bouton auto est cliqué.
  - `activeToggled`: Un signal PyQt qui émet un booléen lorsque l'état activé est modifié.
  - `active`: Un booléen indiquant si le widget est actif ou non.
  - `guiRange`: Un tuple d'entiers représentant la plage de valeurs pour le curseur.
  - `dataRange`: Un tuple de flottants représentant la plage de valeurs réelles.
  - `defaultValue`: Un flottant représentant la valeur par défaut.
  - `precision`: Un entier représentant la précision d'affichage et de saisie.
  - `vbox`: Un `QVBoxLayout` utilisé pour organiser les widgets verticalement.
  - `hboxTop`: Un `QHBoxLayout` pour organiser les widgets horizontalement dans la première ligne.
  - `hbox`: Un `QHBoxLayout` pour organiser les widgets horizontalement.
  - `firstrow`: Un `QFrame` contenant les widgets de la première ligne.
  - `checkBoxActive`: Un `QCheckBox` pour activer ou désactiver l'option.
  - `label`: Un `QLabel` pour afficher le nom de l'attribut.
  - `auto`: Un `QPushButton` pour l'auto-ajustement.
  - `editValue`: Un `QLineEdit` pour afficher et modifier la valeur.
  - `reset`: Un `QPushButton` pour réinitialiser la valeur.
  - `slider`: Un `QSlider` pour ajuster la valeur.

- **Méthodes**:
  - `__init__(self: Self, name: str, defaultValue: float, rangeGUI: tuple[int, int], rangeData: tuple[float, float] | None = None, precision: int = 1000) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `toGui(self, data: float) -> int`: Convertit une valeur réelle en valeur de curseur.
  - `toValue(self, data: int) -> float`: Convertit une valeur de curseur en valeur réelle.
  - `activeChanged(self) -> None`: Méthode de rappel appelée lorsque l'état activé est modifié. Émet le signal `activeToggled`.
  - `sliderChanged(self: Self) -> None`: Méthode de rappel appelée lors du changement de la valeur du curseur. Met à jour la valeur et émet le signal `valueChanged`.
  - `valueEdited(self: Self) -> None`: Méthode de rappel appelée lors de la modification de la valeur dans le champ de texte. Met à jour la valeur et émet le signal `valueChanged`.
  - `resetClicked(self: Self) -> None`: Méthode de rappel appelée lors de la réinitialisation de la valeur. Réinitialise la valeur à la valeur par défaut et émet le signal `valueChanged`.
  - `autoClickedCB(self: Self) -> None`: Méthode de rappel appelée lorsque le bouton auto est cliqué. Émet le signal `autoClicked`.

## AdvanceLineEditGroup.py

### Classes

#### Classe `AdvanceLineEditGroup`
- **Description**: La classe `AdvanceLineEditGroup` est une interface utilisateur pour afficher et éditer un groupe de champs de saisie avec des étiquettes. Elle hérite de `QScrollArea` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `textChanged`: Un signal PyQt qui émet un tuple lorsqu'un texte est modifié.
  - `active`: Un booléen indiquant si le widget est actif ou non.
  - `lines`: Une liste d'objets `AdvanceFormLineEdit` représentant les champs de saisie.
  - `container`: Un `QWidget` contenant les champs de saisie.
  - `layout`: Un `QFormLayout` pour organiser les widgets dans `container`.

- **Méthodes**:
  - `__init__(self: Self, dValues: dict[str, str | tuple[str, bool]]) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `setText(self: Self, texts: list[str]) -> None`: Définit les textes des champs de saisie.
  - `CBtextChanged(self: Self, tag: str, value: str) -> None`: Méthode de rappel appelée lorsque le texte d'un champ de saisie change.

## AdvanceImageGallery.py

### Classes

#### Classe `AdvanceImageGallery`
- **Description**: La classe `AdvanceImageGallery` est une interface utilisateur pour afficher une galerie d'images avec des fonctionnalités avancées telles que le zoom et la navigation. Elle hérite de `QSplitter` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `requestImages`: Un signal PyQt qui émet les indices de début et de fin des images à charger.
  - `imageSelected`: Un signal PyQt qui émet l'indice de l'image sélectionnée.
  - `active`: Un booléen indiquant si le widget est actif ou non.
  - `previousSize`: Un tuple d'entiers représentant la taille précédente de la galerie (lignes et colonnes).
  - `size`: Un tuple d'entiers représentant la taille actuelle de la galerie (lignes et colonnes).
  - `deltaSize`: Un flottant représentant le facteur de changement de taille.
  - `maxColSize`: Un entier représentant le nombre maximal de colonnes.
  - `pageIndex`: Un entier représentant l'index de la page actuelle.
  - `selectedImage`: Un entier ou None représentant l'indice de l'image sélectionnée.
  - `nbImages`: Un entier représentant le nombre total d'images dans la galerie.
  - `gallery`: Un objet de la classe `ImageGallery` pour afficher les images en grille.
  - `navContainer`: Un `QWidget` contenant les boutons de navigation et de zoom.
  - `navLayout`: Un `QHBoxLayout` pour organiser les widgets dans `navContainer`.
  - `previousPage`: Un `QPushButton` pour naviguer vers la page précédente.
  - `one`: Un `QPushButton` pour afficher une seule image.
  - `zoomLabel`: Un `QLabel` pour afficher le texte "zoom:".
  - `zoomMinus`: Un `QPushButton` pour réduire le zoom.
  - `zoomSlider`: Un `QSlider` pour ajuster le zoom.
  - `zoomPlus`: Un `QPushButton` pour augmenter le zoom.
  - `pageLabel`: Un `QLabel` pour afficher les informations de la page actuelle.
  - `nextPage`: Un `QPushButton` pour naviguer vers la page suivante.

- **Méthodes**:
  - `__init__(self: AdvanceImageGallery, nbImages: int = 0) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `incSize(self: AdvanceImageGallery) -> None`: Augmente la taille de la grille (zoom arrière).
  - `decSize(self: AdvanceImageGallery) -> None`: Réduit la taille de la grille (zoom avant).
  - `zoomSliderChanged(self: AdvanceImageGallery) -> None`: Méthode de rappel appelée lorsque la valeur du curseur de zoom change. Ajuste la taille de la grille.
  - `setSize(self: AdvanceImageGallery, size: tuple[int, int]) -> None`: Définit la taille de la grille et met à jour les informations de la page.
  - `firstPage(self: AdvanceImageGallery) -> None`: Navigue vers la première page.
  - `CBnextPage(self: AdvanceImageGallery) -> None`: Méthode de rappel appelée pour naviguer vers la page suivante.
  - `CBpreviousPage(self: AdvanceImageGallery) -> None`: Méthode de rappel appelée pour naviguer vers la page précédente.
  - `setNbImages(self: AdvanceImageGallery, nb: int) -> None`: Définit le nombre total d'images dans la galerie et met à jour les informations de la page.
  - `imageLocalIdxToGlobalIndex(self: AdvanceImageGallery, idxLocal: int) -> int`: Convertit un indice local d'image en indice global.
  - `imageIdxToIndexInPage(self: AdvanceImageGallery, imageIndex: int) -> int`: Convertit un indice d'image en indice dans la page actuelle.
  - `imageIdxToPageIndex(self: AdvanceImageGallery, imageIndex: int) -> int`: Convertit un indice d'image en indice de page.
  - `updatePageInfo(self: AdvanceImageGallery) -> None`: Met à jour les informations de la page.
  - `sendRequestImages(self: AdvanceImageGallery) -> None`: Envoie une requête pour charger les images.
  - `setImage(self: AdvanceImageGallery, index: int, image: ndarray | None) -> None`: Définit une image dans la galerie à l'indice spécifié.
  - `CBimageSelected(self: AdvanceImageGallery, idxIW: int) -> None`: Méthode de rappel appelée lorsque une image est sélectionnée. Émet le signal `imageSelected`.

## AdvanceFormLineEdit.py

### Classes

#### Classe `AdvanceFormLineEdit`
- **Description**: La classe `AdvanceFormLineEdit` est une interface utilisateur pour créer des champs de saisie avec des étiquettes dans un formulaire. Elle hérite de `QObject` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `textChanged`: Un signal PyQt qui émet un nom de label et un texte lorsque le texte change.
  - `active`: Un booléen indiquant si le widget est actif ou non.
  - `defaultText`: Un string représentant le texte par défaut du champ de saisie.
  - `editable`: Un booléen indiquant si le champ de saisie est modifiable.
  - `label`: Un `QLabel` pour afficher le nom du champ de saisie.
  - `lineEdit`: Un `QLineEdit` pour afficher et modifier le texte du champ de saisie.

- **Méthodes**:
  - `__init__(self: Self, labelName: str, defaultText: str, layout: QFormLayout, editable: bool = True) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `CBtextChanged(self: Self) -> None`: Méthode de rappel appelée lorsque le texte du champ de saisie change.
  - `setText(self: Self, txt: str) -> None`: Définit le texte du champ de saisie.

## AdvanceFormCheckBox.py

### Classes

#### Classe `AdvanceFormCheckBox`
- **Description**: La classe `AdvanceFormCheckBox` est une interface utilisateur pour créer une case à cocher avec une étiquette dans un formulaire. Elle hérite de `QObject` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `toggled`: Un signal PyQt qui émet un tuple et un booléen lorsque l'état de la case à cocher change.
  - `keys`: Un tuple de chaînes de caractères représentant les textes gauche et droit de la case à cocher.
  - `checked`: Un booléen indiquant si la case à cocher est cochée par défaut.
  - `active`: Un booléen indiquant si le widget est actif ou non.
  - `editable`: Un booléen indiquant si la case à cocher est modifiable.
  - `label`: Un `QLabel` pour afficher le texte gauche de la case à cocher.
  - `checkbox`: Un `QCheckBox` pour afficher et modifier l'état de la case à cocher.

- **Méthodes**:
  - `__init__(self: Self, leftText: str, rightText: str, layout: QFormLayout, checked: bool = False, editable: bool = True) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `getKeys(self: Self) -> tuple[str, str]`: Retourne les clés (textes gauche et droit) de la case à cocher.
  - `setChecked(self: Self, checked: bool) -> None`: Définit l'état de la case à cocher.
  - `CBtoggled(self: Self) -> None`: Méthode de rappel appelée lorsque l'état de la case à cocher change.

## AdvanceCheckBoxGroup.py

### Classes

#### Classe `AdvanceCheckBoxGroup`
- **Description**: La classe `AdvanceCheckBoxGroup` est une interface utilisateur pour gérer un groupe de cases à cocher avec des étiquettes dans un formulaire défilant. Elle hérite de `QScrollArea` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `toggled`: Un signal PyQt qui émet un tuple et un booléen lorsque l'état d'une case à cocher change.
  - `lines`: Une liste d'objets `AdvanceFormCheckBox` représentant les cases à cocher.
  - `container`: Un `QWidget` contenant les cases à cocher.
  - `layout`: Un `QFormLayout` pour organiser les widgets dans `container`.

- **Méthodes**:
  - `__init__(self: Self, dValues: dict[tuple[str, str], bool | tuple[bool, bool]]) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `getByKey(self: Self, key: tuple[str, str]) -> AdvanceFormCheckBox | None`: Retourne la case à cocher correspondant à la clé donnée.
  - `setValues(self: Self, values: dict[tuple[str, str], bool]) -> None`: Définit les valeurs des cases à cocher selon le dictionnaire fourni.
  - `resetValues(self: Self) -> None`: Réinitialise toutes les cases à cocher à `False`.
  - `addLine(self: Self, dValues: dict[tuple[str, str], bool | tuple[bool, bool]]) -> None`: Ajoute une ligne de cases à cocher selon les valeurs fournies.
  - `removeLine(self: Self, keys: tuple[str, str]) -> None`: Supprime la ligne correspondant aux clés données.
  - `removeAll(self: Self) -> None`: Supprime toutes les lignes de cases à cocher.
  - `CBtextChanged(self: Self, tag: tuple[str, str], value: bool) -> None`: Méthode de rappel appelée lorsque le texte d'une case à cocher change.
  - `CBtoggled(self: Self, key: tuple[str, str], toggled_: bool) -> None`: Méthode de rappel appelée lorsque l'état d'une case à cocher change. Émet le signal `toggled`.

## MainWindow.py

### Classes

#### Classe `MainWindow`
- **Description**: La classe `MainWindow` est la fenêtre principale de l'application pour l'édition d'images HDR. Elle hérite de `QMainWindow` et utilise PyQt6 pour la création de l'interface graphique.

- **Composants**:
  - `dirSelected`: Un signal PyQt qui émet une chaîne de caractères lorsque le répertoire est sélectionné.
  - `requestImages`: Un signal PyQt qui émet deux entiers lorsqu'une demande d'images est faite.
  - `imageSelected`: Un signal PyQt qui émet un entier lorsqu'une image est sélectionnée.
  - `tagChanged`: Un signal PyQt qui émet un tuple et un booléen lorsqu'une étiquette est modifiée.
  - `scoreChanged`: Un signal PyQt qui émet un entier lorsqu'un score est modifié.
  - `scoreSelectionChanged`: Un signal PyQt qui émet une liste lorsqu'une sélection de score est modifiée.
  - `metaBlock`: Un objet de la classe `InfoSelPrefBlock` pour afficher les informations, les sélections et les préférences.
  - `editBlock`: Un objet de la classe `EditorBlock` pour éditer les images.
  - `imageGallery`: Un objet de la classe `AdvanceImageGallery` pour afficher une galerie d'images.
  - `metaDock`: Un `QDockWidget` pour contenir le `metaBlock`.
  - `editDock`: Un `QDockWidget` pour contenir le `editBlock`.

- **Méthodes**:
  - `__init__(self: MainWindow, nbImages: int = 0, tags: dict[Tuple[str, str], bool] = {}) -> None`: Le constructeur initialise les composants de l'interface utilisateur et configure les widgets.
  - `resetGallery(self: MainWindow)`: Réinitialise la galerie d'images.
  - `firstPage(self: MainWindow)`: Navigue vers la première page de la galerie d'images.
  - `setGalleryImage(self: Self, index: int, image: ndarray | None) -> None`: Définit l'image de la galerie à l'indice spécifié.
  - `setNumberImages(self: Self, nbImages: int) -> None`: Définit le nombre total d'images dans la galerie.
  - `setEditorImage(self: Self, image: ndarray) -> None`: Définit l'image dans l'éditeur.
  - `setTagsImage(self: Self, tags: dict[Tuple[str, str], bool]) -> None`: Définit les étiquettes de l'image.
  - `resetTags(self: Self) -> None`: Réinitialise les étiquettes de l'image.
  - `setInfo(self: Self, name: str, path: str, size: tuple[int, int] = (-1, -1), colorSpace: str = "...", type: str = "...", bps: int = -1) -> None`: Définit les informations de l'image.
  - `setScore(self: Self, score: int) -> None`: Définit le score de l'image.
  - `setPrefs(self: Self) -> None`: Définit les préférences.
  - `buildFileMenu(self)`: Construit le menu Fichier avec les options de sélection de répertoire, de sauvegarde et de quitter.
  - `CBSelectDir(self)`: Méthode de rappel pour sélectionner un répertoire via une boîte de dialogue de fichiers. Émet le signal `dirSelected`.
  - `CBrequestImages(self: Self, minIdx: int, maxIdx: int) -> None`: Méthode de rappel pour demander des images. Émet le signal `requestImages`.
  - `CBimageSelected(self: Self, idx: int) -> None`: Méthode de rappel pour sélectionner une image. Émet le signal `imageSelected`.
  - `CBtagChanged(self, key: tuple[str, str], value: bool) -> None`: Méthode de rappel pour changer une étiquette. Émet le signal `tagChanged`.
  - `CBscoreChanged(self, value: int) -> None`: Méthode de rappel pour changer le score. Émet le signal `scoreChanged`.
  - `CBscoreSelectionChanged(self: Self, scoreSelection: list) -> None`: Méthode de rappel pour changer la sélection de score. Émet le signal `scoreSelectionChanged`.
  - `CBSave(self: QMainWindow) -> None`: Méthode de rappel pour sauvegarder l'image affichée dans l'éditeur.

## ImageFiles.py

### Classes

#### Classe `ImageFiles`
- **Description**: La classe `ImageFiles` gère les fichiers d'image dans un répertoire : chargement asynchrone, mise en cache des images. Elle hérite de `QObject` et utilise PyQt6 pour la gestion des signaux et des threads.

- **Composants**:
  - `imageLoaded`: Un signal PyQt qui émet une chaîne de caractères lorsque l'image est chargée.
  - `imagePath`: Un string représentant le chemin des images.
  - `extraPath`: Un string représentant le chemin des données supplémentaires.
  - `nbImages`: Un entier représentant le nombre d'images.
  - `imageFilenames`: Une liste de chaînes de caractères représentant les noms de fichiers d'images.
  - `imageIsLoaded`: Un dictionnaire indiquant si les images sont chargées.
  - `imageIsThumbnail`: Un dictionnaire indiquant si les images sont des miniatures.
  - `images`: Un dictionnaire contenant les données des images sous forme de tableaux numpy.
  - `imageScore`: Un dictionnaire contenant les scores des images.
  - `imageTags`: Un dictionnaire contenant les étiquettes des images.
  - `imageExif`: Un dictionnaire contenant les données EXIF des images.
  - `pool`: Un objet `QThreadPool` pour la gestion des threads.

- **Méthodes**:
  - `__init__(self: ImageFiles) -> None`: Le constructeur initialise les composants et les attributs de la classe.
  - `reset(self: ImageFiles)`: Réinitialise les attributs liés aux images.
  - `__repr__(self: ImageFiles) -> str`: Retourne une représentation en chaîne de caractères de l'objet.
  - `getNbImages(self: ImageFiles) -> int`: Retourne le nombre de fichiers d'images.
  - `getImagesFilesnames(self: ImageFiles) -> list[str]`: Retourne la liste des noms de fichiers d'images.
  - `setPrefs(self: ImageFiles) -> None`: Met à jour les attributs selon les préférences.
  - `setDirectory(self: ImageFiles, dirPath: str) -> int`: Définit le répertoire et scanne les fichiers d'images.
  - `requestLoad(self: ImageFiles, filename: str, thumbnail: bool = True)`: Ajoute une demande de chargement d'image au pool de threads.
  - `endLoadImage(self: ImageFiles, error: bool, filename: str)`: Appelée lorsqu'une image est chargée.
  - `getImage(self: ImageFiles, name: str, thumbnail: bool = True) -> ndarray`: Retourne les données de l'image.
  - `getImageTags(self: ImageFiles, name: str) -> Tags`: Retourne les étiquettes de l'image.
  - `getImageExif(self: ImageFiles, name: str) -> dict[str, str]`: Retourne les données EXIF de l'image.
  - `getImageScore(self: ImageFiles, name: str) -> int`: Retourne le score de l'image.
  - `checkExtra(self: ImageFiles) -> None`: Vérifie et crée le répertoire pour les données supplémentaires.
  - `updateImageTag(self: ImageFiles, imageName: str, type: str, name: str, value: bool) -> None`: Met à jour les étiquettes de l'image et les sauvegarde.
  - `updateImageScore(self: ImageFiles, imageName: str, value: int) -> None`: Met à jour le score de l'image et le sauvegarde.

### Classe `RunLoadImage`
- **Description**: La classe `RunLoadImage` gère le chargement des images de manière asynchrone. Elle hérite de `QRunnable` pour être utilisée avec `QThreadPool`.

- **Composants**:
  - `parent`: Un objet `ImageFiles` représentant le parent.
  - `filename`: Un string représentant le nom du fichier à charger.
  - `thumbnail`: Un booléen indiquant si l'image est une miniature.

- **Méthodes**:
  - `__init__(self: RunLoadImage, parent: ImageFiles, filename: str, thumbnail: bool = True)`: Le constructeur initialise les composants et les attributs de la classe.
  - `run(self: RunLoadImage)`: Méthode appelée pour exécuter le chargement de l'image.

## Jexif.py

### Classes

#### Classe `Jexif`
- **Description**: La classe `Jexif` est utilisée pour gérer les données EXIF des images HDR. Elle contient des méthodes statiques pour charger et convertir les données EXIF.

- **Méthodes**:
  - `load(imageDir: str, imageFilename: str, extraDir: str) -> dict[str, str]`: Cette méthode statique charge les données EXIF d'une image à partir d'un fichier `.jexif` ou extrait les données EXIF brutes si le fichier `.jexif` n'existe pas. 
    - **Paramètres**:
      - `imageDir`: Le répertoire contenant l'image.
      - `imageFilename`: Le nom du fichier de l'image.
      - `extraDir`: Le répertoire supplémentaire pour stocker les données EXIF.
    - **Retour**: Un dictionnaire contenant les données EXIF de l'image.
  - `toTuple(exifDict: dict[str, str]) -> tuple[tuple[int, int], str, str, int]`: Cette méthode statique convertit un dictionnaire EXIF en un tuple.
    - **Paramètres**:
      - `exifDict`: Un dictionnaire contenant les données EXIF.
    - **Retour**: Un tuple contenant la taille, l'espace colorimétrique, le type et les bits par échantillon.

## Score.py

### Classes

#### Classe `Score`
- **Description**: La classe `Score` gère les scores des images HDR. Elle contient des méthodes statiques pour charger et sauvegarder les scores des images.

- **Méthodes**:
  - `load(imageDir: str, imageFilename: str, extraDir: str) -> int`: Cette méthode statique charge le score d'une image à partir d'un fichier `.score`.
    - **Paramètres**:
      - `imageDir`: Le répertoire contenant l'image.
      - `imageFilename`: Le nom du fichier de l'image.
      - `extraDir`: Le répertoire supplémentaire pour stocker les données de score.
    - **Retour**: Un entier représentant le score de l'image.
  - `save(imageDir: str, extraDir: str, imageFilename: str, score: int) -> None`: Cette méthode statique sauvegarde le score d'une image dans un fichier `.score`.
    - **Paramètres**:
      - `imageDir`: Le répertoire contenant l'image.
      - `extraDir`: Le répertoire supplémentaire pour stocker les données de score.
      - `imageFilename`: Le nom du fichier de l'image.
      - `score`: Un entier représentant le score de l'image.

## SelectionMap.py

### Classes

#### Classe `SelectionMap`
- **Description**: La classe `SelectionMap` gère la sélection d'images par score, étiquettes et nom. Elle permet de maintenir et de manipuler les sélections d'images.

- **Composants**:
  - `__imageNameToIsSelected`: Un dictionnaire mappant les noms d'images à leur état de sélection (booléen).
  - `__imageNameToGlobalIndex`: Un dictionnaire mappant les noms d'images à leur indice global.
  - `__globalIndexToImageName`: Un dictionnaire mappant les indices globaux aux noms d'images.
  - `__globalIndexToSelectedIndex`: Un dictionnaire mappant les indices globaux aux indices de sélection.
  - `__selectedIndexToGlobalIndex`: Un dictionnaire mappant les indices de sélection aux indices globaux.
  - `numberImages`: Un entier représentant le nombre total d'images.
  - `numberSelectedImages`: Un entier représentant le nombre d'images sélectionnées.

- **Méthodes**:
  - `__init__(self: SelectionMap, imageNames: list[str])`: Initialise les composants et configure les dictionnaires avec les noms d'images fournis.
  - `__repr__(self: SelectionMap) -> str`: Retourne une représentation en chaîne de caractères de la sélection d'images.
  - `reset(self: SelectionMap) -> None`: Réinitialise les dictionnaires et les compteurs.
  - `setImageNames(self: SelectionMap, names: list[str]) -> None`: Configure les noms d'images et sélectionne toutes les images.
  - `selectAll(self: SelectionMap) -> None`: Sélectionne toutes les images.
  - `applySelection(self: SelectionMap, selection: list[tuple[str, bool]]) -> None`: Applique une sélection d'images fournie.
  - `isSelected(self: SelectionMap, name: str) -> bool|None`: Vérifie si une image est sélectionnée.
  - `imageNameToGlobalIndex(self: SelectionMap, name: str) -> int|None`: Retourne l'indice global d'une image à partir de son nom.
  - `globalIndexToImageName(self: SelectionMap, gIdx: int) -> str|None`: Retourne le nom d'une image à partir de son indice global.
  - `globalIndexToSelectedIndex(self: SelectionMap, gIdx: int) -> int|None`: Retourne l'indice de sélection d'une image à partir de son indice global.
  - `selectedlIndexToGlobalIndex(self: SelectionMap, sIdx: int) -> int|None`: Retourne l'indice global d'une image à partir de son indice de sélection.
  - `selectedIndexToImageName(self: SelectionMap, sIdx: int) -> str|None`: Retourne le nom d'une image à partir de son indice de sélection.
  - `imageNameToSelectedIndex(self: SelectionMap, name: str) -> int|None`: Retourne l'indice de sélection d'une image à partir de son nom.
  - `selectByScore(self: SelectionMap, scores: dict[str, int], scoresSelected: list[int]) -> None`: Sélectionne les images dont le score se trouve dans la liste des scores sélectionnés.
  - `getSelectedImageNumber(self: SelectionMap) -> int`: Retourne le nombre d'images sélectionnées.

## Tags.py

### Classes

#### Classe `Tags`
- **Description**: La classe `Tags` gère les informations supplémentaires définies par l'utilisateur, appelées "Tags". Les étiquettes d'images sont agrégées dans un répertoire spécifique. La structure des étiquettes est organisée par types et noms d'étiquettes avec des valeurs booléennes.

- **Composants**:
  - `tags`: Un dictionnaire contenant les étiquettes sous la forme `{ 'type': { 'name': bool } }`.

- **Méthodes**:
  - `__init__(self: Self, tags: dict[str, dict[str, bool]]) -> None`: Le constructeur initialise l'objet `Tags` avec un dictionnaire d'étiquettes.
  - `load(imageDir: str, imageFilename: str, extraDir: str) -> Tags`: Méthode statique qui charge les étiquettes d'une image à partir d'un fichier. Si le fichier d'étiquettes existe, il est chargé et retourné. Sinon, une instance vide de `Tags` est retournée.
  - `save(self: Self, imageDir: str, extraDir: str, imageFilename: str) -> None`: Sauvegarde les étiquettes d'une image dans un fichier.
  - `add(self: Self, type: str, name: str, value: bool) -> None`: Ajoute une étiquette à l'objet `Tags`. Si le type d'étiquette existe déjà, la nouvelle étiquette est ajoutée sous ce type. Sinon, un nouveau type est créé.
  - `__repr__(self: Self) -> str`: Retourne une représentation en chaîne de caractères de l'objet `Tags`.
  - `aggregateTagsFiles(imagePath: str, extraPath: str) -> dict[str, dict[str, bool]]`: Méthode statique qui agrège les fichiers d'étiquettes dans un répertoire. Retourne un dictionnaire d'étiquettes agrégé.
  - `aggregateTagsData(tags: list[dict[str, dict[str, bool]]]) -> dict[str, dict[str, bool]]`: Méthode statique qui agrège les données d'étiquettes à partir d'une liste de dictionnaires d'étiquettes.
  - `toGUI(self: Self) -> dict[Tuple[str, str], bool]`: Formate les étiquettes pour une interface utilisateur graphique.
  - `aggregate(self: Self, other: Tags) -> None`: Agrège les étiquettes de l'objet actuel avec celles d'un autre objet `Tags`.

## App.py

### Classes

#### Classe `App`
- **Description**: La classe `App` représente l'application principale pour l'édition d'images HDR. Elle gère l'interface utilisateur, la sélection d'images, les préférences et les interactions avec les fichiers d'images.

- **Composants**:
  - `imagesManagement`: Un objet de la classe `ImageFiles` pour gérer les fichiers d'images.
  - `tags`: Un objet de la classe `Tags` pour gérer les étiquettes des images.
  - `selectionMap`: Un objet de la classe `SelectionMap` pour gérer la sélection d'images.
  - `selectedImageIdx`: Un entier ou None représentant l'indice de l'image actuellement sélectionnée.
  - `mainWindow`: Un objet de la classe `MainWindow` pour gérer l'interface utilisateur principale.

- **Méthodes**:
  - `__init__(self: App) -> None`: Le constructeur initialise l'application, charge les préférences, configure les composants et les callbacks, et affiche la fenêtre principale.
  - `getImageRangeIndex(self: App) -> tuple[int, int]`: Retourne l'intervalle des indices des images affichées par la galerie.
  - `update(self: App) -> None`: Met à jour la galerie après un changement de sélection ou de répertoire.
  - `CBdirSelected(self: App, path: str) -> None`: Méthode de rappel appelée lors de la sélection d'un répertoire.
  - `CBExposureSliderChanged(self: App, value: float, active: bool) -> None`: Méthode de rappel appelée lors du changement de la valeur du curseur d'exposition.
  - `CBrequestImages(self: App, minIdx: int, maxIdx: int) -> None`: Méthode de rappel appelée lors de la demande de chargement d'images (lors du changement de page ou de niveau de zoom).
  - `CBimageLoaded(self: App, filename: str) -> None`: Méthode de rappel appelée lorsqu'une image demandée est chargée.
  - `CBimageSelected(self: App, index: int) -> None`: Méthode de rappel appelée lorsqu'une image est sélectionnée.
  - `CBtagChanged(self: App, key: tuple[str, str], value: bool) -> None`: Méthode de rappel appelée lors du changement d'une étiquette.
  - `CBscoreChanged(self: App, value: int) -> None`: Méthode de rappel appelée lors du changement de score.
  - `CBscoreSelectionChanged(self: App, listSelectedScore: list[bool]) -> None`: Méthode de rappel appelée lors du changement de la sélection de score.

## colourData.py

### Fonctions

#### Fonction `buildLchcolourData`
- **Description**: La fonction `buildLchcolourData` génère des données de couleur dans l'espace Lch (Lightness, Chroma, Hue) en fonction des plages de L, c, et h fournies. Les données de couleur sont organisées selon les dimensions spécifiées par `width` et `height`.

- **Paramètres**:
  - `L`: Un tuple de deux flottants représentant la plage de luminosité.
  - `c`: Un tuple de deux flottants représentant la plage de chroma.
  - `h`: Un tuple de deux flottants représentant la plage de teinte.
  - `size`: Un tuple de deux entiers représentant la taille (hauteur, largeur) de la matrice de données de couleur.
  - `width`: Une chaîne de caractères indiquant la dimension utilisée pour l'axe des x (peut être 'L', 'c', ou 'h').
  - `height`: Une chaîne de caractères indiquant la dimension utilisée pour l'axe des y (peut être 'L', 'c', ou 'h').

- **Retour**:
  - `colourData`: Un tableau numpy de dimensions `(size[0], size[1], 3)` contenant les données de couleur Lch.

- **Comportement**:
  - Initialise une matrice de zéros pour `colourData`.
  - Calcule les plages de L, c, et h.
  - Remplit la matrice `colourData` en fonction des dimensions spécifiées par `width` et `height`.
  - Pour chaque combinaison de x et y dans la matrice, calcule les valeurs de L, c, et h en interpolant linéairement entre les valeurs minimales et maximales des plages correspondantes.

## colourSpace.py

### Classes

#### Classe `ColorSpace`
- **Description**: La classe `ColorSpace` est une énumération représentant différents espaces colorimétriques. Elle hérite de `Enum`.

- **Énumérations**:
  - `No = 0`
  - `RGB = 1`
  - `sRGB = 2`
  - `scRGB = 3`
  - `Lab = 4`
  - `Luv = 5`
  - `IPT = 6`
  - `Jzazbz = 7`
  - `XYZ = 8`

## Exif.py

### Classes

#### Classe `Exif`
- **Description**: La classe `Exif` gère la lecture et le filtrage des données EXIF des images. Elle utilise `exiftool` pour lire les métadonnées des fichiers image.

- **Méthodes**:
  - `readExif(imagePath: str, filename: str) -> dict[str, str] | None`: Méthode statique qui lit les données EXIF d'une image en utilisant `exiftool`.
    - **Paramètres**:
      - `imagePath`: Le chemin du répertoire contenant l'image.
      - `filename`: Le nom du fichier de l'image.
    - **Retour**: Un dictionnaire contenant les données EXIF de l'image, ou `None` en cas d'erreur.
  - `recoverExifData(exif: dict[str, str]) -> dict[str, str]`: Méthode statique qui filtre les données EXIF brutes pour récupérer des informations spécifiques comme l'espace colorimétrique, les bits par échantillon, le type et la taille de l'image.
    - **Paramètres**:
      - `exif`: Un dictionnaire contenant les données EXIF brutes.
    - **Retour**: Un dictionnaire contenant les données EXIF filtrées.

## metadata.py

### Classes

#### Classe `tags`
- **Description**: La classe `tags` est utilisée pour définir les tags qui peuvent être appliqués à une image. Les définitions des tags sont chargées à partir d'un fichier JSON (`./preferences/tags.json`).

- **Méthodes**:
  - `__init__(self)`: Constructeur qui initialise les tags à partir du fichier `tags.json`.
  - `getTagsRootName(self) -> str`: Retourne le nom de la racine des tags.

#### Classe `metadata`
- **Description**: La classe `metadata` gère les métadonnées d'une image, telles que le nom de fichier, le chemin, la description, les données EXIF, les catégories et les processus à appliquer à l'image.

- **Composants**:
  - `metadata`: Dictionnaire contenant les métadonnées de l'image.
  - `image`: Référence à l'objet image associé.
  - `otherTags`: Instance de la classe `tags` contenant les autres tags définis dans `tags.json`.

- **Méthodes**:
  - `__init__(self, _image)`: Constructeur qui initialise les métadonnées d'une image.
  - `build(_image)`: Méthode statique qui construit un objet `metadata` à partir d'une image.
  - `save(self)`: Sauvegarde les métadonnées dans un fichier JSON.
  - `readExif(filename)`: Méthode statique qui lit les données EXIF d'un fichier image en utilisant `exiftool`.
  - `recoverData(self, exif)`: Récupère les données pertinentes à partir des métadonnées EXIF.
  - `__repr__(self)`: Convertit les métadonnées en une chaîne de caractères JSON.
  - `__str__(self)`: Convertit les métadonnées en une chaîne de caractères JSON (identique à `__repr__`).

## net.py

### Classes

#### Classe `Net`
- **Description**: La classe `Net` définit un réseau de neurones simple avec une couche linéaire suivie d'une normalisation par lots et d'une activation sigmoïde. Elle hérite de `nn.Module`.

- **Composants**:
  - `layer` (nn.Sequential): Une séquence de couches de réseaux de neurones comprenant une couche linéaire, une normalisation par lots et une activation sigmoïde.

- **Méthodes**:
  - `__init__(self, n_feature, n_output)`: Constructeur qui initialise les couches du réseau de neurones.
  - `forward(self, x)`: Définit la passe avant du réseau de neurones.

## numbafun.py

### Fonctions

#### Fonction `numba_cctf_sRGB_encoding`
- **Description**: Encodage cctf sRGB accéléré avec Numba.
- **Paramètres**:
  - `L` (float ou numpy.ndarray, Required): La luminance d'entrée.
- **Retour**:
  - `v` (float ou numpy.ndarray): La luminance encodée.

#### Fonction `numba_cctf_sRGB_decoding`
- **Description**: Décodage cctf sRGB accéléré avec Numba.
- **Paramètres**:
  - `V` (float ou numpy.ndarray, Required): La luminance encodée.
- **Retour**:
  - `L` (float ou numpy.ndarray): La luminance décodée.

#### Fonction `cuda_cctf_sRGB_decoding`
- **Description**: Décodage cctf sRGB accéléré avec CUDA.
- **Paramètres**:
  - `V` (float ou numpy.ndarray, Required): La luminance encodée.
- **Retour**:
  - `L` (float ou numpy.ndarray): La luminance décodée.

#### Fonction `cuda_cctf_sRGB_encoding`
- **Description**: Encodage cctf sRGB accéléré avec CUDA.
- **Paramètres**:
  - `L` (float ou numpy.ndarray, Required): La luminance d'entrée.
- **Retour**:
  - `v` (float ou numpy.ndarray): La luminance encodée.

## quality.py

### Classes

#### Classe `quality`
- **Description**: La classe `quality` gère les informations sur la qualité des images HDR, y compris les scores de qualité et les artefacts.
  
- **Composants**:
  - `_image`: Référence à l'image associée (initialisée à `None`).
  - `imageNpath` (dict): Dictionnaire contenant le nom et le chemin de l'image.
  - `user` (dict): Dictionnaire contenant des informations sur l'utilisateur (pseudo).
  - `score` (dict): Dictionnaire contenant les scores de qualité de l'image (quality, aesthetics, comfort, naturalness).
  - `artifact` (dict): Dictionnaire indiquant la présence d'artefacts dans l'image (ghost, noise, blur, halo, other).

- **Méthodes**:
  - `__init__(self)`: Constructeur qui initialise les attributs de la classe `quality` avec des valeurs par défaut.
  - `toDict(self) -> dict`: Convertit l'objet `quality` en dictionnaire.
  - `__repr__(self) -> str`: Retourne une représentation en chaîne de caractères de l'objet `quality`.
  - `__str__(self) -> str`: Retourne une représentation en chaîne de caractères de l'objet `quality` (identique à `__repr__`).

## srgb.py

### Fonctions

#### Fonction `eotf_inverse_sRGB`
- **Description**: Définit la fonction de transfert électro-optique inverse (EOTF/EOCF) pour sRGB selon la norme IEC 61966-2-1:1999.
- **Paramètres**:
  - `L` (numeric ou array_like, Required): La luminance de l'image.
- **Retour**:
  - `numeric ou ndarray`: Le signal électrique correspondant.

#### Fonction `eotf_sRGB`
- **Description**: Définit la fonction de transfert électro-optique (EOTF/EOCF) pour sRGB selon la norme IEC 61966-2-1:1999.
- **Paramètres**:
  - `V` (numeric ou array_like, Required): Le signal électrique.
- **Retour**:
  - `numeric ou ndarray`: La luminance correspondante de l'image.

## utils.py

### Fonctions

#### Fonction `filenamesplit`
- **Description**: Récupère le chemin, le nom et l'extension d'un fichier à partir de son nom complet.
- **Paramètres**:
  - `filename` (str, Required): Nom du fichier.
- **Retour**:
  - `tuple[str, str, str]`: Tuple contenant le chemin, le nom et l'extension du fichier.

#### Fonction `filterlistdir`
- **Description**: Retourne les fichiers dans un répertoire qui se terminent par l'une des extensions spécifiées dans `extList`.
- **Paramètres**:
  - `path` (str, Required): Chemin vers le répertoire.
  - `extList` (tuple de str, Required): Extensions de fichiers à filtrer.
- **Retour**:
  - `[str]` ou `tuple de str` ou `str`: Liste, tuple ou chaîne de caractères des fichiers filtrés.

#### Fonction `ndarray2vector`
- **Description**: Transforme un tableau 2D de données de couleur en vecteur.
- **Paramètres**:
  - `nda` (numpy.ndarray, Required): Tableau numpy (2D de scalaire ou vecteur).
- **Retour**:
  - `numpy.ndarray, Required`: Tableau numpy (1D de scalaire ou vecteur).

#### Fonction `NPlinearWeightMask`
- **Description**: Applique un masque de poids linéaire à un tableau 2D.
- **Paramètres**:
  - `x`: Tableau 2D à traiter.
  - `xMin`: Valeur minimale pour le masque.
  - `xMax`: Valeur maximale pour le masque.
  - `xTolerance`: Tolérance pour le masque.
- **Retour**:
  - `numpy.ndarray`: Tableau 2D avec le masque appliqué.

#### Fonction `croppRotated`
- **Description**: Calcule les dimensions recadrées après une rotation.
- **Paramètres**:
  - `h`: Hauteur originale.
  - `w`: Largeur originale.
  - `alpha`: Angle de rotation en degrés.
- **Retour**:
  - `tuple[float, float]`: Dimensions recadrées après rotation.

## processing.py

### Fonctions

#### Fonction `XYZ_to_sRGB`
- **Description**: Convertit un tableau de pixels de l'espace de couleur XYZ vers l'espace de couleur sRGB.
- **Paramètres**:
  - `XYZ` (numpy.ndarray): Tableau de pixels en espace de couleur XYZ.
  - `apply_cctf_encoding` (bool): Applique l'encodage cctf de sRGB si `True`.
- **Retour**: Tableau de pixels en espace de couleur sRGB.

#### Fonction `sRGB_to_XYZ`
- **Description**: Convertit un tableau de pixels de l'espace de couleur sRGB vers l'espace de couleur XYZ.
- **Paramètres**:
  - `RGB` (numpy.ndarray): Tableau de pixels en espace de couleur sRGB.
  - `apply_cctf_decoding` (bool): Applique le décodage cctf de sRGB si `True`.
- **Retour**: Tableau de pixels en espace de couleur XYZ.

#### Fonction `Lab_to_XYZ`
- **Description**: Convertit un tableau de pixels de l'espace de couleur Lab vers l'espace de couleur XYZ.
- **Paramètres**:
  - `Lab` (numpy.ndarray): Tableau de pixels en espace de couleur Lab.
- **Retour**: Tableau de pixels en espace de couleur XYZ.

#### Fonction `XYZ_to_Lab`
- **Description**: Convertit un tableau de pixels de l'espace de couleur XYZ vers l'espace de couleur Lab.
- **Paramètres**:
  - `XYZ` (numpy.ndarray): Tableau de pixels en espace de couleur XYZ.
- **Retour**: Tableau de pixels en espace de couleur Lab.

#### Fonction `Lab_to_sRGB`
- **Description**: Convertit un tableau de pixels de l'espace de couleur Lab vers l'espace de couleur sRGB.
- **Paramètres**:
  - `Lab` (numpy.ndarray): Tableau de pixels en espace de couleur Lab.
  - `apply_cctf_encoding` (bool): Applique l'encodage cctf de sRGB si `True`.
  - `clip` (bool): Coupe les valeurs en dehors des limites de l'espace de couleur si `True`.
- **Retour**: Tableau de pixels en espace de couleur sRGB.

#### Fonction `sRGB_to_Lab`
- **Description**: Convertit un tableau de pixels de l'espace de couleur sRGB vers l'espace de couleur Lab.
- **Paramètres**:
  - `RGB` (numpy.ndarray): Tableau de pixels en espace de couleur sRGB.
  - `apply_cctf_decoding` (bool): Applique le décodage cctf de sRGB si `True`.
- **Retour**: Tableau de pixels en espace de couleur Lab.

#### Fonction `Lch_to_sRGB`
- **Description**: Convertit un tableau de pixels de l'espace de couleur Lch vers l'espace de couleur sRGB.
- **Paramètres**:
  - `Lch` (numpy.ndarray): Tableau de pixels en espace de couleur Lch.
  - `apply_cctf_encoding` (bool): Applique l'encodage cctf de sRGB si `True`.
  - `clip` (bool): Coupe les valeurs en dehors des limites de l'espace de couleur si `True`.
- **Retour**: Tableau de pixels en espace de couleur sRGB.

### Classes

#### Classe `Processing`
- **Description**: Classe abstraite pour les objets de traitement d'image.
- **Méthodes**:
  - `compute(self, image, **kwargs)`: Méthode abstraite pour effectuer le traitement sur une image.

#### Classe `tmo_cctf`
- **Description**: Opérateur de mappage de ton basé sur la fonction de transfert cctf.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique le mappage de ton cctf à une image HDR et retourne une image SDR.

#### Classe `exposure`
- **Description**: Opérateur d'exposition.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique un ajustement d'exposition à une image HDR.
  - `auto(self, img)`: Calcule automatiquement la meilleure exposition pour une image HDR.

#### Classe `contrast`
- **Description**: Opérateur de contraste.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique un ajustement de contraste à une image HDR.

#### Classe `clip`
- **Description**: Opérateur de clipping.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique un clipping des valeurs de couleur d'une image HDR.

#### Classe `ColorSpaceTransform`
- **Description**: Opérateur de transformation de l'espace colorimétrique.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Transforme l'espace colorimétrique d'une image HDR.

#### Classe `resize`
- **Description**: Opérateur de redimensionnement.
- **Méthodes**:
  - `compute(self, img, size=(None, None), anti_aliasing=False)`: Redimensionne une image HDR.

#### Classe `Ycurve`
- **Description**: Opérateur de courbe de luminance.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique une courbe de luminance à une image HDR.

#### Classe `saturation`
- **Description**: Opérateur de saturation.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique un ajustement de saturation à une image HDR.

#### Classe `colorEditor`
- **Description**: Opérateur d'édition des couleurs.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique des ajustements de couleur sélectifs à une image HDR.

#### Classe `lightnessMask`
- **Description**: Opérateur de masque de luminance.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique un masque de luminance à une image HDR.

#### Classe `geometry`
- **Description**: Opérateur de transformation géométrique.
- **Méthodes**:
  - `compute(self, img, **kwargs)`: Applique des transformations géométriques à une image HDR.

#### Classe `ProcessPipe`
- **Description**: Pipeline de processus de traitement d'image.
- **Composants**:
  - `originalImage` (hdrCore.image.Image): Image originale.
  - `__inputImage` (hdrCore.image.Image): Image d'entrée.
  - `__outputImage` (hdrCore.image.Image): Image de sortie.
  - `processNodes` ([ProcessNode]): Liste des nœuds de processus.
  - `previewHDR` (bool): Indicateur de prévisualisation HDR.
  - `previewHDR_process` (): Processus de prévisualisation HDR.

- **Méthodes**:
  - `append(self, process, paramDict=None, name=None)`: Ajoute un nœud de processus au pipeline.
  - `getName(self)`: Retourne le nom de l'image d'entrée.
  - `setImage(self, img)`: Définit l'image d'entrée pour le pipeline.
  - `getInputImage(self)`: Retourne l'image d'entrée.
  - `getImage(self, toneMap=True)`: Retourne l'image de sortie avec mappage de ton si spécifié.
  - `compute(self, progress=None)`: Calcule le pipeline de processus.
  - `setParameters(self, id, paramDicts)`: Définit les paramètres pour un nœud de processus.
  - `getParameters(self, id)`: Retourne les paramètres d'un nœud de processus.
  - `getProcessNodeByName(self, name)`: Retourne un nœud de processus par son nom.
  - `updateProcessPipeMetadata(self)`: Met à jour les métadonnées du pipeline de processus.
  - `updateUserMeta(self, tagRootName, meta)`: Met à jour les métadonnées utilisateur.
  - `export(self, dirName, size=None, to=None, progress=None)`: Exporte l'image traitée.

#### Classe `ProcessNode`
- **Description**: Encapsule un objet de traitement pour créer un nœud de processus.
- **Composants**:
  - `name` (str): Nom du nœud de processus.
  - `process` (hdrCore.processing.Processing): Objet de traitement.
  - `params` (dict): Paramètres du nœud de processus.
  - `defaultParams` (dict): Paramètres par défaut du nœud de processus.
  - `requireUpdate` (bool): Indicateur de mise à jour nécessaire.
  - `outputImage` (hdrCore.image.Image): Image de sortie du nœud de processus.

- **Méthodes**:
  - `compute(self, img)`: Calcule le nœud de processus.
  - `condCompute(self, img)`: Calcule conditionnellement le nœud de processus.
  - `setParameters(self, paramDict)`: Définit les paramètres du nœud de processus.
  - `getParameters(self)`: Retourne les paramètres du nœud de processus.
  - `toDict(self)`: Convertit le nœud de processus en dictionnaire.

## Prefs.py

### Classes

#### Classe `Prefs`
- **Description**: La classe `Prefs` gère les préférences de l'application, y compris les chemins des répertoires, les extensions de fichiers d'image prises en charge, les affichages HDR, les tailles de vignettes et les étiquettes.

- **Attributs de Classe**:
  - `prefsFile` (str): Chemin vers le fichier de préférences JSON.
  - `currentDir` (str): Répertoire de travail actuel.
  - `imgExt` (list[str]): Liste des extensions de fichiers d'image prises en charge.
  - `HDRdisplay` (str): Affichage HDR par défaut.
  - `HDRdisplays` (dict): Dictionnaire des affichages HDR disponibles.
  - `extraPath` (str): Chemin vers le répertoire supplémentaire pour stocker les données HDR.
  - `thumbnailPrefix` (str): Préfixe pour les noms de fichiers des vignettes.
  - `thumbnailMaxSize` (int): Taille maximale des vignettes.
  - `tags` (dict[str, dict[str, bool]]): Dictionnaire des étiquettes d'image.
  - `gallerySize` (tuple[int, int]): Taille de la galerie d'images.

- **Méthodes**:
  - `__init__(self: Self) -> None`: Constructeur qui initialise la classe `Prefs`.
  - `load() -> None`: Méthode statique pour charger les préférences à partir d'un fichier JSON.
  - `__str__() -> str`: Méthode statique pour retourner une représentation en chaîne de caractères des préférences.

