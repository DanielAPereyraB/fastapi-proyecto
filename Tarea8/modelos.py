from pydantic import BaseModel
from typing import List,Optional
class clientes(BaseModel):
    id:int
    cedula:int
    nombre:str
    apellido:str
    correo:str
    rnc:str
    telefono:str

class articulos (BaseModel):
    codigo: int
    tipo :str
    nombre : str
    precio : float
    cantidad : int
    comentario : str

class factura_detalle (BaseModel):
    factura_id:int
    codigo:int
    nombre:str
    precio:float
    cantidad:float
    total:float

class factura (BaseModel):

    id:int
    fecha: str
    cliente_id:int
    Descripcion:str
    Subtotal:float
    Itbis:float
    Total:float
    detalle:List[factura_detalle] = []


