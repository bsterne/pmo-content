#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<html>
<head>
<style>
#result { color: #080; }
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<script src="script/redir-xhr-test.js"></script>
</body>
</html>

