from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'dog': 'Beau Martinez',
        'title': 'Beau the snoot',
        'toy': 'Ball',
        'attribute': 'Ugly',
        'food': 'Bananna'
    },
    {
        'dog': 'Buddy Gomez',
        'title': 'Buddington',
        'toy': 'Burgers',
        'attribute': 'Fat',
        'food': 'Chips'
    }
]


@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
