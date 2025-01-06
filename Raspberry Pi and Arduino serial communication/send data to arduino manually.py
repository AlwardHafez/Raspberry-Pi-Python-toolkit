import serial
import time

# Make sure that you Replace 'ttyACM0' with the port your Arduino is connected to check readme for more info
arduino_port = '/dev/ttyACM0'
baud_rate = 9600  # Ensure this matches the baud rate in your Arduino code

# Start serial communication
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the serial connection to initialize

print("Serial communication connected successfully send data to the Arduino.")
print("Type 'x' to close the program.")

try:
    while True:
        # Get user input
        user_input = input("Enter data to send to Arduino: 1 to 5 ")

        if user_input.lower() == 'x':
            break  # Exit the loop if the user types 'x'

        # Send the input to Arduino
        ser.write((user_input + '\n').encode())  # Send user input to Arduino
        
        # Optional: Wait for a response from Arduino
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            print(f"Arduino response: {response}")

except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    ser.close()  # Close the serial connection
    print("Serial connection closed.")
