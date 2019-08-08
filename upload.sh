#!/bin/bash
# see https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
pandoc --columns=100 --from=markdown --to=rst --output=README.rst README.md
python3 setup.py sdist upload
