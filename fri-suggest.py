import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for Mutual Friend Searching
def mutual_friends(user1, user2, friends_dict):
    return friends_dict.get(user1, set()) & friends_dict.get(user2, set())  # '&' for Intersection

# Function for Suggesting Friends
def suggest_friends(user, friends_dict):
    friends = friends_dict.get(user, set())
    suggestions = set()
    
    for friend in friends:
        suggestions |= friends_dict.get(friend, set())  # '|' for Union
    
    suggestions -= friends
    suggestions.discard(user)
    
    return suggestions

# Example friend connections
friends = {
    'alice': {'bob', 'charlie', 'david'},
    'bob': {'alice', 'emma', 'frank', 'charlie', 'alice'},
    'charlie': {'alice', 'george', 'helen', 'david', 'emma'},
    'david': {'alice', 'ian'},
    'emma': {'bob', 'jack'},
    'frank': {'bob', 'helen', 'charlie'},
    'george': {'charlie'},
    'helen': {'charlie', 'frank', 'bob'},
    'ian': {'david'},
    'jack': {'emma'}
}

clear_console()
time.sleep(1)

# Main Loop
while True:
    user = input("Enter a user's name to get friend suggestions (or type 'q' to quit): ").lower()
    time.sleep(0.5)
    if user == 'q':
        break
    if user in friends:
        # Get Suggestions
        suggestions = suggest_friends(user, friends)

        # Get Mutual Friends
        if suggestions:
            suggestion_list = []
            for suggestion in suggestions:
                mutuals = mutual_friends(user, suggestion, friends)
                suggestion_list.append(f"{suggestion.capitalize()} (Mutual: {len(mutuals)})")
            print(f"Friend suggestions for {user.capitalize()}:\n{', \n'.join(suggestion_list)}\n")
        else:
            print(f"No friend suggestions for {user.capitalize()}.")
    else:
        print("User not found. Please try again.")