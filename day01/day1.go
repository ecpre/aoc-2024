package main

import (
	"fmt"
	"strconv"
	"os"
	"bufio"
	"strings"
	"sort"
)

func main() {
	
	var list1 = [2048]int{}
	var list2 = [2048]int{}

	var nums1 map[int]int
	var nums2 map[int]int

	nums1 = make(map[int]int)
	nums2 = make(map[int]int)

	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)
	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	

	for i, line := range lines {
		split := strings.Split(line, "   ")
		val1, err := strconv.Atoi(split[0])
		if err != nil {
			panic(err)
		}
		val2, err := strconv.Atoi(split[1])
		if err != nil {
			panic(err)
		}
		
		list1[i] = val1
		list2[i] = val2

		nums1[val1]++
		nums2[val2]++
	
	}
	
	res1 := 0
	res2 := 0
	
	sort.Ints(list1[:])
	sort.Ints(list2[:])

	for i := 0; i< len(list1); i++ {

		var absval int
		if list1[i] > list2[i] {
			absval = list1[i] - list2[i]
		} else {
			absval = list2[i] - list1[i]
		}

		res2 += (list1[i] * nums2[list1[i]])
		
		res1 += absval
	}
	
	fmt.Println("Part 1: ", res1)
	fmt.Println("Part 2: ", res2)

}
