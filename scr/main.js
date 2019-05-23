import {PythonShell} from 'python-shell';
 


function include(url) {
        var script = document.createElement('script');
        script.src = url;
        document.getElementsByTagName('head')[0].appendChild(script);
    }



function get_params(form)
{
    alert(form.elements[0].value);
    q = form.elements[0].value;
    let options = {
  	args: [q]
	};
 
	PythonShell.run('parser.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  	console.log('results: %j', results);
  	alert("aa");
  });

}


/*
function include(url) {
        var script = document.createElement('script');
        script.src = url;
        document.getElementsByTagName('head')[0].appendChild(script);
    }

function printer()
{
	alert("i am printer");
}

include("parser.py");

function get_params(form)
{
	alert("aa")
    q = form.elements[0].value;
    alert(q);
    alert(main(q));
    $.ajax({
		type: "GET"
		url: "parser.py"
		data: {param: q}
	}).done(main(q));
}
*/
