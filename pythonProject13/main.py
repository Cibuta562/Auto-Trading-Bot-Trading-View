from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def nu_sex():
    return "Merge !! "

@app.route('/auto_trade' , methods= ['POST'])
def auto_trade():
    data = json.loads(request.data)
    print(data[''])

    return {"code": "success",
            "message": data
            }

if __name__ == '__main__':
    app.run()
