function failTest() {
  var result = document.getElementById("result");
  result.style.color = "#800";
  result.textContent = "FAIL";
}

var xhr = new XMLHttpRequest();
xhr.open('GET', 'resources/redir-xhr.cgi', true);

// Technically, this test is wrong because it checks for the response
// to the redirected request, rather than for the request being made.
// We're limited in what we can test for from web content.  This'll do.
xhr.onreadystatechange = function (e) {
  if (xhr.readyState == 4) {
    if (xhr.status == 200) {
      if (xhr.responseText.match("Other site."))
        failTest();
    }
  }
};

xhr.send(null);

