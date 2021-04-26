package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil && l2 == nil {
		return nil
	}
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}

	currNode := &ListNode{}
	temp := currNode

	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			currNode.Next, l1 = l1, l1.Next
		} else {
			currNode.Next, l2 = l2, l2.Next
		}
		currNode = currNode.Next
	}

	if l1 != nil {
		currNode.Next = l1
	}

	if l2 != nil {
		currNode.Next = l2
	}

	return temp.Next
}

func main() {
	test1 := &ListNode{1, &ListNode{2, &ListNode{4, nil}}}
	test2 := &ListNode{1, &ListNode{3, &ListNode{4, nil}}}
	result := mergeTwoLists(test1, test2)
	fmt.Println(result, result.Next, result.Next.Next, result.Next.Next.Next, result.Next.Next.Next.Next, result.Next.Next.Next.Next.Next)
}
