let baseUrl = "";

window.addEventListener("load", function(){
	baseUrl = window.location.origin;
	getHTML();
}, false)

function getHTML(){
	let thisBody = null;
	fetch(baseUrl +"/theorie/" + data["id"])
	.then(response => response.json())
	.then(body => gotBody(body));
}

function gotBody(body){
	let container = document.getElementById('theorieDisplay');
	console.log(body);
	container.innerHTML = body["html"];
}