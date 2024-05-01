#!/bin/bash

# Remove artifacts
rm -rf dist
rm -rf build
rm -rf *.egg-info

# Create distribution files
python setup.py sdist bdist_wheel