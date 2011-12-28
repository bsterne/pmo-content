#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style>
#result { color: #080; }
#test { display: none }
</style>
<link rel="stylesheet" type="text/css" href="http://hackmill.com/csp/tests/resources/orange.css" />
</head>
<body>
<h1 id="result">PASS</h1>
<div id="test">foo</div>
<script type="text/javascript" src="script/style-src-test.js"></script>
</body>
</html>
