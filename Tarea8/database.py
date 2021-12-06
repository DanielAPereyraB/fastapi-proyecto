from peewee import *
from modelos import *

db = SqliteDatabase('database.db')


#tabla cliente
class Clientes(Model):

    cedula= CharField()
    nombre= CharField()
    apellido= CharField()
    correo= CharField()
    rnc= CharField()
    telefono= CharField()
    class Meta:
        database = db 

#tabla articulo
class Articulos(Model):

    codigo = CharField()
    tipo = CharField()
    nombre = CharField()
    precio = FloatField
    cantidad = IntegerField()
    comentario = CharField()
    class Meta:
        database = db 

#tabla factura
class Factura (Model):
    fecha=TextField()
    cliente_id=IntegerField()
    Descripcion = TextField()
    Subtotal=DoubleField()
    Itbis = DoubleField()
    Total = DoubleField()

    class Meta:
        database = db 
   
#tabla detalle factura

class Factura_Detalle (Model):
    factura_id = ForeignKeyField(Factura,backref='detalle')
    codigo=IntegerField()
    nombre= TextField()
    precio=DoubleField()
    cantidad=DoubleField()
    total=DoubleField()

    class Meta:
        database = db 



db.connect()

db.create_tables([Clientes,Articulos,Factura,Factura_Detalle])




#FUNCIONES CLIENTES

def guardarClientes(obj:clientes):
        customers = Clientes()
        customers.cedula = obj.cedula
        customers.nombre = obj.nombre
        customers.apellido = obj.apellido
        customers.correo = obj.correo
        customers.rnc = obj.rnc
        customers.telefono = obj.telefono
        customers.save()  


def cargarClientes():
    clientes = []
    for customers in Clientes.select().dicts():
        clientes.append(customers)
    return clientes
  
def actualizarClientes(obj:clientes):
    customers=Clientes.get(Clientes.cedula == obj.cedula)
    customers.nombre = obj.nombre
    customers.apellido = obj.apellido
    customers.correo = obj.correo
    customers.rnc = obj.rnc
    customers.telefono = obj.telefono
    customers.save()


def eliminarClientes(cedula: int):
    
  customers= Clientes.delete().where(Clientes.cedula == cedula)

  customers.execute()

#FUNCIONES Articulos

def guardarArticulos(obj:articulos):
         Art = Articulos()
         Art.codigo = obj.codigo
         Art.tipo = obj.tipo
         Art.nombre = obj.nombre
         Art.precio = obj.precio
         Art.cantidad = obj.cantidad
         Art.comentario = obj.comentario
         Art.save()

def cargarArticulos():
    articulos = []
    for Art in Articulos.select().dicts():
        articulos.append(Art)
    return articulos
  
def actualizarArticulos(obj:articulos):

    Art=Articulos.get(Articulos.codigo == obj.codigo)
    Art.tipo = obj.tipo
    Art.nombre = obj.nombre
    Art.precio = obj.precio
    Art.cantidad = obj.cantidad
    Art.comentario = obj.comentario
    Art.save()

def eliminarArticulos(codigo: int):
    
  Art=Articulos.delete().where(Articulos.codigo == codigo)
  Art.execute()
  #Funciones factura

def actualizarFactura(obj:factura):
    fac = Factura.get(Factura.id == obj.id)
    fac.fecha= obj.fecha
    fac.cliente_id=obj.cliente_id
    fac.Descripcion =obj.Descripcion
    fac.Subtotal=obj.Subtotal
    fac.Itbis = obj.Itbis
    fac.Total = obj.Total
    obj.detalle
    fac.save()

    for dett in obj.detalle:
        det = Factura_Detalle()
        det.factura_id = dett.factura_id
        det.codigo = dett.codigo
        det.nombre = dett.nombre
        det.precio = dett.precio
        det.cantidad = dett.cantidad
        det.total = dett.total
        det.save()

def cargarFactura():
    factura = []
    for fac in Factura.select().dicts():
        factura.append(fac)
    return factura

def guardarFactura(obj:factura):
    fac = Factura()
    fac.fecha= obj.fecha
    fac.cliente_id=obj.cliente_id
    fac.Descripcion =obj.Descripcion
    fac.Subtotal=obj.Subtotal
    fac.Itbis = obj.Itbis
    fac.Total = obj.Total
    obj.detalle
    fac.save()

    for dett in obj.detalle:
        det = Factura_Detalle()
        det.factura_id = dett.factura_id
        det.codigo = dett.codigo
        det.nombre = dett.nombre
        det.precio = dett.precio
        det.cantidad = dett.cantidad
        det.total = dett.total
        det.save()

def eliminarFactura(id: int):
    
  fac=Factura.delete().where(Factura.id == id)
  fac.execute()   