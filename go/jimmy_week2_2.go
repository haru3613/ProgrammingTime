package main

import (
	"fmt"
	"strings"
)

func longestCommonPrefix(strs []string) string {
	prefix := ""
	if len(strs) == 0 {
		return prefix
	}

	if len(strs) == 1 {
		return strs[0]
	}

	firstStr := strs[0]
	checkSlice := strs[1:]
	tmpPrefix := ""

	for _, v := range firstStr {
		flag := 0
		tmpPrefix += string(v)
		for _, str := range checkSlice {
			if strings.HasPrefix(str, string(tmpPrefix)) {
				flag++
			}
			if flag == len(checkSlice) {
				prefix = string(tmpPrefix)
			}
		}
	}

	return prefix
}

func main() {
	input1 := []string{"flower", "flow", "flight"}
	input2 := []string{"dog", "racecar", "car"}
	fmt.Println(longestCommonPrefix(input1))
	fmt.Println(longestCommonPrefix(input2))
}
