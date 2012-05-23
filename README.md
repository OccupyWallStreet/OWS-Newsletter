Newsletter Generation Scripts
=============================

## Purpose ##

These scripts turn raw HTML from a Google Doc into stripped-down HTML and text which can be pasted into CiviCRM, as described at [wiki.occupy.net](http://wiki.occupy.net/wiki/Sending_OWS_Newsletter_with_CiviCRM).

## Requirements ##

Python 2.7 and BeautifulSoup

## Usage ##
    
    cat sample-raw.html | ./html-sanitize.py > newsletter.html
    cat sample-raw.html | ./html-strip.py > newsletter.txt

Or just:

    ./docs-to-civi.sh sample-raw.html

Sample CiviCRM Email Collection
===============================

## Purpose ##

Sample code for collecting emails on an arbitrary site and posting them to the CiviCRM instance at [OccupyWallStreet.net](http://crm.occupywallstreet.net).

## Requirements ##

jQuery

## Usage ##

Copy the code from [post-to-civi.html](https://raw.github.com/OccupyWallStreet/OWS-Newsletter/master/post-to-civi.html). Replace the profileId and groupId in the Javascript with the appropriate values from Civi. Paste the code into the desired place in the source of your website.
