from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Myapp(db.Model):
	c_id = db.Column(db.Integer, primary_key=True)
	c_name = db.Column(db.String(500))

@app.route('/')
def home():
	return ':: uma zone by 2giles ::'

@app.route('/insert', methods=["POST"])
def insert():
	c_name = request.form.get("c_name")
	new_c_name = Myapp(c_name=c_name)
	db.session.add(new_c_name)
	db.session.commit()
	return redirect(url_for("mychecklist"))

@app.route('/delete/<int:c_id>')
def delete(c_id):
	#c_name = Myapp.query.filter_by(id=c_id).first()
	c_name = Myapp.query.get_or_404(c_id)
	db.session.delete(c_name)
	db.session.commit()
	return redirect(url_for("mychecklist"))

@app.route('/checklist')
def mychecklist():
	my_list = Myapp.query.all()
	return render_template("base.html", my_list=my_list)

if __name__ == "__main__":
	app.run()

