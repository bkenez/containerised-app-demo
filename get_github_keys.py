from flask import Flask
import requests

app = Flask(__name__)


@app.route('/github_keys/<username>')
def get_ssh_keys(username):
    response = requests.get("https://github.com/" + username + ".keys")

    if response.text == "Not Found":
        return {"error": "GitHub user does not exist"}, 404, {"Content-Type": "application/json"}

    keys = []
    for key in response.text.split("\n")[:-1]:
        keys.append({"type": key.split(" ")[0], "key": key.split(" ")[1]})

    return keys, 200, {"Content-Type": "application/json"}
