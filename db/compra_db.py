from typing import Dict
from datetime import datetime
from pydantic import BaseModel

class CompraInDB(BaseModel):
    compra_id: int = 0
    compra_cliente: int 
    compra_producto: int
    compra_cantProductos: int
    compra_ValorTotal: int

databases_compras = [int, CompraInDB]
databases_compras = { 100: CompraInDB(**{"compra_id": 100,
                                        "compra_cliente": 100000,
                                        "compra_producto": 203,
                                        "compra_cantProductos": 2,
                                        "compra_ValorTotal": 50000
                                        }),
                        110: CompraInDB(**{"compra_id": 110,
                                        "compra_cliente": 100000,
                                        "compra_producto": 230,
                                        "compra_cantProductos": 5,
                                        "compra_ValorTotal": 70000
                                        }) 
                    }

def new_compra(compra: CompraInDB):
    databases_compras[compra.compra_id] = compra
    return compra

def get_compra(llave: int):
    if llave in databases_compras.keys():
        return databases_compras[llave]
    else:
        return None

def obtener_compra_cliente(idcedula: int):
    for i in databases_compras:
        if idcedula == databases_compras[i].compra_cliente:
            return databases_compras[i]
    else:
        return None