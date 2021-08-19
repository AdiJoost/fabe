let testNumber1 = "2.1.5 Kin - ...erläuter den Zusammenhang zwischen coolen Spielsachen und Sozialer Entwicklung";
let testText1 = "Hier steht eine Erklärung für das Leistungsziel. Dabei ist es ein kleiner Fliesstext, der unten evt auf verschiedene Theorien im Theorieblock verweisen kann. Sharring is carring"


window.addEventListener("load", function(){
	getButtons();
	displayTargets();
}, false)

function getButtons(){
	let targetNumber = document.getElementById('testBox');
	targetNumber.addEventListener("click", function(){
		let testText = document.getElementById('testText');
		testText.classList.toggle("hiden");
	}, false)
}


function displayTargets(){
	let targetBody = document.body;
		let targetBox = document.createElement("div");
		targetBox.classList.add("targetBox");
			let targetNumber = document.createElement("div");
			targetNumber.classList.add("targetNumberBox");
				let number = document.createElement("span");
				number.classList.add("targetNumber");
				number.innerText = testNumber1;
				targetNumber.appendChild(number);
			targetBox.appendChild(targetNumber);

			let targetExplain = document.createElement("div");
			targetExplain.classList.add("targetExplain");
				let explaination = document.createElement("p");
				explaination.innerText = testText1;
				targetExplain.appendChild(explaination);
			targetBox.appendChild(targetExplain);

	targetBody.appendChild(targetBox);

	targetNumber.addEventListener("click", function(){
		targetExplain.classList.toggle("hiden");
	}, false);
}