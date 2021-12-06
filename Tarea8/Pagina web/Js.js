async function cargarDatos(url){
   
    let datos = await fetch(url)
    .then(res => res.json())
    .then((data) =>{
        return data
    });
    return datos; 
 }
 async function cargar(url){
     let pokemones = await cargarDatos(url)

     let tablax = document.getElementById('tbody');
         for(let k in pokemones){
             par = pokemones[k]
             tr = document.createElement('tr');
 
             for(let x in par){
                 td = document.createElement('td');
                 td.innerHTML = par[x];
                 tr.appendChild(td);
             }
             tdOpc = document.createElement('td');
             tdOpc.innerHTML = `
             <button class="btn btn-danger" onclick="EliminarDelete(this)"><i class="far fa-trash-alt"></i></button>`;
             tr.appendChild(tdOpc);
 
             tablax.appendChild(tr);
         }     
     
 }

 async function cargard(url){
    let pokemones = await cargarDatos(url)

    let tablax = document.getElementById('tbody');
        for(let k in pokemones){
            par = pokemones[k]
            tr = document.createElement('tr');

            for(let x in par){
                td = document.createElement('td');
                td.innerHTML = par[x];
                tr.appendChild(td);
            }
            tdOpc = document.createElement('td');
            tdOpc.innerHTML = `
            <button class="btn btn-danger" onclick="EliminarDeleted(this)"><i class="far fa-trash-alt"></i></button>`;
            tr.appendChild(tdOpc);

            tablax.appendChild(tr);
        }     
    
}

function EliminarDelete(btn) {

    let fila = btn.parentNode.parentNode;
    let id = fila.firstElementChild.innerHTML;
   
    let url = 'http://127.0.0.1:8000/Clientes/';

    alertify.confirm("Se eliminara el cliente con el ID " + id + "",
        function () {
            fetch(url + id, {
                method: 'DELETE'
            })
                .then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log('Éxito:', response))
                .then(() => location.reload())
            alertify.success('Borrado');
        },
        function () {
            alertify.error('Cancelado');
        });
}
function EliminarDeleted(btn) {

    let fila = btn.parentNode.parentNode;
    let id = fila.firstElementChild.innerHTML;
    
    
    let url = 'http://127.0.0.1:8000/Articulos/';

    alertify.confirm("Se eliminara el articulo con el ID " + id + "",
        function () {
            fetch(url + id, {
                method: 'DELETE'
            })
                .then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log('Éxito:', response))
                .then(() => location.reload())
            alertify.success('Borrado');
        },
        function () {
            alertify.error('Cancelado');
        });
}


    async function guardardatos(url,metodo,data){
            
        await fetch(url, {
          method: metodo,
          body: JSON.stringify(data), 
          headers:{
            'Content-Type': 'application/json'
          }
        }).then(r => r.text()).then(r => {
        
        })
        }
        