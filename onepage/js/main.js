
jQuery(document).ready(function($) {

  $(".main-menu li").click(function() {
  	var link = $(this).attr('rel');

  	$('html, body').animate({
  		scrollTop: $("#"+link).offset().top
  	}, 400);
  });

});