import firebase_admin
from firebase_admin import credentials, firestore
from config.config import configuration
from datetime import datetime
import logging

_firebase_logger = logging.getLogger("firebase")

credPath = configuration.get_property("credPath") # Update with your Firebase key file path
# Initialize Firebase Admin SDK
cred = credentials.Certificate(credPath)  # Update with your Firebase key file path
firebase_admin.initialize_app(cred)
db = firestore.client()  # Initialize Firestore client

def save_password_to_firebase(
    encrypted_password, complexity, key, platform, collection_name="passwords"
):
    current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    doc_ref = db.collection(collection_name).document()

    data = {
        "encrypted_password": encrypted_password.decode(),
        "generated_time": current_time,
        "complexity": complexity,
        "encryption_key": key.decode(),
        "platform": platform,
    }

    doc_ref.set(data)
    _firebase_logger.info(
        f"Password details saved to Firebase in the '{collection_name}' collection."
    )
