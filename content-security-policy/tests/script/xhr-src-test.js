function failTest() {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}
var url = "http://hackmill.com/";
var h = new XMLHttpRequest();
h.open("GET", url, true);
h.onreadystatechange = failTest;
h.send();
