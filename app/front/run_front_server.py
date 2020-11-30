import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    sulphates = StringField('Sulphates [0.33, 2]', validators=[DataRequired()])
    free_sulfur_dioxide = StringField('Free Sulfur Dioxide [1, 72]', validators=[DataRequired()])
    total_sulfur_dioxide = StringField('Total Sulfur Dioxide [6, 289]', validators=[DataRequired()])
    pH = StringField('pH [2.74, 4.01]', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(description, company_profile, benefits):
    body = {"sulphate": [sulphates],
            "free_sulfur_dioxide":[free_sulfur_dioxide],
            "total_sulfur_dioxide": [total_sulfur_dioxide],
            "pH": [pH]}

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['sulphate'] = request.form.get('sulphate')
        data['free_sulfur_dioxide'] = request.form.get('free_sulfur_dioxide')
        data['total_sulfur_dioxide'] = request.form.get('total_sulfur_dioxide')
        data['pH'] = request.form.get('pH')


        try:
            response = str(get_prediction(data['sulphate'],
                                          data['free_sulfur_dioxide'],
                                          data['total_sulfur_dioxide'],
                                          data['pH']))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)