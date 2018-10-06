from flask import Flask
import os

app = Flask(__name__)

@app.route('/mobileapi', methods=['GET'])
def build_mobile_api():
    os.system("bash PullAndDeployMobileApi.sh")
    return "Mobile Api was deployed"

@app.route('/dataadapter', methods=['GET'])
def build_data_adapter():
    os.system("bash PullAndDeployDataAdapter.sh")
    return "Data Adapter was deployed"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
