import os
import sys
from pathlib import Path

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from pos.modulos_ui.ventas.ventas_view import VENTA


os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")


@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture
def venta(qapp):
    widget = QWidget()
    return VENTA(widget)


def test_set_producto_inserta_fila_y_actualiza_totales(venta):
    venta.set_producto(
        {
            "id": "A1",
            "descripcion": "Azucar",
            "precio": 1500,
            "cantidad": 2,
            "total": 3000,
        }
    )

    assert venta.tabla.rowCount() == 1
    assert venta.tabla.item(0, 2).text() == "1.500,00"
    assert venta.tabla.item(0, 4).text() == "3.000,00"
    assert venta.ui_ventas.sub_nro.text() == "3.000,00"
    assert venta.ui_ventas.itbis_nro.text() == "0,00"
    assert venta.ui_ventas.total_nro.text() == "3.000,00"


def test_set_producto_acumula_cantidad_si_id_repetido(venta):
    base = {
        "id": "A1",
        "descripcion": "Azucar",
        "precio": 1000,
        "cantidad": 1,
        "total": 1000,
    }
    venta.set_producto(base)
    venta.set_producto({**base, "cantidad": 2, "total": 2000})

    assert venta.tabla.rowCount() == 1
    assert venta.tabla.item(0, 3).text() == "3"
    assert venta.tabla.item(0, 4).text() == "3.000,00"
    assert venta.ui_ventas.sub_nro.text() == "3.000,00"


def test_solo_columna_cantidad_es_editable(venta):
    venta.set_producto(
        {
            "id": "A1",
            "descripcion": "Arroz",
            "precio": 100,
            "cantidad": 1,
            "total": 100,
        }
    )

    cantidad_flags = venta.tabla.item(0, 3).flags()
    total_flags = venta.tabla.item(0, 4).flags()

    assert bool(cantidad_flags & Qt.ItemFlag.ItemIsEditable)
    assert not bool(total_flags & Qt.ItemFlag.ItemIsEditable)


def test_editar_cantidad_recalcula_total_y_corrige_valor_invalido(venta, qapp):
    venta.set_producto(
        {
            "id": "A1",
            "descripcion": "Leche",
            "precio": 2500,
            "cantidad": 1,
            "total": 2500,
        }
    )

    cantidad_item = venta.tabla.item(0, 3)
    cantidad_item.setText("4")
    qapp.processEvents()

    assert venta.tabla.item(0, 4).text() == "10.000,00"
    assert venta.ui_ventas.sub_nro.text() == "10.000,00"

    cantidad_item.setText("0")
    qapp.processEvents()

    assert venta.tabla.item(0, 3).text() == "1"
    assert venta.tabla.item(0, 4).text() == "2.500,00"
    assert venta.ui_ventas.sub_nro.text() == "2.500,00"


def test_eliminar_fila_seleccionada_actualiza_totales(venta):
    venta.set_producto(
        {
            "id": "A1",
            "descripcion": "Leche",
            "precio": 1000,
            "cantidad": 1,
            "total": 1000,
        }
    )
    venta.set_producto(
        {
            "id": "B2",
            "descripcion": "Pan",
            "precio": 500,
            "cantidad": 2,
            "total": 1000,
        }
    )

    fila_a_eliminar = venta._buscar_fila_por_id("A1")
    venta.tabla.selectRow(fila_a_eliminar)
    venta.ui_ventas.eliminar_articulo.click()

    assert venta.tabla.rowCount() == 1
    assert venta.ui_ventas.sub_nro.text() == "1.000,00"
    assert venta.ui_ventas.total_nro.text() == "1.000,00"


def test_get_producto_usa_consulta_y_limpia_inputs(venta):
    esperado = {
        "id": "Z9",
        "descripcion": "Cafe",
        "precio": 300,
        "cantidad": 2,
        "total": 600,
    }
    venta.consulta.buscar_producto = lambda **kwargs: esperado

    venta.ui_ventas.entry_producto.setText("Z9")
    venta.ui_ventas.entry_cantidad.setText("2")
    venta.ui_ventas.agregar_articulo.click()

    assert venta.tabla.rowCount() == 1
    assert venta.tabla.item(0, 0).text() == "Z9"
    assert venta.ui_ventas.entry_producto.text() == ""
    assert venta.ui_ventas.entry_cantidad.text() == ""
