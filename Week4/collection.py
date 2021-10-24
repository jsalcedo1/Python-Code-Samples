# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

for author, date in authors.items():
    print("%s" % author + " died in " + "%s." % date)

'''
Edited by: Jaime S.
10/22/2021

Corrections: 
========================================================================
Line 12 has 1 error:

Line 12: Syntax Error: Misspelled word for authors, should be spelled "authors"
========================================================================
Line 16 has 1 error:

Line 16: Syntax Error: Missing a curly bracket }, a curly bracket } should be added
========================================================================
Line 18 has 4 errors:

Line 18: Syntax Error: Missing a comma , after author, a comma was added after author
Line 18: Syntax Error: Missing date after the comma, a date was added after the comma
Line 18: Syntax Error: Wrongly expressed, the following expression should be used authors.items () 
Line 18: Syntax Error: Two curly brackets are unnecessarily used, they should be removed
=========================================================================
Line 19 has 3 errors:

Line 19: Syntax Error: Syntax Error: Missing an open and closing parenthesis, an open parenthesis should be added after
print( and a closing parenthesis should be added after Date)
Line 19: Syntax Error: Date should not be capitalized, date should be lowercase, and author_ 
should be added before date so it shows this "author_date"
Line 19: Syntax Error: Percentage sign is wrongly used, a plus + sign should be used instead
Line 19 Syntax Error: Following percentage sign is wrongly used, a plus + sign should be used instead
==========================================================================
Line 20 has 1 error:

Line 20: Unnecessary curly bracket }, the curly bracket } should be removed
===========================================================================

'''
