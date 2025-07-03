from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email,Length


class RegistrationForm (FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="We need your name .it can't be empty")])
    email = StringField("Email",validators=[DataRequired(),Email(message="That does not look like a valid email")])
    password = PasswordField("Password",validators=[DataRequired(message="Passwords must be atleast of six characters"),Length(min=6)])
    submit = SubmitField("Register")