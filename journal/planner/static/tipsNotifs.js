function setTime() {

var currentTime = new Date();

var h = currentTime.getHours();
var m = currentTime.getMinutes();
var s = currentTime.getSeconds();

	document.getElementById("time-clock").innerText = h + ":" + m + ":" + s;
	document.getElementById("time-clock").textContent = h + ":" + m + ":" + s;
	setTimeout(setTime, 1000);
}


setTime();