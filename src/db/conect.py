import sqlite3

class ConexionDB:
    def __init__(self, ruta_db="src/db/data.db"):
        self.nombre_db = ruta_db
        self.conn = None
        self.cursor = None

    def conectar(self):
        """Abre la conexión a la base de datos."""
        self.conn = sqlite3.connect(self.nombre_db)
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
