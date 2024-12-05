package main 

import (
	"fmt"
	"strconv"
	"os"
	_"strings"
	"bufio"
	"regexp"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)
	cont := ""

	//var instructions []string

	for scanner.Scan() {
		cont += scanner.Text()	
	}

	prodsum := 0
	enabled := true

	re := regexp.MustCompile(`mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)`)
	for _, match := range re.FindAllStringSubmatch(cont, -1) {
		if (match[0] == "don't()") {
			enabled = false
			continue
		}
		if (match[0] == "do()") {
			enabled = true
			continue
		}
		if enabled {
			val1, err := strconv.Atoi(match[1])
			if err != nil {
				panic(err)
			}
			val2, err := strconv.Atoi(match[2])
			if err != nil {
				panic(err)
			}
			prodsum += (val1*val2)
		}
	}

	fmt.Println("Part 1: ", prodsum)
}
