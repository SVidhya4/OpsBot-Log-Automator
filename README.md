# 🤖 OpsBot – Log Automator

A high-performance, memory-efficient Python tool designed to parse enterprise log files and extract critical security alerts.**.

---

## 📌 Overview

**OpsBot** is designed to handle **log files** without exhausting system memory.  
It follows a **streaming-based architecture** for efficient log processing and alert detection.

---

## 🚀 Key Features

- **Streaming Architecture (O(1) Space)** Writes alerts directly to disk during the scan. This ensures **constant memory usage** whether processing 1 MB or 100 GB of data.

- **Chunk-Based Processing** Uses a **1 MB buffered read approach** (`readlines(hint)`) to minimize Disk I/O bottlenecks.

- **O(N) Time Complexity** Performs a **single-pass linear scan**, achieving the theoretical lower bound for log parsing performance.

- **Enterprise-Ready Detection** Optimized for **Log4j/Spring Boot** formats, detecting `CRITICAL`, `ERROR`, and `FAILED LOGIN` events using case-insensitive matching.

---

## 🛠️ Technical Highlights (Inch-by-Inch Optimization)

To achieve "Prime" grade performance, this tool implements:
1. **Pre-Calculated Targets:** Lower-case search keywords are computed once during initialization to save CPU cycles inside the million-line processing loop.
2. **Dual-File Pointers:** Simultaneously manages an input stream (Log) and an output stream (Report) to prevent large in-memory data structures.
3. **Regex-Free Core:** Uses high-speed string evaluation for the primary filter to reduce overhead compared to complex regex engines.
   
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
