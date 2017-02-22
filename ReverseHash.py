class RHash:
    def __init__(self):
        self.letters = 'acdegilmnoprstuw'
        self.h = 7

#Function to reverse the hash given in the problem
#reverse of the given algorithm
        # Int64 hash (String s) {
        # Int64 h = 7
        # String letters = "acdegilmnoprstuw"
        # for(Int32 i = 0; i < s.length; i++) {
        # h = (h * 37 + letters.indexOf(s[i]))
        # }
        # return h
        # }
    def reverseHash(self, n):
        result = ''
        while n > 0:
            i = n % 37
            try:
                result += self.letters[i]          # append the letter from the letters String
            except IndexError:
                print('Invalid Hash value')
            n = int(n / 37)

            if n == self.h:
                return result[::-1]                # reverse the result to get the correct hash
            if n < self.h:                         # if value becomes less than the mentioned hash
                print('Invalid Hash value')
        

if __name__ == '__main__':
    RHashObj = RHash()
    print(RHashObj.reverseHash(930846109532517))    # we have got our answer i.e "lawnmower"
    print(RHashObj.reverseHash(680131659347))       # tested this value from question and answer matches the given string