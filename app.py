from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')


class FeedbackForm(FlaskForm):
    """Feedback form with validation"""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit Feedback')


@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page with feedback form"""
    form = FeedbackForm()
    if form.validate_on_submit():
        # Process the form data
        flash(f'Thank you {form.name.data} for your feedback!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
