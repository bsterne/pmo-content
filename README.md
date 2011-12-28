# Brandon Sterne's people.mozilla.org web content

## Summary

This repo includes primarily the Content Security Policy documentation and unit tests that were in use prior to the W3C official repo coming online.  Interested parties should refer to the [official standard](https://dvcs.w3.org/hg/content-security-policy/raw-file/tip/csp-specification.dev.html) as these docs are only preserved for posterity.

## Details

If the content is to be displayed on `people.mozilla.org`, the shell script `content-security-policy/phpToCgi.sh` should be run from the directory it lives in.  The PHP environment is quite bizarre on PMO.  In most Apache/PHP environments, the content should work with no modifications.
