"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject2 import app

@app.route('/')
@app.route('/home/<uid>')
def home(uid):
 
    try:
        import os
        import face_recognition
        import pyodbc 
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=bsafe.database.windows.net;'
                              'Database=BSDMS;'
                              'uid=Srichid;pwd=Bsafe@123')

        cursor = conn.cursor()
        #userid = int(uid)
        cursor.execute('SELECT * FROM UserVerification where Uid='+uid)
        row = cursor.fetchone()

        import os
        import face_recognition

        # make a list of all the available images

        # load your image

        import urllib
        resource = urllib.request.urlopen(row[2])
        output = open("C:/Users/Srichid/Desktop/face project/dataset/"+uid+"1.jpg","wb")
        output.write(resource.read())
        output.close()
        image_to_be_matched = face_recognition.load_image_file('C:/Users/Srichid/Desktop/face project/dataset/'+uid+'1.jpg')

        # encoded the loaded image into a feature vector
        image_to_be_matched_encoded = face_recognition.face_encodings(
            image_to_be_matched)[0]

        #print(image_to_be_matched_encoded)

        # iterate over each image
        resource = urllib.request.urlopen(row[3])
        output = open("C:/Users/Srichid/Desktop/"+uid+"2.jpg","wb")
        output.write(resource.read())
        output.close()
        current_image = face_recognition.load_image_file( 'C:/Users/Srichid/Desktop/'+uid+'2.jpg')
            # encode the loaded image into a feature vector
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
            # match your image with the image and check if it matches
        result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
            # check if it was a match
        if result[0] == True:
            print ("Matched" )
        else:
            print ("Not matched" )
    except(Exception):
        return ("Not matched")
