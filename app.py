from flask import Flask # class

app = Flask(__name__) # object

@app.route('/') # @ - decorator
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

