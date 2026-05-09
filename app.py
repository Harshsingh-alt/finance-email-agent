import streamlit as st
import pandas as pd
from logic import get_overdue_days, get_tone
from email_generator import generate_email

st.title("Finance Credit Follow-Up Email Agent")

df = pd.read_csv("sample_data.csv")

results = []

for index, row in df.iterrows():

    overdue_days = get_overdue_days(row["due_date"])
    tone = get_tone(overdue_days)

    email = generate_email(
        row["client_name"],
        row["invoice_no"],
        row["amount"],
        row["due_date"],
        overdue_days,
        tone
    )

    results.append({
        "Client": row["client_name"],
        "Invoice": row["invoice_no"],
        "Overdue Days": overdue_days,
        "Tone": tone,
        "Generated Email": email
    })

result_df = pd.DataFrame(results)

st.dataframe(result_df)

for r in results:
    st.subheader(f"{r['Client']} - {r['Tone']}")
    st.write(r["Generated Email"])