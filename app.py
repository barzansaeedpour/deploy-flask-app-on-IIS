from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask on IIS!"

# This is required for IIS deployment
if __name__ == '__main__':
    app.run()
else:
    # This is needed for IIS
    application = app