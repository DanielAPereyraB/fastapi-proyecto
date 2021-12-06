<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src = Js.js></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.13.1/build/css/alertify.min.css" />
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.13.1/build/css/themes/default.min.css" />
    <title>Formulario articulo</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar navbar-dark bg-primary">
    <a class="navbar-brand" href="Index.html">Formularios</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="Index.html">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="Cliente.html">Clientes</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="Articulos.html">Articulos</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#">Factura</a>
        </li>
      </ul>
    </div>
  </nav>
  <ul class="nav nav-tabs">
    <li class="nav-item">
      <a class="nav-link active" href="Articulos.html">Formulario</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="TablaC.html">Tabla</a>
    </li>
   
  </ul>
    <div class="container">
        <h3 class="mt-5">Formulario articulo</h3>

      

        <form>
            <div class="row">
              <div class="col">
                  <label for="">id</label>
                  <input id="codigo" type="number" class="form-control" placeholder="Colocar su cedula" > 
                </div>
              <div class="col">
                <label for="">tipo</label>
                <input id="tipo" type="text" class="form-control" placeholder="Colocar su tipo " > 
              </div>
            </div>
            <br>
            <div class="row">
                <div class="col">
                    <label for="">nombre</label>
                    <input id="nombre" type="text" class="form-control" placeholder="Colocar el nombre" > 
                </div>
                <div class="col">
                  <label for="">precio</label>
                  <input id="precio" type="number" class="form-control" placeholder="Colocar el precio" > 
                </div>
              </div>
              <div class="row">
                <div class="col">
                    <label for="">cantidad</label>
                    <input id="cantidad" type="number" class="form-control" placeholder="Colocar el cantidad" > 
                </div>
                <div class="col">
                  <label for="">comentario</label>
                  <input id="comentario" type="text" class="form-control" placeholder="Colocar el comentario" > 
                </div>
              </div>
              <br>
          </form>
    
          <br>
          <button class="btn btn-primary" onclick="guardar()" >Guardar</button>
         
            <a class="btn btn-primary" href="Lista.html">Agregar </a>
       
          <br>
          <br>
        </div>
        <script>
function guardar(){
   

info ={}
info.codigo= document.getElementById('codigo').value;;
info.tipo=document.getElementById('tipo').value;
info.nombre= document.getElementById('nombre').value;
info.precio=document.getElementById('precio').value;
info.cantidad= document.getElementById('cantidad').value;
info.comentario=document.getElementById('comentario').value;

alert(info.comentario);
alertify.confirm("Se agregar a la articulo ",function () {
 guardardatos('http://127.0.0.1:8000/Articulos/agregar','POST',info);   alertify.success('Guardado');
        },function () {
            alertify.error('Cancelado');
          });
}
        </script>
  <script src="Js/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous">
  </script>
  <script src="https://kit.fontawesome.com/f151fc17f0.js" crossorigin="anonymous"></script>
  <script src="//cdn.jsdelivr.net/npm/alertifyjs@1.13.1/build/alertify.min.js"></script>

</body>
</html>