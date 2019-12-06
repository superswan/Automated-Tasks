#! /usr/bin/python
"""
Key-Pro III Automated GUI Report printing
Will automatically Save, Email, or Print
reports from Morse Watchman Key-Pro III
Application.

Note: Key-Pro III window must be open in
order for the script to work.

TODO:
-Email Support

Eli Elderkin
eelderkin@distinctivehospitalitygroup.com
"""
import datetime
import time

import psutil
import pywinauto
from pywinauto.application import Application
from loguru import logger
#import smtplib

#sets up logging and writes to file
logger.add("log.log", level="TRACE", rotation="100 MB")
@logger.catch

#One big clunky main function :)
def main():
    #SETUP | Global variables used to connect to the application 
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S') #Human Readable Timestamp from timestamp in seconds
    PROCNAME = "KeyPro III.exe"

    for proc in psutil.process_iter(): #Find PID based on given PROCNAME and set it PID variable
        if proc.name() == PROCNAME:
            PID = proc.pid

    print("Connecting to KeyPro III @ PID: {}".format(PID))
            
    app = Application(backend='win32').connect(process=PID) #Connect to KeyWatcher Application Via PID ($PID can be repalced with PID manually)

    #EMAIL SMTP CONFIGURATION
    """
    server = smtplib.SMTP('192.168.1.2', 25)
    server.sendmail(
        "dhgscans@distinctivehospitalitygroup.com",
        "eelderkin@distinctivehospitalitygroup.com",
        "Test Message")
    server.quit()
    """
    #RUN REPORT
    #Heavy use of sleep due to the application being rather clunky and the machine running the script is a light VM. This part of the code will open the keywatch REPORTS menu
    time.sleep(1)
    print("Opening Reports Window")
    app_dlg = app['Key-Pro III'] #Attach to the main application window
    app_dlg.set_focus()
    time.sleep(1)
    app_dlg['Reports'].click_input()
    time.sleep(15)
    main_dlg = app['KeyWatcher Report']
    #main_dlg['Database Reports'].print_control_identifiers()
    main_dlg['Transaction Reports'].select('Transaction Reports')
    time.sleep(3)

    print("Running Report...")
    main_dlg['Run Report'].click_input()
    report_dlg = app['Report']

    #SAVE REPORT
    """
    time.sleep(5)
    print("Saving report as REPORT-"+timestamp)
    report_dlg['0'].click()
    time.sleep(5)
    save_dlg = app['Save As']
    save_dlg.Edit.type_keys("REPORT-"+timestamp)
    save_dlg.Save.click()
    """

    #PRINT REPORT AS PDF
    time.sleep(3) #Wait for report to load
    print("Saving and printing report at {}".format(timestamp))
    report_dlg.set_focus()
    time.sleep(2)
    pywinauto.mouse.click(coords=(210,155)) #Have to use mouse coords because pywinauto doesn't work well with kp3 toolbar
    pywinauto.mouse.click(coords=(608,436))

    #RESET UI
    print("Resetting UI")
    main_dlg['User Report'].select('User Report') #Reset UI or script will throw exception on next run
    time.sleep(1)
    report_dlg.close()
    main_dlg.close()

if __name__ == "__main__":
    main()

