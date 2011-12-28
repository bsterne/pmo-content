#!/bin/bash

# convert demo and functions to cgi
for i in demo functions
do
  # only demo.cgi needs the #!
  if [ $i == "demo" ]
    then
    echo "#!/usr/bin/php-cgi" > $i.cgi
  else
    echo "" > $i.cgi
  fi
  cat $i.php | sed "s/\.php/\.cgi/g" >> $i.cgi
  chmod +x $i.cgi
  echo "Created $i.cgi"
done

# convert any references to .php file in the following list of files
# to .html references
for i in details.html discussion.html download.html index.html origin-header-proposal.html wordpress.html
do
  echo "Switching .php to .cgi in $i"
  sed -i "s/\.php/\.cgi/g" $i
done

# change resources from .php to .cgi including internal references
for i in `find . -name "*.php"`
do
  echo "Transforming test file $i"
  echo "#!/usr/bin/php-cgi" > `echo $i | sed s/\.[^\.]*$//`.cgi
  cat $i | sed "s/\.php/\.cgi/g" >> `echo $i | sed s/\.[^\.]*$//`.cgi
  chmod +x `echo $i | sed s/\.[^\.]*$//`.cgi
done
# FIXME
echo "WARNING: MANUALLY FIX tests/resources/redir-xhr.cgi to point to .php on hackmill.com"
echo "WARNING: MANUALLY FIX tests/script/frame-ancestors-test.js to point to .php on hackmill.com"

# change references inside .js files to .cgi
for i in `find . -name "*.js"`
do
  echo "Switching .php to .cgi in $i"
  sed -i "s/\.php/\.cgi/g" $i
done

# point policy-uri to correct resource for server (people.mozilla.org uses UserDir)
for i in policy-uri-test.cgi policy-uri-error-test.cgi
do
  sed -i "s/policy-uri\ .*\//policy-uri\ \/~bsterne\/content-security-policy\/tests\//g" tests/$i
  echo "Fixing policy-uri in $i"
done

# clean up all unneeded .php files
for i in `find . -name \*.php`
do
  echo "Cleaning up $i"
  rm -f $i
done

