import nlp

# Create a chatbot model
chatbot = nlp.Chatbot()

# Train the model on a dataset of conversation examples
chatbot.fit("conversations.txt")

# Start the conversation
while True:
  # Get the user's input
  user_input = input("You: ")

  # Get the chatbot's response
  response = chatbot.predict(user_input)
  
  # Print the chatbot's response
  print("Chatbot:", response)
