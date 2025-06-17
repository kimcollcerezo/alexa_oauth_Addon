from flask import Flask, request, redirect, jsonify
app = Flask(__name__)
@app.route('/auth/authorize')
def authorize():
    redirect_uri = request.args.get('redirect_uri')
    state = request.args.get('state')
    return redirect(f"{redirect_uri}?code=dummy-auth-code&state={state}")
@app.route('/auth/token', methods=['POST'])
def token():
    return jsonify({
        "access_token":"dummy-access-token",
        "token_type":"Bearer",
        "expires_in":3600,
        "refresh_token":"dummy-refresh-token"
    })
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)
