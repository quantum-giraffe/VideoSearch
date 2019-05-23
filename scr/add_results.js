results = [["http://movies1.fox-fan.ru/video2/mpYl2VyWoOknw2gjLVepwA/1558640143/familyguy/3/ren-tv/301.mp4", 'series', [50,68]],
['http://movies5.fox-fan.ru/video2/iO0AaOnZzk4GAavj4sOB0A/1558654902/familyguy/3/original/302.mp4', 'series2', [1291.0,1294.0]]]

function current_video(scr, name, time0, time1)
{
	$("#video-name").replaceWith('<p id="video-name">' + name + '</p>');

	var vid = document.getElementById("thevideo");
	
	vid.src = scr;
	vid.currentTime = time0;
	vid.play()
	
/*	if (vid.played) while (vid.currentTime < time1);
	if (vid.played) {
		vid.pause();
	} 
*/
}

if (results.length > 0) {
		for (i in results) {
			$("#result-list").append("<li><button onclick='current_video(\"" + 
				results[i][0] + "\", \"" + results[i][1] + "\", " + 
				results[i][2] +  ")'>" + results[i][1] + "</a></li>");
		}
	}
	else {
		$("#result-list").append("<p class='notfind'>Sorry, nothing found</p>")
	}