from Count_script import read_and_parselog
from most_accessed import finding_most_accessed_endpoint
from suspicious_activity import detect_suspicious_activity
import csv

def save_to_csv(ip_requests, most_accessed, suspicious_activities, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

       
        csv_writer.writerow(["IP Address", "Request Count"])
        
        for ip, count in ip_requests.most_common():
            csv_writer.writerow([ip, count])

        csv_writer.writerow([])
        csv_writer.writerow(["Most Accessed Endpoint", "Access Count"])
        if most_accessed:
            endpoint, count = most_accessed
            csv_writer.writerow([endpoint, count])

        csv_writer.writerow([])
        csv_writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in suspicious_activities:
            csv_writer.writerow([ip, count])


def main():
  
    log_file = "sample.log"
    output_file = "log_analysis_results.csv"
    threshold = 4  


    # Requests per IP
    
    ip_counter = read_and_parselog(log_file)
    print(f"{'IP Address':<20} {'Request Count':<15}")
    for ip, count in ip_counter.most_common():
        print(f"{ip:<20} {count:<15}")
    
    # Most Accessed Endpoint
    most_accessed = finding_most_accessed_endpoint(log_file)
    if most_accessed:
        endpoint, count = most_accessed
        print(f"\nMost Frequently Accessed Endpoint:\n{endpoint} (Accessed {count} times)")

    # Suspicious Activities
    suspicious_activity = detect_suspicious_activity(log_file, threshold)
    if suspicious_activity:
        print("\nSuspicious Activity Detected:")
        print(f"{'IP Address':<20} {'Failed Login Attempts':<20}")
        for ip, count in suspicious_activity:
            print(f"{ip:<20} {count:<20}")
    else:
        print("\nNo suspicious activity detected.")

   
    save_to_csv(ip_counter, most_accessed, suspicious_activity, output_file)
    print(f"\nResults saved to '{output_file}'.")

if __name__ == "__main__":
    main()
