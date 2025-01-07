def main():
    text = input("What? ").replace(" ", "...")
    slowdown(text)

def slowdown(user_text):
    print(f"Wow slow down: {user_text}")

main()