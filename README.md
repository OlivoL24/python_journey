# Python Journey Repository

Welcome to my Python Journey repository! This repository serves as a collection of Python projects that I have developed as I embark on my programming journey. From small scripts to more complex applications, this repository showcases my growth and progress as a Python developer.

## Table of Contents

1. [Project 1: Compare Router Config](#router-cfg-diff)
2. [Project 2: Find Duplicate Photos](#locate-dup)
3. [Project 3: Guessing Game](#guess_number)
4. [Project 4: Tracetroute](#trace_route)
5. [Contributing](#contributing)
6. [License](#license)

## Project: Compare Router Config

The "Compare Router Config" project is a Python script that enables users to compare the configuration files of network routers. It helps network administrators and engineers identify differences between router configurations, making it easier to troubleshoot and manage network devices.

### Features

- **Config File Comparison:** The script compares two router configuration files and highlights the differences between them.
- **Structured Output:** The differences are presented in a structured and readable format, making it easy to understand the changes.
- **Customizable Comparison:** Users can configure the script to ignore specific sections or lines in the configuration files, focusing only on the relevant parts.
- **Command-Line Interface:** The project provides a command-line interface (CLI) for executing the script and specifying the input files.

### Usage

1. Clone the repository: `git clone https://github.com/OlivoL24/python_journey.git`
2. Navigate to the project directory: `cd python_journey/compare_router_config`
3. Run the script: `python compare_router_config.py [file1] [file2]`
   - Replace `[file1]` and `[file2]` with the paths or names of the router configuration files you want to compare.
   - Optionally, you can use additional flags or options to customize the comparison process.

### Example

Suppose we have two router configuration files: `router1.cfg` and `router2.cfg`. To compare these files, we can run the script as follows:

```
python compare_router_config.py router1.cfg router2.cfg
```

The script will analyze the two configuration files and output the differences in a structured format, highlighting added, modified, and removed lines.

```
Comparing router1.cfg and router2.cfg:

--- router1.cfg
+++ router2.cfg

@@ -10,7 +10,7 @@
  hostname Router1
  ip address 192.168.1.1/24
  interface FastEthernet0/0
-  description Local Network
+  description Internal Network
   ip address 192.168.1.254/24
  interface Serial0/0
   description WAN Connection
```

The output provides a clear overview of the changes made between the two configuration files, allowing for easy identification of modifications.

## Project: Find Duplicate Photos

The "Find Duplicate Photos" project is a Python script that helps users identify and remove duplicate photos from a given directory. It utilizes image hashing techniques to compare and find duplicate or similar images, assisting in organizing and decluttering photo collections.

### Features

- **Duplicate Detection:** The script scans a directory and detects duplicate or similar photos based on their visual content.
- **Image Hashing:** It uses image hashing algorithms to generate unique hash values for each image, enabling efficient comparison and identification of duplicates.
- **Threshold Configuration:** Users can customize the similarity threshold to control the strictness of duplicate detection.
- **Flexible Output:** The project provides options to display and export the list of duplicate photos, allowing users to review and take further action as needed.

### Usage

1. Clone the repository: `git clone https://github.com/OlivoL24/python_journey.git`
2. Navigate to the project directory: `cd python_journey/Find Duplicate Photos`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the script: `python find_duplicate_photos.py [directory]`
   - Replace `[directory]` with the path to the directory containing the photos you want to analyze.

### Example

Suppose we have a directory named `photos` that contains multiple photos, some of which are duplicates. To find and display the duplicate photos, we can run the script as follows:

```
python find_duplicate_photos.py photos
```

The script will scan the `photos` directory, compute the image hashes, and identify the duplicate or similar photos. The output will display the groups of duplicate photos found:

```
Duplicate Photos Found:
Group 1:
- photos/duplicate1.jpg
- photos/duplicate2.jpg

Group 2:
- photos/similar1.jpg
- photos/similar2.jpg
- photos/similar3.jpg
```

The script will provide a list of groups, with each group containing the file paths of the duplicate or similar photos. Users can review this information and decide how they want to handle the duplicates, such as deleting or organizing them.

## Project: Guessing Game

The "Guessing Game" project is a Python script that implements a simple number guessing game. It allows players to guess a randomly generated number and provides feedback on whether their guess is too high, too low, or correct. It offers an interactive and enjoyable experience for users to test their guessing skills.

### Features

- **Random Number Generation:** The script generates a random number within a specified range for the player to guess.
- **User Interaction:** It provides a prompt for users to enter their guesses and displays appropriate feedback based on their inputs.
- **Guess Tracking:** The script keeps track of the number of attempts made by the player and displays the count at the end.
- **Play Again Option:** After completing a round, users have the option to play the game again or exit.

### Usage

1. Clone the repository: `git clone https://github.com/OlivoL24/python_journey.git`
2. Navigate to the project directory: `cd python_journey/guessing_game`
3. Run the script: `python guessing_game.py`

### Example

To play the guessing game, simply run the script using the command `python guessing_game.py`. The script will generate a random number between 1 and 100 (inclusive) and prompt you to enter your guesses.

```
Welcome to the Guessing Game!
I'm thinking of a number between 1 and 100.
Can you guess it?

Enter your guess: 50
Too low! Try a higher number.

Enter your guess: 75
Too high! Try a lower number.

Enter your guess: 63
Congratulations! You guessed the number correctly in 3 attempts.

Do you want to play again? (y/n): n
Thank you for playing! Goodbye.
```

The script will provide feedback after each guess, indicating whether the guess is too high or too low. It will continue until you guess the correct number. Afterward, it will display the number of attempts made and prompt whether you want to play again.

## Project: Traceroute

The "Traceroute" project is a Python script that performs network tracing using the ICMP protocol (Internet Control Message Protocol). It allows users to trace the path taken by network packets from their local machine to a specified destination, revealing the intermediate hops and their corresponding IP addresses. This project provides insights into network connectivity and helps diagnose potential network issues.

### Features

- **Network Tracing:** The script sends ICMP packets with varying Time to Live (TTL) values to trace the route from the local machine to a destination IP address or domain name.
- **Hop Identification:** It identifies each hop along the route and displays the corresponding IP address and round-trip time (RTT) for each hop.
- **Geolocation Data:** The script utilizes IP geolocation services to provide additional information about each hop, such as the country or city associated with the IP address.
- **Interactive Output:** The project offers an interactive command-line interface (CLI) that displays the traceroute results in a clear and readable format.

### Usage

1. Clone the repository: `git clone https://github.com/OlivoL24/python_journey.git`
2. Navigate to the project directory: `cd python_journey/Traceroute`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the script: `python traceroute.py [destination]`
   - Replace `[destination]` with the IP address or domain name of the target destination.

### Example

To perform a traceroute to a specific destination, execute the script using the command `python traceroute.py [destination]`. For instance, let's trace the route to `example.com`:

```
python traceroute.py example.com
```

The script will start sending ICMP packets with increasing TTL values, allowing them to expire at each hop along the network path. It will then display the hop number, IP address, and round-trip time (RTT) for each intermediate hop:

```
Tracing route to example.com [93.184.216.34]
1   192.168.0.1     3.0 ms
2   10.0.0.1        5.0 ms
3   203.0.113.1     8.0 ms
4   172.16.0.1      10.0 ms
5   185.198.176.1   15.0 ms
6   93.184.216.34   20.0 ms
Trace complete.
```

The output displays each hop's number, IP address, and the round-trip time (RTT) measured in milliseconds. The final line, "Trace complete," indicates that the destination has been reached, and the traceroute process is finished.
