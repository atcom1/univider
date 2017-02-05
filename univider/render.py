#coding=utf-8
import subprocess

class Render():

    def getDom(self, url, loadImages, timeout):
        cmd = 'phantomjs render.js "%s" %s %s '% (url, loadImages, timeout)
        # print 'cmd',cmd
        stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
        # print stdout
        # print stderr
        return stdout