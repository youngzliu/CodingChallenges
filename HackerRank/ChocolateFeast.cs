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

    // Complete the chocolateFeast function below.
    static int chocolateFeast(int n, int c, int m) {
        int chocolatesEaten = 0;
        int wrappers = 0;
        chocolatesEaten += n / c;
        wrappers += n / c;
        while(wrappers >= m){
            chocolatesEaten += wrappers / m;
            wrappers = wrappers - ((wrappers / m) * m) + (wrappers / m);
        }
        return chocolatesEaten;

    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            string[] ncm = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(ncm[0]);

            int c = Convert.ToInt32(ncm[1]);

            int m = Convert.ToInt32(ncm[2]);

            int result = chocolateFeast(n, c, m);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
