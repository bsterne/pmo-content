#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style>
#result { color: #080; }
iframe { display: none }
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<script type="text/javascript" src="script/frame-src-test.js"></script>
</body>
</html>
