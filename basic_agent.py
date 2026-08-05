# Basic Python agent that greets the user and responds to simple commands.

# Print a greeting message to the user.
print("Hello! I am your basic Python agent.")

# Ask the user for their name.
name = input("What is your name? ")

# Greet the user by name.
print(f"Nice to meet you, {name}!")

# Ask the user how the agent can help.
help_request = input("How can I help you today? ")

# Respond to the user's help request using if-elif statements.
# This handles specific phrases such as hello, time, and bye.
if help_request.lower() == "hello":
    print("Hello! How can I assist you?")
elif help_request.lower() == "time":
    print("The current time is not available in this basic script, but I am here to help!")
elif help_request.lower() == "bye":
    print("Goodbye! Have a great day!")
else:
    print("I can help with greetings, time, or saying goodbye.")

# End of the basic agent.
