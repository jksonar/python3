### **Following Is The System Admin Modules**
1. from bs4 import BeautifulSoup
2. from collections import Counter
3. from configparser import ConfigParser
4. from dotenv import load_dotenv 
5. from email.mime.image import MIMEImage
6. from email.mime.multipart import MIMEMultipart
7. from email.mime.text import MIMEText
8. from fabric.api import *
9. from ftplib import FTP
10. from matplotlib import style
11. from netmiko import ConnectHandler
12. from numpy import *
13. from openpyxl import Workbook
14. from os import stat, remove
15. from plotly import tools
16. from plotly.graph_objs import Scatter, Layout
17. from PyQt5.QtCore import pyqtSlot
18. from PyQt5.QtGui import QIcon
19. from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
20. from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
21. from sh import rsync
22. from shutil import make_archive
23. import argparse
24. import arithmetic
25. import calendar 
26. import csv
27. import datetime
28. import elevate 
29. import email.utils
30. import fabric 
31. import getopt
32. import getpass
33. import glob
34. import http.client
35. import if_example
36. import imaplib
37. import json
38. import logging
39. import matplotlib.image as mpimg
40. import matplotlib.pyplot as plt
41. import MySQLdb as mdb
42. import numpy as np
43. import openpyxl
44. import os
45. import os.path
46. import pandas as pd
47. import pandas
48. import paramiko
49. import pathlib
50. import platform
51. import plotly
52. import plotly.graph_objs as go
53. import poplib
54. import pprint
55. import psutil
56. import pyAesCrypt
57. import pyPdf
58. import PyPDF2
59. import random
60. import re
61. import requests
62. import resource
63. import sample
64. import shutil
65. import signal
66. import smtplib
67. import socket
68. import sqlite3
69. import stat
70. import string
71. import subprocess
72. import sys
73. import tarfile
74. import telnetlib
75. import tempfile
76. import textwrap
77. import time
78. import timeit
79. import unittest
80. import urllib.request
81. import warnings
82. import webbrowser
83. import xlrd
84. import zeep
85. import zipfile
86. from math import sqrt
---
### **websites**
1. [www.pythoncheatsheet.org](https://www.pythoncheatsheet.org/cheatsheet/basics)
2. [github.com wilfredinni] (https://github.com/wilfredinni/python-cheatsheet.git)
---
Here's a list of essential Python modules that are useful for Linux system administration tasks:

### 1. **OS and File Management**  
- **os** – Interact with the operating system.  
- **shutil** – File and directory operations (copy, move, delete).  
- **pathlib** – Object-oriented filesystem paths.  
- **glob** – File pattern matching.  
- **stat** – File statistics.  
- **fnmatch** – Unix filename pattern matching.  

### 2. **Process and System Monitoring**  
- **subprocess** – Run shell commands and processes.  
- **psutil** – Monitor and manage system processes, CPU, memory, and disk.  
- **signal** – Signal handling.  
- **time** – Time-related functions.  

### 3. **Networking**  
- **socket** – Low-level networking interface.  
- **paramiko** – SSH protocol for remote administration.  
- **fabric** – Automate SSH commands and deployments.  
- **requests** – HTTP requests.  
- **http.client** – Low-level HTTP connections.  
- **netifaces** – Network interface information.  

### 4. **Security and Encryption**  
- **hashlib** – Hashing (MD5, SHA).  
- **cryptography** – Encrypt, decrypt, and generate secure certificates.  
- **ssl** – SSL/TLS for encrypted communications.  

### 5. **Automation and Scheduling**  
- **schedule** – Job scheduling.  
- **croniter** – Parse and handle cron expressions.  
- **threading** – Multithreading for parallel execution.  
- **multiprocessing** – Run parallel processes.  

### 6. **Configuration Management**  
- **configparser** – Parse INI configuration files.  
- **json** – Handle JSON configurations.  
- **yaml** – YAML configuration parsing.  
- **argparse** – CLI argument parsing.  
- **click** – Create command-line interfaces.  

### 7. **System Information**  
- **platform** – System and Python interpreter details.  
- **distro** – Linux distribution detection.  
- **uname** – System information (like `uname -a`).  

### 8. **Database Management**  
- **sqlite3** – Lightweight local database.  
- **pymysql** – Connect to MySQL databases.  
- **psycopg2** – Connect to PostgreSQL databases.  

### 9. **Backup and Archiving**  
- **zipfile** – Create and extract ZIP files.  
- **tarfile** – Work with tar archives.  
- **logging** – Log messages and system events.  

### 10. **Task Queuing and Distributed Systems**  
- **celery** – Distributed task queue.  
- **redis** – In-memory data structure for caching and queuing.  

---
