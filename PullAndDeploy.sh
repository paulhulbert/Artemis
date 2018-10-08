#!/usr/bin/env bash
# $0 = project name
# $1 = branch name
cd /home/pxh8242/supply-chain-visibility
git pull
git checkout $1
cd /home/pxh8242/deployments
git rm -r *
cp -r /home/pxh8242/supply-chain-visibility/* /home/pxh8242/deployments/
git add *
git commit -m "Automated deployment"
git push $0 $1