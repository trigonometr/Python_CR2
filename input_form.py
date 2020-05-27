import flask_wtf
from wtforms import StringField, SubmitField, validators
from wtforms.fields.html5 import DateField


class InputForm(flask_wtf.FlaskForm):
    """form for getting country name and date to get stats"""
    country_name = StringField("Country name: ",
                               validators=[validators.DataRequired()])
    date = DateField("Date: ", format='%Y-%m-%d', validators=(validators.Optional(),))
    submit = SubmitField("Get statistics")
