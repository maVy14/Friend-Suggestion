# Real-Life Application of Set Operations in Friend Suggestion Algorithms

## Introduction
This group project was developed as part of my school assignment in Basic Structures in Discrete Mathematics at University of Information Technology(UIT),Yangon,Myanmar.This project implements a simple friend suggestion system using Python dictionaries and set operations. It identifies mutual friends and suggests new friends based on existing connections in a social network.

## Features
- Find mutual friends between two users
- Suggest new friends based on indirect connections
- Uses Python sets for efficient friend recommendation
- Interactive command-line interface

## How It Works
1. The program takes a user's name as input.
2. It checks the user's direct friends.
3. It finds second-degree connections using set union.
4. Existing friends are removed from suggestions using set difference.
5. The program ranks suggested friends based on mutual connections using set intersection.

## Technologies Used
- Python
- Set operations (`union`, `intersection`, `difference`)
- Dictionary data structure for storing friendships

## Usage
### Prerequisites
Ensure you have Python installed on your system.

### Running the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/maVy14/Friend-Suggestion
   cd Friend-Suggestion
   ```
2. Run the script:
   ```sh
   python fri-suggest.py
   ```
3. Enter a user's name to receive friend suggestions.
4. Type 'q' to exit the program.

## Example Output
```
Enter a user's name to get friend suggestions (or type 'q' to quit): alice
Friend suggestions for Alice:
Emma (Mutual: 1),
Helen (Mutual: 1),
George (Mutual: 1)
```

## Contributions
Feel free to contribute by improving the algorithm or adding new features. Fork the repository, make your changes, and submit a pull request.

## License
This project is open-source and available under the MIT License.

