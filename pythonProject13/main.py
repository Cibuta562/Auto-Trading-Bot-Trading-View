import json, config
from flask import Flask, request, jsonify

app = Flask(__name__)


###########imports############

@app.route('/')
def nu_sex():
    return "Merge !! "


@app.route('/auto_trade', methods=['POST'])
def auto_trade():
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error"
        }

    print(data['ticker'])

    return {"code": "success",
            "message": data
            }


if __name__ == '__main__':
    app.run()
