import json
import uuid


class Transaccion(json.JSONEncoder):
    def __init__(self, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):
        self.transaccion_id = str(uuid.uuid4())
        self.dni_cliente = dni_cliente
        self.tipo_movimiento = tipo_movimiento
        self.monto_movimiento = monto_movimiento
        self.estado = estado
        self.nombre_comercio = nombre_comercio

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def cargar_archivo(self, transaccion):

        archivo = open(f'./data/{self.transaccion_id}.json', "w")
        archivo.write(str(transaccion.toJSON()))
        archivo.close()

    def monto_menor_a_100000(self):
        if self.monto_movimiento < 100000:
            print(f"El movimiento {self.transaccion_id} no requiere justificación")

        else:
            print(f"Se debe solicitar documentación que requiera la justificacion del movimiento {self.transaccion_id}")

    def return_key_tipo_movimiento(self):

        return self.tipo_movimiento