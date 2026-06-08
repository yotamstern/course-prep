
def read_file(file,ip_dict):
    for ip in file:
        clean_line = ip.strip()
        if not clean_line:
            continue
        else:
            if clean_line not in ip_dict:
                ip_dict[clean_line] = 1
            else:
                ip_dict[clean_line] += 1
    top_3_ips = dict(sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)[:3])
    return top_3_ips


def main():
    ip_dict = {}
    try:
        with open('ips.txt', 'r') as file:
            top_3_ips = read_file(file, ip_dict)
    except FileNotFoundError:
        print("File is not found")
        return
    print(f"Top 3 IPs are: {', '.join(f'{ip} ({count} times)' for ip, count in top_3_ips.items())}")


if __name__ == "__main__":
    main()
