import sqlite3
from pathlib import Path

from pos.db import conect
from pos.db.conect import ConexionDB


def test_conexiondb_conecta_y_cierra(monkeypatch, tmp_path):
    db_path = tmp_path / "test_data.db"
    monkeypatch.setattr(conect, "DB_PATH", db_path)

    db = ConexionDB()
    conn, cursor = db.conectar()

    assert db.ruta_db == db_path
    assert isinstance(conn, sqlite3.Connection)
    assert cursor is not None

    cursor.execute("CREATE TABLE IF NOT EXISTS ping (id INTEGER PRIMARY KEY)")
    db.commit()
    assert Path(db_path).exists()

    db.cerrar()
