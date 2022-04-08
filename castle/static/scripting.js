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

function changecolour() {
	spindruid();
	o = document.getElementById("thestyle");
	s = document.styleSheets[0].href;
	if (s.includes("dark")) {
		o.setAttribute("href", "/static/lightstyle.css");
	} else {
		o.setAttribute("href", "/static/darkstyle.css");
	}
}

function spindruid() {
	var x = 0;
	var id = null;
	clearInterval(id);
	id = setInterval(frame, 1);
	var i = document.getElementById("druidimg");
	var b = document.getElementsByClassName("imgbtn");

	function frame() {
		var g = document.getElementById("druidmsg");
		g.style.display="block;"
		if (x==360) {
			i.style.boxShadow = "None;"
			clearInterval(id);
			i.style.filter="invert(0%)";
			g.style.display="none;"
		} else {
			x++;
			i.style.transform = "rotate("+x+"deg)";
			var y = Math.sin(x);
			i.style["boxShadow"] = "0px 0px 30px 30px 5EFFEA#;"

			i.style.filter="invert(1000%)";

			for (let im=0; im < b.length; im++) {
				b[im].style.transform = "rotate(-"+x+"deg)";
			}
			g.display="block";
		}
	}
}
