from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="background-color: yellow;">Hello World!</h1>'

@app.route("/about", methods=["GET", "POST"])
def about():

    if request.method == "GET":
        return "GET METHOD CALLED\n"
    elif request.method == "POST":
        return "POST METHOD CALLED\n"
    else:
        return 'About Us'

@app.route('/contact/<rabta>')
def contact(rabta):
    return f"<h1>Contact Us at {rabta} </h1>"

# @app.route('/sum/<int:num1>/<int:num2>')
@app.route('/sum/<num1>/<num2>')
def rabta(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    return f"Sum of {num1} and {num2} = {num1+num2}"

@app.route('/url_params')
def url_params():
    name = request.args.get('name')
    age = request.args.get('age')
    if name and age:
        return f"<h1>{name} is {age}</h1>"
    elif name:
        return f"<h1>NAME is {name}</h1>"
    elif age:
        return f"<h1>AGE {age}</h1>"
    else:
        return f"<h1>NAME and AGE are required</h1>"


# if app.name == "__main__":

if __name__ == "__main__":
    app.run(debug=True)
