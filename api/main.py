from flask_injector import FlaskInjector
from api import injectorContainer
from flask import Flask
from envyaml import EnvYAML
from api.application.controller.homeController import home
from api.application.controller.campaignController import campaign
from connectionBBDD import ConnectionBBDD

# Load yml config
config = EnvYAML('config/config.yml')

# Flask framework
app = Flask(__name__)

# Import other controller optional
app.register_blueprint(home)
app.register_blueprint(campaign)

# Persistence layer - configuration connection to BBDD
db = ConnectionBBDD(app, config).set_config()


@app.before_first_request
def before_first_request():
    FlaskInjector(app=app, modules=[injectorContainer.configure])


# Run application
app.run(port=config.get('port'), debug=config.get('debug'))
