from flask import Flask

from common import decorators, maps_abstract

app = Flask(__name__)

@app.route('/map/<map_id>/', methods=['GET', 'POST'])
@decorators.method_handler(maps_abstract.Map)
def map(map_id):
    pass

@app.route('/map/meta/<map_id>/', methods=['GET', 'POST'])
@decorators.method_handler(maps_abstract.MapMeta)
def map_meta(map_id):
    pass

@app.route('/map/markers/<map_id>/', methods=['GET', 'POST'])
@decorators.method_handler(maps_abstract.MapMarker)
def map_markers(map_id):
    pass 

@app.route('/map/user/<user_id>/', methods=['GET'])
@decorators.method_handler(maps_abstract.MapUser)
def maps_user(user_id):
    pass


if __name__ == '__main__':
    app.debug = True
    app.run()
