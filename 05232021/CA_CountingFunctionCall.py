# I am assigned to develop a logger module so there I wants to get number of time the logger called.

# Class based approach #1
class Counter:
    occurences = 0

    def __init__(self) -> None:
        Counter.occurences += 1
        self.id = Counter.occurences
        pass

# Funciton definition
def logger():
    Counter() #2
    print('logged.')

# Usage
logger()
print(f'Number of time logger got called {Counter.occurences}.')

logger()
logger()
logger()
logger()
print(f'Number of time logger got called {Counter.occurences}.')

logger()
logger()
logger()
logger()
print(f'Number of time logger got called {Counter.occurences}.')

# Output
'''
logged.
Number of time logger got called 1.
logged.
logged.
logged.
logged.
Number of time logger got called 5.
logged.
logged.
logged.
logged.
Number of time logger got called 9.
'''