$ = jQuery.noConflict();


function listar_autor(){
    $.ajax({
        "url":"/libro/listar_autor",
        "type":"get",
        "dataType":"json",
        "success": function(response){
            
            if ($.fn.dataTable.isDataTable( '#tabla_autores' )) {
                $('#tabla_autores').DataTable().destroy();
            }

            $("#tabla_autores tbody").html("");


            for(var i = 0; i < response.length; i++){
                fila = "<tr>"
                for(var autor_field in response[i].fields){
                    fila += "<td>"+ response[i].fields[autor_field] +"</td>"
                }
                fila+= "<td><button class='btn btn-primary' onclick='abrir_modal_edicion(\"/libro/editar_autor/"+response[i].pk+"\")'>Editar</button>&nbsp;"
                fila+= "<button class='btn btn-danger' onclick='abrir_modal_eliminacion(\"/libro/eliminar_autor/"+response[i].pk+"\")'>Eliminar</button></td>"
                fila+= "</tr>"
                $("#tabla_autores tbody").append(fila);
            }

            

            $("#tabla_autores").DataTable({
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
        "error":function(error){

        }

    })
}


function editar(){
    $.ajax({
        "url":$("#form_edicion").attr("action"),
        "method":$("#form_edicion").attr("method"),
        "data":$("#form_edicion").serialize(),
        "dataType":"json",
        "success":function(response){
            cerrar_modal_edicion();
            listar_autor();
            notificarExito(response.mensaje);
        },
        "error":function(response){
            notificarError(response.responseJSON.mensaje);
            mostrarErrorEdicion(response);
        }
    })
}


function registrar(){
    $.ajax({
        "url":$("#form_creacion").attr("action"),
        "data":$("#form_creacion").serialize(),
        "dataType":"json",
        "type":$("#form_creacion").attr("method"),
        "success": function(response){
            cerrar_modal_creacion();
            notificarExito(response.mensaje);
            listar_autor();
        },
        "error": function(response){
            notificarError(response.responseJSON.mensaje);
            mostrarErrorCreacion(response);

        }
    })
}


function eliminar(){
    $.ajax({
        "url":$("#form_eliminacion").attr("action"),
        "data":$("#form_eliminacion").serialize(),
        "dataType":"json",
        "type":$("#form_eliminacion").attr("method"),
        "success": function(response){
            cerrar_modal_eliminacion();
            notificarExito(response.mensaje);
            listar_autor();
        },
        "error": function(response){
            notificarError(response.responseJSON.mensaje);
            

        }
    })
}

$(document).ready(function(){
    listar_autor();
})
  