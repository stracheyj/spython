"""The task of checking a URL on the web"""
import uuid

class Task(object):
    'Creates a new task object from data off the baord. You need to provide the id, type, the \
    the whether the gaffer needs notifying about the task, the URL, \
    the interval (number of hours between checking), the status, the seek string, \
    and who to report to if the seekstr appears/disappers, the last time the \
    the gaffer was notified of a change, and the number of further notifications \
    they should receive.'

    def __init__(self, taskid, tasktype, status, seekstr, url, interval, gaffer,\
     lastnotified, pendingnotifications):
        self.taskid=taskid # id on the board
        self.interval=interval # number of hours before the task should be run again
        self.tasktype=tasktype # 1 to check for presence, 2 for absense
        self.status=status # 1 if the URL needs checking, 2 if the gaffer needs notifying, 3 if the task is obselete
        self.seekstr=seekstr # the string being checked for 
        self.gaffer=gaffer # who needs notifying about a change in state
        self.lastnotified=lastnotified # when the gaffer was last notified
        self.pendingnotifications=pendingnotifications # how many more times the gaffer needs notifying
        self.lastrun=None # the last time the task was run locally

    def getid(self):
        'Returns the ID of the task'
        return self.taskid

    def getype(self):
        'Returns the task type, 1 (check for presense) or 2 (check for absence)'
        return self.tasktype

    def getstatus(self):
        pass

    def geturl(self):
        pass

    def getinterval(self):
        pass
    
    def getseekstr(self):
        pass

    def getgaffer(self):
        pass

    def getlastnotified(self):
        pass

    def getpendingnotifications(self):
        pass

    def setstatus(self, newvalue):
        'Change the status to 2 (notify) or 3 (obselete)'
        self.status=newvalue

    def setlastnotified(self, newvalue):
        'set the datetime that the gaffer was last notified'
        self.lastnotified=newvalue

    def setpendingnotifications(self, newvalue):
        self.pendingnotifications=newvalue

    def dotask(self):
        'Check the url for the seek str according to the task type'
        pass