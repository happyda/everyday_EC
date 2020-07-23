from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
