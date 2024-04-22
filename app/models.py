from app import db

class Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    telegram = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String, nullable=False)
    languages = db.Column(db.String(200), nullable=True)