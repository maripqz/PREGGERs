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

@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    user_data = request.json
    #Get user provided inputs from form
    stage = user_data['stage']
    breastfeeding = user_data['breastfeeding']
    formula = user_data['formula']
    solid= user_data['solid']
    meal_planning = user_data['meal_planning']
    risks = user_data['risks']
    weight = user_data['weight']
    science = user_data['science']
    diabetes = user_data['diabetes']
    hypertension = user_data['hypertension']
    obesity = user_data['obesity']

    # Setting values to centroids
    if breastfeeding:
        breastfeeding = ()
    if formula:
        formula = ()
    if solid:
        solid = ()
    if meal_planning:
        meal_planning = ()
    if risks:
        risks = ()
    if weight:
        weight = ()
    if science:
        science = ()
    #still need to set diabetes, hypertension, obesity, trimester stage

    #calculate the position of the information that they want
    all_inputs = [breastfeeding, formula, solid, meal_planning, risks, weight, science]
    numerical_inputs = [item for item in position if item[0].isdigit()]
    output = sum(numerical_inputs)/len(numerical_inputs)

    #find the articles closest to this point
    


@app.route('/', methods=['POST'])
def clean():
    text = request.form['text']
    return


if __name__ == "__main__":
    app.run()
