#!/usr/bin/env python3
# Author ID: yyang334(154742225)

import subprocess
    
p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = p.communicate()
print(output)
print(output[0])

def free_space():
    return output[0].decode('utf-8').strip() 

print(free_space())

