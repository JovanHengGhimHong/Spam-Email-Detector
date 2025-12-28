import os
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request, session

PREDICT_FLAG = os.getenv('PREDICT_FLAG')

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def home():
  session[PREDICT_FLAG] = True
  return render_template('index.html')


@routes.route('/predict', methods=['POST'])
def predict():
  # ensure request came from a prior form view
  if not session.get(PREDICT_FLAG):
    flash('Please submit the form from the homepage to get a prediction.', 'warning')
    if request.is_json:
      return jsonify({'error': 'unauthorized'}), 403
    return redirect(url_for('routes.home'))

  # one-time use until the form is revisited
  session.pop(PREDICT_FLAG, None)

  # in lieu of a real model, always predict "1"
  prediction = '1'

  flash(f'Prediction result: {prediction}', 'success')

  if request.is_json:
    return jsonify({'prediction': prediction, 'message': f'Prediction result: {prediction}'})

  return redirect(url_for('routes.home'))

