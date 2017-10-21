from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.sqlite3'
app.config['SECRET_KEY'] = 'myflaskkey'
app.config['FLASK_ADMIN_SWATCH'] = 'default'

db = SQLAlchemy(app)

admin = Admin(app, name='Dashboard', template_mode='bootstrap3')

class Murid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode(64))
    last_name = db.Column(db.Unicode(64))
    birthday = db.Column(db.DateTime)
    email = db.Column(db.Unicode(128))
    phone = db.Column(db.Unicode(32))
    city = db.Column(db.Unicode(128))
    country = db.Column(db.Unicode(128))
    notes = db.Column(db.UnicodeText)


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'





# admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Murid, db.session))




if __name__ == '__main__':
    app.run(debug=True)


  