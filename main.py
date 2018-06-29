""" The main program run at start up  """

from library.connection import Connection
from library.gopher import Gopher
from library.problem import Problem

def main():

    myconnection = Connection()
    if myconnection.testcon():
        gopher = Gopher()
        gopher.managework()
    else:
        problem = Problem('Could not start program')
        problem.report()

if __name__ == "__main__":
    main()