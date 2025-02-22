import os
import winshell
from win32com.client import Dispatch

def create_shortcut():
    try:
        # Get paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        desktop = winshell.desktop()
        python_path = r"C:\Users\suzan\AppData\Local\Microsoft\WindowsApps\python.exe"
        main_script = os.path.join(current_dir, 'main.py')
        icon_path = os.path.join(current_dir, 'dog_icon.ico')
        shortcut_path = os.path.join(desktop, "Honden Spelletjes.lnk")

        # Create shortcut
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = python_path
        shortcut.Arguments = f'"{main_script}"'
        shortcut.IconLocation = icon_path
        shortcut.WorkingDirectory = current_dir
        shortcut.save()
        
        print("Snelkoppeling succesvol gemaakt op het bureaublad!")
        print(f"Python pad: {python_path}")
        print(f"Script pad: {main_script}")
        print(f"Werkmap: {current_dir}")
        return True
    except Exception as e:
        print(f"Fout bij maken snelkoppeling: {str(e)}")
        return False

if __name__ == "__main__":
    create_shortcut()