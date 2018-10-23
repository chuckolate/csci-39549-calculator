from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/<first_number>/<second_number>')
def add(first_number, second_number):
    return render_template('add.html',
                            result = (int(first_number) + int(second_number)),
                            first_number = first_number,
                            second_number = second_number)
    
