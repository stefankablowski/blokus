# The game Blokus as a python console application

![Image](./logo.png)

- 🏆- Build your tiles space-efficient and win the game 
- 🐭🐱🐘 - 3 difficulty modes 
- 🟩🟨🟥🟦 - 0-4 players local multiplayer 

## Setup

1) Install Python > Version 3.11.4
2) Install the windows curses library for printing to the console
```
pip install windows-curses
```
3) Run in Visual Studio Code or Powershell in this directory
```
python .\SinglePlayer.py
```

## Requirements
- Windows
- Python curses library

## Development

- add overflow protection 🟩
- add cool status bar with player display and turns 🟩
    - improve with remaining boxes 🟩
- fix incorrect winning function🟩
- automatically check win condition🟩
- make local multi player possible🟩
- add difficulty modes🟧

- improve player bar 🟨

- fix color selection🟩
- better install guide🟩

### Difficulty Modes
(work in progress)
- easy: AI places a random tile randomly
- medium: AI places a tile in the way that minimizes the possible moves of the other players starting with the biggest tiles
- hard: AI players play together to minimize your possible moves


## Known Bugs
- check if players are transferred correct 🟩
- make players memorize their tile position from the last round
- make q key quit the game