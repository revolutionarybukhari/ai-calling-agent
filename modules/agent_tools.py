from .mongodb import get_userid_by_phone,get_chat_history, set_chat_history, update_chat_history, get_user, add_user, update_user, add_session_log, get_session_logs, add_therapy_progress, get_therapy_progress, update_therapy_progress, book_appointment, get_appointments, update_appointment, delete_appointment
import datetime
#     Updates the chat history for a specific user.
def get_history(user_phone):
    """
    Retrieves the chat history for a specific user.
    """
    user_id = get_userid_by_phone(user_phone)

    return get_chat_history(user_id)

def set_history(user_phone, message_data):
    """
    Creates a new chat history record or updates an existing one for a user.
    """
    user_id = get_userid_by_phone(user_phone)

    set_chat_history(user_id, message_data)

def booking(user_phone, user_message,appointment_time):
    """
    Creates a new chat history record or updates an existing one for a user.
    """
    user_id = get_userid_by_phone(user_phone)
    appointment_data = {
        "user_id": user_id,
        "location": user_message,
        "date": datetime.now(),
        "status": "pending",
        "appointment_time": appointment_time
    }
    user_id=get_userid_by_phone(user_phone)
    book_appointment(user_id,appointment_data)

