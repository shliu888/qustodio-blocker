import os
import shutil


domains = [
    'qustodio.com',
    'api.qustodio.com',
    'logs.qustodio.com',
    'reports.qustodio.com',
    'analytics.qustodio.com',
    'monitoring.qustodio.com',
    'status.qustodio.com',
    'statistics.qustodio.com',
    'activities.qustodio.com',
    'access.qustodio.com'
]

# Path to the hosts file
hosts_path = '/etc/hosts'

# Backup the hosts file
backup_path = '/etc/hosts.bak'
shutil.copy(hosts_path, backup_path)
print("Backup created: ",str(backup_path))

try:
    with open(hosts_path, 'a') as hosts_file:
        for i in domains:
            hosts_file.write("127.0.0.1 "+domain+'\n')
    print("Task completed.")
except PermissionError:
    print("Permission denied: You need to run this script with admin privileges.")
 
