/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        int numNodes = 1;
        ListNode current = head;
        while(current.next != null){
            current = current.next;
            numNodes++;
        }
        int targetNode = (numNodes / 2) + 1;
        ListNode middleNode = head;
        int currentIndex = 1;
        while(currentIndex != targetNode){
            middleNode = middleNode.next;
            currentIndex++;
        }
        return middleNode;
    }
}