#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: policy-uri /~bsterne/content-security-policy/tests/csp-policy.cgi");
?>
<!-- "X-Content-Security-Policy: policy-uri /~bsterne/content-security-policy/tests/csp-policy.cgi" -->
<html>
<head>
<style>
#result { color: #800; }
</style>
</head>
<body>
<h1 id="result">FAIL</h1>
<script type="text/javascript" src="script/policy-uri-test.js"></script>
</body>
</html>
