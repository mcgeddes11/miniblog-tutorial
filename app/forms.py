from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)

class EditForm(Form):
    nickname = StringField("nickname", validators=[DataRequired()])
    about_me = TextAreaField("about_me", validators=[Length(min=0,max=140)])