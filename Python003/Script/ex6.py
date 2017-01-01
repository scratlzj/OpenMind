# define x with 10 as a interge variable, binary, do_not, y.
x = "There are %d types of people." % 10 # s inside s
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # s inside s
# print x, print y
print x
print y
# print I said x ; print I said string(y)
print "I said: %r." % x
print "I also said: '%s'." % y # s inside s
# define hilarious; joke_evaluation(with a string inside);
# print joke_evaluation with hilarious as formatted variable;
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # s inside s
print joke_evaluation % hilarious
# define w, e;
w = "This is the left side of..."
e = "a string with a righr side."
# print string(w) + string(e)
print w + e

# my test
print "%r" % x
print "'x'"
print str(x)
print "%s" % x
print x
print x + y
