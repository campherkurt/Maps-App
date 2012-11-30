from maps import models, db
import json

map_data = {'name':'test kurt 1', 'user_id':'12324', 'deleted':False}

marker_data = [
    {'coordinates': {'lat':-33.989976, 'long':18.501597}, 'name': "lansdowne", 'title': "Lansdowne Church", 'markup': "Cnr of Leafmore Rd and Kritzinger Rd<br/>Kenwyn<br/>Ps.: Dan Serb<br/>Elder: Nigel Tyhalibongo<br/>xtyhalibongo@uwc.ac.za"},
    {'coordinates': {'lat':-34.02669, 'long':18.466301}, 'name': "plumstead", 'title': "Plumstead Church", 'markup': "242 Main Road<br/>Plumstead<br/>Ps.: Dan Serb<br/>Elder: Eric Bender<br/>redneb@telkomsa.net"},
    {'coordinates': {'lat':-33.950358, 'long':18.470487}, 'name': "mowbray", 'title': "Mowbray Church", 'markup': "10 Bollihope Crescent<br/>Mowbray<br/>Ps.: Dan Serb<br/>Head Eldr: Simon Hayes<br/>sdamb@xsinet.co.za"},
    {'coordinates': {'lat':-34.010946, 'long':18.474093}, 'name': "wynberg", 'title': "Wynberg Church", 'markup': "10 Hertford Road<br/>Wynberg<br/>Ps.: Dan Serb<br/>Elder: R Langenhoven<br/>randall@wescape.co.za"},
    {'coordinates': {'lat':-33.982736, 'long':18.463622}, 'name': "claremont", 'title': "Claremont Church", 'markup': "21 Grove Avenue<br/>Claremont<br/>Ps.: Dan Serb<br/>Elder: A Adriaanse<br/>aa@whs.wcape.school.za"},
    {'coordinates': {'lat':-34.139261, 'long':18.42968}, 'name': "fish-hoek", 'title': "Fish Hoek Church", 'markup': "Recreation Road<br/>Fish Hoek<br/>Ps.: Dan Serb<br/>Elder: Jonathan Edwards<br/>elder@fishhoeksda.co.za"},
]

map = models.Map(map_data)

db.session.add(map)
db.session.commit()

for mark in marker_data:
    mark.update({'map_id':map.id})
    marker = models.MapMarker(mark)
    db.session.add(marker)

db.session.commit()

mk = models.MapMarker.query.filter_by(name='plumstead').first()
print mk
