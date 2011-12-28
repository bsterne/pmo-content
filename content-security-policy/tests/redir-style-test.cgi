#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<link rel="stylesheet" type="text/css" href="resources/redir-stylesheet.cgi" />
<style type="text/css">
#result { color: #080; }
#test { display: none }
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<div id="test">test</div>
<script type="text/javascript" src="script/redir-style-test.js"></script>
</body>
</html>

