#!/usr/bin/env bash
# $0 = project name
# $1 = branch name
echo "cd /home/pxh8242/supply-chain-visibility"
cd /home/pxh8242/supply-chain-visibility
echo "git pull"
git pull
echo "checkout $2"
git checkout $2
echo "cd /home/pxh8242/deployments"
cd /home/pxh8242/deployments
echo "git rm -r *"
git rm -r *
echo "cp -r /home/pxh8242/supply-chain-visibility/* /home/pxh8242/deployments/"
cp -r /home/pxh8242/supply-chain-visibility/* /home/pxh8242/deployments/
echo "git add *"
git add *
echo "git commit -m \"Automated deployment\""
git commit -m "Automated deployment"
echo "git push $1 master"
git push $1 master