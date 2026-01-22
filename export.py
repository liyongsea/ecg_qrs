import wfdb
import json
import os
import numpy as np
import tqdm

# --- Configuration ---
data_dir = 'mit_bih_data'
output_dir = 'mit_bih_json_exports'
start_seconds = 120  # 2 minutes
end_seconds = 180    # 3 minutes

# Valid heartbeats (same as before)
valid_beats = [
    'N', 'L', 'R', 'B', 'A', 'a', 'J', 'S', 'V', 
    'r', 'F', 'e', 'j', 'n', 'E', '/', 'f', 'Q', '?'
]

def process_and_export_records():
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of local records by scanning the directory for .dat files
    # (removing extensions to get the ID)
    record_files = [f.replace('.dat', '') for f in os.listdir(data_dir) if f.endswith('.dat')]
    record_files.sort()

    print(f"Found {len(record_files)} records to process.")

    for record_name in tqdm.tqdm(record_files):
        try:
            record_path = os.path.join(data_dir, record_name)
            
            # Read header to get frequency first (lightweight)
            header = wfdb.rdheader(record_path)
            fs = header.fs
            
            # Calculate sample ranges
            sampfrom = start_seconds * fs
            sampto = end_seconds * fs
            
            # 1. Read Signal Slice
            # wfdb allows reading specific ranges directly
            record = wfdb.rdrecord(record_path, sampfrom=sampfrom, sampto=sampto)
            
            # 2. Read Annotation Slice
            # We read annotations within the range
            annotation = wfdb.rdann(record_path, 'atr', sampfrom=sampfrom, sampto=sampto)
            
            # 3. Filter and Adjust Annotations
            # The annotation.sample values are absolute (from start of recording).
            # We must subtract 'sampfrom' to make them relative to our new slice.
            qrs_locs = []
            qrs_types = []
            
            for samp, sym in zip(annotation.sample, annotation.symbol):
                if sym in valid_beats:
                    # Adjust index to be relative to the start of the 2-minute mark
                    relative_sample = int(samp - sampfrom)
                    qrs_locs.append(relative_sample)
                    qrs_types.append(sym)
            
            # 4. Construct Data Dictionary
            # Convert signal to list (nested list: [sample_index][lead_index])
            signal_list = record.p_signal.tolist()
            
            output_data = {
                "record_id": record_name,
                "sampling_rate": fs,
                "start_time_sec": start_seconds,
                "end_time_sec": end_seconds,
                "leads": record.sig_name,
                "qrs_indices": qrs_locs,   # Indices relative to the start of this slice
                "qrs_types": qrs_types,    # The type of beat (N, A, V, etc.)
                "signal": signal_list      # 2D array: [samples x leads]
            }
            
            # 5. Save to JSON
            output_filename = os.path.join(output_dir, f"{record_name}.json")
            with open(output_filename, 'w') as f:
                json.dump(output_data, f)
                
            print(f"Exported Record {record_name} -> {output_filename}")
            
        except Exception as e:
            print(f"Skipping Record {record_name}: {e}")

if __name__ == "__main__":
    process_and_export_records()