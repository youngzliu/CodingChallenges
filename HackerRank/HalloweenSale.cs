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

    // Complete the howManyGames function below.
    static int howManyGames(int p, int d, int m, int s) {
        int games = 0;
        int remainingMoney = s;
        int currentCost = p;
        while(remainingMoney >= currentCost){
            games++;
            remainingMoney -= currentCost;
            currentCost -= d;
            if(currentCost < m){
                currentCost = m;
            }
        }
        return games;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] pdms = Console.ReadLine().Split(' ');

        int p = Convert.ToInt32(pdms[0]);

        int d = Convert.ToInt32(pdms[1]);

        int m = Convert.ToInt32(pdms[2]);

        int s = Convert.ToInt32(pdms[3]);

        int answer = howManyGames(p, d, m, s);

        textWriter.WriteLine(answer);

        textWriter.Flush();
        textWriter.Close();
    }
}
