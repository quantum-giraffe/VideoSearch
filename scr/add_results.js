results = [('http://movies1.fox-fan.ru/video2/mpYl2VyWoOknw2gjLVepwA/1558640143/familyguy/3/ren-tv/301.mp4', 'series', (50,68))]

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