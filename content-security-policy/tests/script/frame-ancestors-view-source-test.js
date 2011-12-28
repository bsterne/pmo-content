function failTest() {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}
var f = document.createElement("iframe");
f.onload = failTest;
// frame.cgi -> X-Content-Security-Policy: allow 'self'; frame-ancestors 'self'"
f.src = "view-source:http://hackmill.com/csp/tests/resources/frame.cgi";
document.body.appendChild(f);
