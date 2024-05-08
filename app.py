from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def front_artisian():
    return render_template("front_artisian.html")

@app.route("/busca")
def front_busca():
    return render_template("front_busca.html")

if __name__ == "__main__":
    app.run(debug=True)