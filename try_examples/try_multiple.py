# 
print
for value in (None, "Hi!"):
    try:
        print "Attempting to convert", value, "-->",
        print float(value)
    except(TypeError, ValueError):
        print "Something went wrong!"

print
for value in (None, "Hi!"):
    try:
        print "Attempting to convert", value, "-->",
        print float(value)
    except(TypeError):
        print "I can only convert a string or a number!"
    except(ValueError):
        print "I can only convert a string of digits!"