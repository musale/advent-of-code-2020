package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
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
	validPassports, validFieldsPassport := 0, 0
	for _, value := range lines {
		allFields := 7
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

		if allFields == 0 {
			validPassports++
			validFieldsCounter := 8
			for _, s := range strings.Split(value, " ") {
				if s != "" {
					fields := strings.Split(s, ":")
					attribute, attributeValue := fields[0], fields[1]
					switch attribute {
					case "byr":
						year, err := strconv.Atoi(attributeValue)
						if err == nil && year >= 1920 && year <= 2002 {
							validFieldsCounter--
						}
						break
					case "iyr":
						year, err := strconv.Atoi(attributeValue)
						if err == nil && year >= 2010 && year <= 2020 {
							validFieldsCounter--
						}
						break
					case "eyr":
						year, err := strconv.Atoi(attributeValue)
						if err == nil && year >= 2020 && year <= 2030 {
							validFieldsCounter--
						}
						break
					case "hgt":
						if strings.HasSuffix(attributeValue, "in") {
							num, err := strconv.Atoi(attributeValue[0:2])
							if err == nil && num >= 59 && num <= 76 {
								validFieldsCounter--
							}
						} else if strings.HasSuffix(attributeValue, "cm") {
							num, err := strconv.Atoi(attributeValue[0:3])
							if err == nil && num >= 150 && num <= 193 {
								validFieldsCounter--
							}
						}
						break
					case "hcl":
						matches, err := regexp.MatchString("^#[0-9a-f]{6}", attributeValue)
						if err == nil && matches {
							validFieldsCounter--
						}
						break
					case "ecl":
						exists := attributeValue == "amb" || attributeValue == "blu" || attributeValue == "brn" ||
							attributeValue == "gry" || attributeValue == "grn" || attributeValue == "hzl" ||
							attributeValue == "oth"
						if exists {
							validFieldsCounter--
						}
						break
					case "pid":
						matches, err := regexp.MatchString("^[0-9]{9}", attributeValue)
						if err == nil && len(attributeValue) == 9 && matches {
							validFieldsCounter--
						}
						break
					case "cid":
						validFieldsCounter--
						break
					default:
						log.Fatal("An unknown attribute ", attribute)
						break
					}
				}
			}
			if validFieldsCounter == 0 || validFieldsCounter == 1 {
				validFieldsPassport++
			}
		}
	}
	fmt.Println(fmt.Sprintf("Part 1: %d", validPassports))
	fmt.Println(fmt.Sprintf("Part 2: %d", validFieldsPassport))
}
