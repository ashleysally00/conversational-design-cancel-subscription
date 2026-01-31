import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def is_valid_email(text):
    """Check if the text is a valid email format."""
    if not text:
        return False
    return bool(EMAIL_REGEX.match(text.strip()))

def extract_service(text):
    """Extract service type from user input."""
    text = text.lower()
    if "gym" in text or "subscription" in text or "membership" in text:
        return "gym"
    return None

def ask_service():
    """Initial prompt to understand user intent."""
    print("\nAgent: What would you like help with?")
    user_input = input("You: ").strip()
    
    service = extract_service(user_input)
    if not service:
        print("Agent: I can help cancel a gym membership. What would you like to do?")
        return ask_service()
    
    print("Agent: Okay — I can help you cancel your gym membership. Would you like step-by-step instructions?")
    response = input("You: ").strip().lower()
    
    if response in ["yes", "y", "sure", "ok", "okay"]:
        return ask_email()
    elif response in ["no", "n"]:
        print("Agent: No problem. Let me know if you need help with anything else.")
        return None
    else:
        print("Agent: I can help cancel a gym membership. What would you like to do?")
        return ask_service()

def ask_email():
    """Ask for the user's email and validate it."""
    print("\nAgent: To proceed with cancellation, I'll need the email address associated with your membership.")
    email_input = input("You: ").strip().lower()
    
    # 1. NEW FLEXIBLE EXIT CHECK
    # This catches "never mind", "nevermind", or "I want to stop"
    exit_keywords = ["no", "cancel", "stop", "exit", "never mind", "nevermind"]
    if any(keyword in email_input for keyword in exit_keywords):
        print("Agent: No problem. Your membership has not been canceled.")
        return None
    
    # 2. EMAIL VALIDATION
    if not is_valid_email(email_input):
        print("Agent: That doesn't look like a valid email address. Please enter a valid email so I can continue.")
        return ask_email()
    
    return confirm_cancellation(email_input)

def confirm_cancellation(email):
    """Final confirmation before cancellation."""
    print(f"\nAgent: Just to confirm: you want to cancel the gym membership associated with {email}. Is that correct?")
    print("Agent: This action cannot be undone. Please type 'yes' to proceed or 'no' to keep your membership.")
    
    confirmation = input("You: ").strip().lower()
    
    if confirmation in ["yes", "y"]:
        return cancel_subscription(email)
    elif confirmation in ["no", "n"]:
        print("Agent: Understood. Your membership has not been canceled.")
        return None
    else:
        print("Agent: Please answer yes or no.")
        return confirm_cancellation(email)

def cancel_subscription(email):
    """Process the cancellation."""
    print(f"\nAgent: I've recorded your request to cancel the gym membership for {email}.")
    print("Agent: In a real system, this is where the cancellation would be processed.")
    print("Agent: Is there anything else I can help you with?")
    return "success"

if __name__ == "__main__":
    print("=== Gym Membership Cancellation Assistant ===")
    ask_service()
