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

    // Complete the equalizeArray function below.
    static int equalizeArray(int[] arr) {
        Dictionary<int, int> counts = new Dictionary<int, int>();
        foreach (int num in arr){
            if(counts.ContainsKey(num)){
                counts[num]++;
            }
            else{
                counts[num] = 1;
            }
        }
        int maxCount = 0;
        foreach (int num in counts.Values){
            if (num > maxCount){
                maxCount = num;
            }
        }
        return arr.Length - maxCount;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
        ;
        int result = equalizeArray(arr);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
