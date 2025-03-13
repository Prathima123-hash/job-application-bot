import requests

def apply_for_jobs():
    url = "https://example-job-portal.com/apply"  # Replace with actual job portal
    payload = {
        "name": "Your Name",
        "email": "your.email@example.com",
        "resume": "path/to/your/resume.pdf"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Application submitted successfully!")
    else:
        print("Failed to apply:", response.text)

if __name__ == "__main__":
    apply_for_jobs()
