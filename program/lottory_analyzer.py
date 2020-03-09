##CMPT 120
##Final Assignment
##Instructor: Diana Cukierman
##Name: Chih-Yang Edward Chen, Melvin Zhang

#global variable used:
#inputfilename=file name of the input csv file
#globalflag=boolean flag for while loop
#outputfilename=file name of the output csv file
#datarange= ALL or SEL or END
#selmonthorday = user selects D or M 

import turtle as t
import calendar

#CODE PROVIDED BY THE INSTRUCTOR:
## TO READ FROM CSV INPUT FILE
def read_csv_into_list_of_lists(IN_file):
    '''
    PROVIDED. CMPT 120
    A csv file should be available in the folder (where this program is)
    A string with the name of the file should be passed as argument to this function
    when invoking it
    (the string would include the csv extension, e.g "ID_data.csv")
    '''

    import csv

    lall = []

    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)
    return lall

def convert_lall_to_separate_lists(lall):
    import csv
    a=[]
    #a is used as an empty list here
    #Later, list a willl contain all the data in the csv file
    with open (lall) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for inrow in csv_reader:
            a.append(inrow)
        for i in range(len(a)):
            print("JUST TO TRACE, the draw being processed is:"+"\n")
            print("index#:",i)
            print("date:",a[i][0])
            print("numbers drawn:",a[i][1:8])
            print("jackpot:",a[i][8])
            print("number of winners:",a[i][9],"\n")

    return a

 #TO WRITE TO CSV INPUT FILE 
            
def append_1_draw_to_output_list(lout,date,lfreq_ran,avg_paid):
    '''
    PROVIDED. CMPT 120
    this function would append one line (the result associated to one draw)
    to a list. (this list will later be used to create the output file)
    
    
    The input parameters to this function are:
        - the list used to incorporate all the results
        - a string representing the date of this one draw to be appended
        - the list with the range frequency distribution for this draw
        - the average paid to each winner for this draw
    '''
    
    lout.append("'" + date + "'" + ",")
    for freq in lfreq_ran:
        lout.append(str(freq) + ",")
    lout.append(str(avg_paid) + "\n")
    return
##
##
def write_list_of_output_lines_to_file(lout,file_name):
    '''
    PROVIDED. CMPT 120
    Assumptions:
    1) lout is the list containing all the lines to be saved in the output file
    2) file_name is the parameter receiving a string with the exact name of the output file
       (with the csv extension, e.g "OUT_results.csv")
    3) after executing this function the output file will be in the same
       directory (folder) as this program 
    4) the output file contains just text representing one draw data per line 
    5) after each line in the file  there is the character "\n"
       so that the next draw is in the next line, and also
       there is (one single) "\n" character after the last line
    6) after the output file was created you should be able to open it
       with Excell as well
    '''
    
    fileRef = open(file_name,"w") # opening file to be written
    for line in lout:
        fileRef.write(line)
                                    
    fileRef.close()  
    return

