$ = jQuery.noConflict();

function listadoUsuario(){

  if ($.fn.dataTable.isDataTable( '#tabla_usuarios' )) {
      $('#tabla_usuarios').DataTable().destroy();
  }

  $.ajax({
    'url':'/usuario/listar_usuario/',
    'type':'get',
    'dataType':'json',
    'success': function(response){

      $("#tabla_usuarios tbody").html("");


      for(i = 0; i< response.length; i++){
        fila = "<tr>"
        fila+= "<td>"+response[i].fields["username"]+"</td>"
        fila+= "<td>"+response[i].fields["email"]+"</td>"
        fila+= "<td>"+response[i].fields["nombres"]+"</td>"
        fila+= "<td>"+response[i].fields["apellidos"]+"</td>"
        fila+= "<td>"+response[i].fields["is_admin"]+"</td>"
        fila+= "<td><button type='button' class='btn btn-primary' onclick='abrir_modal_edicion(\"/usuario/editar_usuario/"+response[i]["pk"]+"\")'>Editar</button>&nbsp;&nbsp;"
        fila+= "<button type='button' class='btn btn-danger' onclick='abrir_modal_eliminacion(\"/usuario/eliminar_usuario/"+response[i]["pk"]+"\")'>Eliminar</button></td>"
        fila+="</tr>"
        $("#tabla_usuarios tbody").append(fila)
      }

      $("#tabla_usuarios").DataTable({
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
    'error': function(error){

    }

  })

}



function registrar(){
	$.ajax({
		'url':$("#form_creacion").attr("action"),
		'type':$("#form_creacion").attr("method"),
		'data':$("#form_creacion").serialize(),
		'dataType':'json',
		'success': function(response){
      cerrar_modal_creacion();
      notificarExito(response.mensaje);
			listadoUsuario();
		},
		'error': function(error){
      notificarError(error.responseJSON.mensaje);
			mostrarErrorCreacion(error);

		}
	})
}

function editar(){
	$.ajax({
		'url':$("#form_edicion").attr("action"),
		'type':$("#form_edicion").attr("method"),
		'data':$("#form_edicion").serialize(),
		'dataType':'json',
		'success': function(response){
      cerrar_modal_edicion();
      notificarExito(response.mensaje);
			listadoUsuario();
		},
		'error': function(error){
      notificarError(error.responseJSON.mensaje);
			mostrarErrorEdicion(error);

		}
	})
}

function eliminar(){
	$.ajax({
		'url':$("#form_eliminacion").attr("action"),
		'type':$("#form_eliminacion").attr("method"),
		'data':$("#form_eliminacion").serialize(),
		'dataType':'json',
		'success': function(response){
      cerrar_modal_eliminacion();
      notificarExito(response.mensaje);
			listadoUsuario();
		},
		'error': function(error){
      notificarError(error.responseJSON.error);

		}
	})
}


$(document).ready(function(){
  listadoUsuario();
})
