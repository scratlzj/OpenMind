# define formatter which is a string contains only four raw variables
formatter = "%r %r %r %r"
# print numbers: 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
# print out strings: one, two, three, four
print formatter % ("one", "two", "three", "four")
# print logic True or False
print formatter % (True, False, False, True)
# print out string word "formatter" * 4
print formatter % (formatter, formatter, formatter, formatter)
# print 4 string sentences
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didin't sing.",
    "So I said goodnight."
)
