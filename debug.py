import re
## DEBUG
test = '12346-789'
if re.match(r'^\d{5}-\d{3}$', test) is not None:
    print('Valid ZIP code format')
else:
    print('Invalid ZIP code format')
        ## END DEBUG