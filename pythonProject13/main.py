from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def nu_sex():
    return "Merge !! "

@app.route('/auto_trade' , methods= ['POST'])
def auto_trade():
    print(request)
    return {"code": "success" }

if __name__ == '__main__':
    app.run()
