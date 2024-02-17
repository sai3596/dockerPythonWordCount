import os
import socket
from collections import Counter


# Function to list all text files in a directory
def ListAllTheExistingTextFiles(directory):
    try:
        return [file for file in os.listdir(directory) if file.endswith('.txt')]
    except Exception as e:
        print("Exception in ListAllTheExistingTextFiles: ", e)
        raise e


# Function to count words in a text file
def wordCountInFile(filepath):
    try:
        with open(filepath, 'r') as file:
            contents = file.read()
            words = contents.split()
            return len(words)
    except Exception as e:
        print("Exception in wordCountInFile: ", e)
        raise e


# Function to get top 3 words in a file
def top3WordsInFile(filepath):
    try:
        with open(filepath, 'r') as file:
            contents = file.read()
            words = contents.lower().split()
            word_counts = Counter(words)
            top_3 = word_counts.most_common(3)
            return top_3
    except Exception as e:
        print("Exception in top3WordsInFile: ", e)
        raise e


# Function to get the machine's IP address
def getIp():
    try:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        return IPAddr
    except Exception as e:
        print("Exception in getIp: ", e)
        raise e


# Main function to perform all tasks
def main():
    try:
        directory = '/home/data'  # Adjusted directory for demonstration
        output_directory = '/home/data/output'  # Adjusted output directory
        os.makedirs(output_directory, exist_ok=True)
        output_file = os.path.join(output_directory, 'result.txt')

        with open(output_file, 'w') as outputFp:
            # List all text files
            textFiles = ListAllTheExistingTextFiles(directory)
            # print(f"Text Files: {', '.join(textFiles)}\n")
            outputFp.write(f"Text Files: {', '.join(textFiles)}\n")


            # Count words in each file and total
            totalWords = 0
            for file in textFiles:
                wordCount = wordCountInFile(os.path.join(directory, file))
                totalWords += wordCount
                # print(f"Words in {file}: {wordCount}\n")
                outputFp.write(f"Words in {file}: {wordCount}\n")
        #
            # print(f"Total Words in All Files: {totalWords}\n")
            outputFp.write(f"Total Words in All Files: {totalWords}\n")
        #
            # Top 3 words in IF.txt
            ifFile = os.path.join(directory, 'IF.txt')
            if os.path.exists(ifFile):
                top3Words = top3WordsInFile(ifFile)
                # print("Top 3 words in IF.txt:\n")
                outputFp.write("Top 3 words in IF.txt:\n")
                for word, count in top3Words:
                    # print(f"{word}: {count}\n")
                    outputFp.write(f"{word}: {count}\n")
        #
            # Get IP address
            ip_address = getIp()
            # print(f"IP Address: {ip_address}\n")
            outputFp.write(f"IP Address: {ip_address}\n")
        #
        # Print the contents of the result.txt
        with open(output_file, 'r') as result:
            print(result.read())
    except Exception as e:
        print("Exception raised from main", e)
        raise e


if __name__ == "__main__":
    main()
