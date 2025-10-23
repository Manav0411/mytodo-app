from flask import Flask, render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
@app.route("/" , methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title =  request.form["title"]
        desc =  request.form["desc"]
        todo = ToDo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = ToDo.query.all()
    return render_template('index.html' , allTodo=allTodo)

@app.route("/show")
def products():
    allTodo = ToDo.query.all()
    print(allTodo)
    return 'this is products page'

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/update/<int:sno>" , methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        title =  request.form["title"]
        desc =  request.form["desc"]
        allTodo = ToDo.query.filter_by(sno=sno).first()
        allTodo.title = title
        allTodo.desc = desc
        db.session.add(allTodo)
        db.session.commit()
        return redirect("/")
        
    allTodo = ToDo.query.filter_by(sno=sno).first()
    return render_template('update.html' , todo=allTodo)

@app.route("/delete/<int:sno>")
def delete(sno):
    allTodo = ToDo.query.filter_by(sno=sno).first()
    db.session.delete(allTodo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port = 8000)