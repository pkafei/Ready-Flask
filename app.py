import os
from flask import Flask, render_template, send_from_directory
from flask import url_for, redirect
from flask_s3 import FlaskS3


#from flask.ext.assets import Environment, Bundle

#-----------------------------
# initialization
# -----------------------------

app = Flask(__name__)
app.config['jsflask'] = 'jsflask'
s3 = FlaskS3(app)


app.config.update(
    DEBUG=True,
)

#------------------------------
#Configuration
#------------------------------

#ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/js')

#app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def base():
    return render_template('test.html')


#------------------------------
#launch
#------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


