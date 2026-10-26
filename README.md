# python-network-monitor
Python network monitoring tool that checks host connectivity using ping. Calculates packetloss, and logs the results in a CSV file.

# Features
- Checks whether host responds to ping requests
- Counts received replies
- Calculates packetloss
- Records timestamps and results
- Saves it in a CSV log

# Tech Involved
- Python
- CSV file handling
- Command-line networking tools
- Visual Studio Code

# How it works
Program gets host= and runs ping checks, analyzes the output, and records the results in a CSV file. Each check has a timestamp, number of replies received, packet loss, and a connection status.

# How to run
1. Install Python 3
2. Download or clone this repository
3. Open the project folder in a terminal
4. Run the script:

   '''Bash
   python network_monitor.py
   '''

# What I learned
-Using Python to run system commands
-Checking network connectivity
-Processing command output
-Calculating packet loss
-Writing monitoring results to a CSV file
