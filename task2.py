import os 

# List of all active OS processes sorted by PID and save output to os_process.txt
process_list = os.popen("wmic process get ProcessId,Description,ParentProcessId > os_process.txt")   
