# Task Accuracy Log Manager

A persistent CLI tool for recording and reviewing task accuracy metrics.

## Project Status: Completed & Finalized
This project is fully functional, stable, and fulfills all its initial design goals. It is a completed portfolio piece and is no longer under active development or maintenance.

## Features
- Calculates performance accuracy percentages based on correct and total numeric metrics.
- Parses and streams historical records from a local flat-file storage system (`records.txt`) into memory.
- Utilizes structured in-memory data collections (lists of dictionaries) to manipulate and review historical transaction lines.

## Why this project
Demonstrates real-world data handling, basic serialization patterns, and persistence without external frameworks.

## Python Version Compatibility
- **Developed and Tested On:** Python 3.13
- **Supported Versions:** This script uses standard built-in features and is fully compatible with **Python 3.6 up to the latest Python 3.13+**.
- **Dependencies:** None. This project runs entirely using the core Python language without requiring any external libraries.

## How to Run
Run the script from your terminal using:
```bash
python log_manager.py
```
