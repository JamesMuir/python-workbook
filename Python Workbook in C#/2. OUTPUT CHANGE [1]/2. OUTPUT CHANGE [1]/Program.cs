using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2.OUTPUT_CHANGE__1_
{
    class Program
    {
        static void Main(string[] args)
        {
            int varOne = 34;
            string varTwo = "wasd";
            double varThree = 5.45;

            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine(varOne);
            Console.WriteLine(varTwo);
            Console.WriteLine(varThree);

            varOne = 43;
            varTwo = "dsaw";
            varThree = 54.5;

            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine(varOne);
            Console.WriteLine(varTwo);
            Console.WriteLine(varThree);

            Console.ForegroundColor = ConsoleColor.White;
        }
    }
}
