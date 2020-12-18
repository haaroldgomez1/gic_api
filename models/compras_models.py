from pydantic import BaseModel
from datetime import datetime

class NuevaCompraIn(BaseModel):
    compra_id: int
    compra_cliente: int 
    compra_producto: int
    compra_cantProductos: int
    compra_ValorTotal: int

class ConsultarCompraOut(BaseModel):
    compra_id: int
    compra_cliente: int 
    compra_producto: int 
    compra_cantProductos: int
    compra_ValorTotal: int