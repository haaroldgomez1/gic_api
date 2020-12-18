from fastapi import FastAPI
from fastapi import HTTPException
from db.cliente_db import get_cliente, created_cliente, update_cliente
from db.compra_db import new_compra, get_compra, obtener_compra_cliente
from models.cliente_models import ConsultarClienteIn, CrearActualizarClienteIn, ClienteOut
from models.compras_models import ConsultarCompraOut, NuevaCompraIn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost","http://127.0.0.1:8080","http://127.0.0.1:8000", "http://localhost:8080""https://gicappii.herokuapp.com"]

app.add_middleware(
     CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],   
)
#Funciones De Clientes
@app.get("/clientes/{cli_cedula}")
async def consultar_cliente(cli_cedula: int):
    cliente_in = get_cliente(cli_cedula)
    if cliente_in == None:
        raise HTTPException (status_code=404, detail="El cliente no fue encontrado")
    else:
        cliente_out = ClienteOut(**cliente_in.dict())
        return cliente_out

@app.put("/clientes")
async def actualizar_cliente(cliente: CrearActualizarClienteIn):
    cliente_in = get_cliente(cliente.cli_cedula)
    if cliente_in == None:
        raise HTTPException(status_code=404, detail="El cliente no fue encontrado")
    else:
        update_cliente(cliente)
        cliente_out = ClienteOut(**cliente.dict())
        return cliente_out

@app.post("/clientes")
async def crear_cliente(cliente: CrearActualizarClienteIn):
    cliente_in = get_cliente(cliente.cli_cedula)
    if cliente_in != None:
        raise HTTPException(status_code=404, detail="El cliente ya existe")
    else:
        created_cliente(cliente)
        cliente_out = ClienteOut(**cliente.dict())
        return cliente_out

#Funciones De Clientes
@app.get("/compras/{compra_id}")
async def consultar_compra(compra_id: int):
    compra_in = get_compra(compra_id)
    if compra_in == None:
        raise HTTPException (status_code="404", detail="La compra no se encontro")
    else:
        compra_out = ConsultarCompraOut(**(compra_in.dict()))
        return compra_out

@app.post("/compras/new")
async def nueva_compra(compra: NuevaCompraIn):
    compra_in = get_compra(compra.compra_id)
    if compra_in != None:
        raise HTTPException(status_code=404, detail="La compra ya existe")
    else:
        new_compra(compra)
        compra_out = ConsultarCompraOut(**compra.dict())
        return compra_out, "La compra se añadio"

#Funcion buscar compras por usuario
@app.get("/clientes/{cedula}/compras")
async def get_compra(cedula: int):
    clientedb = get_cliente(cedula)
    if clientedb == None:
        raise HTTPException (status_code=404, detail="cliente no existe")
    compracliente = obtener_compra_cliente(cedula)
    return compracliente
