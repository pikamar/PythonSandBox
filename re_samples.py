# Credits
#   https://pymotw.com/2/re/index.html#module-re
# Installation

import re
import sys
#sys.path.append( "helper" )
from helper.re_helper import test_patterns

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

print ("\n##########> Repetition ")
test_patterns('abbaaabbbbaaaaa',
              [ 'ab*', 'ab*?',         # a followed by zero or more b
                'ab+', 'ab+?',         # a followed by one or more b
                'ab?', 'ab??',         # a followed by zero or one b
                'ab{3}', 'ab{3}?',     # a followed by three b
                'ab{2,3}', 'ab{2,3}?', # a followed by two to three b
                ])

#          11111
#012345678901234
#abbaaabbbbaaaaa
#Matching "ab*"
#   0 :  2 = "abb"
#   3 :  3 = "a"
#   4 :  4 = "a"
#   5 :  9 = "abbbb"
#  10 : 10 = "a"
#  11 : 11 = "a"
#  12 : 12 = "a"
#  13 : 13 = "a"
#  14 : 14 = "a"
#Matching "ab*?"
#   0 :  0 = "a"
#   3 :  3 = "a"
#   4 :  4 = "a"
#   5 :  5 = "a"
#  10 : 10 = "a"
#  11 : 11 = "a"
#  12 : 12 = "a"
#  13 : 13 = "a"
#  14 : 14 = "a"
#Matching "ab+"
#   0 :  2 = "abb"
#   5 :  9 = "abbbb"
#Matching "ab+?"
#   0 :  1 = "ab"
#   5 :  6 = "ab"
#Matching "ab?"
#   0 :  1 = "ab"
#   3 :  3 = "a"
#   4 :  4 = "a"
#   5 :  6 = "ab"
#  10 : 10 = "a"
#  11 : 11 = "a"
#  12 : 12 = "a"
#  13 : 13 = "a"
#  14 : 14 = "a"
#Matching "ab??"
#   0 :  0 = "a"
#   3 :  3 = "a"
#   4 :  4 = "a"
#   5 :  5 = "a"
#  10 : 10 = "a"
#  11 : 11 = "a"
#  12 : 12 = "a"
#  13 : 13 = "a"
#  14 : 14 = "a"
#Matching "ab{3}"
#   5 :  8 = "abbb"
#Matching "ab{3}?"
#   5 :  8 = "abbb"
#Matching "ab{2,3}"
#   0 :  2 = "abb"
#   5 :  8 = "abbb"
#Matching "ab{2,3}?"
#   0 :  2 = "abb"
#   5 :  7 = "abb"

print ("\n##########> Character Sets ")

test_patterns('abbaaabbbbaaaaa',
              [ '[ab]',    # either a or b
                'a[ab]+',  # a followed by one or more a or b
                'a[ab]+?', # a followed by one or more a or b, not greedy
                ])
                
#          11111
#012345678901234
#abbaaabbbbaaaaa
#
#Matching "[ab]"
#   0 :  0 = "a"
#   1 :  1 = "b"
#   2 :  2 = "b"
#   3 :  3 = "a"
#   4 :  4 = "a"
#   5 :  5 = "a"
#   6 :  6 = "b"
#   7 :  7 = "b"
#   8 :  8 = "b"
#   9 :  9 = "b"
#  10 : 10 = "a"
#  11 : 11 = "a"
#  12 : 12 = "a"
#  13 : 13 = "a"
#  14 : 14 = "a"
#
#Matching "a[ab]+"
#   0 : 14 = "abbaaabbbbaaaaa"
#
#Matching "a[ab]+?"
#   0 :  1 = "ab"
#   3 :  4 = "aa"
#   5 :  6 = "ab"
#  10 : 11 = "aa"
#  12 : 13 = "aa"

print ("\n##########> Character Sets - exclude")

test_patterns('This is some text -- with punctuation.',
              [ '[^-. ]+',  # sequences without -, ., or space
                ])
                
