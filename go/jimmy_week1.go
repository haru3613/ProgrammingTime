package main

import "fmt"

func ValidParentheses(parens string) bool {
	const (
		OPEN = 40
		CLOSE = 41
	)
	result := 0
	for _, v := range parens {
		if int(v) == OPEN {
			result ++
		} else if int(v) == CLOSE {
			result --
			if result < 0 {
				return false
			}
		}
	}

	return result == 0
}

func main() {
	input1 := "(((())))" // true
	input2 := "(()" //false
	input3 := "()(" // false
	fmt.Println(ValidParentheses(input1))
	fmt.Println(ValidParentheses(input2))
	fmt.Println(ValidParentheses(input3))
}

