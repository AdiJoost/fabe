class NavigationItem {
	constructor(name, tail){
		this.name = name;
		this.tail = tail;
	}

	toString(){
		let return_value = "Title: " + this.name + " tail: " + this.tail;
		return return_value;
	}
}

window.addEventListener("load", function(){
	setupHeadNav();
}, false)

function setupHeadNav(){
	let navItems = [
				new NavigationItem("Startseite", "/"),
				new NavigationItem("Leistungsziele", "/targets"),
				new NavigationItem("Modelle", "/models"),
				new NavigationItem("Kontakt", "/contact"),
				new NavigationItem("Impressum", "/impressum"),
				new NavigationItem("Zusammenfassungen", "/resumes"),]

	let container = document.getElementById('headNavContainer');
	for (let item in navItems){
		let mySpan = document.createElement("span");
			let myA = document.createElement("a");
			myA.href = navItems[item].tail;
			myA.innerText= navItems[item].name;
			mySpan.appendChild(myA);
		container.appendChild(mySpan);
	}

}