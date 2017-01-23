#coding=utf-8
import subprocess

def getDom(url, loadImages, timeout):
    cmd = 'phantomjs render.js "%s" %s %s '% (url, loadImages, timeout)
    # print 'cmd',cmd
    stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    # print stderr
    return stdout