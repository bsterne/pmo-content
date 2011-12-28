#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style type="text/css">
#result { color: #080; }
@font-face {
  font-family: "My BVSB";
  src: url("resources/redir-font.cgi");
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
<div id="test1">l</div><div id="test2">m</div>
<script type="text/javascript" src="script/redir-font-test.js"></script>
</body>
</html>

