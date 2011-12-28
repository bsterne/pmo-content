s = 'var r = document.getElementById("result"); r.style.color = "#800"; r.textContent = "FAIL";';
eval(s);
setTimeout(s, 0);
var f = new Function(s);
f();
