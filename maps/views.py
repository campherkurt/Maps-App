from maps import app, models
from common.helpers import api_response

@app.route('/map/<map_id>/', methods=['GET', 'POST'])
def map(map_id):
    map = models.Map.query.filter_by(id=map_id).all()
    return api_response(map)

@app.route('/map/meta/<map_id>/', methods=['GET', 'POST'])
def map_meta(map_id):
    meta = models.MapMeta.query.filter_by(id=map_id).all()
    return api_response(map)

@app.route('/map/markers/<map_id>/', methods=['GET', 'POST'])
def map_markers(map_id):
    markers = models.MapMarker.query.filter_by(id=map_id).all()
    return api_response(map)