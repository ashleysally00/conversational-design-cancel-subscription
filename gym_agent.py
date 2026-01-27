def extract_service(text):
    text = text.lower()
    if "gym" in text or "subscription" in text or "membership" in text:
        return "gym"
    return None


def handle_input(text):
    service = extract_service(text)

    if not service:
        return "I can help cancel a gym membership. What would you like to do?"

    return "Okay — I can help you cancel your gym membership. Do you want step-by-step instructions?"

if __name__ == "__main__":
    while True:
        text = input("What would you like help with? ")
        response = handle_input(text)
        print("Agent:", response)
