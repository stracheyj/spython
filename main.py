""" The main program run at start up  """

from library.connection import Connection
from library.gopher import Gopher
from library.problem import Problem

def main():

    connection = Connection()
    if connection.test():
        gopher = Gopher()
        gopher.managework()
    else:
        problem = Problem()
        problem.report()

if __name__ == "__main__":
    main()