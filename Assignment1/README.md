# Assignment 1 - README

## Instructions for Compiling and Running the Server and Client

To run the server and client programs, use the following commands in separate terminal windows:

python .\Palindrome_Starter_Server.py

python .\Palindrome_Starter_Client.py

## Example Inputs and Outputs

### Example Input
1. Enter the string to check: ra          cerac

2. Enter the string to check: ivicc

3. Simple Palindrome: Enter the string to check: ivicc

### Example Output
1. Server response: Can form a palindrome: True
   Complexity score: 1 (number of swaps)

2. Server response: Can form a palindrome: True
   Complexity score: 2 (number of swaps)

3. Server response: Is palindrome: False

## Assumptions and Limitations
- The server and client communicate over TCP.
- The server runs locally.
- The server and client must be run on the same network.
- Error handling for network issues is minimal.
- The client must provide a valid IP address and port number to connect to the server.
- The server must be started before the client attempts to connect.
