let testNumber1 = "2.1.5 Kin - ...erläuter den Zusammenhang zwischen coolen Spielsachen und Sozialer Entwicklung";
let testText1 = "Hier steht eine Erklärung für das Leistungsziel. Dabei ist es ein kleiner Fliesstext, der unten evt auf verschiedene Theorien im Theorieblock verweisen kann. Sharring is carring"
let testNumber2 = "2.1.6 A - ...zeigt den unterschied zwischen privater und professioneller Beziehung anhand eines Beispieles auf."
let testText2 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

window.addEventListener("load", function(){
	displayTargets(testNumber1, testText1);
	displayTargets(testNumber2, testText2);
}, false)



function displayTargets(target, description){
	let targetBody = document.body;
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