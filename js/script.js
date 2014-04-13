$(document).ready(function(){
	
	// jQuery code once document loaded
	val = 500;
});

// blink led function
function blink()
{
	// create JSON object
	blink = JSON.stringify({speed: val});

	// create request object
	request = new XMLHttpRequestObject();

	// open server file
	request.open("POST", "filename.py", true);

	// set request header
	request.setRequestHeader("Content-type", "application/json");

	// send data
	request.send(blink);

	// code to display response?*/
}