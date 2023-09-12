# importing flask app and some functions
from flask import Flask, request, jsonify
import datetime


def create_app():
    # initializing flask app
    app = Flask(__name__)
    # giving the app a key (which is a configuration variable)
    app.config['SECRET_KEY'] = 'keykeyskeyss'
    return app

app = create_app()

# defining a route to map an endpoint to a function
# the endpoint being a get request that takes two parameters
@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"
    status_code = 200

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=False)
