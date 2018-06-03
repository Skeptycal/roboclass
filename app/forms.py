from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired
from config import Client

class SearchForm(FlaskForm):
	student = StringField('Add Student', validators=[DataRequired()])


	def validate_student(self, student):
		student = Client.db.sheet1.findall(student.data)
		if not student:
			raise ValidationError('Student not found')