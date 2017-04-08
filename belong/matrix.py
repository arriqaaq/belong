# a = [(1,2,3),(4,5,6),(7,8,9)]
# b = [(7,8,9), (4,5,6), (1,2,3)]

import copy

def rotate_list(input_list):
	count = 0
	col_len = len(input_list[0])
	row_len = len(input_list)
	reverse_list = copy.deepcopy(input_list)
	reverse_list.reverse()
	final_list = []

	for _ in xrange(col_len):
		row_item = ()
		for new_tuple in reverse_list:
			row_item = row_item + (new_tuple[count],)
		final_list.append(row_item)
		count += 1

	return final_list


def test():
	input_list = [(1,2,3,4),(5,6,7,8),(9,10,11,12)]
	output = rotate_list(input_list)
	print output