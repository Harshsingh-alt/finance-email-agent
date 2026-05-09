from datetime import datetime

def get_overdue_days(due_date):
    due = datetime.strptime(due_date, "%Y-%m-%d")
    today = datetime.today()
    return (today - due).days

def get_tone(days):
    if days <= 7:
        return "Warm & Friendly"
    elif days <= 14:
        return "Polite but Firm"
    elif days <= 21:
        return "Formal & Serious"
    elif days <= 30:
        return "Stern & Urgent"
    else:
        return "Escalation Required"