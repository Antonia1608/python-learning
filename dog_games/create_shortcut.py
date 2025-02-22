import os
import winshell
from win32com.client import Dispatch

def create_shortcut():
    try:
        # Get paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        desktop = winshell.desktop()
        batch_file = os.path.join(current_dir, 'start_game.bat')
        icon_path = os.path.join(current_dir, 'dog_icon.ico')
        shortcut_path = os.path.join(desktop, "Honden Spelletjes.lnk")

        # Create shortcut
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = batch_file
        shortcut.IconLocation = icon_path
        shortcut.WorkingDirectory = current_dir
        shortcut.WindowStyle = 1  # Normal window
        shortcut.save()
        
        print("Snelkoppeling succesvol gemaakt op het bureaublad!")
        print(f"Batch bestand: {batch_file}")
        print(f"Werkmap: {current_dir}")
        return True
    except Exception as e:
        print(f"Fout bij maken snelkoppeling: {str(e)}")
        return False

if __name__ == "__main__":
    create_shortcut()