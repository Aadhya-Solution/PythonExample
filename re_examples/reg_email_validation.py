def validateEmail(email):
    """Checks for a syntactically valid email address."""
    # Email address must be at least 6 characters in total.
    if len(email) < 6:
		return False # Address too short.
    # Split up email address into parts.
    try:
		localpart, domainname = email.rsplit('@', 1)
		host, toplevel = domainname.rsplit('.', 1)
    except ValueError:
		return False # Address does not have enough parts.
    if localpart[:1] == "." or localpart[-1] == ".":
		return False # Dots at the beginning or end of the localpart
    # Check for Country code length.
    if len(toplevel)<2 or len(toplevel)>6:
		return False # Not a domain name.
    # Check for allowed characters
    for i in '-_.%+':
		localpart = localpart.replace(i, "")
    for i in '-_.':
		host = host.replace(i, "")
    if localpart.isalnum() and host.isalnum():
		return True # Email address is fine.
    else:
		return False # Email address has funny characters.
if __name__ == '__main__':
	email1 = "test.@web.com"
	print email1,"is valid:",validateEmail(email1)
	email2 = "test+john@web.museum"
	print email2,"is valid:",validateEmail(email2)
	email3 = "test+john@web.m"
	print email3,"is valid:",validateEmail(email3)
	email4 = "a@n.dk"
	print email4,"is valid:",validateEmail(email4)
	email5 = "and.bun@webben.de"
	print email5,"is valid:",validateEmail(email5)