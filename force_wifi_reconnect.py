import os
import time
import subprocess

def is_wifi_connected():
    try:
        # Check if the Wi-Fi is connected to a network by getting the SSID
        result = subprocess.run(['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi'], capture_output=True, text=True)
        # Check if there are any SSIDs in the list
        if result.stdout.strip():
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def toggle_wifi():
    while True:
        # Turn off Wi-Fi
        os.system("nmcli radio wifi off")
        print("Wi-Fi turned off")
        
        # Wait for a few seconds
        time.sleep(2)
        
        # Turn on Wi-Fi
        os.system("nmcli radio wifi on")
        print("Wi-Fi turned on")
        
        # Wait for Wi-Fi to connect
        time.sleep(10)
        
        if is_wifi_connected():
            print("Connection established")
            break
        else:
            print("No connection. Retrying...")

if __name__ == "__main__":
    toggle_wifi()
