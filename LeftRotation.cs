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


    //Doesn't currently work for cycles
    static void Main(string[] args) {
        string[] nd = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(nd[0]);

        int d = Convert.ToInt32(nd[1]);

        int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), aTemp => Convert.ToInt32(aTemp))
        ;

        int rotations = d % a.Length;
        int toPutIn = a[0];
        int currentIndex = 0;
        for(int i = 0; i < a.Length; i++){
            currentIndex -= rotations;
            if(currentIndex < 0){
                currentIndex = a.Length + currentIndex;
            }
            int temp = a[currentIndex];
            a[currentIndex] = toPutIn;
            toPutIn = temp;
        }
        Console.Write(String.Join(" ", a));
    }
}
