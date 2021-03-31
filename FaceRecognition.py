import face_recognition
import os

def recognize(known_path,unknown_path):
	"""Face recognizer"""

	#define full path

	
	if os.path.exists(known_path) and os.path.exists(unknown_path):
	
	
		#generate encoding for the known faces
		known_image=face_recognition.load_image_file(known_path)
		knwon_encodings=face_recognition.face_encodings(known_image)[0]

		#generate encoding for the unknown faces
		unknown_image=face_recognition.load_image_file(unknown_path)
		unknwon_encodings=face_recognition.face_encodings(unknown_image)[0]

		#compare the two encodings
		result=face_recognition.compare_faces([knwon_encodings],unknwon_encodings)

		return result[0]
	else:
		return False	

