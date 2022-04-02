function settime() {
	updateTime();
	var t=setInterval(updateTime,1000);
}

function updateTime() {
	var dt = new Date();
	var options = { hour: '2-digit', minute: '2-digit', day: '2-digit', year: 'numeric', month: '2-digit' };
	document.getElementById("datetimebox").innerHTML = dt.toLocaleString("en-GB", options);
}

function goHome() {
	window.location.href="/";
}
