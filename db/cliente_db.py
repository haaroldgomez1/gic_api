from pydantic import BaseModel
from typing import Dict

class ClienteInDB(BaseModel):
    cli_cedula: int = 0
    cli_nombre: str
    cli_telefono: int
    cli_correo: str
    cli_direccion: str
    cli_ciudad: str

database_clientes = Dict[int, ClienteInDB]
database_clientes = {
    100000: ClienteInDB(**{"cli_cedula":100000,
                            "cli_nombre":"Camilo Mendez",
                            "cli_telefono": 123456789,
                            "cli_correo": "camilo24@email.com",
                            "cli_direccion": "Cra 25 #34-16",
                            "cli_ciudad": "Pereira"}),
    100001: ClienteInDB(**{"cli_cedula":100001,
                            "cli_nombre":"Andres Castrillon",
                            "cli_telefono": 123456789,
                            "cli_correo": "andres18@email.com",
                            "cli_direccion": "Clle 18 #2-84",
                            "cli_ciudad": "Tolima"}),
}

def created_cliente(cliente: ClienteInDB):
    database_clientes[cliente.cli_cedula] = cliente
    return cliente

def update_cliente(cliente: ClienteInDB):
    database_clientes [cliente.cli_cedula] = cliente
    return cliente

def get_cliente(cedula: int):
    if cedula in database_clientes.keys():
        return database_clientes[cedula]
    else:
        return None
    