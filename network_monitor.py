import platform
import subprocess
import time
import csv
import re
from datetime import datetime

def check_host(host):
    if platform.system() == "Windows":
        command = ["ping", "-n", "5", "-w", "2000", host]
    else:
        command = ["ping", "-c", "5", "-W", "2", host]

    try:
        result = subprocess.run(
            command,
            capture_output = True,
            text = True,
            timeout = 12
        )

        output = result.stdout + result.stderr

        if platform.system() == "Windows":
            match = re.search(r"Received = (\d+)", output)
        else:
            match = re.search(r"(\d+) received", output)

        if match:
            received = int(match.group(1))
        else:
            received = 0

        return received, 5

    except subprocess.TimeoutExpired:
        return 0, 5

host = "127.0.0.1"

with open("network_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([""
        "Timestamp",
        "Host",
        "Replies",
        "Packet Loss",
        "Status"
    ])

    for i in range(5):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        received, sent = check_host(host)
        packet_loss = ((sent - received) / sent) * 100

        if received > 0:
            status = "Responding"
        else:
            status = "Not responding"

        print(
            timestamp,
            host,
            str(received) + "/" + str(sent),
            str(packet_loss) + "% packet loss",
            status
        )

        writer.writerow([
            timestamp,
            host,
            str(received) + "/" + str(sent),
            str(packet_loss) + "%",
            status
        ])

        time.sleep(2)

print("Results saved to network_log.csv")


