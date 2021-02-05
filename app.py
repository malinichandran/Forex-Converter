from flask import Flask, render_template, request ,redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdfgkjtjkkg45yfdb'

@app.route('/home')
def home_page():
    return render_template('homepage.html')
    

@app.route('/convert', methods = ['POST'])
def convert_page():
    rates_dict = list(cr.get_rates('USD'))
    convertFrom = request.form['convert from']
    convertTo = request.form['convert to']
    amount = float(request.form['amount'])
    symbol = cc.get_symbol(convertTo)
    #if rates_dict.keys()  >= {{convertFrom}, {convertTo}}:
    
       
    if all(key in rates_dict for key in (convertFrom,convertTo)):
        res = round(cr.convert(convertFrom, convertTo, amount),2)
        flash(f' The result is {symbol} {res}')
    else:
        
        flash(f'Please enter a valid currency code')
        
    
    return render_template('convert.html')
    
