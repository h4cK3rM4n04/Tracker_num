#bibliothèque phonenumbers --.-- opencage --.-- carrier--..-- follium
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

#Trouver le pays du numéro
num = "+261345018094"
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")
print(localisation)

#Trouver l'opérateur mobile
operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, 'fr'))

#Trouver la latitude et la longitude
clef = 'ee9bbae0c73e42f1a3c2ab6fc677a763'
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]['geometry']['lat']
lng = reponse[0]['geometry']['lng']
print(lat, lng)

#Création du Map
monmap = folium.Map(location = [lat, lng], zoom_start = 12)
folium.Marker([lat, lng], popup =localisation).add_to(monmap)
monmap.save('map.html')