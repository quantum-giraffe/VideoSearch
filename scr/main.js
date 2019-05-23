
function add_results(results) 
{
	if (results) {
		for (result in results) {
			$("#result-list").append("<li><a href=\"" + 
				result[0] + "\" onclick=\"current_video(" + 
				result + ")\">" + result[1] + "</a></li>");
		}
	}
	else {
		$("#result-list").append("<p class=\"notfind\">Sorry, nothing found</p>")
	}
}

function current_video(result)
{
	$("#video-name").append(result[1]);

	var vid = document.getElementById("thevideo");
	
	vid.src = result[1];
	vid.currentTime = result[2][0];
	
	while (vid.currentTime < result[2][1]);
	if (vid.played) {
		vid.pause();
	} 
}

function get () 
{

}

function scrollTo() {
	var $href = $(this).attr('href');
    var $anchor = $('#'+$href).offset();
	$('body').animate({ scrollTop: $anchor.top });
	return false;
}


#videopage