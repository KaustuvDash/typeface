from metaphone import doublemetaphone
search_string = "Murthy"
words_file = ["Moorthy","Moorthi","haysdasd","asdasdasund","moorrttaaa"]
encoded_search_string = doublemetaphone(search_string)
phonetic_matches = []
for word in words_file:
  encoded_word = doublemetaphone(word)
  if encoded_word == encoded_search_string:
    phonetic_matches.append(word)
print(phonetic_matches)
