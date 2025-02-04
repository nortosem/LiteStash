#!/usr/bin/sh
# run from package root
pylint --rcfile pylintrc --output lint.txt -r y -f text --recursive y --ignore migrations litestash
