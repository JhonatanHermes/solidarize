from datetime import datetime
from flask_login import UserMixin
from .extensions import db, bcrypt

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password:str):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password:str)->bool:
        return bcrypt.check_password_hash(self.password_hash, password)

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    donations = db.relationship("Donation", backref="donor", lazy=True, cascade="all,delete")

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    goal = db.Column(db.Float, default=0.0)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    donations = db.relationship("Donation", backref="campaign", lazy=True, cascade="all,delete")

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donor.id"), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaign.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    note = db.Column(db.String(255))
