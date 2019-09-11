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

    // Complete the circularArrayRotation function below.
    static int[] circularArrayRotation(int[] a, int k, int[] queries) {
        int rotations = k % a.Length;
        int[] results = new int[queries.Length];
        for(int i = 0; i < queries.Length; i++){
            int targetIndex = queries[i] - rotations;
            if (targetIndex < 0){
                targetIndex = a.Length + targetIndex;
            }
            results[i] = a[targetIndex];
        }
        return results;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] nkq = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(nkq[0]);

        int k = Convert.ToInt32(nkq[1]);

        int q = Convert.ToInt32(nkq[2]);

        int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), aTemp => Convert.ToInt32(aTemp))
        ;

        int[] queries = new int [q];

        for (int i = 0; i < q; i++) {
            int queriesItem = Convert.ToInt32(Console.ReadLine());
            queries[i] = queriesItem;
        }

        int[] result = circularArrayRotation(a, k, queries);

        textWriter.WriteLine(string.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
