# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventas.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(684, 537)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.form = QFrame(main)
        self.form.setObjectName(u"form")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.form.sizePolicy().hasHeightForWidth())
        self.form.setSizePolicy(sizePolicy1)
        self.form.setFrameShape(QFrame.Shape.NoFrame)
        self.form.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cliente_label = QLabel(self.form)
        self.cliente_label.setObjectName(u"cliente_label")
        self.cliente_label.setStyleSheet(u"")
        self.cliente_label.setFrameShape(QFrame.Shape.NoFrame)
        self.cliente_label.setFrameShadow(QFrame.Shadow.Plain)
        self.cliente_label.setTextFormat(Qt.TextFormat.AutoText)

        self.gridLayout_2.addWidget(self.cliente_label, 0, 0, 1, 1)

        self.cliente_combo = QComboBox(self.form)
        self.cliente_combo.setObjectName(u"cliente_combo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cliente_combo.sizePolicy().hasHeightForWidth())
        self.cliente_combo.setSizePolicy(sizePolicy2)
        self.cliente_combo.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.cliente_combo.setEditable(True)
        self.cliente_combo.setMaxVisibleItems(5)

        self.gridLayout_2.addWidget(self.cliente_combo, 0, 1, 1, 3)

        self.producto_label = QLabel(self.form)
        self.producto_label.setObjectName(u"producto_label")
        self.producto_label.setStyleSheet(u"font: 16pt \"Sans Serif\";")
        self.producto_label.setFrameShape(QFrame.Shape.NoFrame)
        self.producto_label.setFrameShadow(QFrame.Shadow.Plain)
        self.producto_label.setTextFormat(Qt.TextFormat.AutoText)

        self.gridLayout_2.addWidget(self.producto_label, 0, 4, 1, 2)

        self.entry_producto = QLineEdit(self.form)
        self.entry_producto.setObjectName(u"entry_producto")
        self.entry_producto.setFrame(True)
        self.entry_producto.setDragEnabled(False)
        self.entry_producto.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.gridLayout_2.addWidget(self.entry_producto, 0, 6, 1, 1)

        self.cantidad_label = QLabel(self.form)
        self.cantidad_label.setObjectName(u"cantidad_label")
        self.cantidad_label.setFrameShape(QFrame.Shape.NoFrame)
        self.cantidad_label.setFrameShadow(QFrame.Shadow.Plain)
        self.cantidad_label.setTextFormat(Qt.TextFormat.RichText)
        self.cantidad_label.setWordWrap(False)
        self.cantidad_label.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.cantidad_label, 1, 0, 1, 2)

        self.entry_cantidad = QLineEdit(self.form)
        self.entry_cantidad.setObjectName(u"entry_cantidad")
        sizePolicy2.setHeightForWidth(self.entry_cantidad.sizePolicy().hasHeightForWidth())
        self.entry_cantidad.setSizePolicy(sizePolicy2)
        self.entry_cantidad.setFrame(True)
        self.entry_cantidad.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.gridLayout_2.addWidget(self.entry_cantidad, 1, 2, 1, 2)

        self.stock_label = QLabel(self.form)
        self.stock_label.setObjectName(u"stock_label")
        self.stock_label.setStyleSheet(u"font: 20pt \"Sans Serif\";")
        self.stock_label.setFrameShape(QFrame.Shape.NoFrame)
        self.stock_label.setFrameShadow(QFrame.Shadow.Plain)
        self.stock_label.setTextFormat(Qt.TextFormat.RichText)
        self.stock_label.setWordWrap(False)
        self.stock_label.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.stock_label, 1, 4, 1, 1)

        self.stock = QLabel(self.form)
        self.stock.setObjectName(u"stock")
        self.stock.setStyleSheet(u"font: 20pt \"Sans Serif\";")
        self.stock.setFrameShape(QFrame.Shape.NoFrame)
        self.stock.setFrameShadow(QFrame.Shadow.Plain)
        self.stock.setTextFormat(Qt.TextFormat.RichText)
        self.stock.setWordWrap(True)
        self.stock.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.stock, 1, 5, 1, 2)

        self.factura_label = QLabel(self.form)
        self.factura_label.setObjectName(u"factura_label")
        self.factura_label.setStyleSheet(u"font: 20pt \"Sans Serif\";")
        self.factura_label.setFrameShape(QFrame.Shape.NoFrame)
        self.factura_label.setFrameShadow(QFrame.Shadow.Plain)
        self.factura_label.setTextFormat(Qt.TextFormat.RichText)
        self.factura_label.setWordWrap(False)
        self.factura_label.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.factura_label, 2, 0, 1, 3)

        self.factura = QLabel(self.form)
        self.factura.setObjectName(u"factura")
        self.factura.setStyleSheet(u"font: 20pt \"Sans Serif\";")
        self.factura.setFrameShape(QFrame.Shape.NoFrame)
        self.factura.setFrameShadow(QFrame.Shadow.Plain)
        self.factura.setTextFormat(Qt.TextFormat.RichText)
        self.factura.setWordWrap(True)
        self.factura.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.factura, 2, 3, 1, 1)

        self.accion = QFrame(self.form)
        self.accion.setObjectName(u"accion")
        self.accion.setFrameShape(QFrame.Shape.NoFrame)
        self.accion.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.accion)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.agregar_articulo = QPushButton(self.accion)
        self.agregar_articulo.setObjectName(u"agregar_articulo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.agregar_articulo.sizePolicy().hasHeightForWidth())
        self.agregar_articulo.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.agregar_articulo)

        self.eliminar_articulo = QPushButton(self.accion)
        self.eliminar_articulo.setObjectName(u"eliminar_articulo")
        sizePolicy3.setHeightForWidth(self.eliminar_articulo.sizePolicy().hasHeightForWidth())
        self.eliminar_articulo.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.eliminar_articulo)

        self.editar_articulo = QPushButton(self.accion)
        self.editar_articulo.setObjectName(u"editar_articulo")
        sizePolicy3.setHeightForWidth(self.editar_articulo.sizePolicy().hasHeightForWidth())
        self.editar_articulo.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.editar_articulo)

        self.limpiar_lista = QPushButton(self.accion)
        self.limpiar_lista.setObjectName(u"limpiar_lista")
        sizePolicy3.setHeightForWidth(self.limpiar_lista.sizePolicy().hasHeightForWidth())
        self.limpiar_lista.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.limpiar_lista)

        self.buscar_inventario = QPushButton(self.accion)
        self.buscar_inventario.setObjectName(u"buscar_inventario")
        sizePolicy3.setHeightForWidth(self.buscar_inventario.sizePolicy().hasHeightForWidth())
        self.buscar_inventario.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.buscar_inventario)


        self.gridLayout_2.addWidget(self.accion, 3, 0, 1, 7)


        self.gridLayout.addWidget(self.form, 0, 0, 1, 1)

        self.bottom = QFrame(main)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
        self.bottom.setSizePolicy(sizePolicy1)
        self.bottom.setFrameShape(QFrame.Shape.NoFrame)
        self.bottom.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayout_5 = QGridLayout(self.bottom)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabla_widget = QTableWidget(self.bottom)
        self.tabla_widget.setObjectName(u"tabla_widget")
        self.tabla_widget.setAcceptDrops(True)
        self.tabla_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tabla_widget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tabla_widget.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tabla_widget.setTabKeyNavigation(False)
        self.tabla_widget.setProperty(u"showDropIndicator", False)
        self.tabla_widget.setDragEnabled(True)
        self.tabla_widget.setDragDropOverwriteMode(False)
        self.tabla_widget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.tabla_widget.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.tabla_widget.setAlternatingRowColors(True)
        self.tabla_widget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla_widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
        self.tabla_widget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tabla_widget.setSortingEnabled(True)
        self.tabla_widget.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.gridLayout_5.addWidget(self.tabla_widget, 0, 0, 1, 1)

        self.pago_frame = QFrame(self.bottom)
        self.pago_frame.setObjectName(u"pago_frame")
        self.pago_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.pago_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.pago_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.pago_frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pagar_boton = QPushButton(self.pago_frame)
        self.pagar_boton.setObjectName(u"pagar_boton")
        sizePolicy2.setHeightForWidth(self.pagar_boton.sizePolicy().hasHeightForWidth())
        self.pagar_boton.setSizePolicy(sizePolicy2)
        self.pagar_boton.setStyleSheet(u"font: 20pt \"Sans Serif\";")

        self.gridLayout_3.addWidget(self.pagar_boton, 0, 0, 1, 1)

        self.totales = QFrame(self.pago_frame)
        self.totales.setObjectName(u"totales")
        self.totales.setFrameShape(QFrame.Shape.NoFrame)
        self.totales.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.totales)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sub_total_label = QLabel(self.totales)
        self.sub_total_label.setObjectName(u"sub_total_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sub_total_label.sizePolicy().hasHeightForWidth())
        self.sub_total_label.setSizePolicy(sizePolicy4)
        self.sub_total_label.setStyleSheet(u"font: 16pt \"Sans Serif\";")

        self.gridLayout_4.addWidget(self.sub_total_label, 2, 0, 1, 2)

        self.total_nro = QLabel(self.totales)
        self.total_nro.setObjectName(u"total_nro")
        sizePolicy4.setHeightForWidth(self.total_nro.sizePolicy().hasHeightForWidth())
        self.total_nro.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.total_nro.setFont(font)
        self.total_nro.setStyleSheet(u"font: 16pt \"Sans Serif\";")
        self.total_nro.setWordWrap(True)

        self.gridLayout_4.addWidget(self.total_nro, 0, 1, 1, 5)

        self.itebis_nro = QLabel(self.totales)
        self.itebis_nro.setObjectName(u"itebis_nro")
        sizePolicy4.setHeightForWidth(self.itebis_nro.sizePolicy().hasHeightForWidth())
        self.itebis_nro.setSizePolicy(sizePolicy4)
        self.itebis_nro.setStyleSheet(u"font: 16pt \"Sans Serif\";")
        self.itebis_nro.setWordWrap(True)

        self.gridLayout_4.addWidget(self.itebis_nro, 3, 1, 1, 5)

        self.itebis_label = QLabel(self.totales)
        self.itebis_label.setObjectName(u"itebis_label")
        self.itebis_label.setStyleSheet(u"font: 16pt \"Sans Serif\";")

        self.gridLayout_4.addWidget(self.itebis_label, 3, 0, 1, 1)

        self.total_label = QLabel(self.totales)
        self.total_label.setObjectName(u"total_label")
        sizePolicy4.setHeightForWidth(self.total_label.sizePolicy().hasHeightForWidth())
        self.total_label.setSizePolicy(sizePolicy4)
        self.total_label.setFont(font)
        self.total_label.setStyleSheet(u"font: 16pt \"Sans Serif\";")

        self.gridLayout_4.addWidget(self.total_label, 0, 0, 1, 1)

        self.sub_nro = QLabel(self.totales)
        self.sub_nro.setObjectName(u"sub_nro")
        sizePolicy4.setHeightForWidth(self.sub_nro.sizePolicy().hasHeightForWidth())
        self.sub_nro.setSizePolicy(sizePolicy4)
        self.sub_nro.setStyleSheet(u"font: 16pt \"Sans Serif\";")
        self.sub_nro.setWordWrap(True)

        self.gridLayout_4.addWidget(self.sub_nro, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.totales, 0, 1, 2, 1)


        self.gridLayout_5.addWidget(self.pago_frame, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.bottom, 1, 0, 1, 1)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Form", None))
        self.cliente_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Cliente:</span></p></body></html>", None))
        self.cliente_combo.setCurrentText(QCoreApplication.translate("main", u"default", None))
        self.producto_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">Producto:</span></p></body></html>", None))
        self.entry_producto.setInputMask("")
        self.entry_producto.setText("")
        self.entry_producto.setPlaceholderText(QCoreApplication.translate("main", u"buscar por id", None))
        self.cantidad_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Cantidad: </span></p></body></html>", None))
        self.entry_cantidad.setInputMask("")
        self.entry_cantidad.setText("")
        self.entry_cantidad.setPlaceholderText(QCoreApplication.translate("main", u"Cantidad", None))
        self.stock_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Stock:</span></p></body></html>", None))
        self.stock.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">0</span></p></body></html>", None))
        self.factura_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Nro de Factura:</span></p></body></html>", None))
        self.factura.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">0</span></p></body></html>", None))
        self.agregar_articulo.setText(QCoreApplication.translate("main", u"Agregar Articulo", None))
        self.eliminar_articulo.setText(QCoreApplication.translate("main", u"Eliminar Articulo", None))
        self.editar_articulo.setText(QCoreApplication.translate("main", u"Editar Articulo", None))
        self.limpiar_lista.setText(QCoreApplication.translate("main", u"Limpiar Lista", None))
        self.buscar_inventario.setText(QCoreApplication.translate("main", u"Buscar Inventario", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"Ventas Realizadas", None))
        self.pagar_boton.setText(QCoreApplication.translate("main", u"Pagar", None))
        self.sub_total_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">Sub Total:</span></p></body></html>", None))
        self.total_nro.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">0</span></p></body></html>", None))
        self.itebis_nro.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">0</span></p></body></html>", None))
        self.itebis_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">Itebis:</span></p></body></html>", None))
        self.total_label.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">Total:</span></p></body></html>", None))
        self.sub_nro.setText(QCoreApplication.translate("main", u"<html><head/><body><p><span style=\" font-weight:700;\">0</span></p></body></html>", None))
    # retranslateUi

