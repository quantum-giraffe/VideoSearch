function include(url) {
        var script = document.createElement('script');
        script.src = url;
        document.getElementsByTagName('head')[0].appendChild(script);
    }

include("parser.py")

$.ajax({
	type: "GET"
	url: "parser.py"
	data: q
})

function get_params(form)
{
    q = form.elements[0].value;
    $.ajax({
		type: "GET"
		url: "parser.py"
		data: {param: q}
	}).done(main(q));
}



