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

    // Complete the minimumNumber function below.
    static int minimumNumber(int n, string password) {
        int minCharacters = 0;
        if(!password.Any(char.IsUpper)){
            minCharacters++;
        }
        if(!password.Any(char.IsLower)){
            minCharacters++;
        }
        if(!password.Any(char.IsDigit)){
            minCharacters++;
        }
        if(password.IndexOfAny(new char[] { '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+' }) == -1){
            minCharacters++;
        }
        if(password.Length + minCharacters < 6){
            minCharacters += 6 - (password.Length + minCharacters);
        }
        return minCharacters;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        string password = Console.ReadLine();

        int answer = minimumNumber(n, password);

        textWriter.WriteLine(answer);

        textWriter.Flush();
        textWriter.Close();
    }
}
