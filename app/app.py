from flask import Flask
from flask import render_template
from flask import request, redirect
import cPickle as pickle
import pandas as pd
from scipy.spatial import KDTree
app = Flask(__name__)

with open('static/GBC_model.pkl') as f:
    model = pickle.load(f)



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
    output = sum(numerical_inputs)/float(len(numerical_inputs))

    #build a coordinate tree, and return indexes of the 10 nearest items
    coordinate_ktree = KDTree(coordinates)
    _, knn_indexes = coordinate_ktree.query(output, 10)

    relevant_articles = uniques.iloc[knn_indexes]
    return relevant_articles


@app.route('/', methods=['POST'])
def clean():
    user_data = request.json
    input_title = str(user_data['title'])
    input_text = str(user_data['article'])
    input_article = pd.DataFrame(columns=['title', 'article'])
    input_article = input_article.append({'title': input_title, 'article': input_article}, ignore_index=True)

    return


if __name__ == "__main__":
    app.run(debug=True)
