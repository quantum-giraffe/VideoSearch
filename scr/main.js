
function add_results(results) 
{
	for (result in results) {
		$("#result-list").append("<li><a href=\"" + 
			result[0] + "\">" + result[1] + "</a></li>");
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