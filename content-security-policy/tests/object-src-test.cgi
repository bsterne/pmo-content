#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<!-- "X-Content-Security-Policy: allow 'self'" -->
<html>
<head>
<style>
object { position: absolute; top: 0; left: 0; }
#goodObject { z-index: 0 }
#badObject { z-index: 1; background-color: #fff }
</style>
</head>
<body>
<object id="goodObject" type="text/html" data="resources/local-object.html">
</object>
<object id="badObject" type="text/html" data="http://hackmill.com/csp/tests/resources/object.html">
</object>
</body>
</html>
