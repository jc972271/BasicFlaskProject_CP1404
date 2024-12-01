from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=0.0):
    return f"Celsius: {str(celsius)} degrees converts to Fahrenheit: {str(convert_celsius_to_fahrenheit(celsius))} degrees"


def convert_celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