def convert_csv_into_list(OUT_file):
    import csv
    lall = []
    with open(OUT_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for inrow in csv_reader:
            lall.append(inrow)
    #The rest of this function, under this comment, was taken directly from
    #https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
    for i in range(len(lall)):
        L = lall[i]
        print(", ".join(str(x) for x in L))
    return ""

### END OF PROVIDED CODE
##

#This function split csv fille into lists
def splittedlist(splist):
    import csv
    a=[]
    with open (splist) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for inrow in csv_reader:
            a.append(inrow)
        for i in range(len(a)):
            print(a[i][0:10])
    return a

#This function determines the frequency that each number appears in the desired
#range selected by the user
def numfrequency(lis1):
    numlist = [0]*50
    for i in range(len(lis1)):
        k = 0
        while (int(lis1[i]) >= k):
            k = k+1
        numlist[(k-1)] +=1
    return numlist
#This function determines the frequency for each number between ranges 1-10, 11-20..etc
def numrangefrequency(lis1):
    numrange = [0]*5
    for i in range(len(lis1)):
        k = 0
        while (int(lis1[i]) > k*10):
               k = k+1
        numrange[(k-1)] +=1
    return numrange


c = []
#This function is used when the user select range ALL, it gives all the stats required
def stats (stats):
    import csv
    a=[]
    with open (stats) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for inrow in csv_reader:
            a.append(inrow)
        print("draws processed:",str(len(a))+"\n")
        maxjkpot = 0
        #maxjackpot=maxjkpot
        c = 0
        for i in range(len(a)):
            b = int(a[i][8])
            if b > maxjkpot:
                c = i
            maxjkpot=max(b,maxjkpot)
        datemax = a[c][0]
        #datemax=date that the max jackpot appears
        print("max jackpot:",maxjkpot)
        print("date max jackpot:",str(datemax)+"\n")
        maxavg = 0
        c = 0
        for i in range(len(a)):
            #checking the divisor is not 0
            if int(a[i][9]) != 0:
                b = int(a[i][8])/int(a[i][9])
            if b > maxavg:
                c = i
            maxavg = max(maxavg,b)
            datemaxavg = a[c][0]
        print("max average won:",str(maxavg))
        print("date max average won:",str(datemaxavg)+"\n")
        c = []
        for i in range(len(a)):
            c = a[i][1:8]+c
        print("number of times each number was drawn")
        print(numfrequency(c),"\n")
        numlist = numfrequency(c)
        print("number of numbers in each range - all selected draws considered")
        print("ranges: (0,10], (10,20], (20,30], (30,40], (40,50)")
        print(numrangefrequency(c),"\n")
        gv = numrangefrequency(c)
        print("Six most frequenctly drawn numbers")
        for i in range(6):
            d = 0
            e = 0
            for k in range(len(numlist)):
                if int(numlist[k]) > d:
                    e = k
                d = max(d,int(numlist[k]))
            print("number",e,"was drawn",d,"times")
            numlist[e] = 0
        print(" ")
        rangegraph=input("Would you like to graph the ranges distribution?(Y/N):")
        if rangegraph.upper()=="Y":
            #Using turtle to draw the graph
            t.speed(9)
            t.width(3)
            t.pencolor("black")
            t.pu()
            t.setpos(0,0)
            t.pd()
            t.forward(180)
            t.left(90)
            t.pu()
            x = 0
            b = 0
            for i in range(len(gv)):
                b = max(b,int(gv[i]))
            for i in range(len(gv)):
                if b < 10:
                    height = int(gv[i])*10
                elif b < 50:
                    height = int(gv[i])*5
                else:
                    height = int(gv[i])
                t.fillcolor("blue")
                t.setpos(x,0)
                t.pd()
                t.begin_fill()
                t.forward(height)
                t.right(90)
                t.forward(20)
                t.right(90)
                t.forward(height)
                t.left(180)
                x = x+40
                t.pu()
                t.end_fill()
            print()
        if rangegraph.upper()=="N":
            print()
        
        return ""
#The following function shows the output files that are going to be saved in the new file
def outputlist(lis1):
    import csv
    a=[]
    #a is used as an empty list to add the csv datas later
    selected=[]
    #selected is a list that contains all the selected data from the user
    with open (lis1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for inrow in csv_reader:
            a.append(inrow)
        num = []
        lout = []
        for i in range(len(a)):
            date = a[i][0]
            num = a[i][1:8]
            lnumfrequency = numrangefrequency(num)
            if not(a[i][9] == "0"):
                avgpaid = int(a[i][8])/int(a[i][9])
            else:
                avgpaid = 0
            append_1_draw_to_output_list(lout,date,lnumfrequency,avgpaid)
    return write_list_of_output_lines_to_file(lout,outputfilename)


#The following function gives all the required stats when user wants to select data by month.              
def monthnumvalidation(inputted):
    import csv
    a=[]
    #a is used as an empty list to add the csv datas later
    selected=[]
    #selected is a list that contains all the selected data from the user
    with open (inputted) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for inrow in csv_reader:
            a.append(inrow)
    Localflag=True
    while Localflag:
        selmonthnum = input("Please type a month number(1 to 12)==>")
        if not(selmonthnum.isdigit()):
            print("That was not an integer. Please retype!")
        elif int(selmonthnum)>12 or int(selmonthnum)<=0:
                print("The month number is out of range")
        #monthinalpha means to convert the integer that user inputted into letters (e.g. integer 1 turn into "Jan")
        elif int(selmonthnum)<=12 and int(selmonthnum)>=1:
            monthlist = [0,"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
            #user types in the month number desired
            monthinalpha = monthlist[int(selmonthnum)]
            #position 1 = Jan, pos 2 = Feb and so on
            for i in range(len(a)):
                if monthinalpha in a[i][0]:
                    selected.append(a[i])
                    #after checking for appropriate data, it will add them into the list called selected
            if (selected ==[]):
                print("The file does not have any draws in", monthinalpha)
                print("Nothing will be processed, you can try another option")
            if selected!=[]:
                if monthinalpha in selected[0][0]:
                    lout = []
                    for i in range(len(selected)):
                        print("JUST TO TRACE, the draw being processed is:"+"\n")
                        print("index#:",i)
                        print("date:",selected[i][0])
                        print("numbers drawn:",selected[i][1:8])
                        print("jackpot:",selected[i][8])
                        print("number of winners:",selected[i][9],"\n")
                        date = selected[i][0]
                        num = selected[i][1:8]
                        numrange = numrangefrequency(num)
                        if not(selected[i][9] == "0"):
                            avgwin = int(selected[i][8])/int(selected[i][9])
                        else:
                            avgwin = 0
                        append_1_draw_to_output_list(lout,date,numrange,avgwin)
                    write_list_of_output_lines_to_file(lout,outputfilename)
                    print("TRACING: Here is the output saved to the file!", "\n")
                    convert_csv_into_list(outputfilename)
                    print(" ")
                    print("="*10+"STATS"+"="*10+"\n")
                    print("draws processed:",str(len(selected))+"\n")
                    maxjkpot = 0
                    c = 0
                    for i in range(len(selected)):
                        b = int(a[i][8])
                        if b > maxjkpot:
                            c = i
                        maxjkpot=max(b,maxjkpot)
                    datemax = selected[c][0]
                    print("max jackpot:",maxjkpot)
                    print("date max jackpot:",str(datemax)+"\n")
                    maxavg = 0
                    c = 0
                    for i in range(len(selected)):
                        if int(selected[i][9]) != 0:
                            b = int(selected[i][8])/int(selected[i][9])
                        if b > maxavg:
                            c = i
                        maxavg = max(maxavg,b)
                        datemaxavg = selected[c][0]
                    print("max average won:",str(maxavg))
                    print("date max average won:",str(datemaxavg)+"\n")
                    c = []
                    for i in range(len(selected)):
                        c = selected[i][1:8]+c
                    print("number of times each number was drawn")
                    print(numfrequency(c),"\n")
                    numlist = numfrequency(c)
                    print("number of numbers in each range - all selected draws considered")
                    print("ranges: (0,10], (10,20], (20,30], (30,40], (40,50)")
                    print(numrangefrequency(c),"\n")
                    gv = numrangefrequency(c)
                    print("Six most frequenctly drawn numbers")
                    for i in range(6):
                        d = 0
                        e = 0
                        for k in range(len(numlist)):
                            if int(numlist[k]) > d:
                                e = k
                            d = max(d,int(numlist[k]))
                        print("number",e,"was drawn",d,"times")
                        numlist[e] = 0
                    selrangegraph=input("\n"+"Would you like to graph the range distribution?(Y/N)")
                    if selrangegraph.upper()=="Y":
                        t.speed(9)
                        t.width(3)
                        t.pencolor("black")
                        t.pu()
                        t.setpos(0,0)
                        t.pd()
                        t.forward(180)
                        t.left(90)
                        t.pu()
                        x = 0
                        b = 0
                        for i in range(len(gv)):
                            b = max(b,int(gv[i]))
                        for i in range(len(gv)):
                            if b < 10:
                                height = int(gv[i])*10
                            elif b < 50:
                                height = int(gv[i])*5
                            else:
                                height = int(gv[i])
                            t.setpos(x,0)
                            t.fillcolor("blue")
                            t.pd()
                            t.begin_fill()
                            t.forward(height)
                            t.right(90)
                            t.forward(20)
                            t.right(90)
                            t.forward(height)
                            t.left(180)
                            t.pu()
                            t.end_fill()
                            x = x+40
                        print()
                    if selrangegraph.upper()=="N":
                        print()
                    localflag=False
                       
            return ""
        
#the following function gives all the data when the user wants to select data by the day of the week
def daynumvalidation(inputted):
    import csv
    a=[]
    #a is used as an empty list to add the csv datas later
    datess=[]
    #datess contains all the dates from the selected input
    selected=[]
    #selected is a list that contains all the selected data from the user
    months = [0,"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    with open (inputted) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for inrow in csv_reader:
            a.append(inrow)
    localflag=True
    while localflag:
        seldaynum = input("Please type a day number (0 to 6)(0=Monday,1=Tuesday...6=Sunday)")
        if not(seldaynum.isdigit()):
            print("That was not an integer. Please retype!")
        elif int(seldaynum)>6 or int(seldaynum)<0:
                print("The day of week number is out of range")
        elif int(seldaynum)<=6 and int(seldaynum)>=0:
            #user types in the month number desired
            for i in range(len(a)):
                datess.append(a[i][0])
            for i in range(len(datess)):
                #The following part comes from answer of CodeWrite assignment 5, created by professor Diana Cukierman
                firstDash = datess[i].index("-")
                secondDash = firstDash+4
                day=int(datess[i][ :firstDash])
                year = int(datess[i][secondDash+1: ]) + 2000
                mName = datess[i][firstDash+1 : secondDash]
                m = months.index(mName)
                datess[i]=(str(year),str(m),str(day))
                #ends the part where the code is not written by us
            for i in range(len(datess)):
                #converting into a standard format (yyyy,mm,dd) so we can use method calendar.weekday
                yyear=int(datess[i][0])
                mmonth=int(datess[i][1])
                dday=int(datess[i][2])
                a[i].append(str(calendar.weekday(yyear,mmonth,dday)))
                #Adding a new number that indicates the day of week into the last position of each row
            for i in range(len(a)):
                if int(a[i][-1])==int(seldaynum):
                    #if the last position in the row = day of the week, the data will append into selected
                    selected.append(a[i])
                    #after checking for appropriate data, it will add them into the list called selected
            if (selected ==[]):
                print("The file does not have any draws in weekday number", seldaynum)
                print("Nothing will be processed, you can try another option")
            if selected!=[]:
                if seldaynum == selected[0][10]:
                    lout = []
                    for i in range(len(selected)):
                        #now we show the stats from the selected data
                        print("JUST TO TRACE, the draw being processed is:"+"\n")
                        print("index#:",i)
                        print("date:",selected[i][0])
                        print("numbers drawn:",selected[i][1:8])
                        print("jackpot:",selected[i][8])
                        print("number of winners:",selected[i][9],"\n")
                        date = selected[i][0]
                        num = selected[i][1:8]
                        numrange = numrangefrequency(num)
                        if not(selected[i][9] == "0"):
                            avgwin = int(selected[i][8])/int(selected[i][9])
                        else:
                            avgwin = 0
                        append_1_draw_to_output_list(lout,date,numrange,avgwin)
                    write_list_of_output_lines_to_file(lout,outputfilename)
                    print("TRACING: Here is the output saved to the file!", "\n")
                    convert_csv_into_list(outputfilename)
                    print(" ")
                    print("="*10+"STATS"+"="*10+"\n")
                    print("draws processed:",str(len(selected))+"\n")
                    maxjkpot = 0
                    c = 0
                    for i in range(len(selected)):
                        b = int(a[i][8])
                        if b > maxjkpot:
                            c = i
                        maxjkpot=max(b,maxjkpot)
                    datemax = selected[c][0]
                    print("max jackpot:",maxjkpot)
                    print("date max jackpot:",str(datemax)+"\n")
                    maxavg = 0
                    c = 0
                    for i in range(len(selected)):
                        if int(selected[i][9]) != 0:
                            b = int(selected[i][8])/int(selected[i][9])
                        if b > maxavg:
                            c = i
                        maxavg = max(maxavg,b)
                        datemaxavg = selected[c][0]
                    print("max average won:",str(maxavg))
                    print("date max average won:",str(datemaxavg)+"\n")
                    c = []
                    for i in range(len(selected)):
                        c = selected[i][1:8]+c
                    print("number of times each number was drawn")
                    print(numfrequency(c),"\n")
                    numlist = numfrequency(c)
                    print("number of numbers in each range - all selected draws considered")
                    print("ranges: (0,10], (10,20], (20,30], (30,40], (40,50)")
                    print(numrangefrequency(c),"\n")
                    gv = numrangefrequency(c)
                    print("Six most frequenctly drawn numbers")
                    for i in range(6):
                        d = 0
                        e = 0
                        for k in range(len(numlist)):
                            if int(numlist[k]) > d:
                                e = k
                            d = max(d,int(numlist[k]))
                        print("number",e,"was drawn",d,"times")
                        numlist[e] = 0
                    selrangegraph=input("\n"+"Would you like to graph the range distribution?(Y/N)")
                    if selrangegraph.upper()=="Y":
                        t.speed(9)
                        t.width(3)
                        t.pencolor("black")
                        t.pu()
                        t.setpos(0,0)
                        t.pd()
                        t.forward(180)
                        t.left(90)
                        t.pu()
                        x = 0
                        b = 0
                        for i in range(len(gv)):
                            b = max(b,int(gv[i]))
                        for i in range(len(gv)):
                            if b < 10:
                                height = int(gv[i])*10
                            elif b < 50:
                                height = int(gv[i])*5
                            else:
                                height = int(gv[i])
                            t.setpos(x,0)
                            t.fillcolor("blue")
                            t.pd()
                            t.begin_fill()
                            t.forward(height)
                            t.right(90)
                            t.forward(20)
                            t.right(90)
                            t.forward(height)
                            t.left(180)
                            t.pu()
                            t.end_fill()
                            x = x+40
                        print()
                    if selrangegraph.upper()=="N":
                        print()
                    localflag=False
                       
            return ""

    
##PROGRAM STARTS HERE
print("Welcome to the CMPT 120 6-49 Processing system!")
print("="*50+"\n")
print("You first need to provide the input file name")
print ("You will be asked to provide the output file name later")
print( "The input file should be in this folder"+"\n")
print("The output file will be created in this folder")
print("You will be able to provide new names for the files"+"\n")
print("or accept the default names. Both files should have the extension  .csv"+"\n")
inputfilename=str(input("Type x for INPUT file name 'IN_data_draws3.csv', or a new file name ==>"))
if inputfilename.lower()=="x":
    inputfilename = "IN_data_draws3.csv"
    read_csv_into_list_of_lists("IN_data_draws3.csv")
else:
    read_csv_into_list_of_lists(inputfilename)

globalflag=True
while globalflag:
    print("Please choose one of the three options:"+"\n")
    print("Type ALL to process all the data")
    print("Type SEL to process selected draws")
    print("Type END to end this program"+"\n")
    datarange=input("Type ALL, SEL, or END (not case sensitive)")
    if datarange.upper()== "ALL":
        print("\n"+"="*10+"All the data will be processed"+"="*10+"\n"+"\n")
        print("Please confirm the output file name for your selected data")
        print("(if there is a file with this name in the folder")
        print("this new file will substitute the previous one)"+"\n")
        outputfilename=str(input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==>"))
        if outputfilename.lower() == "x":
            outputfilename = "OUT_results3.csv"
        convert_lall_to_separate_lists(inputfilename)
        print("TRACING: Here is the output saved to the file!", "\n")
        outputlist(inputfilename)
        print(convert_csv_into_list(outputfilename))
        print("\n"+"="*10+"Stats"+"="*10+"\n"+"\n")
        print(stats(inputfilename)+"\n")
        
    if datarange.upper()=="SEL":
        print("\n"+"="*10+"SELECTED data will be processed"+"="*10+"\n"+"\n")
        selmonthorday=input("Want the select by month(M) or day of week(D)?==>")
        if selmonthorday.upper()=="D":
            print("\n"+"Please select a day of the week")
            print("Only the draws associated to this day of the week will be processed")
            print("Please confirm the output file name for your selected data")
            print("(if there is a file with this name in the folder")
            print("this new file will substitute the previous one)"+"\n")
            outputfilename=str(input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==>"))
            if outputfilename.lower() == "x":
                outputfilename = "OUT_results3.csv"
            daynumvalidation(inputfilename)
        if selmonthorday.upper()=="M":
            print("\n"+"Please select a month")
            print("Only the draws associated to this month will be processed")
            print("Please confirm the output file name for your selected data")
            print("(if there is a file with this name in the folder")
            print("this new file will substitute the previous one)"+"\n")
            outputfilename=str(input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==>"))
            if outputfilename.lower() == "x":
                outputfilename = "OUT_results3.csv"
            monthnumvalidation(inputfilename)

    if datarange.upper()=="END":
        print("BYE....no more stats for you!!")
        globalflag=False
