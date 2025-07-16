import praw

# Replace these with your Reddit app credentials
client_id = 'aZrVrFxGAk-pW42yWOdsKA'
client_secret = 'sizpOMp7kNgfXNIy-Ofyn7oxMq3aFg'
user_agent = 'persona_reader_2 by Background_Paint_502'

# Create a Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Ask for Reddit username
username = input("Enter Reddit username: ")

try:
    user = reddit.redditor(username)
    print(f"\nRecent comments by u/{username}:\n")

    for comment in user.comments.new(limit=5):
        print(f"- {comment.body}\n")

except Exception as e:
    print(f"\nError: {e}")
