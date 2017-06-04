#!/usr/bin/python
import re
import os.path
import sys
def CheckValidInput(input):
    #sys.argv[2] prima di input
    if(input!=12):
        print("String inserita non valida")

def LineToRewrite(line,input):
    hours = int(input[0:2])
    fileHour = int(line[0:2])
    minutes= int(input[3:5])
    fileMinutes = int(line[3:5])
    seconds = int(input[6:8])
    fileSeconds = int(line[6:8])
    milliseconds = int(input[9:12])
    fileMilliseconds = int(line[9:12])
    #milliseconds
    calculatedTupleMilliseconds = getSumFromSecondsMinuteHours(milliseconds,fileMilliseconds,1000)
    #print(seconds,fileSeconds,minutes,fileMinutes,hours,fileHour,milliseconds)
    fileMilliseconds = calculatedTupleMilliseconds[1]
    fileSeconds += calculatedTupleMilliseconds[0]
    #seconds
    calculatedTupleSeconds = getSumFromSecondsMinuteHours(seconds,fileSeconds,60)
    fileSeconds =calculatedTupleSeconds[1]
    fileMinutes += calculatedTupleSeconds[0]
    #minutes
    #print(str(fileSeconds)+"fileSeconds"+str(fileMinutes)+"FileMinutes")
    calculatedTupleMinutes = getSumFromSecondsMinuteHours(minutes,fileMinutes,60)
    fileMinutes = calculatedTupleMinutes[1]
    fileHour+= calculatedTupleMinutes[0]
    #print(str(fileMinutes)+"fileMinutes"+str(fileHour)+"fileHour")
    #hours
    calculatedTupleHours = getSumFromSecondsMinuteHours(hours,fileHour,24)
    fileHour= calculatedTupleHours[1]
    #print(str(fileHour)+":"+str(fileMinutes)+":"+str(fileSeconds))
    #ricostrusco la stringa
    rewrittenString =fixString(fileHour,2)+":"+fixString(fileMinutes,2)+":"+fixString(fileSeconds,2)+","+fixString(fileMilliseconds,3)
    return rewrittenString

def fixString(stringToFix,digit):
    toString = str(stringToFix)
    while(len(toString)<digit):
            toString = "0"+toString
    return toString
def getSumFromSecondsMinuteHours(argument1,argument2,modulo):

    sommafraidue = argument1+argument2
    if(sommafraidue > modulo-1):
        result = divmod(sommafraidue,modulo)
        return result
    else:
        return (0,sommafraidue)

def readFile():
    r = re.compile('.*:.*:.*,.*')
    print '----- Example path -----'
    print "\n"
    print '----- OSX: /Users/nameUser/desktop/python/readfile/test.txt -----'
    print "\n"
    path = raw_input('----- Enter a path to read: ')
    print "\n"
    print '----- Path in reading', path
    print "\n"
    print '----- Example format valid -----'
    print '----- hh:mm:ss,msmsms -----'
    print '----- 01:01:01,001 -----'
    print "\n"
    inputFromUser = raw_input('----- Enter a time you want to add')
    print '----- Time:'+inputFromUser

    try:
        if(os.path.isfile(path)):
            with open(path, 'r') as fileOpen:
                with open("fileSub.srt",'w') as fileToWrite:
                    print 'Reading file'
                    for line in fileOpen:

                        if r.match(line) is not None:
                   #print 'matches'
                            print("Processing the line")
                            #print (line)

                            firstLine=LineToRewrite(line[0:12],inputFromUser)
                            secondLine = LineToRewrite(line[17:len(line)],inputFromUser)
                   #Rewrite the string with a plus second input
                   #01:30:09,504 --> 01:30:11,255
                   #seconds



                            line = firstLine+" --> "+secondLine
                            print("Processed line trasfomed succesfully"+secondLine)
                        fileToWrite.write(line)
                   #hour = line.replace()
            # Close opend file
            print("File fileSub.srt created succesfully")
            fileOpen.close()
            fileToWrite.close()
        else:
            print 'file not valid'
    except OSError:
        print "ciao"
if __name__ == "__main__":

    readFile()
