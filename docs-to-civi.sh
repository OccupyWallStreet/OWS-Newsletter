#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 <raw_html_file_name>"
    exit 1
fi

cat $1 | ./html-sanitize.py > newsletter.html
cat $1 | ./html-strip.py > newsletter.txt

