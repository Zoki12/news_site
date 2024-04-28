from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Email
from .models import Category

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField('Войти')

class Registration_Form(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message='Некорректный еmail')])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField("Повторите пароль", validators=[DataRequired(), EqualTo('password', message="Пароли не совпадают")])
    submit = SubmitField("Зарегистрироваться")

def get_categories():
    categories = Category.query.allO
    return [(category.id, category.title) for category in categories]
class NewsForm(FlaskForm):
    title = StringField(
    "Название",
    validators=[DataRequired(message="Поле не должно быть пустым"),
    Length(max=255, message='Введите заголовок длиной до 255 символов')])
    text = TextAreaField(
    "Текст",
    validators=[DataRequired(message="Поле не должно быть пустым")])
    category = SelectField('Kатегория', choices=get_categories, validators=[Optional()])
    submit = SubmitField('Добавить')