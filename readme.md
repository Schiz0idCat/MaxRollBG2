This code tries to get the maximum attribute score in the character creation of Baldur's Gate 2

The algorithm captures a screenshot of the screen at the coordinates where the attribute points appear and stores the highest number. At the beginning, the program asks you to input the minimum acceptable score. It will then continuously store higher numbers exceeding that threshold (updating the minimum number each time a biger one is found).

### Notes:
The game must be run in windowed mode at full screen with a resolution of 1920x1080p.
The AI used in this program seems to have difficulty detecting numbers with a 7 (e.g., 77). Therefore, it is recommended to input at least 80 as the minimum score when prompted.
This code replaces the functionality of the in-game command console (activated by pressing Ctrl + 8 during character creation). This program was created for educational purposes only.