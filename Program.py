import os
#This Function is For Sorting the elements in increasing order based on the dates in the Dictonary
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j+1][2] > arr[j + 2][2]:
                arr[j+1], arr[j + 2] = arr[j + 2], arr[j+1]

#For checking the LeapYear or Not and return the Days in each month of that year
def Check_leap(num,mon):
    if(num%4!= 0):
        a=(31,28,31,30,31,30,31,31,30,31,30,31);
    elif(num%400 in [100,200,300]):
        a=(31,28,31,30,31,30,31,31,30,31,30,31);
    else:
        a=(31,29,31,30,31,30,31,31,30,31,30,31);
    return a[mon-1];
#For calculating the Days, Months, Years between two transactions
def cal_Days(asd1,asd2):
        if asd1[3]> asd2[3]:
            asd2[3]+=Check_leap(num=asd1[1],mon=asd1[2]);
            asd2[2]-=1;
            days=asd2[3]-asd1[3];
        else :
            days=asd2[3]-asd1[3];
        if asd1[2]> asd2[2]:
            asd2[2]+=12;
            asd2[1]-=1;
            months=asd2[2]-asd1[2];
        else:
            months = asd2[2] - asd1[2];
        years=asd2[1]-asd1[1];
        a=(asd1[0],years,months,days);
        return a;
#For calculating the Amount to be paid
def cal_Amount(asd1,rate=24):
    a_tot=0;
    for i in asd1:
        pr=a_tot+i[0];
        print(pr);
        print(i[1]);
        tot_y= pr *((1+rate/100) ** (i[1]));
        print(tot_y);
        ip = (tot_y * (i[2] + (i[3] / 30)) * rate)/1200;
        print(ip)
        a_tot =tot_y+ip;
        print(a_tot);

    print(a_tot);

def convertdate(a):
    b=a[::-1];
    b.insert(0,0);
    return b;


a=input("Enter the Name You want to search:");
d=input("Enter todays date (dd/mm/yyyy) format Note: Enter the Year Completely:");
b={};
c={};
e=[];
i=0;
file=open("E:/My Project/Acconts.txt", 'r')
#This will get all the transaction details into b based on the Name entered
for line in file:
    x=line.split();
    if(x[1] in [a,a.lower(),a.upper()]):
        print(x)
        i+=1;
        b[i]=x;
file.close();
#This will display all the details in dictonary
if(bool(b) == False):
    print("Sorry we are not having any records");
else:
    print(b);
print("This is data after Sorting:");
bubbleSort(b);
print(b);
#This will split the dates into year, month, day  respectively and store it in c
for i in b:
    c[i]=b[i][2].split("/");
    c[i].insert(0,int(b[i][3]));
print(c);
#This will convert the string format into integer
for i in c:
    for j in range(1,4):
        c[i][j]=int(c[i][j]);
print(c);
print(len(c));
k=d.split("/");
d=convertdate(k);
print(d);
for i in range(0,4):
    d[i]=int(d[i]);
c[len(c)+1]=d;
print(c);
for i in range(1,len(c)):
    e.append(cal_Days(asd1=c[i],asd2=c[i+1]));
print(e);
o=input("Are Intrested to go with default rate(that is 24%) ?. Type Y for Yes or Press Enter for No");
if o not in ["Y", "y", "yes", "YES", "Yes"]:
    num1 = float(input("Enter Intrest rate per year : "))
    cal_Amount(e,num1);
else:
    cal_Amount(e);



