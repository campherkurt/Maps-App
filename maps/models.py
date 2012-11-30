import json

from maps import db
from common.helpers import as_dict

class Map(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique=True)
    user_id = db.Column(db.String(120), index = True)
    deleted = db.Column(db.Boolean(), default=False)

    def __init__(self, data):
        self.name = data['name']
        self.user_id = data['user_id']
        self.name = data['name']
        self.deleted = False

    def __repr__(self):
        return '<Map id:%s ,name: %r, user_id: %s, deleted:%s>' % (self.id, self.name, self.user_id, self.deleted)

    def as_dict(self):
        return as_dict(self)

class MapMarker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    markup = db.Column(db.String(200))
    coordinates = db.Column(db.String())

    map_id = db.Column(db.Integer, db.ForeignKey('map.id'))
    map = db.relationship('Map', backref=db.backref('marker'))

    def __init__(self, data):
        data['coordinates'] = json.dumps(data['coordinates'])
        self.name = data['name']
        self.title = data['title']
        self.markup = data['markup']
        self.coordinates = data['coordinates']
        self.map_id = data['map_id']

    def __repr__(self):
        return '<MapMarker id:%s, name:%s , title:%s , map_id:%s >' % (self.id, self.name, self.title, self.map_id)

    def as_dict(self):
        mk_dict = as_dict(self)
        mk_dict['coordinates'] = json.loads(mk_dict['coordinates'])
        return mk_dict

class MapMeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_styling = db.Column(db.String(200))
    marker_styling = db.Column(db.String(200))

    map_id = db.Column(db.Integer, db.ForeignKey('map.id'))
    map = db.relationship('Map', backref=db.backref('mapmeta'))

    def __init__(self, data):
        self.map_styling = data['map_styling']
        self.marker_styling = data['marker_styling']
        self.map = data['map']

    def __repr__(self):
        return '<MapMeta id:%s , map_id:%s >' % (self.id, self.map_id)

