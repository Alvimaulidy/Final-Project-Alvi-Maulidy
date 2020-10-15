import joblib
from flask import Flask, request, render_template
from prediction import prediction
app = Flask(__name__)



@app.route('/')
def home():
    
    return render_template('index.html')
@app.route('/pred')
def immo():
    
    return render_template('immo.html')


@app.route('/prediction', methods = ['POST','GET'])
def rent():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['newlyConst'] = bool(data['newlyConst'])
        data['balcony'] = bool(data['balcony'])
        data['picturecount'] = float(data['picturecount'])
        data['hasKitchen'] = bool(data['hasKitchen'])
        data['cellar'] = bool(data['cellar'])
        data['livingSpace'] = float(data['livingSpace'])
        data['noRooms'] = float(data['noRooms'])
        data['garden'] = bool(data['garden'])
        data['lift'] = bool(data['lift'])
        data['big_cities'] = bool(data['big_cities'])
        data['interiorQual'] = str(data['interiorQual'])
        data['typeOfFlat'] = str(data['typeOfFlat'])
        data['condition'] = str(data['condition'])
        

        

        hasil = int(prediction(data))
        return render_template('result.html', prediksi = hasil)



if __name__ == "__main__":
    Model = joblib.load('model')

    app.run(debug=True)