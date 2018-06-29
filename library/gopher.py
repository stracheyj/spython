"""Repetitively goes to blackboard and gets current task list
and instantiates a task for every relevant item on the list
then does them"""

class Gopher(object):
    'Goes to blackboard and gets current task list, instantiates a task for every relevant item on the list \
    It calculates the minimum frequency for rechecking the blackboard \
    It calculates the minimum frequency for running the tasks \
    '

    def __init__(self):

        currenttasks = []
        nexttriptobb = 0
        nextrunofdotasks = 0

    def getlatesttasks(self, parameter_list):
        "Refreshes the list of tasks from the blackboard (clearing the old and \
        reinstatiating from the blackboard) so that we only do the tasks we need to do now."
        pass

    def docurrenttasks(self, parameter_list):
        "Run through the tasklist doing all"
        pass

    def managework(self, parameter_list):
        "Works out when to run the getlatesttask and docurrenttasks methods and kickes them off"
        pass