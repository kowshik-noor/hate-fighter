from flask_app import api, app
from flask_app.controllers.videos import RandomVideo

api.add_resource(RandomVideo, "/api")

if __name__ == '__main__':
    app.run(debug=True)