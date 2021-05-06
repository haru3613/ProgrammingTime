package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	slice := strings.Split(strings.TrimSpace(s), " ")

	return len(slice[len(slice) - 1])
}

func main() {
	input1 := "Hello World"
	fmt.Println(lengthOfLastWord(input1))
}
