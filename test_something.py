# Simple Test Function Example
# This script defines and tests a basic factorial function using an assert statement.

def fat(n):
    if(n==0):
        return 1
    return n * fat(n-1)

def test_fat():
    assert fat(0) == 1