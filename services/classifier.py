def classify_ticket(text: str):
    text = text.lower()

    if any(word in text for word in ["refund", "charged", "payment", "billing"]):
        intent = "billing"
    elif any(word in text for word in ["error", "bug", "not working", "issue"]):
        intent = "technical"
    elif any(word in text for word in ["account", "login", "password"]):
        intent = "account"
    else:
        intent = "other"

    if any(word in text for word in ["urgent", "immediately", "asap", "now"]):
        urgency = "critical"
        priority = "P1"
    elif "refund" in text:
        urgency = "high"
        priority = "P2"
    else:
        urgency = "medium"
        priority = "P3"

    confidence = 0.85  # placeholder, realistic value

    return {
        "intent": intent,
        "urgency": urgency,
        "priority": priority,
        "confidence": confidence
    }
