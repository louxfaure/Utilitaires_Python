#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Modules externes
import os
import pysftp
from datetime import datetime


SERVICE = "Alma_Chargeur_De_Cours"
LOGS_LEVEL = 'DEBUG'
LOGS_DIR = os.getenv('LOGS_PATH')


with pysftp.Connection(host=os.getenv("SFTP_UB_HOSTNAME"), username=os.getenv("SFTP_UB_LOGIN"), password=os.getenv("SFTP_UB_PW")) as sftp:
    print("Connection succesfully stablished ... ")
    remoteFilePath = '/DEPOT/THESES'
    file_list = sftp.listdir(remoteFilePath)
    print(file_list)
    for entry in sftp.listdir_attr(remoteFilePath):
        timestamp = entry.st_mtime
        createtime = datetime.fromtimestamp(timestamp)
        now = datetime.now()
        delta = now - createtime
        if delta.days > 15:
            filepath = remoteFilePath + '/' + entry.filename
            sftp.remove(filepath)