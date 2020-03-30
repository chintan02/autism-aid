import pyrebase
import firebase
firebaseConfig ={
            "apiKey": "AIzaSyDbEslT3tpBwDTDQfP_8ZOMRBGObKEUjao",
            "authDomain": "autism-aid.firebaseapp.com",
            "databaseURL": "https://autism-aid.firebaseio.com",
            "projectId": "autism-aid",
            "storageBucket": "autism-aid.appspot.com",
            "messagingSenderId": "616345484183",
            "appId": "1:616345484183:web:406ce8cb76552cf5b9a2d2",
            "measurementId": "G-9HBX2L5ZWE"
}
firebase = pyrebase.initialize_app(firebaseConfig)
str1='ques'
str2='8'
db = firebase.database()
data={str1:str2}

file = open("login.txt","r")
line = file.readline()
print(line)
db.child("users").child(str(line)).set(data)
