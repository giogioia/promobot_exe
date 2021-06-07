#!/bin/bash
cd -- "$(dirname "$BASH_SOURCE")"
rm -rf PromoBot.egg-info build
mv dist/*.whl .
rm -r dist
