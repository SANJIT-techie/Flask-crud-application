from flask import Flask, render_template




app = Flask(__name__)


@app.route('/') #initally when the website is opened return the following function or anything mentioned below                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
def Index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True,port=5009)