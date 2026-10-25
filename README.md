# CodeAlpha Basic Network Sniffer

## 📌 Project Overview

The **Basic Network Sniffer** is a Python-based cybersecurity project developed using Scapy in Kali Linux. It captures a limited number of IP packets and displays basic network information, helping users understand how network traffic is analyzed.

## 🎯 Project Objectives

* Understand basic network packet capture.
* Identify source and destination IP addresses.
* Recognize TCP and UDP protocols.
* Display source and destination port numbers.
* Gain practical experience with network traffic analysis.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Library:** Scapy
* **Operating System:** Kali Linux

## ✨ Features

* Captures up to 10 IP packets per execution.
* Displays source and destination IP addresses.
* Identifies TCP and UDP traffic.
* Displays source and destination ports when available.
* Shows a completion message after packet capture.

## 📂 Project Structure

```text
CodeAlpha_Basic_Network_Sniffer/
├── sniffer.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Update Kali Linux

```bash
sudo apt update
```

### 2. Install Scapy

```bash
sudo apt install python3-scapy -y
```

### 3. Navigate to the Project Directory

```bash
cd ~/CodeAlpha_Basic_Network_Sniffer
```

### 4. Run the Network Sniffer

```bash
sudo python3 sniffer.py
```

The program captures up to 10 IP packets and displays available packet information in the terminal.

## 📊 Sample Output

```text
Basic Network Sniffer Started...
Source IP: 192.168.1.10
Destination IP: 192.168.1.1
Protocol: TCP
Ports: 51520 -> 443
------------------------------
Capture complete.
```

*Note: The IP addresses and ports above are illustrative examples.*

## 🎥 Project Demonstration

A screen-recorded demonstration shows the project execution and packet information displayed in the Kali Linux terminal. The demonstration uses English text captions without voice-over.

## 📚 Learning Outcomes

* Learned the fundamentals of network packet sniffing.
* Practiced using Scapy in Python.
* Understood IP addresses, protocols, and port numbers.
* Gained hands-on experience with basic network traffic analysis.

## 🔐 Ethical Use

This project is intended for educational purposes and authorized network analysis only. Capture traffic only on networks and systems for which you have permission. Do not collect, expose, or share private network data.

## 👩‍💻 Author

**Muskan Kumari**

B.Tech CSE – Cyber Security

## 🏁 Conclusion

This project provided practical experience in building a basic network sniffer using Python and Scapy. It helped develop an understanding of packet capture and fundamental network traffic analysis techniques.
