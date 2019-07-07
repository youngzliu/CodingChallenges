using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    /*
     * Complete the pageCount function below.
     */
    static int pageCount(int n, int p) {
        int fromBegTurns;
        int fromEndTurns;
        if (n % 2 == 0){
            fromBegTurns = p / 2;
            fromEndTurns = (n - p + 1) / 2;
        }
        else{
            fromBegTurns = p / 2;
            fromEndTurns = (n - p) / 2;
        }
        return Math.Min(fromBegTurns, fromEndTurns);
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int p = Convert.ToInt32(Console.ReadLine());

        int result = pageCount(n, p);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
