import sqlite3
import logging
from pathlib import Path
import os
import sys

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent


def _resolver_ruta_db() -> Path:
    env_db_path = os.getenv("POS_DB_PATH", "").strip()
    if env_db_path:
        return Path(env_db_path).expanduser()

    if getattr(sys, "frozen", False):
        return Path.home() / ".pos_system" / "data.db"

    return BASE_DIR / "data.db"


DB_PATH = _resolver_ruta_db()


class ConexionDB:
    def __init__(self):
        self.ruta_db = DB_PATH
        self.conn = None
        self.cursor = None

    def conectar(self):
        """Abre la conexión a la base de datos."""
        self.ruta_db.parent.mkdir(parents=True, exist_ok=True)
        logger.debug("Abriendo conexion SQLite en %s", self.ruta_db)
        self.conn = sqlite3.connect(self.ruta_db)
        self.cursor = self.conn.cursor()
        return self.conn, self.cursor

    def commit(self): # con esto guardamos cambios en la db
        """Guarda los cambios."""
        if self.conn:
            self.conn.commit()

    def cerrar(self): #cerramos conexion con db
        """Cierra la conexión."""
        if self.conn:
            self.conn.close()
            logger.debug("Conexion SQLite cerrada")
