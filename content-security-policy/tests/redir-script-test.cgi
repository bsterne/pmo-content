#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style>
#result { color: #080; }
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<script type="text/javascript" src="resources/redir-script.cgi"></script>
</body>
</html>

