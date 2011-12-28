#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'; options inline-script");
?>
<!-- "X-Content-Security-Policy: allow 'self'; options inline-script" -->
<html>
<head>
<style>
#result { color: #800; }
</style>
<script>
function passTest() {
  var result = document.getElementById("result");
  result.style.color = "#080";
  result.textContent = "PASS";
}
</script>
</head>
<body>
<h1 id="result">FAIL</h1>
<img src="resources/redir-image-other-host.cgi" onerror="passTest()" />
</body>
</html>

