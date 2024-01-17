from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/profile2')
def profile2():
    return render_template("profile2.html")

@app.route('/profile3')
def profile3():
    return render_template("profile3.html")

@app.route('/done')
def done():
    return render_template("done.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get("name")
    email= request.args.get("email")
    print(name)
    print(email)
    props = {
        "name": name,
        "email": email
    }
    return render_template("confirmation.html", data=props)

if __name__ == '__main__':
    app.run(debug=True, port=3000)