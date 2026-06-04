import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Large Data Analyzer", page_icon="📊", layout="wide")
st.title("📊 Memory-Safe Large Dataset Analyzer")
st.write("Optimized to handle files up to 1 GB safely using chunked data processing.")

# 2. File Uploader Widget 
uploaded_file = st.file_uploader("Upload your large CSV file", type=["csv"])

if uploaded_file is not None:
    
    # --- STEP 1: DATASET PREVIEW ---
    st.subheader("Dataset Preview (First 5 Rows)")
    df_preview = pd.read_csv(uploaded_file, nrows=5)
    st.dataframe(df_preview)
    
    uploaded_file.seek(0)
    
    # --- STEP 2: CHUNKED PROCESSING ---
    chunk_size = 100000 
    total_rows = 0
    total_missing = None
    
    # Identify numerical columns for calculations (e.g., Math, English)
    numeric_cols = df_preview.select_dtypes(include=['number']).columns.tolist()
    column_sums = {col: 0 for col in numeric_cols}
    column_counts = {col: 0 for col in numeric_cols}
    
    # Initialize a global histogram tracker for student averages
    # This keeps counts of student averages in specific score ranges (0 to 100+)
    bin_edges = np.arange(0, 105, 5)  # Bins: 0-5, 5-10, ..., 95-100
    hist_counts = np.zeros(len(bin_edges) - 1)
    
    with st.spinner("Processing large dataset in chunks to optimize memory..."):
        for chunk in pd.read_csv(uploaded_file, chunksize=chunk_size):
            total_rows += len(chunk)
            
            # 1. Missing values aggregation
            if total_missing is None:
                total_missing = chunk.isnull().sum()
            else:
                total_missing += chunk.isnull().sum()
                
            # 2. Accumulate metrics for subject averages
            for col in numeric_cols:
                clean_series = chunk[col].dropna()
                column_sums[col] += clean_series.sum()
                column_counts[col] += clean_series.count()
            
            # 3. Calculate each student's average row-by-row within this chunk
            if numeric_cols:
                # Calculates row-wise average across the subjects for this chunk
                student_averages = chunk[numeric_cols].mean(axis=1).dropna()
                
                # Incrementally count how many students fall into each score bin
                chunk_counts, _ = np.histogram(student_averages, bins=bin_edges)
                hist_counts += chunk_counts
                
    # --- STEP 3: METRICS DISPLAY ---
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dataset Dimensions")
        num_columns = len(df_preview.columns)
        st.metric(label="Total Rows", value=f"{total_rows:,}")
        st.metric(label="Total Columns", value=num_columns)
        
    with col2:
        st.subheader("Missing Values Table")
        st.write(total_missing)
        
    # --- STEP 4: DATA VISUALIZATION ---
    st.markdown("---")
    vis_col1, vis_col2 = st.columns(2)
    
    with vis_col1:
        st.subheader("Subject Averages")
        if numeric_cols:
            averages = {col: column_sums[col] / column_counts[col] for col in numeric_cols if column_counts[col] > 0}
            df_averages = pd.Series(averages)
            
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            df_averages.plot(kind="bar", ax=ax1, color="#4B7BFF")
            ax1.set_ylabel("Average Score")
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig1)
        else:
            st.info("No numerical columns found.")

    with vis_col2:
        st.subheader("Student Performance Distribution")
        if numeric_cols and hist_counts.sum() > 0:
            # Recreate the histogram curve safely using the collected tiny bin summary counts
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            
            # Plotting the pre-calculated histogram counts safely
            bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
            ax2.bar(bin_centers, hist_counts, width=4, color="#2ECC71", edgecolor="black", alpha=0.8)
            
            ax2.set_xlabel("Student Average Score Range")
            ax2.set_ylabel("Number of Students")
            ax2.set_title("How Students are Performing Globally")
            plt.grid(axis='y', linestyle='--', alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig2)
        else:
            st.info("Could not generate student averages.")

    # --- STEP 5: MISSING DATA STATUS ---
    st.markdown("---")
    st.subheader("Missing Data Status")
    if total_missing.sum() > 0:
        st.warning(f"Found missing values. Check the table above.")
    else:
        st.success("Excellent data quality! Zero missing values detected across the entire dataset.")