from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reference(db.Model):
    __tablename__ = 'references'
    id = db.Column('reference_PK', db.Integer, primary_key=True)
    campaign_id = db.Column('reference_FK_campaign_PK', db.Integer, nullable=False)
    name = db.Column('reference_name', db.String(50), nullable=False)
    details = db.Column('reference_details', db.String(255))
    created = db.Column('reference_created', db.DateTime, nullable=False)
    modified = db.Column('reference_modified', db.DateTime)

    def dictionary(self):
        return {
            'id': self.id,
            'campaign_id': self.campaign_id,
            'name': self.name,
            'details': self.details,
            'created': self.created.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'modified': self.modified.strftime('%Y-%m-%dT%H:%M:%S.%f')
        }
