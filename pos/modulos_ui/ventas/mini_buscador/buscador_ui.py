# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscador.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_buscador(object):
    def setupUi(self, buscador):
        if not buscador.objectName():
            buscador.setObjectName(u"buscador")
        buscador.setWindowModality(Qt.WindowModality.ApplicationModal)
        buscador.resize(628, 572)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(buscador.sizePolicy().hasHeightForWidth())
        buscador.setSizePolicy(sizePolicy)
        buscador.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        buscador.setSizeGripEnabled(False)
        buscador.setModal(False)
        self.verticalLayout = QVBoxLayout(buscador)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_busqueda = QLabel(buscador)
        self.label_busqueda.setObjectName(u"label_busqueda")
        self.label_busqueda.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_busqueda.setAutoFillBackground(False)
        self.label_busqueda.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.47541 rgba(0, 134, 102, 255), stop:0.928962 rgba(255, 255, 255, 255));")
        self.label_busqueda.setMargin(1)
        self.label_busqueda.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.label_busqueda)

        self.entry_busqueda = QLineEdit(buscador)
        self.entry_busqueda.setObjectName(u"entry_busqueda")
        self.entry_busqueda.setStyleSheet(u"")
        self.entry_busqueda.setFrame(False)

        self.verticalLayout.addWidget(self.entry_busqueda)

        self.tabla = QTableView(buscador)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setAutoFillBackground(False)
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla.setTabKeyNavigation(False)
        self.tabla.setProperty(u"showDropIndicator", False)
        self.tabla.setDragDropOverwriteMode(False)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.frame = QFrame(buscador)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.aceptar = QPushButton(self.frame)
        self.aceptar.setObjectName(u"aceptar")

        self.horizontalLayout.addWidget(self.aceptar)

        self.cancelar = QPushButton(self.frame)
        self.cancelar.setObjectName(u"cancelar")

        self.horizontalLayout.addWidget(self.cancelar)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(buscador)

        QMetaObject.connectSlotsByName(buscador)
    # setupUi

    def retranslateUi(self, buscador):
        buscador.setWindowTitle(QCoreApplication.translate("buscador", u"Buscar", None))
        self.label_busqueda.setText(QCoreApplication.translate("buscador", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">BUSQUEDA</span></p></body></html>", None))
        self.entry_busqueda.setPlaceholderText(QCoreApplication.translate("buscador", u"Buscar un producto", None))
        self.aceptar.setText(QCoreApplication.translate("buscador", u"\u2705 ENTER - Aceptar", None))
        self.cancelar.setText(QCoreApplication.translate("buscador", u"\u274c ESC - Cancelar", None))
    # retranslateUi

