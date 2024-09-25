import urllib.parse

def decode_url(url):
    # Use the unquote function to decode the URL
    return urllib.parse.unquote(url)

# Open the file in append mode ('a') to preserve original data and add new data
with open("data.txt", "a") as file:
    while True:
        # Ask the user to input an encoded URL
        encoded_url = input("Enter the encoded Data: ")
        
        # Check if the input is empty
        if not encoded_url:
            break
        
        # Decode the URL
        decoded_url = decode_url(encoded_url)
        
        # Write the decoded URL to the file and include a newline for each entry
        file.write(decoded_url + "\n")
        print("Successfully data added to data.txt")
