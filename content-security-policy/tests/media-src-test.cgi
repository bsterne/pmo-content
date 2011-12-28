#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'; media-src 'none'");
?>
<!-- "X-Content-Security-Policy: allow 'self'; media-src 'none'" -->
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
<script type="text/javascript" src="script/media-src-test.js"></script>
</body>
</html>
