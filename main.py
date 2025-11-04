"""
Disappearing Text Application
Author: Hemant Vijay
Last Updated: 4-Nov-2025

This application is part of the 100 Days of Code course by Angela Yu.
Course URL: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

Description:
This is a writing application that encourages continuous typing. If the user stops
typing for more than 5 seconds, all the text they have written will disappear.
This helps writers overcome writer's block by forcing them to keep writing without
overthinking or editing.

Legal Disclaimer:
This software is provided "as is" without warranty of any kind. The author is not
responsible for any data loss, misuse, or any other damages arising from the use
of this application. Users are advised to save their work regularly in another
application if they want to preserve it.
"""

# Import tkinter library for creating the graphical user interface (GUI)
# tkinter is Python's standard GUI library and comes built-in with Python
import tkinter as tk

# This is the main class that represents our Disappearing Text Application
class DisappearingTextApp:
    """
    Main application class that handles the disappearing text functionality.

    How it works:
    1. User sees a text box where they can type
    2. Every time user presses a key, a 5-second timer starts/resets
    3. If 5 seconds pass without any typing, all text disappears
    4. User can see remaining time in the status bar
    """

    def __init__(self, root):
        """
        Initialize the application and set up all the components.

        Parameters:
        root - The main window of the application
        """
        # Store the main window reference
        self.root = root

        # Set the title that appears at the top of the window
        self.root.title("Disappearing Text App - Keep Typing!")

        # Set the initial size of the window (width x height)
        self.root.geometry("800x600")

        # Set minimum window size so it doesn't get too small
        self.root.minsize(600, 400)

        # This variable will store the timer ID so we can cancel it if needed
        self.timer_id = None

        # The countdown time in seconds (how long before text disappears)
        self.countdown_time = 5

        # The remaining time that will be displayed to the user
        self.remaining_time = self.countdown_time

        # Set up all the visual components (labels, text box, etc.)
        self.setup_ui()

        # Give focus to the text area so the cursor appears and user can start typing
        self.text_area.focus_set()

    def setup_ui(self):
        """
        Create and arrange all the visual components of the application.
        This includes:
        - Title label at the top
        - Text area in the middle where user types
        - Status bar at the bottom showing remaining time
        """

        # Create a title label at the top of the window
        title_label = tk.Label(
            self.root,
            text="Keep Typing or Your Text Will Disappear!",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )
        # Pack means to place the widget in the window
        # fill=tk.X makes it stretch horizontally
        title_label.pack(fill=tk.X)

        # Create instructions label with more detailed information
        instructions_label = tk.Label(
            self.root,
            text="Start typing below. If you stop for 5 seconds, your text will disappear! Watch the status bar for remaining time. This app does not save your work.",
            font=("Arial", 11),
            bg="#ecf0f1",
            fg="#34495e",
            pady=12,
            wraplength=750,
            justify=tk.CENTER
        )
        instructions_label.pack(fill=tk.X)

        # Create a frame (container) to hold the text area and scrollbar
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a scrollbar for when text gets too long
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the main text area where user will type
        self.text_area = tk.Text(
            text_frame,
            font=("Arial", 12),
            wrap=tk.WORD,  # Wrap text at word boundaries
            yscrollcommand=scrollbar.set,  # Connect scrollbar to text area
            bg="#ffffff",
            fg="#2c3e50",
            insertbackground="#e74c3c",  # Color of the cursor
            insertwidth=3,  # Make cursor wider so it's more visible
            relief=tk.FLAT,
            padx=10,
            pady=10,
            state=tk.NORMAL  # Explicitly set to normal/enabled state
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Configure the scrollbar to work with the text area
        scrollbar.config(command=self.text_area.yview)

        # Bind the key release event to our handler function
        # This means every time a key is released, our function will be called
        # We use KeyRelease instead of KeyPress so the character appears first
        self.text_area.bind("<KeyRelease>", self.on_key_press)

        # Create a status bar at the bottom to show remaining time
        self.status_bar = tk.Label(
            self.root,
            text=f"Time remaining: {self.remaining_time} seconds",
            font=("Arial", 10),
            bg="#27ae60",
            fg="white",
            pady=5,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        # Create a footer with attribution
        footer_label = tk.Label(
            self.root,
            text="Project by Hemant Vijay | Part of 100 Days of Code Course by Angela Yu",
            font=("Arial", 8),
            bg="#95a5a6",
            fg="white",
            pady=3
        )
        footer_label.pack(fill=tk.X, side=tk.BOTTOM)

    def on_key_press(self, event):
        """
        This function is called every time the user presses a key.
        It resets the countdown timer to give the user another 5 seconds.

        Parameters:
        event - Information about the key press event
        """
        # If there's already a timer running, cancel it
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)

        # Reset the remaining time back to the full countdown
        self.remaining_time = self.countdown_time

        # Update the status bar to show the reset time
        self.update_status_bar()

        # Start a new countdown timer (schedule it for 1 second from now)
        # This gives the user the full 5 seconds before the first countdown
        self.timer_id = self.root.after(1000, self.start_countdown)

    def start_countdown(self):
        """
        Start or continue the countdown timer.
        This function calls itself every second to update the countdown.
        """
        # Decrease the remaining time by 1 second
        self.remaining_time -= 1

        # Update the status bar to show the new time
        self.update_status_bar()

        # Check if time has run out
        if self.remaining_time <= 0:
            # Time's up! Delete all the text
            self.delete_all_text()
        else:
            # Time hasn't run out yet, schedule this function to run again in 1 second
            # 1000 milliseconds = 1 second
            self.timer_id = self.root.after(1000, self.start_countdown)

    def update_status_bar(self):
        """
        Update the status bar to show the current remaining time.
        Also changes the color based on how much time is left.
        """
        # Change status bar color based on remaining time
        if self.remaining_time <= 2:
            # Red warning when time is almost up
            bg_color = "#e74c3c"
        elif self.remaining_time <= 3:
            # Orange warning when time is getting low
            bg_color = "#e67e22"
        else:
            # Green when there's plenty of time
            bg_color = "#27ae60"

        # Update the status bar with new time and color
        self.status_bar.config(
            text=f"Time remaining: {self.remaining_time} seconds - Keep typing!",
            bg=bg_color
        )

    def delete_all_text(self):
        """
        Delete all text from the text area and show a message to the user.
        This happens when the countdown reaches zero.
        """
        # Delete all text from the text area
        # "1.0" means line 1, character 0 (the very beginning)
        # tk.END means the end of all text
        self.text_area.delete("1.0", tk.END)

        # Insert a temporary warning message in the text area
        warning_msg = "⚠️ YOUR TEXT HAS DISAPPEARED! ⚠️\n\nYou stopped typing for too long.\n\nStart typing to continue..."
        self.text_area.insert("1.0", warning_msg)

        # Change text color to red for the warning
        self.text_area.tag_add("warning", "1.0", tk.END)
        self.text_area.tag_config("warning", foreground="#e74c3c", font=("Arial", 14, "bold"), justify=tk.CENTER)

        # Schedule the warning message to be cleared after 3 seconds
        # or on the next keypress (whichever comes first)
        self.root.after(3000, self.clear_warning_if_present)

        # Reset the timer variables
        self.remaining_time = self.countdown_time
        self.timer_id = None

        # Update the status bar to show reset time
        self.update_status_bar()

    def clear_warning_if_present(self):
        """
        Clear the warning message if it's still present in the text area.
        This is called automatically after 3 seconds.
        """
        # Get the current text content
        current_text = self.text_area.get("1.0", tk.END).strip()

        # Check if it's still showing the warning message
        if "YOUR TEXT HAS DISAPPEARED" in current_text:
            # Clear it
            self.text_area.delete("1.0", tk.END)
            # Remove the warning tag
            self.text_area.tag_remove("warning", "1.0", tk.END)


# This is the main entry point of the program
# This code only runs if this file is run directly (not imported)
if __name__ == "__main__":
    # Create the main window for the application
    root = tk.Tk()

    # Create an instance of our DisappearingTextApp
    app = DisappearingTextApp(root)

    # Start the application's main loop
    # This keeps the window open and responsive to user actions
    root.mainloop()