#          1111111111222222222233333333
#01234567890123456789012345678901234567
#This is some text -- with punctuation.
#
#Matching "[^-. ]+"
#   0 :  3 = "This"
#   5 :  6 = "is"
#   8 : 11 = "some"
#  13 : 16 = "text"
#  21 : 24 = "with"
#  26 : 36 = "punctuation"

print ("\n##########> Character Sets - ranges")

test_patterns('This is some text -- with punctuation.',
              [ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+', # one upper case letter followed by lower case letters
                ])
                
#          1111111111222222222233333333
#01234567890123456789012345678901234567
#This is some text -- with punctuation.
#
#Matching "[a-z]+"
#   1 :  3 = "his"
#   5 :  6 = "is"
#   8 : 11 = "some"
#  13 : 16 = "text"
#  21 : 24 = "with"
#  26 : 36 = "punctuation"
#
#Matching "[A-Z]+"
#   0 :  0 = "T"
#
#Matching "[a-zA-Z]+"
#   0 :  3 = "This"
#   5 :  6 = "is"
#   8 : 11 = "some"
#  13 : 16 = "text"
#  21 : 24 = "with"
#  26 : 36 = "punctuation"
#
#Matching "[A-Z][a-z]+"
#   0 :  3 = "This"

print ("\n##########> Character Sets - any character")

test_patterns('abbaaabbbbaaaaa',
              [ 'a.',   # a followed by any one character
                'b.',   # b followed by any one character
                'a.*b', # a followed by anything, ending in b
                'a.*?b', # a followed by anything, ending in b
                ])
                
#          11111
#012345678901234
#abbaaabbbbaaaaa
#
#Matching "a."
#   0 :  1 = "ab"
#   3 :  4 = "aa"
#   5 :  6 = "ab"
#  10 : 11 = "aa"
#  12 : 13 = "aa"
#
#Matching "b."
#   1 :  2 = "bb"
#   6 :  7 = "bb"
#   8 :  9 = "bb"
#
#Matching "a.*b"
#   0 :  9 = "abbaaabbbb"
#
#Matching "a.*?b"
#   0 :  1 = "ab"
#   3 :  6 = "aaab"

print ("\n##########> Escape Codes")

# Code	Meaning
# \d	a digit
# \D	a non-digit
# \s	whitespace (tab, space, newline, etc.)
# \S	non-whitespace
# \w	alphanumeric
# \W	non-alphanumeric

test_patterns('This is a prime #1 example!',
              [ r'\d+', # sequence of digits, !!! pattern of type r, so we don`t have to escape special characters, like \
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ])
                
#           11111111112222222
# 012345678901234567890123456
# This is a prime #1 example!
# 
# Matching "\d+"
#   17 : 17 = "1"
# 
# Matching "\D+"
#    0 : 16 = "This is a prime #"
#   18 : 26 = " example!"
# 
# Matching "\s+"
#    4 :  4 = " "
#    7 :  7 = " "
#    9 :  9 = " "
#   15 : 15 = " "
#   18 : 18 = " "
# 
# Matching "\S+"
#    0 :  3 = "This"
#    5 :  6 = "is"
#    8 :  8 = "a"
#   10 : 14 = "prime"
#   16 : 17 = "#1"
#   19 : 26 = "example!"
# 
# Matching "\w+"
#    0 :  3 = "This"
#    5 :  6 = "is"
#    8 :  8 = "a"
#   10 : 14 = "prime"
#   17 : 17 = "1"
#   19 : 25 = "example"
# 
# Matching "\W+"
#    4 :  4 = " "
#    7 :  7 = " "
#    9 :  9 = " "
#   15 : 16 = " #"
#   18 : 18 = " "
#   26 : 26 = "!"

print ("\n##########> Anchoring")

# Code	Meaning
# ^	start of string, or line
# $	end of string, or line
# \A	start of string
# \Z	end of string
# \b	empty string at the beginning or end of a word
# \B	empty string not at the beginning or end of a word

test_patterns('This is some text -- with punctuation.',
              [ r'^\w+',     # word at start of string
                r'\A\w+',    # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z', # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\B',    # 't', not start or end of word
                ])
                
