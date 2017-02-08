#!/bin/bash -xe

gcloud app logs read -s default --level info --version last
