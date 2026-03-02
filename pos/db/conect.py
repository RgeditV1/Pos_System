import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
# 4. Construimos la ruta hacia la base de datos
DB_PATH = BASE_DIR / "data.db"
class ConexionDB:
    def __init__(self):
        self.ruta_db = DB_PATH
        self.conn = None
        self.cursor = None

    def conectar(self):
        """Abre la conexión a la base de datos."""
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
