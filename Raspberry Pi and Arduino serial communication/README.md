# Raspberry Pi and Arduino Serial Communication

This directory contains tools and code examples for establishing and managing serial communication between a Raspberry Pi and an Arduino.
Whether you're manually sending commands or automating tasks, these files provide a solid foundation for your projects.

---

## **Contents**

### **1. Arduino Code**
This file contains the Arduino sketch needed to handle serial communication with the Raspberry Pi.  
- **Features:**
  - Listens for incoming commands from the Raspberry Pi over a USB connection.
  - Executes tasks based on the received command.
  - Provides feedback to the Raspberry Pi for debugging or confirmation.

---

### **2. Python Code**
#### **`send data to arduino manually.py`**
This Python script allows you to manually send data to the Arduino via serial communication.  
- **Features:**
  - Establishes a serial connection with the Arduino over a USB cable.
  - Accepts user input from the terminal and sends it as a command to the Arduino.
  - Displays responses from the Arduino for confirmation or debugging.

---

## **How to Use**

### **1. Setting Up the Hardware**
1. Connect your Raspberry Pi and Arduino using a USB cable.
2. Make sure the Arduino is powered and programmed with the provided **Arduino Code** sketch. you need to copy and paste the code. 
3. Program the Arduino with simple tasks to be triggered when commands are received from the Raspberry Pi.

### **2. Running the Python Script**
1. Run the Python script:
2. input 1 to 5 to be send to Arduino 

