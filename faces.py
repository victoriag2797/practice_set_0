def main():
    text = input("How are you feeling? ").replace(":)", "🙂").replace("):", "🙁").replace("(:","🙂").replace(":(", "🙁")
    emoji(text)

def emoji(user_text):
    print(user_text)

main()