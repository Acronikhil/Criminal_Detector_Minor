import face_recognition
import sys
import os
# C:\Users\HP\Downloads\minor assets\Criminal\Osama\pic
# directory = r'F:\Minor Criminal\CD\minor\media\Criminal_Images'
crimPath = ""
directory = r'C:\Users\HP\Downloads\minor assets\Criminal\Osama\pic'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directory, filename))

        image_of_Criminal = face_recognition.load_image_file(
            os.path.join(directory, filename))

        face_encoding = face_recognition.face_encodings(image_of_Criminal)[0]
        print("face_encoding = ", face_encoding[0])
        Unknown_Criminal = face_recognition.load_image_file(
            'C:/Users/HP/Downloads/minor assets/Criminal/test.jpg')

        Unknown_encoding = face_recognition.face_encodings(Unknown_Criminal)[0]
        print("Unknown_encoding = ", Unknown_encoding[0])
        results = face_recognition.compare_faces(
            [face_encoding], Unknown_encoding)

        if results[0]:
            print("He IS VIKAS DUBEY:", results)
            crimPath = os.path.join(directory, filename)
            print('Path:', crimPath)
        else:
            print("HE is TED BUNDY:", results)

    else:
        continue
