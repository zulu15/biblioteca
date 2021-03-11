function reservarLibro(libro,usuario){
    data = {
        "libro":libro,
        "usuario":usuario,
        csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()    
    }
    $.ajax({
        url: "/libro/reservar-libro/",
        data: data,
        type: "POST",
        success:function(response){    
             Swal.fire({
                title:'Buen trabajo!',
                text:response.mensaje,
                icon:'success'
             }).then((result) => {
                window.location.href = "/"
              })
        },
        error:function(response){
            notificarError(response.responseJSON.error);
        }
    })
}