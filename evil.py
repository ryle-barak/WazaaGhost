#!/usr/bin/env python3

import os
import time
import webbrowser
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Configuration
ASCII_ART = r"""
 __      __                               
/  \    /  \_____  _____________  _____   
\   \/\/   /\__  \ \___   /\__  \ \__  \  
 \        /  / __ \_/    /  / __ \_/ __ \_
  \__/\  /  (____  /_____ \(____  (____  /
       \/        \/      \/     \/     \/                        ............                 
              .....::.:.:..                   
           .....:::::::::...                  
          ..:.:::.:::---:....                 
         .....:===-::-----...                 
       .......:::.-::-  :::..                 
      .......::   :::-   .: ..                
     ......::     ::.:     -..                
     ..:.:-.      .::-       :-               
     ..::        :::-:-       -:              
     ...       .:.-====:-.   =-.              
     ..:-:  -=-:.:--=-=-::---:.               
       ..:::....:::     :.                    
             ......:::--::.                   
          .....::.--------:.                  
           ....:.:.      ::                   
            .....        :.                   
              ..:        :                    
               .:        :                    
                .        .                    
                .-                             
                 .      .                      
                  -     .                      
                  .:                            
                   .     :                     
                    - .. .                     
                     : .:                      
"""

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
