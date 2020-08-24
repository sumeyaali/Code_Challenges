def findEmailDomain(address):
    # loop through the email address and return domain after the at
    address = address.split('@')
    return address[-1]

    

var  x = 21;
function addTwo(x) {
    return x + 2;
    console.log(x);
};
addTwo()