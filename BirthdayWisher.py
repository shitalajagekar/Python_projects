
import stat
import pandas as pd
import datetime
import os
from stat import*
import smtplib



gmail_id= "userid@gmail.com"
gmail_password = "userpassword"

def sendMail(to,sub,msg):
    # print(f"Email has been send to {email} and message is {msg} ")
    print("email send")
    s = smtplib.SMTP('smtp-relay.gmail.com',587)
    s.starttls()
    s.login(gmail_id, gmail_password)
    s.sendmail(gmail_id, to,f" Subject: {sub} \n\n meassage : {msg}" )
    s.quit()


if __name__ == "__main__":
    # sendMail("shitalajagekar@gmail.com","Birthday wish","Wish u very happy birthday...")
    # exit()


    df = pd.read_excel("Birthday_data2.xls")
    
    today_date = datetime.datetime.now().strftime("%d-%m")
    today_year = datetime.datetime.now().strftime("%Y")
    # print(today_date)

sr_no=0
item_index =[]

for index , item in df.iterrows():
    bdate= item['Birthday'].strftime("%d-%m")
    sr_no = item['Sr_no']
    
    
    # print(bdate)
    if today_date == bdate :
        sendMail(item["Email"],"BirthDay Wish",item["Message"])
        # df.loc[sr_no, 'Year'] = str(int(today_year) + 1)
        item_index.append(index)

    
    for i in item_index:
        yr = df.loc[i, "Year"]
        df.loc[i, "Year"] = str(yr)+ "" + str(today_year)

    os.chmod("Birthday_data2.xls", stat.S_IWGRP  | stat.S_IRUSR | stat.S_IXUSR )

    df.to_excel(r"C:\Users\shita\AppData\Roaming\Python\Python37\Birthday_data2.xls", engine = "openpyxl",nidex= False)

    # print(df)

        # print(str(int(today_year) + 1))
        # print(sr_no)


        


