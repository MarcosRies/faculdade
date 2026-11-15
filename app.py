from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta-padrao')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///acms.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definição básica dos Models (Beneficiário e Entrega)
class Beneficiario(db.Model):
    __tablename__ = 'beneficiario'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    entregas = db.relationship('Entrega', backref='beneficiario', lazy=True)

class Entrega(db.Model):
    __tablename__ = 'entrega'
    id = db.Column(db.Integer, primary_key=True)
    data_entrega = db.Column(db.DateTime, nullable=False)
    beneficiario_id = db.Column(db.Integer, db.ForeignKey('beneficiario.id'), nullable=False)

@app.route('/')
def index():
    return "Sistema de Gestão e Triagem de Beneficiários – ACMS (MVP Online)"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)