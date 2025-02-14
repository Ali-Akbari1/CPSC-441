import socket
import threading
import logging
from collections import Counter

# Set up basic logging configuration
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Constants for the server configuration
HOST = 'localhost'  # Server host
PORT = 12345  # Server port

def handle_client(client_socket, client_address):
    """ Handle incoming client requests. """
    logging.info(f"Connection from {client_address}")
    
    try:
        while True:
            # Receive data from the client
            request_data = client_socket.recv(1024).decode()
            if not request_data:  # Client has closed the connection
                break

            logging.info(f"Received request: {request_data}")
            
            # Process the request and generate a response
            response = process_request(request_data)
            client_socket.send(response.encode())  # Send the response to the client
            logging.info(f"Sent response: {response}")
    finally:
        # Close the client connection
        client_socket.close()
        logging.info(f"Closed connection with {client_address}")

def process_request(request_data):
    """ Process the client's request and generate a response. """
    try:
        check_type, input_string = request_data.split('|')  # Split request into check type and input string
        input_string = ''.join(e for e in input_string if e.isalnum()).lower()  # Clean input string
        
        if check_type == 'simple':
            result = is_palindrome(input_string)  # Perform simple palindrome check
            return f"Is palindrome: {result}"
        else:
            can_form, swaps = complex_ispalindrome(input_string)  # Perform complex palindrome check
            return f"Can form a palindrome: {can_form}\nComplexity score: {swaps} (number of swaps)"
    except Exception as e:
        logging.error(f"Error processing request: {e}")  # Log any errors
        return "Error processing request"

def is_palindrome(input_string):
    """ Check if the given string is a palindrome. """
    return input_string == input_string[::-1]  # Compare string with its reverse

def min_swaps_to_palindrome(s):
    s = list(s)  # Convert string to list for swapping
    swaps = 0  # Initialize swap counter
    left, right = 0, len(s) - 1  # Initialize left and right pointers
    
    while left < right:
        # Find the correct match for s[left] from the right side
        if s[left] != s[right]:
            match_index = right
            while match_index > left and s[match_index] != s[left]:
                match_index -= 1  # Find a match for s[left]
            
            if match_index == left:  # If no match found, it's the center character
                s[left], s[left + 1] = s[left + 1], s[left]  # Swap to center
                swaps += 1  # Count swap
            else:
                # Swap directly to put s[match_index] in the right position
                s[match_index], s[right] = s[right], s[match_index]
                swaps += 1  # Count swap
        
        left += 1
        right -= 1

    return swaps  # Return the total number of swaps

def min_swaps_to_make_palindrome(s):
    return min(min_swaps_to_palindrome(s), min_swaps_to_palindrome(s[::-1]))  # Min of normal and reversed string swaps

def complex_ispalindrome(input_string):
    """ Check if the string can be rearranged into a palindrome and calculate swaps. """
    char_counts = Counter(input_string)  # Count character occurrences
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)  # Count characters with odd frequency
    
    if odd_count > 1:
        return False, -1  # Cannot be rearranged into a palindrome if more than 1 odd character
    
    return True, min_swaps_to_make_palindrome(input_string)  # Can form palindrome, return swap count

def start_server():
    """ Start the server and listen for incoming connections. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))  # Bind server to host and port
        server_socket.listen(5)  # Listen for incoming connections
        logging.info(f"Server started and listening on {HOST}:{PORT}")
        
        while True:
            # Accept new client connections and start a thread for each client
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()  # Handle client in a new thread

if __name__ == '__main__':
    start_server()  # Start the server when the script is run
