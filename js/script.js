$(document).ready(function(){
	
	// jQuery code once document loaded
	val = 500;
});

// blink led function
function myFunction()
{
	// create JSON object
	json = JSON.stringify({ x: val});

	obj = JSON.parse(json);

	alert(obj.x);
	/*
	// create request object
	request = new XMLHttpRequestObject();

	// open server file
	////request.open("POST", "filename.py", true);

	// set request header
	request.setRequestHeader("Content-type", "application/json");

	// send data
	request.send(str_json);

	// code to display response?*/
}