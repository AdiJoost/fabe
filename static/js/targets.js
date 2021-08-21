let baseUrl = "";

window.addEventListener("load", function(){
	baseUrl = window.location.origin;
	loadAllTargets();
}, false)

function loadAllTargets(){
	let thisBody = null;
	fetch(baseUrl +"/all_targets")
	.then(response => response.json())
	.then(body => gotBody(body));
}

function gotBody(body){
	clearBody();
	for (target in body){
		item = body[target]
		displayTargets(item["target_title"] + " " + item["name"], item["description"]);
	}
}

function clearBody(){
	let targetBody = document.getElementById('targetBody');
	targetBody.innerText = "";
}



function displayTargets(target, description){
	let targetBody = document.getElementById('targetBody');
		let targetBox = document.createElement("div");
		targetBox.classList.add("targetBox");
			let targetNumber = document.createElement("div");
			targetNumber.classList.add("targetNumberBox");
				let number = document.createElement("span");
				number.classList.add("targetNumber");
				number.innerText = target;
				targetNumber.appendChild(number);
			targetBox.appendChild(targetNumber);

			let targetExplain = document.createElement("div");
			targetExplain.classList.add("targetExplain");
			targetExplain.classList.add("hiden");
				let explaination = document.createElement("p");
				explaination.innerText = description;
				targetExplain.appendChild(explaination);
			targetBox.appendChild(targetExplain);

	targetBody.appendChild(targetBox);

	targetNumber.addEventListener("click", function(){
		targetExplain.classList.toggle("hiden");
	}, false);
}