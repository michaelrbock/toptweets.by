# [START gae_python38_app]
from flask import Flask, redirect, url_for


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/<screen_name>')
def redirect_to_search(screen_name):
    return redirect(twitter_search_url(screen_name))


@app.route('/@<screen_name>')
def redirect_with_at(screen_name):
    return redirect(twitter_search_url(screen_name))


def twitter_search_url(screen_name):
    return f"https://twitter.com/search?q=from%3A{screen_name}%20min_faves%3A50"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
