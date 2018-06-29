"""Periodically goes to the board, reads off tasks that need doing, puts \
them on its task list and periodically does them. Works out when to go through \
the tasks and when to go back to the blackboard based on requested frequency \
of running each task"""

class Gopher(object):
    "Creates a new Gopher object with an empty task list \
    and null values for the next activity \
    and the wait time until doing it."

    def __init__(self):

        self.currenttasks = [] 
        self.nextactivity = None # either refresh or run, initially unknown.
        self.waitingtime = None # how many seconds to wait until doing the next activity, initially unknown.
        self.lastrefresh = None # the exact time the gopher last checked the board, initially unknown.
        self.lastrun = None # the exact time that the gopher last ran its tasklist, initially unknown.

    def refreshtasks(self):
        "Refreshes the list of tasks from the board \
        Empties the current list then adds to it any tasks that need \
        doing now"
        pass

    def runtasks(self):
        "Do everything on the tasklist, then go back to managing work"
        self.managework()

    def managework(self):
        "Work out what the next activity is and when to do it. Sleep for \
        as long as necessary, then kick off the next activity.  If being called \
        for the first time, just refresh the task list and then run them"
        pass