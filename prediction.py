import joblib
import pandas as pd

model = joblib.load('model')
realcolumn = joblib.load('realcolumn')
hotcolumn = joblib.load('xdummiescolumn')

def prediction(data):
    df = pd.DataFrame(data, index = [0])
    df = pd.get_dummies(df)
    df = df.reindex(columns = hotcolumn, fill_value = 0)
    hasil = model.predict(df)
    return hasil[0]
