def classify_ticket(text: str):
    text = text.lower()

    if any(word in text for word in ["refund", "charged", "payment", "billing"]):
        intent = "billing"
        confidence = 0.85
    elif any(word in text for word in ["error", "bug", "not working", "issue"]):
        intent = "technical"
        confidence = 0.80
    elif any(word in text for word in ["account", "login", "password"]):
        intent = "account"
        confidence = 0.78
    else:
        intent = "other"
        confidence = 0.60

    if any(word in text for word in ["urgent", "immediately", "asap", "now"]):
        urgency = "critical"
        priority = "P1"
    elif intent == "billing":
        urgency = "high"
        priority = "P2"
    else:
        urgency = "medium"
        priority = "P3"

    return intent, urgency, priority, confidence
