"""
Utility functions for the project.
"""

import csv
import json

def export_to_csv(data, filename):
    """Export list of dicts to CSV file."""
    if not data:
        return
    with open(filename, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def export_to_json(data, filename):
    """Export data to JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