#           1111111111222222222233333333
# 01234567890123456789012345678901234567
# This is some text -- with punctuation.
# 
# Matching "^\w+"
#    0 :  3 = "This"
# 
# Matching "\A\w+"
#    0 :  3 = "This"
# 
# Matching "\w+\S*$"
#   26 : 37 = "punctuation."
# 
# Matching "\w+\S*\Z"
#   26 : 37 = "punctuation."
# 
# Matching "\w*t\w*"
#   13 : 16 = "text"
#   21 : 24 = "with"
#   26 : 36 = "punctuation"
# 
# Matching "\bt\w+"
#   13 : 16 = "text"
# 
# Matching "\w+t\b"
#   13 : 16 = "text"
# 
# Matching "\Bt\B"
#   23 : 23 = "t"
#   30 : 30 = "t"
#   33 : 33 = "t"

print ("\n##########> Dissecting Matches with Groups")

test_patterns('abbaaabbbbaaaaa',
              [ 'a(ab)',    # 'a' followed by literal 'ab'
                'a(a*b*)',  # 'a' followed by 0-n 'a' and 0-n 'b'
                'a(ab)*',   # 'a' followed by 0-n 'ab'
                'a(ab)+',   # 'a' followed by 1-n 'ab'
                ])
                
#           11111
# 012345678901234
# abbaaabbbbaaaaa
# 
# Matching "a(ab)"
#    4 :  6 = "aab"
# 
# Matching "a(a*b*)"
#    0 :  2 = "abb"
#    3 :  9 = "aaabbbb"
#   10 : 14 = "aaaaa"
# 
# Matching "a(ab)*"
#    0 :  0 = "a"
#    3 :  3 = "a"
#    4 :  6 = "aab"
#   10 : 10 = "a"
#   11 : 11 = "a"
#   12 : 12 = "a"
#   13 : 13 = "a"
#   14 : 14 = "a"
# 
# Matching "a(ab)+"
#    4 :  6 = "aab"

print ("\n##########> Dissecting Matches with Groups - naming groups")

text = 'This is some text -- with punctuation.'

print (text)
print

