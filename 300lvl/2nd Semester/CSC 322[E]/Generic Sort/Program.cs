using System;
using System.Collections;
using System.Collections.Generic; 

namespace Generic_Sort
{
    class Program
    {
        static void Main(string[] args)
        {
            //demo input
            Sortable<String> randomStrings = new Sortable<String>(new List<String>{"Ore is a good boy", "Timi is a bad boy", "a", "t"});
            Sortable<int> matricNums = new Sortable<int>(new List<int>{170805034, 170805029, 170805007, 170805670});
            Sortable<double> accountBalances = new Sortable<double>(new List<double>{9500.38, 10678.90, 500003.50, 7.90, });

            Console.WriteLine("***Before Sorting***");
            foreach (var i in randomStrings.Items) {
                Console.Write("{0} ", i.ToString()); 
            }
            Console.WriteLine();

            foreach (var i in matricNums.Items) {
                Console.Write("{0} ", i.ToString()); 
            }
            Console.WriteLine();

            foreach (var i in accountBalances.Items) {
                Console.Write("{0} ", i.ToString()); 
            }
            Console.WriteLine();

            randomStrings.Sort();
            matricNums.Sort();
            accountBalances.Sort();

            Console.WriteLine("\n***After Sorting***");
            foreach (var i in randomStrings.Items) {
                Console.Write("{0} ", i.ToString()); 
            }
            Console.WriteLine();

            foreach (var i in matricNums.Items) {
                Console.Write("{0} ", i.ToString()); 
            }
            Console.WriteLine();

            foreach (var i in accountBalances.Items) {
                Console.Write("{0} ", i.ToString()); 
            }
            Console.WriteLine();
        }
    }
}
