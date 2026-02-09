from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Successfully CI/CD SUCCESS On KubernetesKubernetes Cluster (kind)i am happy"

app.run(host="0.0.0.0", port=5000)
