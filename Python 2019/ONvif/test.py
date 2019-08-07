from onvif import ONVIFCamera


mycam = ONVIFCamera('192.168.0.6', 80, 'admin', 'Whitehall', '/etc/onvif/wsdl/')

# Get Hostname
resp = mycam.devicemgmt.GetHostname()
print ('My camera`s hostname: ' + str(resp.Name))

# Get system date and time
dt = mycam.devicemgmt.GetSystemDateAndTime()
tz = dt.TimeZone
year = dt.UTCDateTime.Date.Year
hour = dt.UTCDateTime.Time.Hour