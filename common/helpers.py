import json

def as_dict(query_set):
    data = []
    
    def get_dict(object):
        dict = object.__dict__.copy()
        if dict.get('_sa_instance_state'):
            del dict['_sa_instance_state']
        return dict

    if type(query_set) != list:
        return get_dict(query_set)
    
    for object in query_set:
        data.append(get_dict(object))
    return data

def as_json(data):
    return json.dumps(data)

def api_response(query_set):
    if not query_set:
        return ('Object Not Found', 404, {})
    dict = as_dict(query_set)
    json_data = as_json(dict)
    return (json_data, 200, {'Content-Type':'text/json'})
