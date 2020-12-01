package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	numbers := loadNumbers()
	first, second, product := partOne(numbers)
	fmt.Println(first, second, product)
}

func partOne(arr []int) (int, int, int) {
	for _, value := range arr {
		target := 2020 - value
		if checkExistsInArray(arr, target) {
			return value, target, value * target
		}
	}
	return 0, 0, 0
}

func checkExistsInArray(arr []int, item int) bool {
	for _, value := range arr {
		if value == item {
			return true
		}
	}
	return false
}

func loadNumbers() []int {
	file, err := os.Open("day_01/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var numbers []int
	for scanner.Scan() {
		value := scanner.Text()
		v, _ := strconv.Atoi(value)
		numbers = append(numbers, v)
	}
	return numbers
}
