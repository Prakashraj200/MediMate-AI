from firebase_admin import auth

from backend.services.firebase_service import get_user


# =========================
# CREATE AUTH USER
# =========================

def create_auth_user(email, password):

    user_record = auth.create_user(
        email=email,
        password=password
    )

    return user_record


# =========================
# GET AUTH USER BY EMAIL
# =========================

def get_auth_user_by_email(email):

    try:
        user_record = auth.get_user_by_email(email)
        return user_record

    except auth.UserNotFoundError:
        return None


# =========================
# GET AUTH USER BY UID
# =========================

def get_auth_user_by_uid(uid):

    try:
        user_record = auth.get_user(uid)
        return user_record

    except auth.UserNotFoundError:
        return None


# =========================
# DELETE AUTH USER
# =========================

def delete_auth_user(uid):

    auth.delete_user(uid)

    return True