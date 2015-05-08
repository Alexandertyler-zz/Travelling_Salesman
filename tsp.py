import sys
import random

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
    #print "in optimal"
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
    
def swap_dis_shit(graph, swap_tour, colors, num):
    """
    i=0
     1|2|3.
     1|3|2.

    i=2
     2|1|3
     3|1|2

    i=1
     3|2|1
     2|3|1
    """
    j = 0
    dict = {}
    dict[tour_cost(graph,num,swap_tour)] = list(swap_tour)
    while (j < 10000):
        first = random.randint(0,num-1)
        second = random.randint(0,num-1)
        # while (first == second or colors[swap_tour[first]] != colors[swap_tour[second]]):
            # second = random.randint(0,num-1)
        third = random.randint(0,num-1)
        # while (first == third or second == third or colors[swap_tour[first]] != colors[swap_tour[third]]):
            # third = random.randint(0,num-1)

        city1 = swap_tour[first]
        city2 = swap_tour[second]
        city3 = swap_tour[third]
       
        for i in range(0,3):
            swap_tourc = list(swap_tour)

            #replace swap_tour[first] with swap_tour two value
            if i != 0:
                if i == 2:
                    swap_tourc[second] = city1
                    swap_tourc[first] = city2
                    if (is_valid(graph, colors, num, swap_tourc)):
                        dict[tour_cost(graph,num,swap_tourc)] = list(swap_tourc)
                else:
                    swap_tourc[third] = city1
                    swap_tourc[first] = city3
                    if (is_valid(graph, colors, num, swap_tourc)):
                        dict[tour_cost(graph,num,swap_tourc)] = list(swap_tourc)
            if i == 0:
                if (is_valid(graph, colors, num, swap_tourc)):
                    dict[tour_cost(graph,num,swap_tourc)] = list(swap_tourc)
            
            if i == 0:
                swap_tourc[second] = city3
                swap_tourc[third] = city2 
            if i == 1:
                swap_tourc[second] = city3
                swap_tourc[first] = city2
            if i == 2:
                swap_tourc[first] = city3
                swap_tourc[third] = city2
                
            if is_valid(graph, colors, num, swap_tourc):
                dict[tour_cost(graph,num,swap_tourc)] = list(swap_tourc)

        if (random.randint(0,10) < 7):
            swap_tour = dict[min(dict.keys())]
        else:
            swap_tour = dict[random.choice(dict.keys())]

        j += 1;
    return dict

def invert_swap(swap_tour, num):
	result = [0] * num
	for i in range(0, len(swap_tour)):
		result[swap_tour[i]] = i+1
	return result

def parse_files(test_num):
    fout = open("answer.out", "w")
    for t in range(1, int(test_num)+1):
        fin = open("instances/"+str(t) + ".in", "rw")

        city_num = int(fin.readline())
        city_graph = [[] for i in range(0, city_num)]

        for graph_iter in range(0, city_num):
            line = fin.readline().split()
            city_graph[graph_iter] = [int(x) for x in line]
        color_string = fin.readline()
        # find an answer, and put into assign

        swap_tour = find_optimal_path(city_num, city_graph, color_string)
        res = swap_dis_shit(city_graph, swap_tour, color_string, city_num)
        print "Result " + str(t) +" is:", min(res.keys())
        #print res[min(res.keys())]
        swap_tour = res[min(res.keys())]
        for element in range(0, len(swap_tour)):
            swap_tour[element] = swap_tour[element] + 1
        assign = swap_tour
        #print swap_tour
        #print assign
		

        fout.write("%s\n" % " ".join(map(str, assign)))
    fout.close()


def main():
    print "Running %s test cases." % str(sys.argv[1])
    parse_files(sys.argv[1])

if __name__ == "__main__":
    main()


