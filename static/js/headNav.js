let baseUrl = "";

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
	baseUrl = window.location.origin;
	setupHeadNav();
}, false)

function setupHeadNav(){
	let navItems = [
				new NavigationItem("Startseite", "/"),
				new NavigationItem("Leistungsziele", "/targets")]

	let container = document.getElementById('headNavContainer');
	for (let item in navItems){
		console.log(navItems[item].toString());
	}

}