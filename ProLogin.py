import os
import time
        #Assign the location on the machine, usually here
ArcGIS_Pro_filepath = r"C:\Program Files\ArcGIS\Pro\bin\ArcGISPro.exe"
        #Use os.startfile(), this will launch ArcPro
os.startfile(ArcGIS_Pro_filepath)
        #Use time.sleep() to wait 60 seconds, enough time for ArcPro to open properly
time.sleep(60)
        #Use os.system() to forcefully quit named process, ArcGISPro.exe
        #https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill
os.system("taskkill /f /im ArcGISPro.exe")
        #You can use the following output to determine if the command was successful
        #SUCCESS: The process "ArcGISPro.exe with PID 4408 has been terminated

        #If running as a scheduled task then make sure it only runs when user is logged in.