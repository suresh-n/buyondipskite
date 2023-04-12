username=''  # Add kite username here
password=''  # Add your kite password here
secret=''  # Add your secret here
enctoken=None

try:
    enctoken = open('enctoken.txt', 'r').read().rstrip()
except Exception as e:
    print('Exception occurred :: {}'.format(e))
    enctoken = None
