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

@app.route("/shop-single")
def shop_single():
    return render_template('shop-single.html')

@app.route("/check-out")
def check_out():
    return render_template('checkout.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
