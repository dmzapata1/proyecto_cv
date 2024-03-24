from flask import Flask, render_template, url_for
from data import inputs

app = Flask(__name__)

@app.context_processor
def inject_dict_for_all_templates():
    global_ = {'last name':inputs['last name']}
    return dict(global_=global_)

@app.route('/')
def index():
    return render_template('index.html', data=inputs)

if __name__ == '__main__':
    app.run(debug=True)
