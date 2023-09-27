from flask import render_template, url_for, flash, redirect, request
from app import app
import requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
    return render_template('pokemon.html')