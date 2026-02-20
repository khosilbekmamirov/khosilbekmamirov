# Log Intrusion Detector

A simple Python script to analyze Linux auth logs and find suspicious IPs.

## Features
- Reads auth.log or sample log files
- Detects failed SSH login attempts
- Displays top 5 suspicious IPs

## Tech Stack
- Python 3
- Regex
- Collections

## How to Run
```bash
cd log_intrusion_detector
python3 detector.py log_sample.txt
