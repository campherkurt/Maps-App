from exceptions import NotImplementedError


class Base():

    @classmethod
    def get(self):
        raise NotImplementedError

    @classmethod
    def post(self):
        raise NotImplementedError

    @classmethod
    def put(self):
        raise NotImplementedError

    @classmethod
    def delete(self):
        raise NotImplementedError

class Map(Base):

    @classmethod
    def get(self):
        return "We got a GET playa"

    @classmethod
    def post(self):
        return "We got a POST playa"

class MapMeta(Base):

    @classmethod
    def get(self):
        return "We got a GET Meta playa"

    @classmethod
    def post(self):
        return "We got a POST Meta playa"

class MapMarker(Base):

    @classmethod
    def get(self):
        return "We got a GET Marker playa"

    @classmethod
    def post(self):
        return "We got a POST Marker playa"

class MapUser(Base):

    @classmethod
    def get(self):
        return "We got a GET Map User playa"