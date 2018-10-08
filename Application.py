from flask import Flask, jsonify
from git import Git
import os

application = Flask(__name__)

g = Git('/home/pxh8242/supply-chain-visibility')

@application.route('/mobileapi', methods=['GET'])
def build_mobile_api():
    os.system("bash PullAndDeploy.sh azureMobileApi master")
    return "Mobile Api was deployed"

@application.route('/dataadapter', methods=['GET'])
def build_data_adapter():
    os.system("bash PullAndDeploy.sh azureDataAdapter master")
    return "Data Adapter was deployed"


@application.route('/branches', methods=['GET'])
def get_list_of_branches():
    output = g.branch()
    branches_raw = output.split('\n')
    branches = []
    for branch in branches_raw:
        branches.append(branch.strip('*').strip())
    return jsonify(branches)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
