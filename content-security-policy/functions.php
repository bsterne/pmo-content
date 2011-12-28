<?php
function printHeader($s){
  print "<h1>" . $s . "</h1>";
}

function printHNav(){
  $links = array("Overview" => "index.html", "Details" => "details.html", "Spec" => "https://dvcs.w3.org/hg/content-security-policy/raw-file/tip/csp-specification.dev.html", "Download" => "download.html", "Demo" => "demo.php", "WordPress" => "wordpress.html", "Origin Header" => "origin-header-proposal.html", "Discussion" => "discussion.html");
  $temp = explode(".", end(explode("/", $_SERVER["PHP_SELF"])));
  $cur = $temp[0];
	print "<ul>";
  foreach($links as $k => $v){
    $temp = explode(".", $v);
    if($temp[0] == $cur)
      print "<li><a class=\"current\" href=\"$v\">$k</a></li>";
    else
      print "<li><a href=\"$v\">$k</a></li>";
  }
  print "</ul>";
}

function printSubNav(){
  $links = array("Overview" => "index.html", "Details" => "details.html", "Spec" => "https://dvcs.w3.org/hg/content-security-policy/raw-file/tip/csp-specification.dev.html", "Download" => "download.html", "Demo" => "demo.php", "WordPress" => "wordpress.html", "Origin Header" => "origin-header-proposal.html", "Discussion" => "discussion.html");
  $temp = explode(".", end(explode("/", $_SERVER["PHP_SELF"])));
  $cur = $temp[0];
  foreach($links as $k => $v){
    $temp = explode(".", $v);
    if($temp[0] == $cur)
      $s .= "<a class=\"current\" href=\"$v\">$k</a> | ";
    else
      $s .= "<a href=\"$v\">$k</a> | ";
  }
  $s = substr($s, 0, -3);
	print $s;
}

function printFooter(){
	printf("<a href=\"http://www.mozilla.com/firefox\"><img src=\"images/FF.png\" alt=\"Get Firefox\" style=\"border:0;margin:.25em\"/></a><br><small><a href=\"http://people.mozilla.org/~bsterne\">bsterne %s</a></small>", date("Y"));
}

function sanitize($s){
  $bad = array(":nn:", ":ff:", "\n");
  $good = array(":Nn:", ":Ff:", "<br>");
  return str_replace($bad, $good, htmlentities($s));
}
?>
