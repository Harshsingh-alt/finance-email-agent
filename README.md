# Finance Credit Follow-Up Email Agent

## Overview
The Finance Credit Follow-Up Email Agent is an AI-powered automation system that helps finance teams generate professional payment reminder emails for overdue invoices.

The system automatically:
- Reads invoice records from CSV
- Detects overdue payments
- Applies tone escalation logic
- Generates AI-powered follow-up emails
- Displays results in a Streamlit dashboard

---

# Features

- AI-generated payment reminder emails
- Dynamic tone escalation
- Overdue invoice detection
- Streamlit interactive dashboard
- CSV-based invoice management
- OpenAI API integration via OpenRouter

---

# Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend/UI | Streamlit |
| Data Processing | Pandas |
| AI Model | GPT-3.5 Turbo |
| API Provider | OpenRouter |
| Environment Variables | python-dotenv |

---

# Project Architecture

CSV Invoice Data  
↓  
Overdue Detection Logic  
↓  
Tone Escalation Engine  
↓  
AI Email Generation  
↓  
Streamlit Dashboard Output

---

# Tone Escalation Logic

| Overdue Days | Tone |
|---|---|
| 1–7 Days | Warm & Friendly |
| 8–14 Days | Polite but Firm |
| 15–21 Days | Formal & Serious |
| 22–30 Days | Stern & Urgent |
| 30+ Days | Escalation Required |

---

# Security Measures

- API keys stored securely using `.env`
- No hardcoded credentials
- Local CSV processing
- Secure environment variable handling

---

# LLM & Framework Choice

The project uses GPT-3.5 Turbo through OpenRouter because it provides:
- fast response generation
- affordable/free API access
- reliable text generation
- easy integration with Python applications

Streamlit was selected because it enables rapid dashboard development with minimal frontend complexity.

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/finance-email-agent.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Project

```bash
streamlit run app.py
```

---

# Sample Output

The dashboard displays:
- Client details
- Invoice number
- Overdue days
- Escalation tone
- AI-generated follow-up emails

---

# Future Improvements

- Real email sending integration
- PDF invoice support
- Database integration
- Admin dashboard
- Authentication system

---

# Testing Mode

This project runs in dry-run mode and does not send real emails to clients. It only generates sample AI-powered follow-up emails for demonstration and testing purposes.

# Author

Harsh Singh Rajput
