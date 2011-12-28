#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'; font-src 'none'");
?>
<!-- "X-Content-Security-Policy: allow 'self'; font-src 'none'" -->
<html>
<head>
<style type="text/css">
#result { color: #080; }
@font-face {
  font-family: "My BVSB";
  src: url("resources/VeraSeBd.ttf");
}
#test1, #test2 { 
  font-family: "My BVSB", monospace;
  position: absolute;
  height: auto;
  width: auto;
  color: #fff;
}
</style>
</head>
<body>
<h1 id="result">PASS</h1>
<!-- if the downloadable font loads, test1 and test2 will have
     different clientWidth's -->
<div id="test1">l</div><div id="test2">m</div>
<script type="text/javascript" src="script/font-src-test.js"></script>
</body>
</html>
