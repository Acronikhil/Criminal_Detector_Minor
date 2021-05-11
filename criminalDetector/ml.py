import face_recognition
import sys
import os
# C:\Users\HP\Downloads\minor assets\Criminal\Osama\pic
# directory = r'F:\Minor Criminal\CD\minor\media\Criminal_Images'


def detect(toSearch):
    temp = 0
    crimPath = ""
    directory = r'F:/Minor Criminal/CD/minor/media/Criminal_Images'
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(os.path.join(directory, filename))

            image_of_Criminal = face_recognition.load_image_file(
                os.path.join(directory, filename))

            face_encoding = face_recognition.face_encodings(image_of_Criminal)[
                0]
            # print("face_encoding = ", face_encoding[0])
            Unknown_Criminal = face_recognition.load_image_file(
                f'F:/Minor Criminal/CD/minor/media/{toSearch}')

            Unknown_encoding = face_recognition.face_encodings(Unknown_Criminal)[
                0]
            # print("Unknown_encoding = ", Unknown_encoding[0])
            results = face_recognition.compare_faces(
                [face_encoding], Unknown_encoding)

            if results[0]:
                print("Criminal Detected:")
                crimPath = filename
                print('Path:', crimPath)
                # return crimPath
                temp = 1
                break
            else:
                # print("Criminal Not Detected:")
                temp = 0

        else:
            continue

    if temp == 1:
        return crimPath
    else:
        return "NOT FOUND"
