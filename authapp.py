import os
from flask import Flask, request
from slackclient import SlackClient

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
oauth_scope = 'bot'

app = Flask(__name__)

@app.route("/begin_auth", methods=["GET"])
def pre_install():
    return '''
      <a href="https://slack.com/oauth/authorize?scope={0}&client_id={1}">
          Add to Slack
      </a>
    '''.format(oauth_scope, client_id)

@app.route("/finish_auth", methods=["GET", "POST"])
def post_install():
    auth_code = request.args['code']
    sc = SlackClient("")
    auth_response = sc.api_call("oauth.access", client_id=client_id, client_secret=client_secret, code=auth_code)

    os.environ["SLACK_USER_TOKEN"] = auth_response['access_token']
    os.environ["SLACK_BOT_TOKEN"] = auth_response['bot']['bot_access_token']

    return "Auth complete!"

if __name__ == '__main__':
    app.run(debug=True)
