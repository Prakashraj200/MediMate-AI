import os
import firebase_admin
from firebase_admin import credentials, firestore


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVICE_ACCOUNT_PATH = os.path.join(
    BASE_DIR,
    "config",
    "firebase-service-account.json"
)


def initialize_firebase():
    """Initialize Firebase Admin SDK and return Firestore client."""

    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)

    return firestore.client()


db = initialize_firebase()