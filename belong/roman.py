# input_time = [(3,4),(5,6),(6,9),(5,10),(5,6),(11,12),(8,9),(8,10)]

# def get_ranges(min_hr, max_hr):
# 	base_list = range(min_hr, max_hr + 1)
# 	combinations = [(i, i+1) for i in base_list if (base_list.index(i) + 1) !=len(base_list)]

def count_rooms(input_time):
	room_time_set = set()
	base_elem = [i[0] for i in input_time]
	base_dict = {i[0] : i for i in input_time}
	base_elem.sort()

	sorted_list = [base_dict[i] for i in base_elem]
	count = 0
	room_count = 0


	for _ in sorted_list:
		next_count = count + 1
		if next_count >= len(sorted_list):
			break

		first = sorted_list[count]
		last = sorted_list[next_count]

		if first[1] > last[0]:
			room_count += 1

		count+=1

	return room_count


def test():
	input_time = [(3,4),(5,6),(6,9),(5,10),(5,6),(11,12),(8,9),(8,10)]
	count = count_rooms(input_time)
	print count