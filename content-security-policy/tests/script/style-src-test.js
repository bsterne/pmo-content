function failTest() {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}
var t = document.getElementById("test");
var c = window.getComputedStyle(t, null);
if (c.getPropertyValue("color") == "rgb(255, 165, 0)")
  failTest();


