import google.generativeai as genai

# Configure your Gemini API Key

# from .views import Listdoc
from .models import Doc
from .models import ChatMessage
from django.contrib.auth.models import User
import pdfplumber

def generate_ai_description_from_pdf_text(text):
    genai.configure(api_key="AIzaSyBzAUSFhBrF4HPUUwxObFnXItzBf5ie0uM")
    client = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Read this PDF content and summarize about the file it in 2-3 professional sentences :\n\n{text[:8000]}"  # Truncate if long
    response = client.generate_content(prompt)
    return response.text

def generate_ai_user_response(usser,text):
    user_docs  = Doc.objects.filter(user=usser).values_list('Text', flat=True)
    concatenated_text = ' '.join(filter(None, user_docs))

    message_docs  = ChatMessage.objects.filter(user=usser).values_list('user_message', flat=True)
    message_text = ' '.join(filter(None, message_docs)) + text
    augmented_prompt = f"""
        Read this PDF content and find the answer to the question in 2-3 professional sentences.

        Context:  
        {concatenated_text}  

        Query: {message_text}
        """

    # DAT = Listdoc.as_view()

    
    genai.configure(api_key="AIzaSyBzAUSFhBrF4HPUUwxObFnXItzBf5ie0uM")
    client = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"{augmented_prompt}"  # Truncate if long
    response = client.generate_content(prompt)
    return response.text

# def extract_text_from_pdf(file_path):
#     text = ""
#     with fitz.open(file_path) as doc:
#         for page in doc:
#             text += page.get_text()
#     return text.strip()


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""  # Avoid NoneType
    return text.strip()
