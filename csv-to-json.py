import json
import os
import csv

def convert_csv_to_json(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' was not found.")
    
    if not input_file.lower().endswith('.csv'):
        raise ValueError("The input file must be a CSV file (.csv)")
    
    # Initialize the result list
    ip_collections = []
    
    # Read CSV file, skipping the header row
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        
        for row in reader:
            if len(row) >= 4:  # Ensure we have enough columns
                name = row[0].strip()
                address_type = row[1].strip()
                ip_addresses = row[2].strip()
                
                # Split IP addresses on commas or spaces
                ips = []
                for ip in ip_addresses.replace(',', ' ').split():
                    ip = ip.strip()
                    if ip:  # Only add non-empty strings
                        ips.append(ip)
                
                if name and ips:
                    ip_collections.append({
                        "name": name,
                        "address-type": address_type,
                        "ip-addresses": ips,
                        "ip-collections": []  # Empty list as specified
                    })
    
    # Write to JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(ip_collections, jsonfile, indent=2)

if __name__ == "__main__":
    try:
        input_file = input("Please enter the name of the CSV file (including .csv extension): ")
        output_file = "ip_collections.json"
        
        convert_csv_to_json(input_file, output_file)
        print(f"\nConversion successful!")
        print(f"Output saved as: {output_file}")
        
    except FileNotFoundError as e:
        print(f"\nError: {e}")
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")