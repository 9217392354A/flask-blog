form flask_wtf import Form
from wtforms import StringField, validators
from author.form import RegisterForm

class SetupForm(Form):
    name = StringField('Blog name', [
        validators.Required(),
        validators.Length(max=80)
        ])