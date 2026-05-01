# The simplest chatbot in the world
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input('You:').lower()
    if user_input == "hello":
        print("Chatbot: Hi there!")

    elif user_input == "how are you":
        print("I'm just code, but i'm working fine.")

    elif user_input == "what is your name":
        print("Chatbot: I'm a simple Python chatbot.")

    elif user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    
    else:
        print("Chatbot: I don't understand that yet.")
