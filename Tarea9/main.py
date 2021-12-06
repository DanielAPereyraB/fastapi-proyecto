from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from modelos import *
import database 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
      title="Dia de pokemones",
    description="Programa de CRUD de pokemones",
    version="2020.9992",
)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Cliente

@app.post("/Clientes/agregar", tags=['Clientes'])
def agregar_Clientes(customers: clientes):
    database.guardarClientes(customers)
    return {"Mensaje": "Se guardo el clientes"}


@app.put("/Clientes/Actualizar", tags=['Clientes'])
def actualizar_Clientes(customers: clientes):
    database.actualizarClientes(customers)
    return {"Mensaje": "Se actualizar el clientes"}


@app.get("/Clientes/Listado", tags=['Clientes'])
def lista_Clientes():
    tmp = database.cargarClientes()
    return tmp

@app.delete("/Clientes/{cedula}", tags=['Clientes'])
def eliminar_Clientes(cedula: int):
    database.eliminarClientes(cedula)
    return {"Mensaje": "Se elimino el clientes"}  

#Articulos

@app.post("/Articulos/agregar", tags=['Articulos'])
def agregar_Articulos(Art: articulos):
    database.guardarArticulos(Art)
    return {"Mensaje": "Se guardo el articulos"}


@app.put("/Articulos/Actualizar", tags=['Articulos'])
def actualizar_Articulos(Art: articulos):
    database.actualizarArticulos(Art)
    return {"Mensaje": "Se actualizar el articulos"}


@app.get("/Articulos/Listado", tags=['Articulos'])
def lista_Articulos():
    tmp = database.cargarArticulos()
    return tmp

@app.delete("/Articulos/{codigo}", tags=['Articulos'])
def eliminar_Articulos(codigo: int):
    database.eliminarArticulos(codigo)
    return {"Mensaje": "Se elimino el articulos"}  

   
 #Factura

@app.post("/Factura/agregar", tags=['Factura'])
def agregar_Factura(Fac: factura):
    database.guardarFactura(Fac)
    return {"Mensaje": "Se guardo el factura" + str(len(Fac.detalle))}


@app.put("/Factura/Actualizar", tags=['Factura'])
def actualizar_Factura(Fac: factura):
    database.actualizarFactura(Fac)
    return {"Mensaje": "Se actualizar el factura"}


@app.get("/Factura/Listado", tags=['Factura'])
def lista_Factura():
    tmp = database.cargarFactura()
    return tmp

@app.delete("/Factura/Listado", tags=['Factura'])
def eliminar_Factura(id: int):
    database.eliminarFactura(id)
    return {"Mensaje": "Se elimino el factura"}  