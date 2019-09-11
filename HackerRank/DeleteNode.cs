using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    class SinglyLinkedList {
        public SinglyLinkedListNode head;
        public SinglyLinkedListNode tail;

        public SinglyLinkedList() {
            this.head = null;
            this.tail = null;
        }

        public void InsertNode(int nodeData) {
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

            if (this.head == null) {
                this.head = node;
            } else {
                this.tail.next = node;
            }

            this.tail = node;
        }
    }

    static void PrintSinglyLinkedList(SinglyLinkedListNode node, string sep, TextWriter textWriter) {
        while (node != null) {
            textWriter.Write(node.data);

            node = node.next;

            if (node != null) {
                textWriter.Write(sep);
            }
        }
    }

    // Complete the deleteNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode deleteNode(SinglyLinkedListNode head, int position) {
        if(head == null){
            return null;
        }
        else if(head.next == null){
            return null;
        }
        else if(position == 0){
            return head.next;
        }
        else{
            SinglyLinkedListNode prevNode = head;
            SinglyLinkedListNode afterNode = head.next.next;
            for(int i = 0; i < position - 1; i++){
                if(prevNode.next != null){
                    prevNode = prevNode.next;
                }
                if(afterNode != null){
                    afterNode = afterNode.next;
                }
            }
            prevNode.next = afterNode;
            return head;
        }
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        SinglyLinkedList llist = new SinglyLinkedList();

        int llistCount = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < llistCount; i++) {
            int llistItem = Convert.ToInt32(Console.ReadLine());
            llist.InsertNode(llistItem);
        }

        int position = Convert.ToInt32(Console.ReadLine());

        SinglyLinkedListNode llist1 = deleteNode(llist.head, position);

        PrintSinglyLinkedList(llist1, " ", textWriter);
        textWriter.WriteLine();

        textWriter.Flush();
        textWriter.Close();
    }
}
