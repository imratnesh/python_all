# -*- coding: utf-8 -*-
import pymysql
global conn
import pandas as pd
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='bsgp')
print(conn)
#print(cursor.fetchone())

#cursor.execute("select * from bsgpData")
#for r in cursor.fetchall():
#    print(r[3])
#'%d'" % (20)
def insertAll(file):
    try:
#        print(file)
        data = pd.read_csv(str(file),sep=';')
        cols = data.columns
        
        data.fillna(str(' '), inplace=True)
        #filename = data['File name']
        data['name'] = data[cols[3:29]].astype(str).sum(1)
        data['name'] = data.apply(lambda x: x['name'].strip(), axis=1)
        data['fname'] = data[cols[29:55]].astype(str).sum(1)
        data['fname'] = data.apply(lambda x: x['fname'].strip(), axis=1)
        data['schoolCode'] = data.apply(lambda x: x['File name'][:4], axis=1)
        data['classs'] = getClass(data[cols[1]][0])
        data['section'] = data[cols[2]]
        data['abcd'] = data[cols[-100:]].astype(str).sum(1)
        insertSqlStmt = "insert into bsgpData values (0,LOAD_FILE('/home/ratnesh/3372 2016-12-17/3372 002.jpg'),'"+data['File name']+"as','"+data['name']+"',  '"+data['fname']+"','"+data['schoolCode']+"','"+data['classs']+"','"+data['section']+"','"+data['abcd']+"')"
#        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='bsgp')
        
        cursor = conn.cursor()
        
        for query in insertSqlStmt:
            print(query)
            cursor.execute(query)
        conn.commit()    
        return "Added succesfully"
    except:
        conn.rollback()
        return "Error"
    conn.close()

def deleteById(id):
    try:
        cursor = conn.cursor()
        deleteSqlStmt = "DELETE FROM bsgpData where id =  %d" % (id)
        cursor.execute(deleteSqlStmt)
        return "Deleted succesfully"
    except:
        conn.close()
        return "Error"
    
def update(name,fname,schoolCode,classs,section,id):
    try:
        cursor = conn.cursor()
        updateSqlStmt = "UPDATE bsgpData SET name='%s',fname='%s',schoolCode='%s',class='%s',section='%s' where id = %d" % (name,fname,schoolCode,classs,section,id)
        print(updateSqlStmt)
        cursor.execute(updateSqlStmt)
        conn.commit()
        return "Updated succesfully %s" % (id)
    except:
        conn.rollback()
        conn.close()
        return "Error"
    

def gotoId(id):
    try:
        cursor = conn.cursor()
        selectSqlStmt = "SELECT * from bsgpData where id = %d" % (id)
        print('Executing...',selectSqlStmt)
        cursor.execute(selectSqlStmt)
        print()
        return cursor.fetchone()
    except:
        conn.close()
        return "Error"
codes = pd.read_csv("csv/codes2017.csv",sep=",")
def getSchoolNameByCode(schoolCode):
    try:
        
        data = codes[codes['code'] == int(schoolCode)].values[0]
#        print(data[1]+','+data[2]+','+data[3])  
        return data[1]+','+data[2]+','+data[3]
    except Exception as e: 
        print("School--"+e)
        return "Error,Error,Error"
    
def generateExcel():
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        selectSqlStmt = "SELECT id, name, fname, class, section, schoolCode,abcd from bsgpData order by schoolCode, class, section" 
        cursor.execute(selectSqlStmt)
        da = []
        for s in cursor.fetchall():
            std = s["class"]
            scode = s["schoolCode"]
            marks = marksCalculation(int(std),s["abcd"])   
#            print(marks[0],marks[1],scode)
            
            da.append(str(s["id"] )+","+ str(s["name"])+","+ str(s["fname"])+","+ 
                      str(std)+","+ str(s["section"])+","+ str(marks[0])+","+ 
                      str(marks[1])+ ","+ getSchoolNameByCode(scode)+","+ str(scode))
        
        out_df = pd.DataFrame({'id,name,fname,class,section,grade,marks,schoolname,schoolCode':da})
        file = out_df.to_csv("tecfdg_submission.csv", index=False)  
        print(type(file))
        return "Generated successfully"
    except Exception as e: 
        print(e)
        conn.close()
#        print("Errorr")
        return "Error"

from reportlab.pdfgen import canvas
#import pdfGenerate as pg
def generateSchoolCertificate():
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        selectSqlStmt = "SELECT id, name, fname, class, section, schoolCode, abcd from bsgpData order by schoolCode, class, section" 
        cursor.execute(selectSqlStmt)
        cert= canvas.Canvas("simplesss.pdf")

#        cert.drawString(150,50,"My name is ratnesh")
        print("dcsdc")
        for s in cursor.fetchall():
#            pg.generatePdf(cert,s[1]+s[2]+s[3]+s[4])
            std = str(s["class"])
            scode = s["schoolCode"]
            marks = marksCalculation(int(std),s["abcd"])    
            print(marks[0],marks[1],scode)
            address = str(getSchoolNameByCode(scode)).split(",")
            print(address[2])
