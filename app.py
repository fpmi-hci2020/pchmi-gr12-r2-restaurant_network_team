from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    page = '<html><body><h1>'
    page += "HI"
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
