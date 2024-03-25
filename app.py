from flask import Flask, render_template, url_for
from data import inputs

app = Flask(__name__)

# Obtén el puerto desde la variable de entorno, o utiliza el 5000 por defecto
port = int(os.environ.get("PORT", 5000))

@app.context_processor
def inject_dict_for_all_templates():
    global_ = {'last name':inputs['last name']}
    return dict(global_=global_)

@app.route('/')
def index():
    return render_template('index.html', data=inputs)

if __name__ == '__main__':
    app.run(debug=True)
