package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	loadPassports()
}

func loadPassports() {
	file, err := os.Open("day_04/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var line strings.Builder
	var lines []string
	for scanner.Scan() {
		value := scanner.Text()
		if len(value) == 0 {
			lines = append(lines, line.String())
			line = strings.Builder{}
			continue
		} else {
			line.WriteString(value + " ")
		}
	}
	lines = append(lines, line.String())
	validPassports := 0
	for _, value := range lines {
		allFields := 8
		if strings.Contains(value, "ecl") {
			allFields--
		}
		if strings.Contains(value, "iyr") {
			allFields--
		}
		if strings.Contains(value, "pid") {
			allFields--
		}
		if strings.Contains(value, "eyr") {
			allFields--
		}
		if strings.Contains(value, "hcl") {
			allFields--
		}
		if strings.Contains(value, "byr") {
			allFields--
		}
		if strings.Contains(value, "hgt") {
			allFields--
		}

		if allFields == 1 {
			validPassports++
		}
	}
	fmt.Println(fmt.Sprintf("Part 1: %d", validPassports))
}
