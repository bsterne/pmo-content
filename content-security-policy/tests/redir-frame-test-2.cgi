#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'; report-uri http://people.mozilla.org/csp-report");
?>
<!-- "X-Content-Security-Policy: allow 'self'; report-uri http://people.mozilla.org/csp-report" -->
<html>
<head>
<style>
#result { color: #080; }
iframe { display: none }
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<script type="text/javascript" src="script/redir-frame-test.js"></script>
</body>
</html>

