import os
from flask import Flask, render_template, url_for
from data import inputs

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))  # Obtener el puerto de las variables de entorno de Heroku

@app.context_processor
def inject_dict_for_all_templates():
    global_ = {'last name':inputs['last name']}
    return dict(global_=global_)

@app.route('/')
def index():
    return render_template('index.html', data=inputs)

if __name__ == '__main__':
    app.run(debug=True)
