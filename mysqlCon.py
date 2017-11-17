# -*- coding: utf-8 -*-

#import MySQLdb
import pymysql
import crudFunctions as cf
#conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='bsgp')
#
#cursor = conn.cursor()
#print(cursor.fetchall)
#data =cursor.execute("select name from bsgpData where id =3")
#
#print(cursor.fetchone()[0])
#print(data)
##for r in cursor.fetchall():
##    print(r[3])
#conn.close()

#from tkinter import *
#
#class ScaleDemo( Frame ):
#   def __init__( self ):
#      Frame.__init__( self )
#      self.pack( expand = YES, fill = BOTH )
#      self.master.title( "Scale Demo" )
#      self.master.geometry( "220x270" )
#
#      self.control = Scale( self, 
#                            from_ = 0, 
#                            to = 20getClass0, 
#                            orient = HORIZONTAL, 
#                            command = self.updateCircle )
#                            
#      self.control.pack( side = BOTTOM, fill = X )
#      self.control.set( 10 )
#
#      self.display = Canvas( self, bg = "white" )
#      self.display.pack( expand = YES, fill = BOTH )
#
#   def updateCircle( self, scaleValue ):
#      end = int( scaleValue ) + 10
#      self.display.delete( "circle" )
#      self.display.create_oval( 10, 10, end, end,fill = "black", tags = "circle" )
#
#def main():
#   ScaleDemo().mainloop()   

#if __name__ == "__main__":
#   main()
import pandas as pd
data = pd.read_csv(str('/media/ratnesh/SONGS/pythonProjects/BSGP/scan_results_20170116110500.csv'),sep=';')
#print(data.O)
#,usecols=["File name", "Q_003", "Q_004"], names=["Date", "O", "C"]
import pymysql
cols = data.columns
print(data.shape)
data.fillna(str(' '), inplace=True)
#filename = data['File name']
data['name'] = data[cols[3:29]].astype(str).sum(1)
data['name'] = data.apply(lambda x: x['name'].strip(), axis=1)
data['fname'] = data[cols[29:55]].astype(str).sum(1)
data['fname'] = data.apply(lambda x: x['fname'].strip(), axis=1)
data['schoolCode'] = data.apply(lambda x: x['File name'][:4], axis=1)
data['classs'] = cf.getClass(data[cols[1]][0])
#data['section'] = data[cols[2]]
data['abcd'] = data[cols[-100:]].astype(str).sum(1)
#print(data.columns)

#for col in data.columns:
#    print(col,type(data[col][5]),data[col][5])
#insertSqlStmt = "insert into bsgpData values (0,LOAD_FILE('/home/ratnesh/3371-2016-12-17/7.jpg'),'1098_16s_11_2016.jpg','RAFEEN SHEIKH','MEHRUDDIN','6670','6','','BBCACDAADCDBABCBACBCACACB DD CCCCACBAABCBAACADCADBBBDCAABCCDCBCBDACACCBD ABCBCAD BCBDBCBDA  BDADACCD')"
#insertSqlStmt = "insert into bsgpData values (0,LOAD_FILE('"+filename+"'),'"+filename+"','"+data['name']+"',  '"+data['fname']+"','"+data['schoolCode']+"','"+data['classs']+"','"+data['section']+"','"+data['abcd']+"')"
insertSqlStmt = "insert into bsgpData values (0,LOAD_FILE('/home/ratnesh/3372 2016-12-17/3372 002.jpg'),'"+data['File name']+"ss1','"+data['name']+"',  '"+data['fname']+"','"+data['schoolCode']+"','"+data['classs']+"','"+data[cols[2]]+"','"+data['abcd']+"')"
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='bsgp')

cursor = conn.cursor()

#print(insertSqlStmt[7])
try:
    for query in insertSqlStmt:
        print(query)
#        cursor.execute(query)
    conn.commit()    
except:
    conn.rollback()
    print("Error")

conn.close()
#marks5 = "ABBDABAADDADADAADAADACCADCDDBDDDCABACABDADAADCADBCDCABAADBCBDCDDDBDDDADADADBADADADDDDDBDBDDDBAAACBBB"
#print(len(marks5))
##print(data['fname'])
#import tkinter as tk
#
#root = tk.Tk()
#sv = tk.StringVar()
#
#def callback():
#    print(sv.get())
#    return True
#
#e = tk.Entry(root, textvariable=sv, validate="focusout", validatecommand=callback)
#e.grid()
#e = tk.Button(root)
#e.grid()
#root.mainloop()
#import pdfkit
#
#import subprocess
#test = subprocess.Popen(["python","--version"], stdout=subprocess.PIPE,stderr=subprocess.PIPE )
#output,err = test.communicate()
#print(output,err)