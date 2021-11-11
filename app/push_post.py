from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Push_post(FlaskForm):
    username = StringField('Как тебя зовут?', validators=[DataRequired()])
    p_text = StringField('Напиши что-нибудь', validators=[DataRequired()])
    submit = SubmitField('Отправить')
