import urllib.request
import csv
from datetime import datetime
import ssl

print("Fetching latest Canadian immigration data...\n")

try:
    # Bypass SSL verification
    ssl_context = ssl._create_unverified_context()
    
    # Direct download URL
    url = "https://open.canada.ca/data/en/dataset/90115b00-f8b5-4a34-86e1-d96fae81a4d3/resource/522b07bd-9f8d-4a89-84f9-8330f190f62e/download/express-entry-rounds.csv"
    
    print("Downloading data...")
    with urllib.request.urlopen(url, context=ssl_context) as response:
        csv_data = response.read().decode('utf-8')
    
    # Parse CSV data
    reader = csv.DictReader(csv_data.splitlines())
    latest_draw = next(reader)  # Get first/most recent record
    
    # Print results
    print("\n✅ Latest Express Entry Draw Results:")
    print("====================================")
    print(f"Draw Number: #{latest_draw['drawNumber']}")
    print(f"Date: {latest_draw['drawDate']}")
    print(f"Program: {latest_draw['drawName']}")
    print(f"Invitations: {latest_draw['drawSize']}")
    print(f"Minimum CRS: {latest_draw['drawCRS']}")
    
    # Save full data to CSV
    with open('canada_immigration_data.csv', 'w', encoding='utf-8', newline='') as f:
        f.write(csv_data)
    
    print("\n✅ Full dataset saved to: canada_immigration_data.csv")
    print(f"\nRetrieved: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")

except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    print("\nTroubleshooting options:")
    print("1. Visit the data source directly:")
    print("   https://open.canada.ca/data/en/dataset/90115b00-f8b5-4a34-86e1-d96fae81a4d3")
    print("2. Try again later")
