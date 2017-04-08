def is_anagram(word, matching_word):
	uniq_word_set = set(word)
	uniq_match_set = set(matching_word)
	bool_condition = (set(uniq_word_set) == set(uniq_match_set) \
						and len(uniq_word_set) == len(uniq_match_set))
	return bool_condition


def main(word_string, anagram):
	count = 0
	letter_count = 0
	SPACE = ' '
	position_arr = []
	word_length = len(anagram)

	for i in word_string:
		# letter_index = word_string.index(i)
		last_pos = letter_count + word_length
		word = word_string[letter_count : last_pos]
		print 101, word, letter_count
		if is_anagram(word, anagram):
			count += 1
			position_arr.append(letter_count)
		letter_count += 1

	return count, position_arr


def test():
	sentence = 'ABCDEABCCBA'
	word = 'ABC'
	count, pos_arr = main(sentence, word)
	print count, pos_arr