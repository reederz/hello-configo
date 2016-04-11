from functools import wraps
from flask import request, Response, Flask, url_for


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

app = Flask(__name__)

@app.route('/prod.yml')
@requires_auth
def prod_conf():
    return app.send_static_file('./prod.yml')

@app.route('/dev.yml')
@requires_auth
def dev_conf():
    return app.send_static_file('./dev.yml')

if __name__ == '__main__':
    app.run(port=8000)
