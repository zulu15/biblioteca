
function listar_libros(){
    $.ajax({
        "url":"/libro/listar_libro",
        "type":"get",
        "dataType":"json",
        "success":function(response){

            if ($.fn.dataTable.isDataTable( '#tabla_libros' )) {
                $('#tabla_libros').DataTable().destroy();
            }

            $("#tabla_libros tbody").html("");
            
            for(var i = 0; i< response.length; i++){
                var fila = "<tr>"
                for(var field in response[i].fields ){
                    var columna = "<td>"+response[i].fields[field]+"</td>"     
                    fila += columna;
                }
                fila+= "<td><button class='btn btn-primary' onclick='abrir_modal_edicion(\"/libro/editar_libro/"+response[i].pk+"\")'>Editar</button>&nbsp;"
                fila+= "<button class='btn btn-danger' onclick='abrir_modal_eliminacion(\"/libro/eliminar_libro/"+response[i].pk+"\")'>Eliminar</button></td>"
                fila += "</tr>"
                $("#tabla_libros tbody").append(fila);
            }

            $("#tabla_libros").DataTable({
                language : {
                 "processing": "Procesando...",
                 "lengthMenu": "Mostrar _MENU_ registros",
                 "zeroRecords": "No se encontraron resultados",
                 "emptyTable": "Ningún dato disponible en esta tabla",
                 "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                 "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
                 "infoFiltered": "(filtrado de un total de _MAX_ registros)",
                 "search": "Buscar:",
                 "infoThousands": ",",
                 "loadingRecords": "Cargando...",
                 "paginate": {
                     "first": "Primero",
                     "last": "Último",
                     "next": "Siguiente",
                     "previous": "Anterior"
                 },
                 "aria": {
                     "sortAscending": ": Activar para ordenar la columna de manera ascendente",
                     "sortDescending": ": Activar para ordenar la columna de manera descendente"
                 },
               }
              });

        },
        "error": function(error){
            console.log(error);

        }
    })

}



function registrar(){
    $.ajax({
        "url":$("#form_creacion").attr("action"),
        "type":$("#form_creacion").attr("method"),
        "data":$("#form_creacion").serialize(),
        "dataType":"json",
        "success":function(response){
            cerrar_modal_creacion();
            listar_libros();
            notificarExito(response.mensaje);
        },
        "error":function(error){
            notificarError(error.responseJSON.mensaje);
            mostrarErrorCreacion(error);
        }

    })
}


function editar(){
    $.ajax({
        "url":$("#form_edicion").attr("action"),
        "type":$("#form_edicion").attr("method"),
        "data":$("#form_edicion").serialize(),
        "dataType":"json",
        "success":function(response){
            cerrar_modal_edicion();
            listar_libros();
            notificarExito(response.mensaje);
        },
        "error":function(error){
            notificarError(error.responseJSON.mensaje);
            mostrarErrorEdicion(error);
        }

    })
}


function eliminar(){
    $.ajax({
        "url":$("#form_eliminacion").attr("action"),
        "type":$("#form_eliminacion").attr("method"),
        "data":$("#form_eliminacion").serialize(),
        "dataType":"json",
        "success": function(response){
            cerrar_modal_eliminacion();
            listar_libros();
            notificarExito(response.mensaje);
        },
        "error":function(error){
            notificarError(error.responseJSON.mensaje)
        }


    })
}




$(document).ready(function(){
    listar_libros();

})




