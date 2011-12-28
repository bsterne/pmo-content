#!/usr/bin/php-cgi
<?php
header("X-Content-Security-Policy: allow 'self'");
?>
<p>"X-Content-Security-Policy: allow 'self'"</p>
<iframe src="inner.html"></iframe>
