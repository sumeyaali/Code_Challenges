def findEmailDomain(address):
    # loop through the email address and return domain after the at
    address = address.split('@')
    return address[-1]