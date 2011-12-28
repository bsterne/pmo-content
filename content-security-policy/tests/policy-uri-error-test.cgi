#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: policy-uri /~bsterne/content-security-policy/tests/csp-policy-404.cgi");
?>
<!-- "X-Content-Security-Policy: policy-uri /~bsterne/content-security-policy/tests/csp-policy-404.cgi" -->
<html>
<head>
<style>
#result { color: #080; }
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<script type="text/javascript" src="script/policy-uri-error-test.js"></script>
</body>
</html>
