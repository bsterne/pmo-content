var t = document.getElementById("test");
var s = window.getComputedStyle(t, null);
if (s.getPropertyValue("color") == "rgb(255, 0, 0)") {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}
