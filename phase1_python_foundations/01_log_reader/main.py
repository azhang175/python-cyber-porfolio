import os

count = 0
error_count = 0
warning_count = 0 
filename = os.path.join("sample_data", "sample.log")

try:
    with open("sample_data/sample.log", "r") as f:
        for line in f:
            count += 1
            if "ERROR" in line:
                error_count += 1
            if "WARNING" in line:
                warning_count += 1
except FileNotFoundError:
    print("There is no such file or directory")

print("count:", count)
print("error count:", error_count)
print("warning count:", warning_count)