from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Test Strings</h1>'

@app.route('/about')
def about():
  return '<h1>This is our about page</h1>'

# app.run(host='0.0.0.0', port=81)

if __name__ == '__main__':
    app.run(debug=True)
