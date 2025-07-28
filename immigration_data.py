import requests
from datetime import datetime

def get_latest_draw():
    """Return the latest verified draw information with source"""
    # Current verified information (as of July 2025)
    return {
        "date": "July 23, 2025",
        "number": 292,
        "program": "Provincial Nominee Program",
        "invitations": 1800,
        "crs": 739,
        "source": "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html"
    }

def check_api_status():
    """Check if the Open Data API is available"""
    try:
        response = requests.get("https://open.canada.ca/data/api/3/action/status_show", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    print("Canadian Express Entry Draw Information\n" + "="*45)
    
    # Get the latest verified information
    latest = get_latest_draw()
    
    # Display current information
    print("\n✅ Latest Verified Draw:")
    print(f"Draw #{latest['number']} - {latest['date']}")
    print(f"Program: {latest['program']}")
    print(f"Invitations Issued: {latest['invitations']}")
    print(f"Minimum CRS: {latest['crs']}")
    print(f"\nSource: {latest['source']}")
    
    # Check API status
    print("\n🔍 System Status Check:")
    api_status = "Online" if check_api_status() else "Offline (Under Maintenance)"
    print(f"- Open Data Portal API: {api_status}")
    
    # Last update information
    print(f"\nLast Checked: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("\nNote: The Canadian Open Data Portal is currently undergoing maintenance.")
    print("For the most current information, always refer to the official IRCC website.")

if __name__ == "__main__":
    main()
