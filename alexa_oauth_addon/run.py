from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

@app.route('/auth/authorize')
def authorize():
    redirect_uri = request.args.get('redirect_uri')
    state = request.args.get('state')
    code = 'dummy-auth-code'
    return redirect(f"{redirect_uri}?code={code}&state={state}")

@app.route('/auth/token', methods=['POST'])
def token():
    return jsonify({
        "access_token": "dummy-access-token",
        "token_type": "Bearer",
        "expires_in": 3600,
        "refresh_token": "dummy-refresh-token"
    })

if __name__ == '__main__':
    # Escoltem al port 5001 per fer servir el túnel configurat
    app.run(host='0.0.0.0', port=5001)
