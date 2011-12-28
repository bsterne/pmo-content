#!/usr/bin/php-cgi
<?php
setcookie("bsterne", "1");
header("X-Content-Security-Policy: allow 'self'; report-uri http://people.mozilla.org/~bsterne/content-security-policy/tests/process-report.cgi");
?>
<html>
<head>
<style>
#result { color: #008; }
</style>
</head>
<body>
<h1 id="result">MANUAL</h1>
<img src="http://hackmill.com/csp/tests/resources/1x1.gif" />
</body>
</html>

