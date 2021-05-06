package main

import (
	"fmt"
)

func maxSubArray(nums []int) int {
	currSum := nums[0]
	maxSum := currSum

	for _, value := range nums[1:] {
		currSum += value

		if currSum < value {
			currSum = value
		}

		if currSum > maxSum {
			maxSum = currSum
		}
	}

	return maxSum
}

func main() {
	input1 := []int{-2,1,-3,4,-1,2,1,-5,4}
	fmt.Println(maxSubArray(input1))
}
