# 🤖 OpsBot – Log Automator

A high-performance, memory-efficient Python tool designed to parse enterprise log files and extract critical security alerts.**.

---

## 📌 Overview

**OpsBot** is designed to handle **log files** without exhausting system memory.  
It follows a **streaming-based architecture** for efficient log processing and alert detection.

---

## 🚀 Key Features

- **Chunk-Based Processing**  
  Uses a **1 MB buffered read approach** to process large files efficiently.

- **O(N) Time Complexity**  
  Performs a **single-pass linear scan** for optimal performance.

- **Enterprise-Ready Detection**  
  Detects:
  - `CRITICAL`
  - `ERROR`
  - `FAILED LOGIN`  
  using **case-insensitive pattern matching**.

- **Automated Reporting**  
  Generates:
  - **Alert frequency counts**  
  - **Detailed logs of detected events**

---

## 🛠️ Installation

**Clone the repository:**

```bash
git clone https://github.com/SVidhya4/OpsBot-Log-Automator.git
cd OpsBot-Log-Automator
```

---

## 🚀 How to Use

To see OpsBot in action, you need a log file named **server.log** in the same directory as the script.

### 1. Prepare your log file

Ensure you have a file named **server.log**.
Supported format (Log4j-style logs): YYYY-MM-DD HH:MM:SS [Thread-ID] LEVEL IP Logger - Message 'User'

### 2. Run the Analysis

Execute the main script using Python:

```bash
python opsBot.py
```
