import wfdb
import os

def download_all_mit_bih_data(download_dir='mit_bih_data'):
    """
    Downloads ALL records from the MIT-BIH Arrhythmia Database.
    """
    # Create the download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"Directory ensured: {download_dir}")

    try:
        # 1. Get the list of all records in the 'mitdb' database
        print("Fetching record list for 'mitdb'...")
        record_list = wfdb.get_record_list('mitdb')
        print(f"Found {len(record_list)} records: {record_list}")

        # 2. Download all records in the list
        print("Starting download (this may take a few moments)...")
        wfdb.dl_database('mitdb', download_dir, records=record_list)
        
        print(f"Successfully downloaded all {len(record_list)} records to {download_dir}/")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_all_mit_bih_data()