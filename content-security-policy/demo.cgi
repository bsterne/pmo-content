#!/usr/bin/php-cgi
<?php
require_once("functions.cgi");
$testPath = sprintf("http://%s/%s/tests/", $_SERVER["SERVER_NAME"], substr($_SERVER["PHP_SELF"], 1, -9));
?>
<html>
<head>
<link rel="stylesheet" href="style/style.css" type="text/css" />
<title>Content Security Policy Demo</title>
<style type="text/css">
#tests { margin: 1em auto; }
#tests td { float: left; }
.source { font-size: 75%; }
</style>
<script type="text/javascript">
var tests = ['eval-script-test.cgi', 'font-src-test.cgi', 'frame-ancestors-test.cgi', 'frame-src-test.cgi', 'img-src-test.cgi', 'inline-script-test.cgi', 'media-src-test.cgi', 'object-src-test.cgi', 'policy-uri-test.cgi', 'policy-uri-error-test.cgi', 'redir-font-test.cgi', 'redir-frame-test.cgi', 'redir-img-test.cgi', 'redir-media-test.cgi', 'redir-object-test.cgi', 'redir-script-test.cgi', 'redir-style-test.cgi', 'redir-worker-test.cgi', 'redir-xhr-test.cgi', 'script-src-test.cgi', 'style-src-test.cgi', 'xhr-src-test.cgi'];
function loadTests() {
  var table = document.getElementById("tests");
  var row = document.createElement("tr");
  var c = 0;
  for (var i = 0 ;  i < tests.length ; i++) {
    var cell = document.createElement("td");
    var content = "<div><a href=\"tests/"+tests[i]+"\">"+tests[i]+"</a> ";
		content += "<span class=\"source\">[<a href=\"<?php echo sprintf("view-source:%s", $testPath);?>"+tests[i]+"\">source</a>]</span></div>";
    content += "<iframe src=\"tests/"+tests[i]+"\">";
    cell.innerHTML = content;
    row.appendChild(cell);
    c++;
    if (c % 3 == 0) {
      table.appendChild(row);
      row = document.createElement("tr");
    }
  }
  if (row.hasChildNodes())
    table.appendChild(row);
}
</script>
</head>
<body onload="loadTests()">
<div id="outer">
  <div id="inner">
    <div id="header"><div id="headerWrap"><?php printHeader("Content Security Policy Demo");?></div></div>
    <div id="hnav"><?php printHNav(); ?></div>
    <div id="main">
      <div id="mainWrapper">
        <div class="highlight">
          <p>The following tests demonstrate the core functionality of Content Security Policy.  Grab a copy of <a href="http://mozilla.org/firefox">Firefox 4</a> and load this page to see how CSP works.  For each individual test, a CSP-supporting browser will display <span style="color:#080">PASS</span> while a non-supporting browser will display <span style="color:#800">FAIL</span>.  Each test also contains a comment showing the CSP header that was sent.</p>
          <p>There is also additional debugging information provided on the JavaScript Error console.  For example, loading the <a href="tests/img-src-test.cgi">img-src test</a> in a CSP-enabled build will produce (among others) the following message:</p>
          <p class="nomargin" style="font-family:monospace">CSP debug: blocking request for http://hackmill.com/csp/tests/resources/1x1.gif</p>
        </div>
        <table id="tests"></table>
        <p class="center"><?php printSubNav(); ?></p>
      </div>
    </div><!-- end main -->
    <div id="footer"><?php printFooter(); ?></div>
  </div>
</div>
</body>
</html>
