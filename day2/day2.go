package main

import (
	"fmt"
	"strconv"
	"os"
	"bufio"
	"strings"
)

func main() {
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

	safe := 0
	safe2 := 0

	for _, line := range lines {
		split := strings.Split(line, " ")

		var increasing bool

		sp0, err := strconv.Atoi(split[0])
		if err != nil {
			panic(err)
		}
		sp1, err := strconv.Atoi(split[1])
		if err !=nil {
			panic(err)
		}

		if sp0 == sp1 {
			sp0 = sp1
			sp1, err = strconv.Atoi(split[2])
		} 
		if sp0 > sp1 {
			increasing = false
		} else {
			increasing = true
		}

		if !validate(split, increasing) {
			for i := range split {
				skipsplit := append(append([]string{}, split[:i]...), split[i+1:]...)
				if validate(skipsplit, increasing) {
					safe2++
					break
				} else if validate (skipsplit, !increasing) {
					// poor part 1 implementation don't want to change necessitates this
					safe2++
					break
				}
			}
		} else {
			safe++
		}

	}
	fmt.Println("Part 1: ", safe)
	fmt.Println("Part 2: ", safe+safe2)
}

func validate(split []string, increasing bool) bool {

	for j := range split {
		if j == len(split)-1 {
			break
		}
		val1, err := strconv.Atoi(split[j])
		if err != nil {
			panic(err)
		}
		val2, err := strconv.Atoi(split[j+1])
		if err != nil {
			panic(err)
		}

		if !compare(increasing, val1, val2) {
			return false
		}
	}
	return true
}

func compare(increasing bool, val1 int, val2 int) bool {

	if val1 < val2 {
		diff := val2 - val1
		if !increasing || diff > 3 {
			return false
		} 
	} else if val1> val2 {
		diff := val1 - val2
		if increasing || diff > 3{
			return false
		}
	} else {
		return false
	}
	return true
}
