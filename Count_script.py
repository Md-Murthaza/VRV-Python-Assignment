import re
from collections import Counter

Log_file_Path = "sample.log"

Log_pattern=r'(?P<ip>\d+\.\d+\.\d+\.\d+)'

def read_and_parselog(logs_file):
    ip_counter = Counter()

    with open(logs_file,'r') as file:
        for files in file:
            match = re.match(Log_pattern,files.strip())
            if match:
                ip_address = match.group('ip')
                ip_counter[ip_address]+=1
    return ip_counter

def request_count(ip_counter):
    sorted_ip_count = ip_counter.most_common()
    print(f"{'IP Address':20} {'Request Count'}")   
    print("=" * 35) 
    
    for ip , count in sorted_ip_count:
        print(f"{ip:20} {count}")



#main format
if __name__ == "__main__":
    ip_counter = read_and_parselog(Log_file_Path)
    request_count(ip_counter)
