def knights1(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

c=knights1('Ni!')

print(c)