from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class DonorForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(3, 30)])
    address = StringField('Address', validators=[Length(5, 50)])
    phone_no = StringField('phone number', validators=[DataRequired(), Length(10)])
    type = StringField('Blood Type', validators=[DataRequired(), Length(2, 3)])
    submit = SubmitField('Submit')

