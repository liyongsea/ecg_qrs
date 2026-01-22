# ECG QRS Detection Challenge

This repository contains the workflow and implementation for developing an automated QRS detection algorithm using the MIT-BIH Arrhythmia Database.

## 1. Domain Background

### What is an ECG?
An **Electrocardiogram (ECG)** is a recording of the electrical activity of the heart over time. It is captured via electrodes placed on the skin and is the primary tool for diagnosing cardiac arrhythmias.

### What is the QRS Complex?
https://en.wikipedia.org/wiki/QRS_complex
The ECG signal consists of several waves (P, QRS, T) that correspond to different phases of the heart's polarization.
* **P-wave:** Atrial depolarization (upper chambers contract).
* **QRS complex:** Ventricular depolarization (lower chambers contract). This is the most prominent feature of the ECG and corresponds to the main heartbeat.
* **T-wave:** Ventricular repolarization (recovery).



**Accurate detection of the QRS complex is the fundamental first step in almost all automated ECG analysis**, as it allows for the calculation of heart rate and the segmentation of individual beats.

## 2. The Task

The objective of this project is to build and evaluate a robust algorithm to automatically detect QRS complexes in raw ECG signals. The project is structured into four stages:

### Phase 1: Data Understanding
* Download and inspect the **MIT-BIH Arrhythmia Database** (the gold standard for ECG analysis).
* Visualize raw signals alongside expert annotations (ground truth).
* Handle data parsing and signal extraction (filtering for specific leads and time windows).

### Phase 2: Baseline Algorithm
* Implement a **simple, rule-based QRS detector** (e.g., thresholding or moving averages) to establish a baseline performance.
* Focus on speed and simplicity over perfect accuracy.

### Phase 3: Metrics & Evaluation
* Define standard performance metrics.
* Implement an evaluation script to calculate **Sensitivity (Recall)** and **Positive Predictive Value (Precision)** against the MIT-BIH annotations.

### Phase 4: Optimization
* Split the dataset into **Training** and **Testing** sets to avoid data leakage.
* Implement a more sophisticated algorithm (e.g., Pan-Tompkins, Wavelet Transform, or a 1D CNN) to improve upon the baseline.
* Benchmark the final model on the hidden Test set.

## 3. Getting Started

### Prerequisites
The project relies on the PhysioNet `wfdb` library for data access.

```bash
pip install wfdb numpy matplotlib pandas scipy

```

### Repository Structure

* `notebooks/`: Exploratory Data Analysis (EDA) and visualization.
* `src/data_loader.py`: Scripts to download and parse MIT-BIH data.
* `src/detector.py`: Implementation of QRS detection algorithms.
* `src/evaluate.py`: Evaluation metrics and scoring logic.
* `data/`: Local storage for downloaded PhysioNet records.

## 4. References

* **Dataset:** [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/)
* **Standard:** [ANSI/AAMI EC57:1998](https://www.aami.org/) (Testing and reporting performance results of cardiac rhythm and ST-segment measurement algorithms).
