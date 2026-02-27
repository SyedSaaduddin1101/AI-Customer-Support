def generate_reply(ticket, faq_text):
    prompt = f"""
You are a customer support agent.

Ticket Subject: {ticket.subject}
Ticket Message: {ticket.message}

Company Knowledge Base:
{faq_text}

Write a polite, helpful response addressing the issue.
"""

    # Placeholder for AI (mocked for now)
    return f"Hi there,\n\nThanks for reaching out. Regarding your issue:\n{ticket.message}\n\nBased on our policy, refunds are processed within 5–7 business days. If you were charged twice, any extra amount will be reversed shortly.\n\nBest regards,\nSupport Team"
