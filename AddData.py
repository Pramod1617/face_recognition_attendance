import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccounKey/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://facerecognition-6dd41-default-rtdb.firebaseio.com/"


})

ref = db.reference('Students')
data = {
    "321654":
        {
            "name":"Murtaza Hussan",
            "major":"Robotics",
            "Starting_years":2017,
            "total_attendance":6,
            "standing":"G",
            "year": 4,
            "Last_attendance_time":"2022-12-11 00:54:34"
        },
    "852741":
            {
                "name":"Emily Blunt",
                "major":"Economics",
                "Starting_years":2018,
                "total_attendance":9,
                "standing":"B",
                "year": 2,
                "Last_attendance_time":"2022-12-11 00:54:34"
            },
    "963852":
        {
            "name":"Elon Musk",
            "major":"Physics",
            "Starting_years":2011,
            "total_attendance":7,
            "standing":"M",
            "year": 5,
            "Last_attendance_time":"2022-12-11 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
