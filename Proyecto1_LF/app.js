
const datosobtenidos = document.getElementById('datos')

var texto = document.getElementsByName("Input")

var opciones = document.getElementsByClassName("opciones")

var lista1 = document.getElementsByClassName("lista")

var datos = []
var capturado

var evento1 = "info"
var evento2 = "entrada"

var boton
if(document.getElementById(evento1)){
    
    var boton = document.getElementById("info").onclick = mostrar_datos;
}

else if(document.getElementById(evento2)){
    var boton = document.getElementById("entrada").onclick = mostrar_archivo;

}



//var boton = document.getElementById("entrada").onclick = mostrar_archivo;


function mostrar_datos(){
    
    for(var i=0; i<texto.length; i++){
        console.log(texto[i].value)
        datos.push(texto[i].value)

    }
    var id1 = 1

    for(var i=0; i<opciones.length; i++){
        var op = document.getElementsByName(id1)
       

        for(var x=0; x<op.length; x++){
            if (op[x].checked){
                console.log(op[x].value)
                datos.push(op[x].value)
            }
        }
        
        id1 = id1 + 1
    }
    var id2 = 1
    for(var i=0; i<lista1.length; i++){
        var lista = document.getElementById(id2);

        var indiceSeleccionado = lista.selectedIndex;

        var opcionSeleccionada = lista.options[indiceSeleccionado];

        var textoSeleccionado = opcionSeleccionada.text;

        var valor = opcionSeleccionada.value;

        console.log(valor)
        datos.push(valor)
        id2 = id2 + 1
    }
    
    for(var i=0; i<datos.length; i++){
        capturado+=datos[i]
        capturado+="\n"

    }


    let html = `
    <div class="modal" tabindex="-1" id="modalexample">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="Datos obtenidos">Modal title</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>${capturado}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>`

    datosobtenidos.innerHTML = html
    var model = document.getElementById("modalexample");
    model.classList.toggle("show")
    
    //popup.classList.toggle("show");
    
    alert(capturado)
    capturado = ""

  
}

function mostrar_archivo(){

    console.log("hola")

}