import os
import sys
def check_reboot():
 """ returns True if the computer has q pending reboot
 """
 return os.path.exist("/run/reboot-required")

 pass

def main():
 if check_reboot():
  print("pending reboot")
  sys.exit(1)
  print("every thing is ok")
  sys.exit(0)

 
 pass


 main()