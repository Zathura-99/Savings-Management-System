import mysql.connector as connector
conn=connector.connect(host="localhost",user="root",passwd="brooklyn99",database="BANKproject")
#databse BANKproject already created
if conn.is_connected():
     print('Successfully Connected to MySQL Database')

#tables Account and Amount already created

def openAcc():
     n=input("Enter Name:")
     ac=input("Enter Account No.:")
     db=input("Enter Date of Birth:")
     p=input("Enter Phone no.:")
     ad=input("Enter City:")
     ob=int(input("Enter Opening Balance:"))
     data1=(n,ac,db,p,ad,ob)
     data2=(n,ac,ob)
     sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
     sql2='insert into amount values(%s,%s,%s)'
     c=conn.cursor()
     c.execute(sql1,data1)
     c.execute(sql2,data2)
     conn.commit()
     print("Data Entered Successfully")
     main()

def depoAmo():
     am=int(input("Enter Amount to be Deposited:"))
     ac=input("Enter Account No:")
     a="Select Bal from Amount where bank_AccNo=%s"
     data=(ac,)
     c=conn.cursor()
     c.execute(a,data)
     result=c.fetchone()
     tam=result[0]+am
     sql="update Amount set Bal=%s where bank_AccNo=%s"
     d=(tam,ac)
     c.execute(sql,d)
     conn.commit()
     print("Amount Deposited Successfully")
     main()

def withAmo():
     am=int(input("Enter Amount to be Withdrawn:"))
     ac=input("Enter Account No:")
     a="Select Bal from Amount where bank_AccNo=%s"
     data=(ac,)
     c=conn.cursor()
     c.execute(a,data)
     result=c.fetchone()
     tam=result[0]-am
     sql="update Amount set Bal=%s where bank_AccNo=%s"
     d=(tam,ac)
     c.execute(sql,d)
     conn.commit()
     print("Amount Withdrawn Successfully") 
     main()

def balance():
     ac=input("Enter Account No. whose Balance you want to know:")
     a="Select Bal from Amount where bank_AccNo=%s"
     data=(ac,)
     c=conn.cursor()
     c.execute(a,data)
     result =c.fetchone()
     print("Balance for Account:",ac,"is",result[0])
     main()

def dispAcc():
     ac=input("Enter Account No. whose Details you want to know:")
     a="Select * from Account where bank_AccNo=%s"
     data=(ac,)
     c=conn.cursor()
     c.execute(a,data)
     result=c.fetchone()
     for i in result:
          print(i,end="\n")
     main()
 
def closeAcc():
    ac=input("Enter Account No. which needs to be Closed:")
    sql1="delete from Account where bank_AccNo=%s"
    sql2="delete from Amount where bank_AccNo=%s"
    data=(ac,)
    c=conn.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    conn.commit()
    print("Account Closed Successfully")
    main()
    
def report():
     c=conn.cursor()
     c.execute("select A.Name,A.bank_AccNo,DOB,City,Ph_No,Open_Bal,B.Bal from Account A,Amount B\
     where A.bank_AccNo=B.bank_AccNo")
     a=c.fetchall()
     std_lst=list(a)
     std_lst2=[]
     for i in std_lst:
         i=list(i)
         std_lst2.append(i)
     gap=' '*5  #inter-field gap of 3 spaces
     heading=f"{'Name':25s}{gap}{'Bank_AccNo':24s}{gap}{'DOB':20s}\
     {gap}{'Phone_No':26s}{gap}{'City':24s}{gap}{'Opening_Bal':20s}{gap}{'Current_Bal':20s}"
     print("Report to display the details of people who have enrolled in BANK MANAGEMENT SERVICES")
     print("="*140)
     print(heading)
     print("-"*140)
     for data in std_lst2[:]:
          rec=f"{data[0]:25s}{gap}{data[1]:27s}{gap}{data[2]:20s}\
          {gap}{data[4]:21s}{gap}{data[3]:14s}{gap}{data[5]:20d}{gap}{data[6]:20d}"
          print(rec)
     print("="*140)


def main():
     print("*"*140)
     m=("1.OPEN NEW BANK ACCOUNT".center(140),
        "2.DEPOSIT AMOUNT".center(140),
        "3.WITHDRAW AMOUNT".center(140),
        "4.BALANCE AMOUNT".center(140),
        "5.SEARCH RECORD DETAILS AS PER THE BANK ACCOUNT NO.".center(140),
        "6.CLOSE A BANK ACCOUNT".center(140),
        "7.GENERATE A REPORT".center(140),
        "8.EXIT".center(140))
     for i in m:
          print(i)
     print("*"*140)
     choice =input("Enter Task No.:")
     if(choice=='1'):
          openAcc()
     elif (choice=='2'):
          depoAmo()
     elif (choice=='3'):
          withAmo()
     elif (choice=='4'):
          balance()
     elif (choice=='5'):
          dispAcc()
     elif (choice=='6'):
          closeAcc()
     elif (choice=='7'):
          report()
     elif (choice=="8"):
          exit()
     else:
          print("Wrong choice..........")
     main()
main()
