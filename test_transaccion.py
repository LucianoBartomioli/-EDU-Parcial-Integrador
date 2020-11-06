from transaccion import Transaccion
import json


def creacion_de_archivo():

    transaccion_a = Transaccion(45990339, "CONSUMO", 2000, "RECHAZADO", "MUSIMUNDO")
    transaccion_b = Transaccion(45990339, "CONSUMO", 2000, "APROBADO", "MUSIMUNDO")
    transaccion_c = Transaccion(30949303, "CASH_IN", 50000, "APROBADO", "PAGOFACIL")
    transaccion_a.cargar_archivo(transaccion_a)
    transaccion_b.cargar_archivo(transaccion_b)
    transaccion_c.cargar_archivo(transaccion_c)


def test_monto_movimiento():
    transaccion_a = Transaccion(dni_cliente=45990339, tipo_movimiento="CONSUMO", monto_movimiento=200000, estado="APROBADO", nombre_comercio="DISCO")
    transaccion_a.monto_menor_a_100000()


def test_json_movimiento():
    transaccion_a = Transaccion(30949303, "CASH_IN", 500, "APROBADO", "PAGOFACIL")
    movimiento_to_dict = json.loads(transaccion_a.toJSON())

    keys = movimiento_to_dict.keys()
    items = movimiento_to_dict.values()
    print()
    print(f"Las keys son: {keys}")
    print()
    print(f"Los items son: {items}")
    print()
    key_tipo_movimiento = transaccion_a.return_key_tipo_movimiento()
    print(f"El tipo de movimiento es {key_tipo_movimiento}")


creacion_de_archivo()
test_monto_movimiento()
test_json_movimiento()
