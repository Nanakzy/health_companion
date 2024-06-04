#!/usr/bin/python3

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    # Additional fields for user profile
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    # Add more fields as needed

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class HealthPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    plan_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    # Add more fields as needed

    user = db.relationship
    ('User', backref=db.backref('health_plans', lazy=True))

    def __repr__(self):
        return f"HealthPlan('{self.user_id}', '{self.plan_name}')"


class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    medication_name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50))
    frequency = db.Column(db.String(50))
    # Add more fields as needed

    user = db.relationship
    ('User', backref=db.backref('medications', lazy=True))

    def __repr__(self):
        return f"Medication('{self.user_id}', '{self.medication_name}')"
