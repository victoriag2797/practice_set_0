def main():
    question = input("what's your favorite color?").lower().strip()
    shush(question)

def shush(user_question):
    print(f"shush, {user_question}")
main()