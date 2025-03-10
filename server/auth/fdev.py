from authlib.integrations.flask_client import OAuth
from flask import url_for, redirect, session
import os

oauth = OAuth()

def configure_oauth(app):
    app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')

    oauth.init_app(app)
    oauth.register(
        name='oauth2',
        client_id=os.getenv('OAUTH2_CLIENT_ID'),
        client_secret=os.getenv('OAUTH2_CLIENT_SECRET'),
        authorize_url=os.getenv('AUTH_URL') + "/auth",
        authorize_params=None,
        access_token_url=os.getenv('AUTH_URL') + "/token",
        access_token_params=None,
        refresh_token_url=None,
        redirect_uri=os.getenv('AUTH_CALLBACK', 'http://localhost:5001/auth/callback'),
        client_kwargs={'scope': 'auth capi'},
    )

    @app.route('/login')
    def login():
        redirect_uri = url_for('auth_callback', _external=True)
        return oauth.oauth2.authorize_redirect(redirect_uri)

    @app.route('/auth/callback')
    def auth_callback():
        token = oauth.oauth2.authorize_access_token()
        user_info = oauth.oauth2.parse_id_token(token)
        session['user'] = user_info
        return redirect(url_for('index'))

    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('index'))