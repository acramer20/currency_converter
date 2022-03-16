from crypt import methods
from flask import Flask, session, redirect, render_template, jsonify, request, flash 
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug = DebugToolbarExtension(app)

responses = []
@app.route('/')
def home_page():
    """Showing the currency converter page/form"""
    return render_template('index.html', responses=responses)

@app.route('/convert', methods=['POST'])
def convert_currency():
    """converting the currency from specified currency to desired currency"""
    fromCurr = request.form['fromCurr']
    toCurr = request.form['toCurr']
    amount = request.form['amount']



    if fromCurr != 'USD' and fromCurr != 'EUR' and fromCurr !='GBP':
        flash(f'Not a valid code: {fromCurr}', 'error')
        return redirect('/')
    if toCurr != 'USD' and toCurr != 'GBP' and toCurr != 'EUR':
        flash(f'Not a valid code: {toCurr}', 'error')
        return redirect('/')
    if int(amount) < 0:
        flash(f'Not a valid amount: {amount}', 'error')
        return redirect('/')

    c = CurrencyRates()
    s = CurrencyCodes()

    fromSym = s.get_symbol(fromCurr)
    toSym = s.get_symbol(toCurr)

    response = c.convert(fromCurr.upper(), toCurr.upper(), float(amount))
    rounded = round(response,2)
    resp = f"{fromSym}{amount} {fromCurr} equals {toSym}{str(rounded)} {toCurr}"
    responses.clear()
    responses.append(resp)
    return redirect('/')


    # for tests, try testing if the current rate is blank then the answer should be... blank instead of hard coding.
