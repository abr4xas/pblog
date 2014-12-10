#!/bin/bash
#
rm output.tar.gz && tar -zcvf output.tar.gz output && cp output.tar.gz /var/www/ -v && rm -r output
exit 0
