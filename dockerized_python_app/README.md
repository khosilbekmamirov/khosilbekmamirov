# Khosilbek Mamirov — Projects Portfolio

This repository contains real projects demonstrating skills in **Python, Docker, Linux, and Cybersecurity**.  

## Projects

### 1. Log Intrusion Detector
- **Language:** Python 3  
- **Description:** Parses log files (`auth.log` or sample logs) and identifies top suspicious IPs.  
- **Features:**
  - Counts failed login attempts
  - Outputs top suspicious IPs
  - Ready for integration with remote Linux servers
- **Usage:**
```bash
cd log_intrusion_detector
python detector.py -f log_sample.txt
