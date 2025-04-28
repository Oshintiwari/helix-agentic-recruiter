# # backend/services/agent_service.py

# from models.database import save_message
# # import openai  # Uncomment if you fix billing in future
# # import os

# # Uncomment if real OpenAI use
# # openai.api_key = os.getenv("OPENAI_API_KEY")

# def process_user_message(user_message):
#     """
#     Process the user's message and return an AI response.
#     Saves the conversation into the database.
#     """
#     try:
#         # If OpenAI was available, use this:
#         # response = openai.ChatCompletion.create(
#         #     model="gpt-3.5-turbo",
#         #     messages=[{"role": "user", "content": user_message}]
#         # )
#         # ai_response = response['choices'][0]['message']['content']

#         # Since OpenAI quota is exhausted, use mock agent behavior:
#         user_message_lower = user_message.lower()

#         if "machine learning" in user_message_lower:
#             ai_response = "Let's create a recruiting sequence for hiring a machine learning engineer."
#         elif "backend" in user_message_lower:
#             ai_response = "Let's draft a backend engineer outreach plan together!"
#         elif "frontend" in user_message_lower:
#             ai_response = "I'll help you create a frontend engineer hiring sequence."
#         elif "data scientist" in user_message_lower:
#             ai_response = "I'm drafting a sequence to attract top data scientist candidates."
#         else:
#             ai_response = "Thanks for the input! I'm preparing a recruiting sequence now."

#     except Exception as e:
#         print(f"[Agent Service Error]: {e}")
#         ai_response = f"FAKE AI RESPONSE for '{user_message}'"

#     # Save user message and AI response into database
#     save_message(user_message, ai_response)

#     return ai_response


import openai
import os
from models.database import save_message

openai.api_key = os.getenv("OPENAI_API_KEY")  # or hardcode temporarily for testing

def process_user_message(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful recruiter assistant. Build outreach sequences based on user ideas."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7
        )
        ai_response = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"[Agent Service Error]: {e}")
        ai_response = f"Error: {e}"

    save_message(user_message, ai_response)
    return ai_response
