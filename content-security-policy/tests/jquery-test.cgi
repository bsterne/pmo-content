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
<script type="text/javascript" src="script/jquery-1.3.2.min.js"></script>
</head>
<body>
<h1 id="result">PASS</h1>
<script type="text/javascript">
//<![CDATA[
$("#result").hide("slow", function() {
  $("#result").css({'color' : '#800'});
  $("#result").text("FAIL");
  $("#result").show("slow");
});
//]]>
</script>
</body>
</html>
