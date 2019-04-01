# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:04:43 2019
adapated from https://github.com/konradhafen/download-prism-data

@author: aseck

Download data from ftp and unzip it

"""

import os
import ftplib
import zipfile
#from os import path

ftp = ftplib.FTP("prism.nacse.org")
ftp.login("anonymous", "aseck@icprb.org")

#Change the folder if need temperature or other variables
ftp.cwd("monthly/ppt") #remote folder containing data (monthly precipitation data)
fnbase = "PRISM_ppt_stable_4kmM" #filename before year
fnmid = "2_" #for years before 1981
fnend = "_all_bil.zip" #filename after year and extension
#fnend = "_bil.zip" #filename after year and extension

savedir = "D:/2019_demandstudy/PRISM_data/monthly"
#E:/konrad/Projects/usgs/prosper-nhd/data/ppt/raw" #directory to save files
os.chdir(savedir) #change local directory to save directory

startyear = 1981 #year to start downloading precipitation data
endyear = 2018 #last year to download data


"""
for year in range(startyear, endyear+1): #loop through years
    #if year > 1980:
    #    fnmid = "3_" #different filename for years after 1980
    ftp.cwd(str(year)) #change remote directory to download year
    
    fn = fnbase + fnmid + str(year) + fnend #create filename
    print fn
    file = open(fn, "wb") #create and open local file to write data to
    ftp.retrbinary("RETR " + fn, file.write) #write data to local file
    file.close() #close local file
    zfile = zipfile.ZipFile(fn) #local file is zipfile, create zipfile object
    zfile.extractall() #extract zipfile contents
    zfile.close() #close zip file after extraction
    ftp.cwd("../") #move up one level in remote directory
    os.remove(fn) #delete zip file after files have been extracted
    print str(year) + " done"
"""

filematch = '*.bil.zip' # works to get all .laz files in a block
for year in range(startyear, endyear+1): #loop through years
    if not os.path.exists(str(year)):
        os.mkdir(str(year))
    os.chdir(str(year))
    
    print year    
    ftp.cwd(str(year)) #change remote directory to download year
    files = ftp.nlst()
    #print files
    
    for filename in files:
        fhandle = open(filename, 'wb')
        print 'Getting ' + filename #Displays which file is being downloaded
        ftp.retrbinary('RETR '+ filename, fhandle.write)
        fhandle.close()
        zfile = zipfile.ZipFile(filename) #local file is zipfile, create zipfile object
        zfile.extractall() #extract zipfile contents
        zfile.close() #close zip file after extraction
        #os.remove(filename)
    print str(year) + " done"
    ftp.cwd("../") #move up one level in remote directory
    os.chdir("../")