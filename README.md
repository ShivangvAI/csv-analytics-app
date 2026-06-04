# Memory-Safe Large Dataset Analyzer

A high-performance, memory-optimized Streamlit web application built to analyze massive CSV datasets (up to 1GB) without crashing your system or exceeding cloud hosting memory thresholds.

🔗 **Live Application URL:** [https://csv-analytics-app-mxvdbfeeylq45rd5vtcay4.streamlit.app/]

---

## Key Features

* **1GB File Upload Support:** Custom server configuration engineered to override standard upload bottlenecks.
* **Memory-Safe Chunk Processing:** Dynamically reads and compiles datasets in smaller fragments (`chunks`) to ensure low, stable RAM utilization.
* **Instant Analytics Summary:** Automatically tracks dataset shapes, column names, missing data patterns, and basic statistical aggregates.
* **Interactive Filtering:** Allows granular data evaluation without parsing the entire file into global RAM all at once.

---

## Tech Stack & Architecture

* **Language:** Python 3.11+
* **Framework:** Streamlit (UI & Web Interface)
* **Core Library:** Pandas (Engineered with `chunksize` iterator parameters)
* **Hosting Platform:** Streamlit Community Cloud

---

## Local Installation & Setup

If you want to run this application locally on your computer, follow these simple steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd CSV-analytics-app
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the web interface:**
   ```bash
   streamlit run app.py
   ```

---

## How It Works Under the Hood

Standard CSV loaders import entire files directly into system RAM. If your dataset is 800MB, it can balloon up to 3GB of active RAM memory during parsing. 

This app utilizes an **Iterator Chunking Strategy**:
```python
# Conceptual memory workflow used in the background
for chunk in pd.read_csv("large_file.csv", chunksize=50000):
    process_metrics(chunk)  # Memory is flushed after every iteration block!
```
This guarantees that whether your file is 10MB or 1GB, the system RAM profile remains flat, constant, and fast.
   ```

3. **Run the Dashboard:**
   ```bash
   streamlit run app.py
   ```
