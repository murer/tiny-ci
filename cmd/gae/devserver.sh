#!/bin/bash -xe

cd tiny-ci-api
dev_appserver.py app.yaml
cd -
