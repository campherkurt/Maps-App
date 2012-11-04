from maps import db

class Map(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    user_id = db.Column(db.String(120), index = True, unique = True)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<Map id:%s ,name: %r, user_id: %s>' % (self.id, self.name, self.user_id)


class MapMarker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    details = db.Column(db.String(200))
    coordinates = db.Column(db.String())
    user_id = db.Column(db.Integer)

    map_id = db.Column(db.Integer, db.ForeignKey('map.id'))
    map = db.relationship('Map', backref=db.backref('marker'))

    def __init__(self, data):
        self.name = data['name']
        self.title = data['title']
        self.details = data['details']
        self.coordinates = data['coordinates']
        self.user_id = data['user_id']
        self.map_id = data['map_id']

    def __repr__(self):
        return '<MapMarker id:%s, name:%s , title:%s , user_id:%s , map_id:%s >' % (self.id, self.name, self.title, self.user_id, self.map_id)

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

