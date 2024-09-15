from flask import Flask, render_template, redirect, url_for
from models import db, Pet
from forms import PetForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)
@app.route('/', methods=['GET', 'POST'])
def index():
form = PetForm()
if form.validate_on_submit():
pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)
db.session.add(pet)
db.session.commit()
return redirect(url_for('index'))
pets = Pet.query.all()
return render_template('view_pets.html', form=form, pets=pets)
if __name__ == '__main__':
app.run(debug=True)
