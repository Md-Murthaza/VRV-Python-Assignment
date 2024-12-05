import re
from collections import Counter

def finding_most_accessed_endpoint(logs_file):
    pattern = r'"(?:GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) (?P<endpoint>\S+)'
    counts = Counter()



    try:
        with open(logs_file, 'r') as file :
            for files in file:
                match = re.search(pattern,files)
                if match:
                    endpoint = match.group("endpoint")
                    counts[endpoint] +=1

    except FileNotFoundError:
        print(f"File '{logs_file}' not Found")
        return None
        
                

    if counts:
        most_common = counts.most_common(1)[0]
        return most_common

    else:
        print("No endpoints found in the log file")
        return None

def main():
    log_file = "sample.log"
    result = finding_most_accessed_endpoint(log_file)

    if result:
        endpoint,Count = result
        print(f"Most Frequently Accessed Endpoint:\n{endpoint} (Accessed {Count} times)")

    else:
        print("Unable to find it.")

if __name__ == "__main__":
    main()

