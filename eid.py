import time

messages = [
    "🌙✨ Eid-Ul-Adha Mubarak ✨🌙",
    ""
    "May your life be filled with happiness ❤️",
    "Wishing you peace, success, and blessings 🌟",
    "Have a wonderful Eid with your family 🎉"
]

for line in messages:
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("\n")
    time.sleep(0.5)