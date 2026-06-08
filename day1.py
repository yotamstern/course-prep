log_lines = [
    "INFO  user logged in",
    "ERROR database connection failed",
    "WARN  disk usage at 82%",
    "INFO  request handled in 45ms",
    "ERROR null pointer in handler",
    "INFO  cache refreshed",
    "WARN  retry attempt 2",
    "ERROR timeout contacting service",
    "INFO  user logged out",
    "WARN  config value deprecated",
    "ERROR database connection failed",
    "INFO  healthcheck passed",
]
list_type = ["INFO", "WARN", "ERROR"]
log_dict = {key: [] for key in list_type}
count_info = count_error = count_warn = 0
for i in log_lines:
    word = i.split()[0]
    match word:
        case "INFO":
            log_dict["INFO"].append(i.split(maxsplit=1)[1])
            count_info += 1
        case "ERROR":
            log_dict["ERROR"].append(i.split(maxsplit=1)[1])
            count_error += 1
        case "WARN":
            log_dict["WARN"].append(i.split(maxsplit=1)[1])
            count_warn += 1
        case _:
            print("Unknown logging format")

highest_count = max(count_info, count_error, count_warn)
name_of_highest = "ERROR" if highest_count == count_error else "WARN" if highest_count == count_warn else "INFO"
print(f"Highest log count was {highest_count} which is {name_of_highest}")
print(f"INFO was logged {count_info} times")
print(f"WARN was logged {count_warn} times")
print(f"ERROR was logged {count_error} times")
