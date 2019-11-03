pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  #original = Mike
  #word = mike
  #first = m
  #new_word = mikemay
  #new_word = ikemay
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
    print 'empty'