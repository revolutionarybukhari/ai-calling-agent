from pymongo import MongoClient
from config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client.Cluster0
# Collection Definitions
users_collection = db.users
session_logs_collection = db.session_logs
therapy_progress_collection = db.therapy_progress
appointments_collection = db.appointments
chat_history_collection = db.chat_history

# User operations
def add_user(user_data):
    return users_collection.insert_one(user_data).inserted_id

def get_user(user_id):
    return users_collection.find_one({"_id": user_id})

def update_user(user_id, update_data):
    users_collection.update_one({"_id": user_id}, {"$set": update_data})

def get_userid_by_phone(phone):
    return users_collection.find_one({"phone": phone})['_id']

def verify_user(phone):
    return users_collection.find_one({"phone": phone}) is not None

def has_interacted_before(phone):
    user = users_collection.find_one({"phone": phone})
    if user is not None:
        return user.get('has_interacted_before', False)
    return False

def set_interacted_before(phone):
    users_collection.update_one({"phone": phone}, {"$set": {"has_interacted_before": True}})
    return True


# Session logs operations
def add_session_log(session_data):
    return session_logs_collection.insert_one(session_data).inserted_id

def get_session_logs(user_id):
    return list(session_logs_collection.find({"user_id": user_id}))

# Therapy progress operations
def add_therapy_progress(progress_data):
    return therapy_progress_collection.insert_one(progress_data).inserted_id

def get_therapy_progress(user_id):
    return list(therapy_progress_collection.find({"user_id": user_id}))

def update_therapy_progress(progress_id, update_data):
    therapy_progress_collection.update_one({"_id": progress_id}, {"$set": update_data})

# Appointment operations
def book_appointment(userid,appointment_data):
    return appointments_collection.insert_one({"user_id":userid},{"appointment_data":appointment_data})

def get_appointments(user_id):
    return list(appointments_collection.find({"user_id": user_id}))

def update_appointment(appointment_id, update_data):
    appointments_collection.update_one({"_id": appointment_id}, {"$set": update_data})

def delete_appointment(appointment_id):
    appointments_collection.delete_one({"_id": appointment_id})

# Chat history operations
def set_chat_history(user_id, message_data):
    """
    Creates a new chat history record or updates an existing one for a user.
    """
    chat_history_collection.update_one(
        {"user_id": user_id},
        {"$push": {"messages": {"$each": message_data}}},  # Using $each to add all elements
        upsert=True
    )

def get_chat_history(user_id):
    """
    Retrieves the chat history for a specific user.
    """
    return chat_history_collection.find_one({"user_id": user_id})

def update_chat_history(user_id, update_data):
    """
    Updates the chat history record for a specific user.
    """
    chat_history_collection.update_one(
        {"user_id": user_id},
        {"$set": update_data}
    )