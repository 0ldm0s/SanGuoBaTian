﻿#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     08-03-2011
# Copyright:   (c) Administrator 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sqlite3

class SqliteManager:
    filePath = ''

    def __init__(self,fp):
        self.filePath = fp

    def setFilePath(self,fp):
        self.filePath = fp

    def inert(self,tableName,data={}):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute('insert into ?(?) values(?)',tableName,','.join(data.keys()),','.join(data.values()))
        conn.commit()
        cur.close()

    def update(self,tableName,data={},where):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        str = 'update ? set '
        for k,v in data:
            str = str+' '+k+'='+v

        str = str+' where ?'
        cur.execute(str,tableName,where)
        conn.commit()
        cur.close()

    def delete(self,tableName,where):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute('delete from ? where ?',tableName,where)
        conn.commit()
        cur.close()

    def sel(self,tableName,clumns=[],where='1=1'):
        conn = sqlite3.connect(self.filePath)
        cur = conn.cursor()
        cur.execute('select ? from ? where ?',','.join(clumns),tableName,where)
        s = cur.fetchall()
        return s

