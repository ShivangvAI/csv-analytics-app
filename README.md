# CSV-analytics-app
CSV Analytics Dashboard built with Streamlit
# 📊 Memory-Safe Large Dataset Analyzer

A high-performance, memory-efficient data analysis dashboard built with **Streamlit**, **Pandas**, and **Matplotlib**. This application is engineered to handle massive CSV files (up to 1 GB) smoothly on standard consumer hardware without running out of RAM or crashing the server.

## ✨ Features

- **Chunked Data Processing:** Utilizes specialized Pandas stream chunking (`chunksize=100,000`) to process massive data footprints in low-RAM environments.
- **Instant Data Previews:** Safely reads and displays the top rows of a dataset instantly without parsing the entire file into memory first.
- **Automated Missing Data Audits:** Scans datasets incrementally to map and log null values across all dimensions.
- **Dynamic Subject Averages Chart:** Identifies numerical metrics (like Math, English, etc.) and visually scales performance averages.
- **Student Performance Distribution:** Computes row-wise student averages on the fly and groups them into an interactive distribution histogram.

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** (Web Dashboard Framework)
- **Pandas** (Memory-Optimized Data Processing)
- **Matplotlib / NumPy** (Lightweight Aggregated Visualizations)

## 🚀 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Increase Upload Threshold:**
   Ensure your `.streamlit/config.toml` file allows large file sizes:
   ```toml
   [server]
   maxUploadSize = 1024
   ```

3. **Run the Dashboard:**
   ```bash
   streamlit run app.py
   ```
