import cohere

co = cohere.Client("pWOg0RlxmrZr27CYd1TdjR9N7Rv0BTQSjIJPowC4")

def converse(prompt: str) -> str:
    print("Calling Cohere Chat API...")

    try:
        response = co.chat(
            model="command-r",  
            message=prompt,
            temperature=0.7,
            max_tokens=150
        )

        result = response.text.strip()
        return result

    except Exception as e:
        print("Error communicating with Cohere API:", e)
        return "Sorry, I couldn't get a response. Please try again later."
