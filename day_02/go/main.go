package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func main() {
	policies := loadPasswordsAndPolicies()
	validPasswords := 0
	for _, policy := range policies {
		if policy.WithinMinMax() {
			validPasswords++
		}
	}
	fmt.Println(validPasswords)
}

// Password represents the password and the policy
type Password struct {
	min, max            int
	character, password string
}

// WithinMinMax checks if a password is within the min/max requirements
func (p *Password) WithinMinMax() bool {
	var charCounts int
	for _, char := range p.password {
		if string(char) == p.character {
			charCounts++
		}
	}
	if p.min <= charCounts && p.max >= charCounts {
		return true
	}
	return false
}

func loadPasswordsAndPolicies() []*Password {
	file, err := os.Open("day_02/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var policies []*Password
	for scanner.Scan() {
		value := scanner.Text()
		re := regexp.MustCompile(`(?P<min>\d+)-(?P<max>\d+)\s(?P<value>[a-z]):\s(?P<password>.*)`)
		results := re.FindStringSubmatch(value)
		min, max, character, password := results[1], results[2], results[3], results[4]
		minInt, _ := strconv.Atoi(min)
		maxInt, _ := strconv.Atoi(max)
		policy := &Password{
			min:       minInt,
			max:       maxInt,
			character: character,
			password:  password}
		policies = append(policies, policy)
	}
	return policies
}
