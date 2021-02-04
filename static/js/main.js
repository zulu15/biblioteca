$ = jQuery.noConflict();

jQuery(document).ready(function($) {

	"use strict";

	[].slice.call( document.querySelectorAll( 'select.cs-select' ) ).forEach( function(el) {
		new SelectFx(el);
	});

	jQuery('.selectpicker').selectpicker;




	$('.search-trigger').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').addClass('open');
	});

	$('.search-close').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').removeClass('open');
	});

	$('.equal-height').matchHeight({
		property: 'max-height'
	});

	// var chartsheight = $('.flotRealtime2').height();
	// $('.traffic-chart').css('height', chartsheight-122);


	// Counter Number
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 3000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});




	// Menu Trigger
	$('#menuToggle').on('click', function(event) {
		var windowWidth = $(window).width();
		if (windowWidth<1010) {
			$('body').removeClass('open');
			if (windowWidth<760){
				$('#left-panel').slideToggle();
			} else {
				$('#left-panel').toggleClass('open-menu');
			}
		} else {
			$('body').toggleClass('open');
			$('#left-panel').removeClass('open-menu');
		}

	});


	$(".menu-item-has-children.dropdown").each(function() {
		$(this).on('click', function() {
			var $temp_text = $(this).children('.dropdown-toggle').html();
			$(this).children('.sub-menu').prepend('<li class="subtitle">' + $temp_text + '</li>');
		});
	});


	// Load Resize
	$(window).on("load resize", function(event) {
		var windowWidth = $(window).width();
		if (windowWidth<1010) {
			$('body').addClass('small-device');
		} else {
			$('body').removeClass('small-device');
		}

	});


});


function abrir_modal_creacion(url){
	$("#creacion").load(url, function(){
		$(this).modal('show');
	});
}


function abrir_modal_edicion(url){
	$("#edicion").load(url, function(){
		$(this).modal('show');
	});
}


function cerrar_modal_creacion(){
	$("#creacion").modal('hide');
}

function abrir_modal_edicion(url){
	$("#edicion").load(url, function(){
		$(this).modal('show');
	});
}


function cerrar_modal_edicion(){
	$("#edicion").modal('hide');
}

function abrir_modal_eliminacion(url){
	$("#eliminacion").load(url, function(){
		$(this).modal('show');
	});
}


function cerrar_modal_eliminacion(){
	$("#eliminacion").modal('hide');
}



function mostrarErrorCreacion(errores){
	//Limpiamos los errores
	$("div.alert").remove();

	for(var error in errores.responseJSON.error){
			$('#form_creacion #'+error).after('<div class="alert alert-danger" role="alert">'+errores.responseJSON.error[error]+'</div>');
	}


}


function mostrarErrorEdicion(errores){
	//Limpiamos los errores
	$('#form_edicion').find('input').each(function(){
			if(this.id){
					$(this).next("div").remove();
			}

	});

	for(var error in errores.responseJSON.error){
		$('#form_edicion #'+error).after('<div class="alert alert-danger" role="alert">'+errores.responseJSON.error[error]+'</div>');

	}
}

function notificarError(error){
	Swal.fire({
		icon: 'error',
		title: 'Error...',
		text: error
	})
}


function notificarExito(mensaje){
	Swal.fire(
		'Buen trabajo!',
		 mensaje,
		'success'
	)
}
