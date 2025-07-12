import pyautogui
import time
import pyperclip
from transformers import pipeline

# Set your own name exactly as it appears in the chat
YOUR_NAME = "Amitesh Pandey"

# Load Hugging Face text-generation model (you can use another if needed)
generator = pipeline("text-generation", model="gpt2")

def get_last_sender(chat_log):
    """
    Extract the sender of the last message from the WhatsApp chat log.
    """
    lines = [line.strip() for line in chat_log.strip().splitlines() if line.strip()]
    if not lines:
        return None

    last_line = lines[-1]

    try:
        # Example: [12:24 am, 25/5/2025] Deepankar bharti: Tm bhej do
        sender_part = last_line.split("] ", 1)[1]  # Get 'Deepankar bharti: Tm bhej do'
        sender_name = sender_part.split(":")[0].strip()  # Get 'Deepankar bharti'
        return sender_name
    except IndexError:
        return None

def generate_response(prompt):
    """
    Generate a response using Hugging Face transformer model.
    """
    result = generator(prompt, max_length=100, do_sample=True, temperature=0.7)
    return result[0]['generated_text']

# Step 1: Open Chrome or WhatsApp Web window (adjust if needed)
pyautogui.click(1639, 1412)
time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Select chat area (adjust coordinates for your screen)
    pyautogui.moveTo(756, 260)
    pyautogui.dragTo(760, 997, duration=2.0, button='left')

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    # Step 4: Get chat history
    chat_history = pyperclip.paste()
    last_sender = get_last_sender(chat_history)

    print("Chat history:\n", chat_history)
    print("Last sender:", last_sender)

    # Step 5: Only respond if last sender isn't you
    if last_sender and last_sender.lower() != YOUR_NAME.lower():
        prompt = f"You are Naruto, a funny Indian coder. Roast this:\n{chat_history}"
        response = generate_response(prompt)

        print("Generated response:", response)

        pyperclip.copy(response)

        # Step 6: Click on chat box
        pyautogui.click(815, 1015)
        time.sleep(1)

        # Step 7: Paste and send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
