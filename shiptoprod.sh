#!/bin/bash
git checkout deploy-fr-prod && git merge master && git push origin deploy-fr-prod && git checkout deploy-ko-prod && git merge master && git push origin deploy-ko-prod git checkout deploy-en-prod && git merge master && git push origin deploy-en-prod && git checkout master
