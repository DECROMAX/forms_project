from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'dog': 'snoots',
        'toy': 'ball',
        'attribute': 'ugly',
        'food': 'bannana'
    },
    {
        'dog': 'buddy',
        'toy': 'burger',
        'attribute': 'fat',
        'food': 'chips'
    }
]


@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', post=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