#            (x-axis,y-axis) increase y for upwards,increase x for rightwards
            cert.drawString(150,50,"2017-18")          
            cert.drawString(150,60,str(s["id"]))          
            cert.drawString(150,80,str(s["name"]))          
            cert.drawString(200,90,str(s["fname"]))          
            cert.drawString(150,100,std)          
            cert.drawString(200,110,address[0])          
            cert.drawString(150,120,address[1])        
            cert.drawString(150,130,address[2])          
            cert.drawString(150,140,"Grade:"+marks[1])          
#            print(string)
#            cert.drawString(10,10,string,2)
            cert.showPage()
#            print(s[0],s[1],s[2],s[3],s[4],s[5], marksCalculation(int(s[3]),s[6]))
        cert.save()
        return "Generated successfully"
    except Exception as e:
        print("Pdf:-"+ e.__cause__)
        conn.close()
        return "Error"            

marks5 =  "ABBDABAADDADADAADAAADCADCDDBDDDCABACACBDADAADCADBCDCABAADBCBDCDDDBDDDADADADBADADADDDDDBDBDDDBAAACBBB"
marks6 =  "AABDCBABDDBDACCABBDDDCABCDDBDADCABDCACBBDAADCADBCDCABAADCCBDCDDDCDDDADADADBADCDADDDDDBDBDDDAABCAABDB"
marks7 =  "CADCCCABCADCBCADAADAADCADCDDBDDDCABACABDADAADCADBCDCABAADBCBDCDDDBDDDADADADBADADADDDDDBDBDDDBAAACBBB"
marks8 =  "ABBDABAADDADDDADADAADAADCADCDDBDDDCABACABDADAADCADBCDCABAADBCBDCDDDBDDDADADADBADADADDDDDBDBAAACBBBBC"
marks9 =  "CADCCCABCADCBCBDDADDACBBACDDDADADBAABBAABDCABAABADDDDCBDCCDDACBAADBBDDDDAADACBAADABADDADDDCDAAADDDDA"
marks10 = "ABBDABAABDDADDACBBACDDDADADBAABBAABDCABAABADDDDCBDCCDDACBAADBBDDDDAADACBAADABADDADDDCDAAADDDDADCDAAA"
marks11 = "CADCCCABCADCBCBDDADDACBBACDDDADADBAABBAABDCABAABADDDDCBDCCDDACBAADBBDDDDAADACBAADABADDADDDCDAAADDDDA"
marks12 = "ABBDABAADDADADAADAADCADCDDBDDDCABACABDADAADCADBCDCABAADBCBDCDDDBDDDADADADBADADADDDDDBDBDDDBAAACBBBDA"
    
def marksCalculation(classCode,abcd):
    marks=0   
    print(classCode)
    marksCode = marks5
    if(classCode==6):
        marksCode = marks6
        print(6)
    elif(classCode==7):
        marksCode = marks7
        print(7)
    elif(classCode==8):
        marksCode = marks8
        print(8)
    elif(classCode==9):
        marksCode = marks9
        print(9)
    elif(classCode==10):
        marksCode = marks12
        print(10)
    elif(classCode==11):
        marksCode = marks11
        print(10)
    elif(classCode==12):
        marksCode = marks12
        print(10)
    else:
        print(5)
    cnt = 0    
    for s in marksCode:
        if(abcd[cnt] == s):
            marks =marks+1
        cnt=cnt+1
    return marks, getGrade(marks)
    
def getGrade(num):
    if(num<51):
        return "General"
    elif(num<81):
        return "Best"
    else:
        return "Excellent"
def getClass(classCode):
    
    if(classCode=='B'):
        return '6'
    elif(classCode=='C'):
        return '7'
    elif(classCode=='D'):
        return '8'
    elif(classCode=='E'):
        return '9'
    elif(classCode=='F'):
        return '10'
    elif(classCode=='G'):
        return '11'
    elif(classCode=='H'):
        return '12'
    else:
        return '5'
    
#conn.close()    
#insert into bsgpData values (0,LOAD_FILE('/home/ratnesh/3371-2016-12-17/4.jpg'),'109845 3.jpg','SHEIKH',  'MEHRUDDIN','6670','6','','BBCACDAADCDBABCBACBCACACB DD CCCCACBAABCBAACADCADBBBDCAABCCDCBCBDACACCBD ABCBCAD BCBDBCBDA  BDADACCD')
#
#UPDATE bsgpData SET name='reeya',fname='kush' where id =5
#SELECT * from bsgpData LIMIT 1
#
#DELETE FROM bsgpData where id = '1'
    # Create plot
#from mpl_toolkits.mplot3d import axes3d
#fig = plt.figure(figsize=(12,12))
#ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
#ax = fig.gca(projection='3d')
#
#try:
#    for dataS, color, group in zip(dataS, colors, groups):
#        x, y, z = dataS
#        ax.scatter(x, y, z, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
#        plt.title('3d scatter plot')
#        plt.legend(loc=2)
#except TypeError:
#    pass
# 
#
##plt.show()