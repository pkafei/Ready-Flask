import os
from flask import Flask, render_template, send_from_directory

#-----------------------------
# initialization
# -----------------------------

app = Flask(__name__)

app.config.update(
    DEBUG=True,
)

#------------------------------
#controllers
#------------------------------


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/tech')
def tech():
    return render_template('tech.html')


@app.route('/graphs')
def graphs():
    return render_template('graphs.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')
#------------------------------
#launch
#------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


