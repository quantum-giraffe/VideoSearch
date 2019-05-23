
function scrollTo() {
	var $href = $(this).attr('href');
    var $anchor = $('#'+$href).offset();
	$('body').animate({ scrollTop: $anchor.top });
	return false;
}
