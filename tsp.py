#!/usr/bin/python
import sys

def is_valid(graph, colors, num, swap_tour):
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

def tour_cost(graph, num, swap_tour):
	tour_cost = 0
	city_iter = 0
	start_city = swap_tour[0]
	#find the city index in the swap
	#update the cost from curr city to the next one
	while city_iter < num-1:
		curr_city = swap_tour[city_iter]
		next_city = swap_tour[city_iter+1]
		tour_cost += graph[curr_city][next_city]
		city_iter += 1
	#we need to finally move from the last city to the origin
	tour_cost += graph[next_city][start_city]
	return tour_cost

def find_optimal_path(num, graph, colors):
	print "in optimal"
	city_used = [num]
	tour = [num]
	swap_tour = [0] * num
		
	#3 swap
	#for loop for choosing bunch of 3 nodes.
	#step 1 - build initial tour

	curr_city = 0
	used = [0] * num
	
	used[0] = 1
	city_count = 0
	tour_iter = 1
	#for every city in our graph
	while city_count < num-1:
		local_min = [0, float("inf")]
		#for every city in the range of my current city
		for next_city in range(0, len(graph[curr_city])):
			if used[next_city] == 0:
				if colors[curr_city] != colors[next_city]:
					#[city traveling to, cost]
					path = [next_city, graph[curr_city][next_city]]
					if local_min[1] > path[1]:
						local_min = path

		used[local_min[0]] = 1
		city_count += 1
		swap_tour[city_count] = local_min[0]
		curr_city = local_min[0]

	return swap_tour
	


def parse_files(test_num):
	fout = open("answer.out", "w")
	for _iter in xrange(1, int(test_num)+1):
		fin = open("instances/"+str(_iter) + ".in", "r")
		print fin
		city_num = int(fin.readline())
		city_graph = [[] for i in range(city_num)]
    	for i in xrange(0,city_num):
    		#print i
       		city_graph[i] = [int(x) for x in fin.readline().split()]
        color_string = fin.readline()
        #print color_string
        #print city_graph
    	
        # find an answer, and put into assign
        swap_tour = find_optimal_path(city_num, city_graph, color_string)
        result = is_valid(city_graph, color_string, city_num, swap_tour)
        print result
        cost = tour_cost(city_graph, city_num, swap_tour)
        print cost

    	assign = swap_tour

    	fout.write("%s\n" % " ".join(map(str, assign)))
	fout.close()


def main():
	print "Running %s test cases." % str(sys.argv[1])
	parse_files(sys.argv[1])

if __name__ == "__main__":
	main()


