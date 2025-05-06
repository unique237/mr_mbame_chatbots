def simple_chatbot():
    print("Hi! I'm a bot. Type 'hello', 'help', or 'bye'.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hey there!")
        elif user_input == "help":
            print("Bot: I can greet or say goodbye.")
        elif user_input == "bye":
            print("Bot: See ya!")
            break
        else:
            print("Bot: I don't understand. Try 'hello', 'help', or 'bye'.")
simple_chatbot()