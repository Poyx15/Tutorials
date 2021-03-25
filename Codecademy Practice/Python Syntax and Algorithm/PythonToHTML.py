from flask import Flask, render_template

app = Flask(__name__)


@app.route('/sensors')
def sensors():
    name = 'alert level 5'
    return render_template('sensor.html', name=name)

