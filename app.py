from flask import Flask, render_template, redirect, url_for, request
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

@app.route('/remove_pet/<int:pet_id>', methods=['POST'])
def remove_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if pet:
        db.session.delete(pet)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)

