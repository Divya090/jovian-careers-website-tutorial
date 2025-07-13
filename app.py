from flask import Flask, render_template # class

app = Flask(__name__) # object

@app.route('/') # @ - decorator
#def hello_world():
#    return 'Hello, World!'
def hello_dd():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

