@echo off

pyinstaller main.py --windowed --onefile --name "DiscordRPCGUI" --collect-all "dearpygui" --collect-all "pypresence" --icon=NONE