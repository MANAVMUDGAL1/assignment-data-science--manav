from flask import Flask,render_template,url_for,request,jsonify
import joblib

model1=joblib.load('kmeans_model.lb')
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inputdata')
def inputdata():
    return render_template('inputdata.html')

@app.route('/prediction' , methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
          
          N=int(request.form["N"])
          P=int(request.form["P"])
          K=int(request.form["K"])
          temp=int(request.form["Temp"])
          hum=int(request.form["Hum"])
          ph=int(request.form["ph"])  
          rain=int(request.form["rain"]) 
          
               
          user_data= [[N, P, K, temp, hum, ph, rain]]

          pred = model1.predict(user_data)[0]
          crops_dicts={1:('coffee,cotton ','R.jpg'),2:('pomegranate,coconut','pomegranate.jpg'),3:('grapes,apple','download.jpg'),4:('banana,maize','banana.jpg'),5:("mango,pigeonpeas","mango.jpg"),6:("mungbean ,blackgram","OIP.jpg"),7:("chickpea,kidneybeans","cp.jpg"),8:("rice,jute","rice.jpg"),9:("papaya,orange","pa.jpg"),10:("watermelon,muskmelon","wm.jpg")}
          
          crop_name, crop_image = crops_dicts[pred]
          
          return render_template('prediction.html', output=str(pred), crop_name=crop_name, crop_image=crop_image)
          
          

if __name__ == '__main__':
    app.run(debug=True)

print(__name__)