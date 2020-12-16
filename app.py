from flask import Flask, Blueprint, render_template
from controllers.merchant_controller import merchants_blueprint

app = Flask(__name__)

app.register_blueprint(merchants_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
