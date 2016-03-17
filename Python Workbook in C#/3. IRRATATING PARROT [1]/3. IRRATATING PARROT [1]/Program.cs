using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3.IRRATATING_PARROT__1_
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Please enter name: ");
                string name = Console.ReadLine();
                Console.WriteLine(String.Format("Your name is {0}.", name));

                Console.WriteLine("Please enter age: ");
                string age = Console.ReadLine();
                Console.WriteLine(String.Format("Your age is {0}.", age));

                Console.WriteLine("Please enter the correct word to brake out of the never ending loop: ");
                string question = Console.ReadLine();

                if (question == "word")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("You are a failure.");
                }
            }
        }
    }
}
