from config import *


class Cat(db.Model):
    __tablename__ = 'cat'

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.String(256))
    name = db.Column(db.String(256))
    image = db.Column(db.String(256))

    def __repr__(self):
        return f'Cat{self.id}'
