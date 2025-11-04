# Disappearing Text Application

## Project Information

**Author:** Hemant Vijay
**Last Updated:** 4-Nov-2025
**Version:** 1.0

## Course Attribution

This project is part of an assignment for the 100 Days of Code: The Complete Python Pro Bootcamp course by Angela Yu on Udemy. Full credit for the project concept and requirements goes to Angela Yu.

**Course URL:** https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

## What is This Application?

The Disappearing Text Application is a writing tool designed to help overcome writer's block. The concept is simple but powerful: if you stop typing for 5 seconds, all your text disappears. This forces you to keep writing without overthinking or constantly editing your work.

This application is meant to be used as a writing exercise tool, not as a word processor or document editor. It encourages continuous creative flow and helps writers get past the habit of constantly revising as they write.

## How It Works

When you start the application, you will see a text area where you can begin typing. As soon as you press a key, a 5 second countdown timer starts. Every time you press another key, the timer resets back to 5 seconds.

If you stop typing and the timer counts down to zero, all the text in the text area will be erased automatically. A warning message will appear letting you know that your text has disappeared.

The application displays the remaining time in a status bar at the bottom of the window. The status bar changes color as time runs out:

* Green: You have plenty of time (4 to 5 seconds remaining)
* Orange: Time is running low (3 seconds remaining)
* Red: Time is almost up (1 to 2 seconds remaining)

## System Requirements

This application has been designed and tested to work on the following platforms:

**Windows**
* Windows 11 Pro 64 bit or higher

**Linux**
* Ubuntu 24.04.3 LTS 64 bit or higher

The application uses Python and the tkinter library, which is built into Python. As long as you have Python installed on your system, the application should work.

## Installation Instructions

### Prerequisites

You need to have Python installed on your system. Python 3.8 or higher is recommended.

**On Windows:**
1. Download Python from the official website: https://www.python.org/downloads/
2. Run the installer and make sure to check the box that says "Add Python to PATH"
3. Complete the installation

**On Ubuntu:**
Python usually comes pre installed on Ubuntu. To verify, open a terminal and type:

```
python3 --version
```

If Python is not installed, you can install it by running:

```
sudo apt update
sudo apt install python3 python3-tk
```

Note: The python3-tk package is needed for the graphical interface to work on Ubuntu.

### Running the Application

1. Download or clone this repository to your computer
2. Open a terminal or command prompt
3. Navigate to the folder where you saved the application files
4. Run the following command:

**On Windows:**
```
python main.py
```

**On Ubuntu:**
```
python3 main.py
```

The application window should open and you can start typing immediately.

## How to Use

1. When the application starts, a welcome message will appear explaining the rules. Click OK to close it.

2. Click in the text area and start typing. You will see the countdown timer at the bottom showing "Time remaining: 5 seconds".

3. Keep typing continuously. Every key press resets the timer back to 5 seconds.

4. If you stop typing, watch the status bar countdown. The color will change from green to orange to red as time runs out.

5. If the timer reaches zero, all your text will disappear and a warning message will appear.

6. Start typing again to continue your writing exercise.

## Important Warnings

**This application does NOT save your work.** It is designed specifically as a writing exercise tool where text disappearing is the main feature. Do not use this application to write important documents that you need to keep.

If you want to save something you wrote in this application, you need to copy it and paste it into another program before the timer runs out.

The author is not responsible for any data loss. This is explained in detail in the LICENSE.dat file.

## Tips for Using the Application

* Use this app when you have writer's block and need to get words flowing without worrying about quality
* Do not try to write a final draft in this app. Use it to generate ideas and rough text.
* Set a personal challenge: try to write continuously for 5 minutes without letting the text disappear
* After your writing session, copy any useful ideas to a proper document editor
* Remember: the goal is to write freely without self editing, not to create perfect prose

## Technical Details

**Programming Language:** Python 3
**GUI Library:** tkinter (built into Python)
**Timer Mechanism:** Uses tkinter's after() method to schedule countdown updates every second
**Text Widget:** Standard tkinter Text widget with scrollbar support

The application creates a graphical window with a text area, title, instructions, and status bar. When a key is pressed, it triggers an event handler that resets the countdown timer. The timer function calls itself every second to update the countdown. When the countdown reaches zero, it deletes all text from the text area.

## File Structure

The application consists of the following files:

* **main.py**: The main application file containing all the code
* **README.md**: This file, containing documentation and instructions
* **LICENSE.dat**: Legal information, disclaimers, and credits
* **requirements.txt**: Description of what the application should do

## Troubleshooting

**Problem:** The application window does not open when I run the command.

**Solution:** Make sure you have tkinter installed. On Ubuntu, install it with: `sudo apt install python3-tk`

**Problem:** I get an error message about Python not being recognized.

**Solution:** Python is not in your system PATH. On Windows, reinstall Python and check the "Add Python to PATH" option. On Ubuntu, use `python3` instead of `python`.

**Problem:** The text disappears too quickly and I cannot write fast enough.

**Solution:** This is by design. The application is meant to challenge you to write quickly without stopping. If you need more time, you can modify the countdown_time variable in the code (line 63 in main.py).

**Problem:** Can I change the countdown time?

**Solution:** Yes. Open main.py in a text editor and find the line that says `self.countdown_time = 5`. Change the 5 to however many seconds you want.

## Legal and Licensing

This software is provided "as is" without any warranty. The author is not responsible for any data loss, damages, or other issues arising from the use of this application.

This application intentionally deletes text as its core feature. Users are warned not to rely on it to save or preserve their work.

For complete legal information, disclaimers, and credits, please read the LICENSE.dat file included with this application.

## Credits and Acknowledgments

**Project Concept:** Angela Yu (100 Days of Code course)
**Implementation:** Hemant Vijay
**Python and tkinter:** Python Software Foundation

This project was created as part of the learning journey through Angela Yu's excellent 100 Days of Code course on Udemy. Thank you to Angela Yu for creating such comprehensive and practical programming challenges.

## Version History

**Version 1.0 (4-Nov-2025)**
* Initial release
* Basic disappearing text functionality with 5 second timer
* Visual countdown display with color coding
* Welcome message explaining the rules
* Status bar showing remaining time
* Cross platform support for Windows 11 and Ubuntu 24.04.3 LTS
* Comprehensive code comments for educational purposes

## Contact

This is an educational project created as part of a coding course. There is no formal support provided. Users experiencing issues should refer to the troubleshooting section above or consult the course materials.

For questions about the course itself, please contact the course instructor Angela Yu through the Udemy platform.

## Final Notes

Thank you for trying the Disappearing Text Application. Remember, the purpose of this tool is to help you write freely without the burden of perfectionism. Embrace the challenge, let your ideas flow, and do not worry about losing your text. That is the whole point.

Happy writing and keep coding!
