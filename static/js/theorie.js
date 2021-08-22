let baseUrl = "";

window.addEventListener("load", function(){
	baseUrl = window.location.origin;
	getTheories();
}, false)

function getTheories(){
	let thisBody = null;
	fetch(baseUrl +"/theories")
	.then(response => response.json())
	.then(body => gotBody(body));
}

function gotBody(body){
	clearBody();
	for (modell in body){
		displayModell(body[modell]);
	}
}

function clearBody(){
	let targetBody = document.getElementById('modellBody');
	targetBody.innerText = "";
}

function displayModell(body){
	let modellBody = document.getElementById('modellBody');
		let modellContainer = document.createElement("a");
		modellContainer.classList.add("modellContainer");
		modellContainer.href = baseUrl + "/model/" + body["html"];
			let picture = document.createElement("img");
			picture.src = baseUrl + "/static/pictures/" + body["picture"];
			picture.classList.add("modellPicture");
			modellContainer.appendChild(picture);

			let title = document.createElement("h3");

			title.innerText = body["name"];
			modellContainer.appendChild(title);

	modellBody.appendChild(modellContainer);
}

