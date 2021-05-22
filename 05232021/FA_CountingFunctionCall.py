# I am assigned to develop a logger module so there I wants to get number of time the logger called.

# Functional approach
occurances = 0 #1

# Funciton definition
def logger():
    global occurances #2
    occurances += 1 #3
    print('logged.')

# Usage
logger()
print(f'Number of time logger got called {occurances}.')

logger()
logger()
logger()
logger()
print(f'Number of time logger got called {occurances}.')

logger()
logger()
logger()
logger()
print(f'Number of time logger got called {occurances}.')

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