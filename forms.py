from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class AddTaskForm(FlaskForm):
    taskname = StringField('Name of Task', validators=[DataRequired(), Length(max=20)])
    taskcontent = StringField('Description of Task', validators=[DataRequired()])
    duedate = DateField('When is it due', validators=[DataRequired()])
    submit = SubmitField('Add Task')