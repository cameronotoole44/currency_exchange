
from flask import Flask, render_template, request
from currency_exchange import Currency

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        # creating an object(Currency) and converting it 
        currency = Currency(value, from_unit)
        currency.changeTo(to_unit)


        result = str(currency)
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)