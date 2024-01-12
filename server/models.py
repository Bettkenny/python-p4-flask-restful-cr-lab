from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float(precision=2), nullable=False)

    def __repr__(self):
        return f"Plant(name={self.name}, image={self.image}, price={self.price}"
    
    db.create_all()