import re
from collections import Counter

def detect_suspicious_activity(logs_file, attempts):
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?(401|Invalid credentials)'
    failed_attempts = Counter()
    
    try:
        with open(logs_file, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    ip = match.group("ip")
                    failed_attempts[ip] += 1
    except FileNotFoundError:
        print(f"Error: File '{logs_file}' not found.")
        return None
    
   
    suspicious_ips = []
    for ip, count in failed_attempts.items():
        if count > attempts:
            suspicious_ips.append((ip, count))
            
    return suspicious_ips


def main():
    log_file = "sample.log"
    attempts = 4  # Threshold for failed login attempts

    suspicious_activity = detect_suspicious_activity(log_file, attempts)
    
    if suspicious_activity:
        print("Suspicious Activity Detected:")
        print(f"{'IP Address':<20} {'Failed Login Attempts':<20}")
        for ip, count in suspicious_activity:
            print(f"{ip:<20} {count:<20}")
    else:
        print("No suspicious activity detected.")

if __name__ == "__main__":
    main()
