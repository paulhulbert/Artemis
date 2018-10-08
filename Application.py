from flask import Flask, jsonify, request
from git import Git
import os

application = Flask(__name__)

g = Git('/home/pxh8242/supply-chain-visibility')

@application.route('/mobileapi', methods=['GET'])
def build_mobile_api():
    branch = request.args.get('branch', default='master')
    return build_and_deploy("azureMobileApi", branch)

@application.route('/dataadapter', methods=['GET'])
def build_data_adapter():
    branch = request.args.get('branch', default='master')
    return build_and_deploy("azureDataAdapter", branch)


@application.route('/branches', methods=['GET'])
def get_list_of_branches_api():
    return jsonify(get_list_of_branches())


def build_and_deploy(project, branch):
    g.pull()
    if branch not in get_list_of_branches():
        return "Branch" + branch + " is not in the list of branches"
    os.system("bash PullAndDeploy.sh " + project + " " + branch)
    return project + " was deployed"


def get_list_of_branches():
    output = g.branch()
    branches_raw = output.split('\n')
    branches = []
    for branch in branches_raw:
        branches.append(branch.strip('*').strip())
    return branches


if __name__ == '__main__':
    application.run(host='0.0.0.0')
