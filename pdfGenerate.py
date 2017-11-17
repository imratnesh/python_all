# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
import pymysql
import pandas as pd
#global conn
def generatePdf(canv, string):
    canv.drawString(10,10,string,2)
    canv.showPage()

#conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='bsgp')
#print(conn)
#cursor = conn.cursor(pymysql.cursors.DictCursor)
#selectSqlStmt = "SELECT id, name, fname, class, section from bsgpData " 
#
#print(selectSqlStmt)
#cursor.execute(selectSqlStmt)
##cert= canvas.Canvas("simple.pdf")
##
##cert.drawString(150,50,"My name is ratnesh")
##print("dcsdc")
#
#da = []
#for s in cursor.fetchall():
##    generatePdf(cert,str(s[1]+str(s[2]+str(s[3]+str(s[4])
##    print(str(s[0],str(s[1],str(s[2],str(s[3],s[4],s[0])
#    da.append(str(s["id"] )+","+ str(s["name"])+","+ str(s["fname"])+","+ str(s["class"])+","+ str(s["section"])+","+ str(s["name"])+","+ str(s["name"])+","+ str(s["fname"])+","+ str(s["schoolCode"]))
##    out_df = pd.DataFrame({"Application_ID":str(str(s[0]), "Loan_Status":str(str(s[4])})
#
#out_df = pd.DataFrame({'id,name, fname, class,section,grade,marks,schoolname,schoolCode':da})
#file = out_df.to_csv("tecfdg_submission.csv", index=False)  
#cert.save()
#return "Generated successfully"

#conn.close()
#return "Error"     
import crudFunctions as cf
try:
#    codes = pd.read_csv("csv/codes2017.csv")
##    print(codes.info())
#    data = codes[codes['code'] == 1005].values[0]
##    data = data.values[0]
#    print(data)
#    print(str(data[1]+','+data[2]+','+data[3]).split(",")[0])   
     cf.generateSchoolCertificate()
except Exception as e:
    print(e)
    print("Error")
