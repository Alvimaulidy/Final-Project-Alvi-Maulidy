import joblib
from flask import Flask, request, render_template

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
        input = request.form
        b = float(input['b'])
        k = float(input['k'])
        c = float(input['c'])
        ls = float(input['ls'])
        nr = float(input['nr'])
        g = float(input['g'])
        con = float(input['con'])
        bc = float(input['bc'])
        sc = float(input['sc'])
        iq = float(input['iq'])
        l = float(input['l'])
        nc = float(input['nc'])

        pred = Model.predict([[b, k, c,ls,nr,g,con,bc,sc,iq,l,nc]])[0]
        return render_template('result.html', data = input, prediksi = pred)



if __name__ == "__main__":
    Model = joblib.load('model')

    app.run(debug=True)