# IP Collections Converter

A simple tool to convert Excel (.xlsx/.xls) and CSV files to importable JSON format for PSM to create IP Collections.

## Usage

```bash
python3 csv-to-json.py
```

Just follow the prompts to enter your input file path. The script will generate `ip_collections.json` in the same directory.

## Supported Formats

- **CSV files**: Format with columns for name, address-type, ip-addresses, ip-collections

## Supported IP Address Types

- Single IPv4 addresses: `10.1.1.1`
- IPv4 subnets: `10.5.5.0/24`
- IPv4 ranges: `10.8.8.1-10.8.8.99`
- Mixed formats in a single entry

## Output Format

The tool produces a structured JSON file with standardized IP collections:

![image](https://github.com/Max1211/Images/blob/main/ip-collection-import.png)
![image](https://github.com/Max1211/Images/blob/main/ip-collections.png)
