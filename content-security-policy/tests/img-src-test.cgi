#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style>
#result { color: #800; }
</style>
</head>
<body>
<h1 id="result">FAIL</h1>
<img id="badImage" />
<script type="text/javascript" src="script/img-src-test.js"></script>
</body>
</html>
