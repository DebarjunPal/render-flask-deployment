from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return "<h1>First Flask App</h1>"

if __name__ == "__main__":
    app.run()