#RouterCracker
#Hacking routers and telnet passwords. 
#Tool By NSK B3 aka Bence Csikos
#######################################
import time, os, argparse
import fontstyles
try:
  import requests
except ImportError:
  print "Install The requests module please."
 def banner():
     print("""
     |______________|
         |NSK B3|
        RouterCrack
     |--------------|
    """) 
def args():
       parser = argparse.ArgumentParser() 
       parser.add_argument('-l', '--load', help="Load script") 
       args = parser.parse_args() 
       os.system('python2",args.load)
banner()
args() 
