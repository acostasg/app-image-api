from flask_sqlalchemy import SQLAlchemy


class ConnectionBBDD:
    def __init__(self, app, config):
        self.app = app
        self.config = config

    def set_config(self):
        # Persistence layer - connection to BBDD
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "{}://{}:{}@{}:{}/{}".format(
            self.config.get('connection.adapter'),
            self.config.get('connection.username'),
            self.config.get('connection.password'),
            self.config.get('connection.host'),
            self.config.get('connection.port'),
            self.config.get('connection.database'),
        )
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SECRET_KEY'] = self.config.get('secretKey')
        return SQLAlchemy(self.app)
