from app import app
from flask import render_template, url_for, flash, request, redirect, jsonify
from app.forms import SearchForm
from config import Client


# list for storing added students 
added = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
	
	# dummy variable for the date
	date = {'date': 'May 23'}

	# get students records 
	students = Client.db.sheet1.get_all_records()

	# searchbar for adding students
	form = SearchForm()

	# render form with added students
	if form.validate_on_submit():
		for student in students:
			# add a student to the list of added students
			if int(form.student.data) == student['id']:
				if student not in added:
					added.append(student)
		return render_template('index.html', form=form, students=added, date=date)

	return render_template('index.html', form=form, students=added, date=date)

@app.route('/delete/<student_id>', methods=['POST'])
def delete_student(student_id):
    for student in added:
    	if student['id'] == int(student_id):
    		added.remove(student)
    		
    return redirect(url_for('index'))
