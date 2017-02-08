#!/bin/bash -xe

gcloud app deploy --version last -q --verbosity=info \
    tiny-ci-api/app.yaml \
    tiny-ci-api/queue.yaml
    
