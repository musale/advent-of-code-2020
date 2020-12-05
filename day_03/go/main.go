package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	mapValues := loadMap()
	mapLen := len(mapValues)
	for mapLen > 0 {
		fmt.Println(mapLen)
		mapLen--
	}
	fmt.Println(len(mapValues))
}

func partOne(mapValues []string) int {
	
	return 0
}

func loadMap() []string {
	file, err := os.Open("day_03/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var mapValues []string
	for scanner.Scan() {
		value := scanner.Text()
		mapValues = append(mapValues, value)
	}
	return mapValues
}
