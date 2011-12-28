var r = document.getElementById("result5");
r.textContent = "LOADED";
r.parentElement.className = "test fail";
// make the unit test in the parent window fail
top.document.getElementById("frame").parentElement.className = "test fail";
