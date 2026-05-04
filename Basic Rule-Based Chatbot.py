# The simplest chatbot in the world. Level 1
# print("Chatbot: Hello! Type 'bye' to exit.")

# while True:
#     user_input = input('You:').lower()
#     if user_input == "hello":
#         print("Chatbot: Hi there!")

#     elif user_input == "how are you":
#         print("I'm just code, but i'm working fine.")

#     elif user_input == "what is your name":
#         print("Chatbot: I'm a simple Python chatbot.")

#     elif user_input == "bye":
#         print("Chatbot: Goodbye!")
#         break
    
#     else:
#         print("Chatbot: I don't understand that yet.")


# Make it smarter (basic "AI thinking") Level 
# This is already closer to how real bots start thinking
print("Welcome to Chatbot")
print("Chatbot: What can i do for you?")
while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input:
        print("Chatbot: Hey!")
        
    elif "name" in user_input:
        print("Chatbot: I am your Python bot.")
        
    elif "help" in user_input:
        print("Chatbot: I can respond to simple messages.")
        
    elif "bye" in user_input:
        print("Chatbot: Bye!")
        
    else:
        print("Chatbot: Try asking something else.")







































