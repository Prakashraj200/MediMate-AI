import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_SERVICE_ACCOUNT = os.path.join(BASE_DIR, "config", "firebase-service-account.json")
RENDER_SECRET_PATH = "/etc/secrets/firebase-service-account.json"

def initialize_firebase():
    """Initialize Firebase Admin SDK supporting Local, Render Secret Files, and Env Vars."""
    if not firebase_admin._apps:
        # 1. Environment Variable containing raw JSON string (Render / Cloud best practice)
        env_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT_JSON")
        if env_json:
            try:
                cert_data = json.loads(env_json)
                cred = credentials.Certificate(cert_data)
                firebase_admin.initialize_app(cred)
                return firestore.client()
            except Exception as e:
                print("Failed to initialize Firebase from FIREBASE_SERVICE_ACCOUNT_JSON env var:", e)

        # 2. Render Secret File mounted at /etc/secrets/
        if os.path.exists(RENDER_SECRET_PATH):
            cred = credentials.Certificate(RENDER_SECRET_PATH)
            firebase_admin.initialize_app(cred)
            return firestore.client()

        # 3. Local JSON credential file in repository
        if os.path.exists(LOCAL_SERVICE_ACCOUNT):
            cred = credentials.Certificate(LOCAL_SERVICE_ACCOUNT)
            firebase_admin.initialize_app(cred)
            return firestore.client()

        raise FileNotFoundError(
            f"Firebase service account not found. Checked: {LOCAL_SERVICE_ACCOUNT}, {RENDER_SECRET_PATH}, "
            "and FIREBASE_SERVICE_ACCOUNT_JSON env var."
        )

    return firestore.client()

db = initialize_firebase()
