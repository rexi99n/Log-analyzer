access_log = open("access.log", "r")
no_ip_logs= 0
ignored_lines = 0
failed_logins = 0
ip_values = {}
for line in access_log:
  if not 'FAILED_LOGIN' in line and not 'SUCCESS_LOGIN' in line:
    ignored_lines += 1
  if 'ip=' not in line:
    no_ip_logs += 1  
  elif 'FAILED_LOGIN' in line:
    failed_logins += 1
    lines_with_failed_logins.append(line)
    splitted_lines = (line.split())
    ip_dirty = (splitted_lines[4])
    ip_clean = ip_dirty.removeprefix('ip=')
    if ip_clean not in ip_values:
      ip_values[ip_clean] = 1
    else: 
      ip_values[ip_clean] += 1
  elif 'SUCCESS_LOGIN' in line:
        pass

ip_values_ordenado = dict(sorted(ip_values.items(), key=lambda item: item[1], reverse=True))
for ip, value in ip_values_ordenado.items():
  if value >= 5:
    print(f"{ip} [DANGER] --> {value} tries")
  else:
    print(f"{ip} --> {value} tries")

print(f"Ignored lines: {ignored_lines}")
    



   
    
    




    
    
    
    
