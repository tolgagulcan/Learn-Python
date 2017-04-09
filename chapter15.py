"""
"""

import sys
def h(k):
    """
Function for returning
a type's members
"""
    print(k," members:")
    print([s for s in dir(k) if not s.startswith("_")])

h(dict)
print(sys.__doc__)
print(len(sys.argv))


k=map(lambda x:x*x,[1,2,3])

print(map.__doc__)
print(list(k))
