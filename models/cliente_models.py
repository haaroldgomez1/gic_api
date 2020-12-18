from pydantic import BaseModel

class CrearActualizarClienteIn(BaseModel):
    cli_cedula: int
    cli_nombre: str
    cli_telefono: int
    cli_correo: str
    cli_direccion: str
    cli_ciudad: str

class ConsultarClienteIn(BaseModel):
    cli_cedula: int

class ClienteOut(BaseModel):
    cli_cedula: int 
    cli_nombre: str
    cli_telefono: int
    cli_correo: str
    cli_direccion: str
    cli_ciudad: str