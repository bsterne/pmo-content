function passTest() {
  var r = document.getElementById("result");
  r.style.color = "#080";
  r.textContent = "PASS";
}
var i = document.getElementById("badImage");
i.onerror = passTest;
i.src = "http://hackmill.com/csp/tests/resources/1x1.gif";
