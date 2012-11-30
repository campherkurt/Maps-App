from flask import request, render_template

from maps import app, models, db
from common.helpers import api_response, as_dict


@app.route('/map/', methods=['POST'])
@app.route('/map/<map_id>/', methods=['GET', 'PUT', 'DELETE'])
def map(map_id=None):
    if map_id:
        map = models.Map.query.filter_by(id=map_id, deleted=False).first()
        if not map: return api_response([])

    if request.method == 'DELETE':
        map.deleted = True
        db.session.commit()
        return ('Object Deleted', 200, {})

    if request.method == 'GET':
        pass

    if request.method == 'PUT':
        map.name = request.form['name']
        map.user_id = request.form['user_id']
        map.title = request.form['title']

    if request.method == 'POST':
        data = dict(
            name=request.form['name'],
            user_id=request.form['user_id'],
            title=request.form['title'],
        )
        map = models.Map(data)
        db.session.add(map)

    db.session.commit()
    return api_response([map])

@app.route('/map/meta/<map_id>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def map_meta(map_id):
    meta = models.MapMeta.query.filter_by(id=map_id).all()
    return api_response(map)

@app.route('/map/markers/<map_id>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def map_markers(map_id):
    markers = models.MapMarker.query.filter_by(id=map_id).all()
    return api_response(map)

@app.route('/map/view/<map_id>/', methods=['GET'])
def map_view(map_id):
    map = models.Map.query.filter_by(id=map_id, deleted=False).first()
    markers = [mk.as_dict() for mk in map.marker]
    content = {'map':map.as_dict(), 'markers':markers}
    return render_template('test.html', content=content)

