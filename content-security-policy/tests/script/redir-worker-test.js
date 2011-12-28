// redirects to http://hackmill.com/csp/tests/resources/worker-other.js
var w = new Worker("resources/redir-worker-script.cgi");

w.onmessage = function(e) {
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}

