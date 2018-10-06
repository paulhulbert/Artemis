from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/build', methods=['GET'])
def build():
    subprocess.call("PullAndDeployMobileApi.sh")
    return "hi"


if __name__ == '__main__':
    app.run(host='0.0.0.0')