import json

def as_dict(query_set):
    data = []
    for object in query_set:
        dict = object.__dict__.copy()
        if dict.get('_sa_instance_state'):
            del dict['_sa_instance_state']
        data.append(dict)
    return data

def as_json(data):
    return json.dumps(data)

def api_response(query_set):
    if not query_set:
        return ('Object Not Found', 404, {})
    dict = as_dict(query_set)
    json_data = as_json(dict)
    return (json_data, 200, {'Content-Type':'text/json'})


