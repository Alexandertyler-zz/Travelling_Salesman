#!/usr/bin/python
import sys


def parse_files(test_num):
	fout = open("answer.out", "w")
	for _iter in xrange(1, int(test_num)+1):
		fin = open("instances/"+ str(test_num) + ".in", "r")
	
		city_num = int(fin.readline())
		city_graph = [[] for i in range(city_num)]
    	for i in xrange(city_num):
       		city_graph[i] = [int(x) for x in fin.readline().split()]
    	color_string = fin.readline()
    	print city_graph

    	# find an answer, and put into assign
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


