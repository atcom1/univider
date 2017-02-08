# -*- coding: utf-8 -*-
import os
import subprocess

class Render():

    def getDom(self, url, loadImages, timeout):
        path =os.path.dirname(__file__)
        cmd = 'phantomjs ' + path + '/render.js "%s" %s %s '% (url, loadImages, timeout)
        print 'cmd:',cmd
        stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
        # print stdout
        # print stderr
        return stdout