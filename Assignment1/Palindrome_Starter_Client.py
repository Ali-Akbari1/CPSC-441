import socket

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

def start_client():

    retries = 0 # retry counter
    while retries < 3: 
        try:
            """ Start the client and connect to the server. """
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.settimeout(5) # Set a timeout to 5 seconds for the connection
                client_socket.connect((SERVER_HOST, SERVER_PORT)) # Connect to the server
                
                # Client interaction loop
                while True:
                    # Display the menu and get user input
                    print("\nMenu:")
                    print("1. Simple Palindrome Check")
                    print("2. Complex Palindrome Check")
                    print("3. Exit")
                    choice = input("Enter choice (1/2/3): ").strip()

                    # If choice is simple palindrome 
                    if choice == '1':
                        input_string = input("Enter the string to check: ")
                        message = f"simple|{input_string}"
                        client_socket.send(message.encode()) # Send the message to the server
                        try:
                            response = client_socket.recv(1024).decode() # Receive the response from the server
                            print(f"Server response: {response}")
                        except socket.timeout:
                            print("Error: Server took too long to respond.")
                            break  # Exit inner loop to retry connection

                    # If choice is complex palindrome            
                    elif choice == '2':
                        input_string = input("Enter the string to check: ")
                        message = f"complex|{input_string}"
                        client_socket.send(message.encode()) # Send the message to the server
                        try:
                            response = client_socket.recv(1024).decode() # Receive the response from the server
                            print(f"Server response: {response}")
                        except socket.timeout:
                            print("Error: Server took too long to respond.")
                            break  # Exit inner loop to retry connection
                    elif choice == '3':
                        print("Exiting the client...")
                        client_socket.close() # Close the client socket
                        break
                    else:
                        print("Invalid choice. Please try again.")
            break # Exit the loop if the connection is successful
        except (socket.timeout, ConnectionRefusedError):
            print("Error: Could not connect to the server. Retrying...")
            retries += 1 # Increment the retry counter

if __name__ == "__main__":
    start_client()
