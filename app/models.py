from app import db

# SQLAlchemy allow us to work with classes when setting our tables to the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False) # Changed to 60 due the hashed password 

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"