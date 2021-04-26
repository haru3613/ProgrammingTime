package main

import (
	"fmt"
)

func searchInsert(nums []int, target int) int {
	min := nums[0]
	max := nums[len(nums)-1]
	if target <= min {
		return 0
	}
	if target >= max {
		return len(nums)
	}

	for i := 0; i <= len(nums)-2; i++ {
		currNum := nums[i]
		nextNum := nums[i+1]
		if currNum == target {
			return i
		}
		if nextNum == target {
			return i + 1
		}

		if currNum < target && nextNum > target {
			return i + 1
		}
	}
	return -1
}

func main() {
	n1 := []int{1, 3, 5, 8}
	t1 := 2
	r1 := searchInsert(n1, t1)
	fmt.Println(r1)
}
