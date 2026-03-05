from pos.core.inventario import Inventario
from pos.db import conect


def test_inventario_crud_basico(monkeypatch, tmp_path):
    db_path = tmp_path / "inventario_test.db"
    monkeypatch.setattr(conect, "DB_PATH", db_path)

    inventario = Inventario()
    try:
        creado = inventario.agregar_producto("P1", "Cafe", 125.0, 10, 90.0, 110.0)
        assert creado is True

        producto = inventario.buscar_producto(id_producto="P1")
        assert producto is not None
        assert producto[0] == "P1"
        assert producto[1] == "Cafe"
        assert float(producto[2]) == 125.0
        assert int(producto[3]) == 10

        listado = inventario.mostrar_productos()
        assert len(listado) == 1

        actualizado = inventario.actualizar_producto("P1", precio=150.0, stock=12)
        assert actualizado is True

        sumar_stock = inventario.añadir_stock("P1", 3)
        assert sumar_stock is True
        producto_actualizado = inventario.buscar_producto(id_producto="P1")
        assert int(producto_actualizado[3]) == 15

        eliminado = inventario.eliminar_producto("P1")
        assert eliminado is True
        assert inventario.buscar_producto(id_producto="P1") is None
    finally:
        inventario.cerrar_db()


def test_inventario_no_duplica_id(monkeypatch, tmp_path):
    db_path = tmp_path / "inventario_unico.db"
    monkeypatch.setattr(conect, "DB_PATH", db_path)

    inventario = Inventario()
    try:
        assert inventario.agregar_producto("P2", "Azucar", 80.0, 5) is True
        assert inventario.agregar_producto("P2", "Azucar", 80.0, 5) is False
    finally:
        inventario.cerrar_db()
