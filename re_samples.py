# Credits
#   https://pymotw.com/2/re/index.html#module-re
# Installation

import re

print ("\n##########> RE search()")

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print ('Looking for "%s" in "%s" ->' % (pattern, text))
    
    if re.search(pattern, text):
        print ("found a match!")
    else:
        print ('no match')

# Looking for "this" in "Does this text match the pattern?" ->
# found a match!
# Looking for "that" in "Does this text match the pattern?" ->
# no match

		
print ("\n##########> RE match()")

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start() # start of mathed string, index starts from 0
e = match.end() # ebd of mathed string

print ('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e]))
	
# Found "this" in "Does this text match the pattern?" from 5 to 9 ("this")

print ("\n##########> RE compile()")

# Pre-compile the patterns and save it as RegexObject
regexes = [ re.compile(p) for p in [ 'this','that',] ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print ('Looking for "%s" in "%s" ->' % (regex.pattern, text))

    if regex.search(text):
        print ('found a match!')
    else:
        print ('no match')

# Looking for "this" in "Does this text match the pattern?" ->
# found a match!
# Looking for "that" in "Does this text match the pattern?" ->
# no match

print ("\n##########> RE findall() ")
# The findall() function returns all of the substrings of the input that match the pattern without overlapping.

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.findall(pattern, text):
    print ('Found "%s"' % match)

# Found "ab"
# Found "ab"

print ("\n##########> RE finditer() ")
text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e) )

# Found "ab" at 0:2
# Found "ab" at 5:7

