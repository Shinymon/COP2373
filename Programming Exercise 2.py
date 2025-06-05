# Define a function to calculate the spam score based on the email message and spam keywords
def calculate_spam_score(message, spam_keywords):
    # Convert the entire message to lowercase for case-insensitive matching
    message_lower = message.lower()
    # Create a list to keep track of which spam keywords were found
    spam_words_found = []
    # Initialize spam score to zero
    score = 0

    # Loop through each keyword in the list of spam keywords
    for keyword in spam_keywords:
        # Check if the keyword exists in the message
        if keyword in message_lower:
            # Add the keyword to the list of found spam words
            spam_words_found.append(keyword)
            # Add to the spam score based on how many times the keyword appears
            score += message_lower.count(keyword)

    # Return the final spam score and list of spam words found
    return score, spam_words_found

# Define a function to rate the likelihood of spam based on the score
def rate_spam_likelihood(score):
    # If score is 0, it's not spam
    if score == 0:
        return "Not Spam"
    # If score is between 1 and 3, low chance of spam
    elif 1 <= score <= 3:
        return "Low likelihood of spam"
    # If score is between 4 and 6, moderate chance
    elif 4 <= score <= 6:
        return "Moderate likelihood of spam"
    # If score is between 7 and 10, high chance
    elif 7 <= score <= 10:
        return "High likelihood of spam"
    # If score is greater than 10, very high chance
    else:
        return "Very high likelihood of spam!"

# Define the main function that runs the application
def main():
    # Display the program title
    print("=== Spam Scanner ===")
    # Prompt the user to enter their email message
    email_message = input("Enter your email message:\n")

    # Call the calculate_spam_score function and get the score and matched keywords
    score, spam_words = calculate_spam_score(email_message, spam_keywords)
    # Call the rating function to determine how spammy it is
    likelihood = rate_spam_likelihood(score)

    # Display the results of the scan
    print("\n=== Scan Results ===")
    # Show the spam score
    print(f"Spam Score: {score}")
    # Show the likelihood of it being spam
    print(f"Spam Likelihood: {likelihood}")

    # If any spam keywords were found, print them
    if spam_words:
        print("Spam Keywords Found:")
        # Print each spam word found on a new line with a dash
        for word in spam_words:
            print(f"- {word}")
    else:
        # Let the user know their message is clean
        print("No spam keywords found. Nice job!")

# Define the list of 30 spam keywords and phrases that I found
spam_keywords = [
    "buy now", "click here", "free", "guarantee", "urgent",
    "winner", "limited time", "risk-free", "money back", "cheap",
    "make money", "earn cash", "act now", "credit card", "investment",
    "double your income", "no cost", "lowest price", "get paid", "instant",
    "lose weight", "miracle", "trial", "subscribe", "deal",
    "extra cash", "cash bonus", "earn per week", "pre-approved", "congratulations"
]

# Call the main function to start the program
main()