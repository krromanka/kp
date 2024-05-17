from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class books(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    genr = db.Column(db.String(50), nullable=False)
    auftor = db.Column(db.String(500), nullable=False)
    yers = db.Column(db.String(5), nullable=False)


    def __init__(self, name, genr, auftor, yers):
        self.name = name
        self.genr = genr
        self.auftor = auftor
        self.yers = yers

    def __repr__(self):
        return '<books %r>' % self.ID


@app.route('/')
def index():
    boks = books.query.all()
    return render_template("index.html", boks=boks)


@app.route('/Inform')
def about():
    return render_template("Inform.html")

@app.route('/POSTS')
def posts():
    boks = books.query.all()
    return render_template("POSTS.html", boks=boks)


@app.route('/POSTS/<int:id>')
def post_detail(id):
    bok = books.query.all()
    return render_template("POST_PRAVOSL.html", bok=bok)


@app.route('/create-books', methods=['GET', 'POST'])
def novels():
    if request.method == "POST":
        name = request.form['name']
        genr = request.form['genr']
        auftor = request.form['auftor']
        yers = request.form['yers']

        bok = books(name=name, genr=genr, auftor=auftor, yers=yers)

        try:
            db.session.add(bok)
            db.session.commit()
            return redirect('/')
        except:
            return "Inform"
    else:
        return render_template('create-books.html')


if __name__ == "__main__":
    app.run(debug=True)