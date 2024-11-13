from flask import Flask, request
app = Flask(__name__)

@app.route("/")  # Default route
def hello():
    return "Hello World!"

@app.route("/greetme")  # Greeting route
def helloall():
    # Get the 'name' parameter from the URL
    name = request.args.get('name')
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'privkey.pem'))
