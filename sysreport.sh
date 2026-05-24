#!/bin/bash
set -euo pipefail
date
echo ""
#-e : any error will immediately exit
#-u : will catch any variables that are undefined and exit immediately
#-o : prevents errors in the pipeline from being masked and returns the error code of the command that failed as the error code of the entire pipeline

get_hostname(){
	echo "---------HOSTNAME-----------"
	my_host=$(hostname)
	echo "Hostname: $my_host"
	echo "----------------------------"
}

get_kernel_info(){
	echo ""
	echo "----------KERNEL------------"
	my_kernel=$(uname -a)
	echo "Kernel info: $my_kernel"
	echo "----------------------------"
}

get_uptime(){
	echo ""
	echo "--------UPTIME--------------"
	sys_uptime=$(uptime)
	echo "Uptime: $sys_uptime"
	echo "----------------------------"
}

memory(){
	echo ""
	echo "----------MEMORY------------"
	free -h
	echo "----------------------------"
}

disk_usage(){
	usage_limit=80
	echo ""
	echo "---------DISK USAGE----------"
	df -h
	echo ""
	df -h | tail -n +2 | while read -r line; do
		current_usage=$(echo "$line" | awk '{print $5}' | tr -d '%')
		current_name=$(echo "$line" | awk '{print $1}')
	if [ "$current_usage" -gt "$usage_limit" ]; then
		echo "WARNING: "$current_name" is over the "$usage_limit" precent disk usage limit!" 
	fi
	done

	echo "-----------------------------"
}

top_5_processes_by_memory(){
	echo ""
	echo "--------Processes------------"
	ps aux --sort=-%mem | head -n 6
	echo "-----------------------------"
}

failed_services(){
	if ( ! systemctl --quiet is-failed ); then
		echo ""
		echo "----Unit/services check------"
		echo "No failed units/services"
	else
		echo ""
		echo "-------Failed Units----------"
		systemctl --failed
	fi	
		echo "-----------------------------"
}
show_tcp_ports(){
	echo ""
	echo "---------TCP-----------------"
	ss -tlnp
	echo "-----------------------------"
}

logged_in_users(){
	echo ""
	echo "---------Users---------------"
	w
	echo "-----------------------------"
}


get_hostname
get_kernel_info
get_uptime
memory
disk_usage
top_5_processes_by_memory
failed_services
show_tcp_ports
logged_in_users


