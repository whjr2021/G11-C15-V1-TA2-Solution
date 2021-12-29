# From "firebase" library import "firebase" module
from firebase import firebase

# Establish connection between Python and Car Racing databse created on Firbase. 
# The connection is stored in the variable "db"
# Before running the code replace the database URL -https://car-racing-b9871-default-rtdb.firebaseio.com/ 
# in FirebaseApplication() with your database URL created in TA1.
db = firebase.FirebaseApplication('https://car-racing-b9871-default-rtdb.firebaseio.com/', None)

# Add player1 data to db. player1 name is stored as John
db.put("","player1","John")