for pattern in [ r'^(?P<first_word>\w+)',
                 r'(?P<last_word>\w+)\S*$',
                 r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
                 r'(?P<ends_with_t>\w+t)\b',
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print ('Matching "%s"' % pattern)
    print ('  ', match.groups())
    print ('  ', match.groupdict())
    print
    
# This is some text -- with punctuation.
# Matching "^(?P<first_word>\w+)"
#    ('This',)
#    {'first_word': 'This'}
# Matching "(?P<last_word>\w+)\S*$"
#    ('punctuation',)
#    {'last_word': 'punctuation'}
# Matching "(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)"
#    ('text', 'with')
#    {'t_word': 'text', 'other_word': 'with'}
# Matching "(?P<ends_with_t>\w+t)\b"
#    ('text',)
#    {'ends_with_t': 'text'}

print ("\n##########> Search Options - Case-insensitive Matching")

# Flag	        Abbreviation
# IGNORECASE	i
# MULTILINE	    m
# DOTALL	    s
# UNICODE	    u
# VERBOSE	    x

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print ('Text            :', text)
print ('Pattern         :', pattern)
print ('Case-sensitive  :', with_case.findall(text))
print ('Case-insensitive:', without_case.findall(text))

# Text            : This is some text -- with punctuation.
# Pattern         : \bT\w+
# Case-sensitive  : ['This']
# Case-insensitive: ['This', 'text']

print ("\n##########> Search Options - Input with Multiple Lines")

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print ('Text        :', repr(text))
print ('Pattern     :', pattern)
print ('Single Line :', single_line.findall(text))
print ('Multline    :', multiline.findall(text))

# Text        : 'This is some text -- with punctuation.\nAnd a second line.'
# Pattern     : (^\w+)|(\w+\S*$)
# Single Line : [('This', ''), ('', 'line.')]
# Multline    : [('This', ''), ('', 'punctuation.'), ('And', ''), ('', 'line.')]

print ("\n##########> Search Options - Verbose Expression Syntax")

address = re.compile(
    '''

    # A name is made up of letters, and may include "." for title
    # abbreviations and middle initials.
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+)
       \s*
       # Email addresses are wrapped in angle brackets: < >
       # but we only want one if we found a name, so keep
       # the start bracket in this group.
       <
    )? # the entire name is optional

    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
    )

    >? # optional closing angle bracket
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    u'<first.last@example.com>',
    ]

for candidate in candidates:
    print
    print ('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print ('  Match name :', match.groupdict()['name'])
        print ('  Match email:', match.groupdict()['email'])
    else:
        print ('  No match')
        
# Candidate: first.last@example.com
#   Match name : None
#   Match email: first.last@example.com
# 
# Candidate: first.last+category@gmail.com
#   Match name : None
#   Match email: first.last+category@gmail.com
# 
# Candidate: valid-address@mail.example.com
#   Match name : None
#   Match email: valid-address@mail.example.com
# 
# Candidate: not-valid@example.foo
#   No match
# 
# Candidate: First Last <first.last@example.com>
#   Match name : First Last
#   Match email: first.last@example.com
# 
# Candidate: No Brackets first.last@example.com
#   Match name : None
#   Match email: first.last@example.com
# 
# Candidate: First Last
#   No match
# 
# Candidate: First Middle Last <first.last@example.com>
#   Match name : First Middle Last
#   Match email: first.last@example.com
# 
# Candidate: First M. Last <first.last@example.com>
#   Match name : First M. Last
#   Match email: first.last@example.com
# 
# Candidate: <first.last@example.com>
#   Match name : None
#   Match email: first.last@example.com

print ("\n##########> Search Options - Embedding Flags in Patterns")

text = 'This is some text -- with punctuation.'
pattern = r'(?i)\bT\w+'
regex = re.compile(pattern)

print ('Text      :', text)
print ('Pattern   :', pattern)
print ('Matches   :', regex.findall(text))

# Text      : This is some text -- with punctuation.
# Pattern   : (?i)\bT\w+
# Matches   : ['This', 'text']

print ("\n##########> Modifying Strings with Patterns")

bold = re.compile(r'\*{2}(.*?)\*{2}', re.UNICODE)

text = 'Make this **bold**.  This **too**.'

print ('Text:', text)
print ('Bold:', bold.sub(r'<b>\1</b>', text))

# Text: Make this **bold**.  This **too**.
# Bold: Make this <b>bold</b>.  This <b>too</b>.

print ("\n##########> Modifying Strings with Patterns - by group name")

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}', re.UNICODE)

text = 'Make this **bold**.  This **too**.'

print ('Text:', text)
print ('Bold:', bold.sub(r'<b>\g<bold_text></b>', text))

# Text: Make this **bold**.  This **too**.
# Bold: Make this <b>bold</b>.  This <b>too</b>.

print ("\n##########> Modifying Strings with Patterns - count")

bold = re.compile(r'\*{2}(.*?)\*{2}', re.UNICODE)
text = 'Make this **bold**.  This **too**.'

print ('Text:', text)
print ('Bold:', bold.sub(r'<b>\1</b>', text, count=1))

# Text: Make this **bold**.  This **too**.
# Bold: Make this <b>bold</b>.  This **too**.

print ("\n##########> Modifying Strings with Patterns - subn()")

bold = re.compile(r'\*{2}(.*?)\*{2}', re.UNICODE)

text = 'Make this **bold**.  This **too**.'

print ('Text:', text)
print ('Bold:', bold.subn(r'<b>\1</b>', text))

# Text: Make this **bold**.  This **too**.
# Bold: ('Make this <b>bold</b>.  This <b>too</b>.', 2)

print ("\n##########> Splitting with Patterns")

text = 'Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'

print ('With findall:')
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)):
    print (num, repr(para))
    print

print
print ('With split:')
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print (num, repr(para))
    print
    
# With findall:
# 0 ('Paragraph one\non two lines.', '\n\n')
# 
# 1 ('Paragraph two.', '\n\n\n')
# 
# 2 ('Paragraph three.', '')
# 
# 
# With split:
# 0 'Paragraph one\non two lines.'
# 
# 1 'Paragraph two.'
# 
# 2 'Paragraph three.'