from flask import Flask,render_template,url_for,request
import pickle as pkl
import numpy as np
import pandas as pd
import sklearn
import xgboost
app = Flask(__name__)
mod = pkl.load(open("mod.pkl",'rb'))
cols = ['size', 'os', 'ram', 'gprm', 'fp', 'Touch_or_not', 'wid', 'hgt', 'usb2','usb3', 'usbc', 'ethr', 'blth', 'strtype', 'amst', 'ncrs', 'thrds','bc', 'mcl', 'pnm']
def fnc1(a):
    if a=='5060':
        return 'Rs.50000 to Rs.60000'
    elif a=='3040':
        return 'Rs.30000 to Rs.40000'
    elif a=='4050':
        return 'Rs.40000 to Rs.50000'
    elif a=='6070':
        return 'Rs.60,000 to Rs.70,000'
    elif a=='7080':
        return 'Rs.70,000 to Rs.80,000'
    elif a=='2030':
        return 'Rs.20,000 to Rs.30,000'
    elif a=='8090':
        return 'Rs.80,000 to Rs.90,000'
    elif a=='100120':
        return 'Rs.1,00,000 to Rs.1,20,000'
    elif a=='90100':
        return 'Rs.90,000 to Rs.1,00,000'
    elif a=='120140':
        return 'Rs.1,20,000 to Rs.1,40,000'
    elif a=='200250':
        return 'Rs.2,00,000 to Rs.2,50,000'
    elif a=='140160':
        return 'Rs.1,40,000 to Rs.1,60,000'
    elif a=='160180':
        return 'Rs.1,60,000 to Rs.1,80,000'
    elif a=='180200':
        return 'Rs.1,80,000 to Rs.2,00,000'
    elif a=='250300':
        return 'Rs.2,50,000 to Rs.3,00,000'
    elif a=='1020':
        return 'Rs.10,000 to Rs.20,000'
    elif a=='300350':
        return 'Rs.3,00,000 to Rs.3,50,000'
    elif a=='350400':
        return 'Rs.3,50,000 to Rs.4,00,000'
    else:
        return 'Rs.5,00,000 to Rs.5,50,000'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    int_feat=[x for x in request.form.values()]
    fin_feat = pd.DataFrame(data=np.array(int_feat).reshape(1,20),columns=cols)
    #pred = mod.predict(fin_feat)
    a1 = mod.predict(fin_feat)
    
    return render_template('index.html',prediction_text=fnc1(a1))

if __name__ == '__main__':
 	app.run(debug=True)
