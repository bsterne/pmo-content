function passTest() {
  var r = document.getElementById("result");
  r.style.color = "#080";
  r.textContent = "PASS";
}
var v = document.getElementById("badVideo");
v.onerror = passTest;
v.src = "resources/video.ogv";
