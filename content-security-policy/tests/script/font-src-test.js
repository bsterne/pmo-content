function failTest() {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}
window.onload = function() {
  var t1 = document.getElementById("test1");
  var t2 = document.getElementById("test2");
  if (t1.clientWidth != t2.clientWidth)
    failTest();
}
