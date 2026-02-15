import sqlite3
from db.conect import ConexionDB


class Inventario:
    def __init__(self):
        self.db = ConexionDB()
        self.con, self.consulta = self.db.conectar()
        self.crear_tabla()

    # -------------------------
    # CREAR TABLA
    # -------------------------
    def crear_tabla(self):
        try:
            self.consulta.execute("""
                CREATE TABLE IF NOT EXISTS productos(
                    id TEXT PRIMARY KEY NOT NULL,
                    descripcion TEXT NOT NULL,
                    precio REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    costo REAL,
                    mayoreo REAL
                )
            """)
            self.con.commit()
        except sqlite3.Error as err:
            print("Error creando tabla:", err)

    # -------------------------
    # CREATE
    # -------------------------
    def agregar_producto(self, id_producto, descripcion, precio, stock, costo=0, mayoreo=0):
        try:
            if self.existe_producto(id_producto):
                return False

            self.consulta.execute("""
                INSERT INTO productos (id, descripcion, precio, stock, costo, mayoreo)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (id_producto, descripcion, precio, stock, costo, mayoreo))

            self.con.commit()
            return True

        except sqlite3.IntegrityError:
            return False
        except sqlite3.Error as err:
            print("Error agregando producto:", err)
            return False

    # -------------------------
    # READ
    # -------------------------
    def buscar_producto(self, id_producto=None, descripcion=None):
        try:
            if descripcion:
                patron = f"%{descripcion}%"
                self.consulta.execute(
                    "SELECT * FROM productos WHERE descripcion LIKE ?",
                    (patron,)
                )
                return self.consulta.fetchall()

            if id_producto:
                self.consulta.execute(
                    "SELECT * FROM productos WHERE id = ?",
                    (id_producto,)
                )
                return self.consulta.fetchone()

            return None

        except sqlite3.Error as err:
            print("Error buscando producto:", err)
            return None

    def mostrar_productos(self):
        try:
            self.consulta.execute("SELECT * FROM productos")
            return self.consulta.fetchall()
        except sqlite3.Error as err:
            print("Error mostrando productos:", err)
            return []

    # -------------------------
    # VALIDACIÓN
    # -------------------------
    def existe_producto(self, id_producto):
        try:
            self.consulta.execute(
                "SELECT 1 FROM productos WHERE id = ?",
                (id_producto,)
            )
            return self.consulta.fetchone() is not None
        except sqlite3.Error:
            return False

    # -------------------------
    # UPDATE DINÁMICO
    # -------------------------
    def actualizar_producto(self, id_producto, **campos):

        if not self.existe_producto(id_producto):
            return False

        if not campos:
            return False

        campos_validos = {"descripcion", "precio", "stock", "costo", "mayoreo"}

        columnas = []
        valores = []

        for campo, valor in campos.items():
            if campo in campos_validos:
                columnas.append(f"{campo} = ?")
                valores.append(valor)

        if not columnas:
            return False

        valores.append(id_producto)

        sql = f"""
            UPDATE productos
            SET {', '.join(columnas)}
            WHERE id = ?
        """

        try:
            self.consulta.execute(sql, valores)
            self.con.commit()
            return True
        except sqlite3.Error as err:
            print("Error actualizando producto:", err)
            return False

    # -------------------------
    # UPDATE STOCK
    # -------------------------
    def añadir_stock(self, id_producto, cantidad):
        if cantidad <= 0:
            return False

        if not self.existe_producto(id_producto):
            return False

        try:
            self.consulta.execute(
                "UPDATE productos SET stock = stock + ? WHERE id = ?",
                (cantidad, id_producto)
            )
            self.con.commit()
            return True
        except sqlite3.Error as err:
            print("Error añadiendo stock:", err)
            return False

    # -------------------------
    # DELETE
    # -------------------------
    def eliminar_producto(self, id_producto):
        if not self.existe_producto(id_producto):
            return False

        try:
            self.consulta.execute(
                "DELETE FROM productos WHERE id = ?",
                (id_producto,)
            )
            self.con.commit()
            return True
        except sqlite3.Error as err:
            print("Error eliminando producto:", err)
            return False

    # -------------------------
    # CERRAR CONEXIÓN
    # -------------------------
    def cerrar_db(self):
        self.db.cerrar()
