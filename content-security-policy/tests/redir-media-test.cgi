#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style>
#result { color: #800; }
#badVideo { display: none }
</style>
</head>
<body>
<h1 id="result">FAIL</h1>
<video id="badVideo">Your browser does not support &lt;video&gt;</video>
<script type="text/javascript" src="script/redir-media-test.js"></script>
</body>
</html>
