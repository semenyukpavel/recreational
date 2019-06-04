def char_to_unicode(c):
	if c == '_':
		return c
	s = c.encode('utf-8').hex()
	f = '%'+s[0].upper()+s[1].upper()+'%'+s[2].upper()+s[3].upper()
	return f

def string_to_unicode(s):
	f = ""
	words = s.split(' ')
	for w in words:
		for i in range(len(w)):
			f = f + char_to_unicode(w[i])
		f = f + '+'
	return f.rstrip('+')