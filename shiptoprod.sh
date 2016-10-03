#!/bin/bash
git checkout deploy-fr-prod && git merge master && git push origin deploy-fr-prod && git checkout master
