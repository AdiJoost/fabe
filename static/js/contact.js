let baseUrl = "";
let messageSwitch = 0;

window.addEventListener("load", function(){
	baseUrl = window.location.origin;
	setupButtons();
}, false)

function setupButtons(){
	let submit = document.getElementById('contactButton');
	submit.addEventListener("click", function(){
		if (messageSwitch < 3){
			sendMessage();
		} else {
			alert("Bitte sende nicht zu viele Nachrichten auf einmal.")
		}
	}, false)
}

function sendMessage(){
	fetch(baseUrl + "/sendMail",{
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({
			"name": document.getElementById('contactName').value,
			"email": document.getElementById('contactMail').value,
			"subject": document.getElementById('contactSubject').value,
			"text": document.getElementById('contactMessage').value
		})
	})
	.then(response => response.json())
	.then(body => gotBody(body));
}

function gotBody(body){
	alert(body["message"]);
	messageSwitch += 1;
}


