function failTest() {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}
var f = document.createElement("iframe");
f.onload = failTest;
f.src = "http://hackmill.com/";
document.body.appendChild(f);
