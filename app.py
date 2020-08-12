import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    int_features = []
    int_features.append(int(features[0]))
    int_features.append(int(features[1]))
    int_features.append(int(features[2]))
    int_features.append(int(features[3]))
    int_features.append(int(int(features[2])-int(features[3])))
    int_features.append(int(features[4]))
    int_features.append(int(features[5]))
    
    # now for tenutre status 
    if features[6] == "Other" :
        int_features.append(1) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[6] == "Owned and fully paid" :
        int_features.append(0) 
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif features[6] == "Owned but not yet paid off" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    elif features[6] == "Rented" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
    else :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        
    # now for living quater 
    if features[7] == "House" :
        int_features.append(1)
    else :
        int_features.append(0)
    
    # for toilet 
    if features[8] == "Chemical Toilet" :
        int_features.append(1) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[8] == "flush toilet connected to sewage system" :
        int_features.append(0) 
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif  features[8] == "flush toilet with septic tank" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[8] == "other" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif  features[8] == "pit latrine with ventilation VIP" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif features[8] == "pit latrine without ventilation" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    elif features[8] == "not known" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
    else :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    
    ## for toilet 
    if features[9] == "Piped tap water inside dwelling" :
        int_features.append(1) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[9] == "Piped tap water inside the yard" :
        int_features.append(0) 
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif  features[9] == "Piped tap water on community stand distance more than 1 km" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[9] == "Piped tap water on community stand distance less than 200m" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif  features[9] == "Piped tap water on community stand distance between  200m to 500 m" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    elif features[9] == "Piped tap water on community stand between 500m to 1 km" :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
    else :
        int_features.append(0) 
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    
    # for Interney access 
    if features[10] == "From elsewhere" :
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[10] == "From home" :
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif features[10] == "From work" :
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    elif features[10] == "No access" :
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
    else :
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        
    # for gender 
    if features[11] == "Male" :
        int_features.append(1)
    else :
        int_features.append(0)
        
    # for employement 
    if features[12] == "Employed" :
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
    elif features[12] == "Household head out of working age scope i.e. 15-64" :
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
    elif features[12] == "Not economically active" :
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
    elif features[12] == "Unemployed" :
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
    else :
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        
    
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    
    if output == 1 :
        outputs = "active"
    else :
        outputs = "inactive"

    return render_template('index.html', prediction_text='person is economically {}'.format(outputs))

if __name__ == "__main__":
    app.run(debug=True)
