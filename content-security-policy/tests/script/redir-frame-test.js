function receiveMsg(event) {
  if (event.data != "redirected frame loaded")
    return false;
  var r = document.getElementById("result");
  r.style.color = "#800";
  r.textContent = "FAIL";
}

window.addEventListener("message", receiveMsg, false);

var f = document.createElement("iframe");
f.src = "resources/redir-frame.cgi";
document.body.appendChild(f);
