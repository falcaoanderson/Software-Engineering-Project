import subprocess
import platform

def clean_screen():
    """
    Clears the console screen.

    This function clears the console screen based on the operating system.
    On Windows, it uses the 'cls' command, while on other operating systems,
    it uses the 'clear' command.

    Returns:
        None
    """
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)