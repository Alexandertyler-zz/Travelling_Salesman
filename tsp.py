#!/usr/bin/python
import sys

def is_valid(graph, swap_tour, colors):
	city_iter = 0
	r_count = 0
	b_count = 0
	curr_color = ''
	prev_color = ''

	while city_iter < num:
		curr_city = swap_tour[city_iter]
		curr_color = colors[curr_city]

		if curr_color != prev_color:
			r_count = 0
			b_count = 0

		if curr_color == 'R':
			r_count += 1
		else:
			b_count += 1

		if r_count == 4 or b_count == 4:
			return False

		prev_color = curr_color
		city_iter += 1

	#do it for the loop back to the beginning now
	curr_city = swap_tour[0]
	curr_color = colors[curr_city]
	if curr_color != prev_color:
		return True
	if curr_color == 'R':
		r_count += 1
	else:
		b_count += 1
	if r_count == 4 or b_count == 4:
		return False
	return True
	

def tour_cost(graph, swap_tour, num):
	tour_cost = 0
	city_iter = 0
	start_city = swap_tour[0]
	#find the city index in the swap
	#update the cost from curr city to the next one
	while city_iter < num-1:
		curr_city = swap_tour[city_iter]
		next_city = swap_tour[city_iter]
		tour_cost += graph[curr_city][next_city]
		city_iter += 1
	#we need to finally move from the last city to the origin
	tour_cost += graph[next_city][start_city]

def find_optimal_path(num, graph, colors):
	city_used = [num]
	tour = [num]
	swap_tour = [num]

	


def parse_files(test_num):
	fout = open("answer.out", "w")
	for _iter in xrange(1, int(test_num)+1):
		fin = open("instances/"+ str(test_num) + ".in", "r")
	
		city_num = int(fin.readline())
		city_graph = [[] for i in range(city_num)]
    	for i in xrange(city_num):
       		city_graph[i] = [int(x) for x in fin.readline().split()]
        color_string = fin.readline()
    	
        # find an answer, and put into assign
        result = find_optimal_path(city_num, city_graph, color_string)

    	assign = [0] * city_num
    	for i in xrange(city_num):
       		assign[i] = i+1

    	fout.write("%s\n" % " ".join(map(str, assign)))
	fout.close()


def main():
	print "Running %s test cases." % str(sys.argv[1])
	parse_files(sys.argv[1])

if __name__ == "__main__":
	main()


