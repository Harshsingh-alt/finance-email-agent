from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_email(client_name, invoice, amount, due_date, overdue_days, tone):

    prompt = f"""
    Write a professional finance payment follow-up email.

    Client Name: {client_name}
    Invoice Number: {invoice}
    Amount Due: ₹{amount}
    Due Date: {due_date}
    Days Overdue: {overdue_days}
    Tone: {tone}

    Make the email professional and realistic.
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content