# From "firebase" library import "firebase" module
from firebase import firebase

# Establish connection between Python and Car Racing databse created on Firbase.
# The connection is stored in the variable "db"
db = firebase.FirebaseApplication('https://car-racing-b9871-default-rtdb.firebaseio.com/', None)

# Add player1 data to db
db.put("","player1","John")