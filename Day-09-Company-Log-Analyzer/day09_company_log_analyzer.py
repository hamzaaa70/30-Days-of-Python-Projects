import re


print("       COMPANY LOG ANALYZER")



# Open the log file
log_file = open("server.log", "r")


# Counters
total_entries = 0
info_count = 0
warning_count = 0
error_count = 0


# Store error messages
errors = []


# Read log file line by line
for line in log_file:

    # Remove unnecessary whitespace
    line = line.strip()

    # Count total entries
    total_entries = total_entries + 1


    # Check INFO
    if "INFO" in line:

        info_count = info_count + 1


    # Check WARNING
    elif "WARNING" in line:

        warning_count = warning_count + 1


    # Check ERROR
    elif "ERROR" in line:

        error_count = error_count + 1


        # Extract error message
        match = re.search(r"ERROR (.*)", line)


        if match:

            error_message = match.group(1)

            errors.append(error_message)


# Close the file
log_file.close()


# Display report
print()
print("========== LOG ANALYSIS REPORT ==========")

print()
print("Total log entries:", total_entries)

print("INFO messages:", info_count)

print("WARNING messages:", warning_count)

print("ERROR messages:", error_count)


print()
print("Error messages:")

for error in errors:

    print("-", error)


print()
print("==========================================")