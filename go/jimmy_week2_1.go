package main

import "fmt"

func romanToInt(s string) int {
	myMap := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	result := 0
	for index, value := range s {
		curNum := myMap[string(value)]
		nextNum := 0
		if index+1 != len(s) {
			nextNum = myMap[string(s[index+1])]
		}

		if curNum >= nextNum {
			result += curNum
		} else {
			result -= curNum
		}
	}
	return result
}

func main() {
	input1 := "III"
	input2 := "IV"
	input3 := "IX"
	input4 := "LVIII"
	fmt.Println(romanToInt(input1))
	fmt.Println(romanToInt(input2))
	fmt.Println(romanToInt(input3))
	fmt.Println(romanToInt(input4))
}
