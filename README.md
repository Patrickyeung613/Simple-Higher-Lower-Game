# Higher Lower Game

## Overview
The Higher Lower Game is a Python-based console game where players compare the follower counts of various social media platforms. The goal is to guess which platform has more followers to achieve the highest score possible. The game continues until the player makes an incorrect guess or there are no more platforms to compare.

## Files
- **main.py**: The main game logic, including the game loop, comparison functions, and user interaction.
- **game_data.py**: Contains a list of social media platforms with their follower counts, descriptions, and countries.
- **art.py**: Stores ASCII art for the game logo and the "vs" graphic displayed between comparisons.

## How to Play
1. Run `main.py` in a Python environment.
2. The game displays the logo and presents two social media platforms (A and B) with their names, descriptions, and countries.
3. Type `A` or `B` to guess which platform has more followers.
4. If you guess correctly, your score increases, and a new comparison is presented.
5. The game ends if you guess incorrectly or if there are fewer than two platforms left to compare.
6. Your final score is displayed at the end.


## Setup
1. Ensure all three files (`main.py`, `game_data.py`, `art.py`) are in the same directory.
2. Run the game by executing:
   ```bash
   python main.py
   ```

## Game Mechanics
- The game randomly selects two platforms from `game_data.py` for comparison.
- Platforms are removed from the list after each comparison to avoid repetition.
- The game checks if there are enough platforms (at least two) for a comparison. If not, the player wins, and the final score is displayed.
- A correct guess increments the score by 1, while an incorrect guess ends the game.

## Example Gameplay
```
╦ ╦┬┌─┐┬ ┬┌─┐┬─┐  ╦  ┌─┐┬ ┬┌─┐┬─┐
╠═╣││ ┬├─┤├┤ ├┬┘  ║  │ ││││├┤ ├┬┘
╩ ╩┴└─┘┴ ┴└─┘┴└─  ╩═╝└─┘└┴┘└─┘┴└─

Compare A: Instagram, Social media platform.
 __      _______ 
 \ \    / / ____|
  \ \  / / (___  
   \ \/ / \___ \ 
    \  /  ____) |
     \/  |_____/ 
                     
Compare B: Twitter, Microblogging platform.
Who has more followers? Type 'A' or 'B': A

You are right! Current score: 1
```
