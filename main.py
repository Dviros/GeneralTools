from datetime import datetime
import ip_finder
import getpass
import platform


now = datetime.now()


print "Made by Dviros"
print "me@dviros.com"
print '%s/%s/%s %s:%s:%s' % (now.day, now.month, now.year, now.hour, now.minute, now.second)
print ""

try:
    print "| Username: " + getpass.getuser()
    print "| Machine: " + platform.node()
    print "| External IP: " + ip_finder.external_ip()
    print "| Internal IP: " + ip_finder.internal_ip()
except:
    print "Something Went Wrong..."
