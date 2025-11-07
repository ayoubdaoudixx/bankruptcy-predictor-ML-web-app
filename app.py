import logging

from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler

application=Flask(__name__, static_folder='static')

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predictdata():
    from src.pipline.predict_pipline import CustomData, PredictPipeline
    if request.method=='GET':
        return render_template('predictdata.html')
    else:
        data=CustomData(
            atr1=float(request.form.get('atr1')),
            atr2=float(request.form.get('atr2')),
            atr3=float(request.form.get('atr3')),
            atr4=float(request.form.get('atr4')),
            atr5=float(request.form.get('atr5')),
            atr6=float(request.form.get('atr6')),
            atr7=float(request.form.get('atr7')),
            atr8=float(request.form.get('atr8')),
            atr9=float(request.form.get('atr9')),
            atr10=float(request.form.get('atr10')),
            atr11=float(request.form.get('atr11')),
            atr12=float(request.form.get('atr12')),
            atr13=float(request.form.get('atr13')),
            atr14=float(request.form.get('atr14')),
            atr15=float(request.form.get('atr15')),
            atr16=float(request.form.get('atr16')),
            atr17=float(request.form.get('atr17')),
            atr18=float(request.form.get('atr18')),
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipline=PredictPipeline()
        results = predict_pipline.predict(pred_df)
        logging.info(f"the prediction is {results}")
        if results[0]==1:
            return render_template('predictTrue.html')
        else:
            return render_template('predictFalse.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)