function passTest() {
  var r = document.getElementById("result");
  r.style.color = "#080";
  r.textContent = "PASS";
}
var v = document.getElementById("badVideo");
v.onerror = passTest;
// set video src to a resource that will redirect to a different domain
v.src = "resources/redir-video.cgi";

