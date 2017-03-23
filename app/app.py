from flask import Flask
from flask import render_template
from flask import request, redirect
import cPickle as pickle
app = Flask(__name__)

def load_model(filename):
    """
    Loads and returns trained sklearn random forest model.
    Parameters
    ----------
    filename: str
        The filename/path of the pickled model
    Returns
    -------
    model:
        Trained sklearn Naive Bayes model
    """
    with open(filename) as f:
        model = pickle.load(f)
    return model



@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html')

@app.route('/', methods=['POST'])
def recommend():
    user_data = request.json
    a, b, c = user_data['a'], user_data['b'], user_data['c']
    root_1, root_2 = _solve_quadratic(a, b, c)
    return jsonify({'root_1': root_1, 'root_2': root_2})

@app.route('/', methods=['POST'])
def clean():
    text = request.form['text']
    return


if __name__ == "__main__":
    app.run()
