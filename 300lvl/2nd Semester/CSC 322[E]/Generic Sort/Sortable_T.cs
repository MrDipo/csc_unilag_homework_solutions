using System;
using System.Collections.Generic; //IComparable, List<T> are here

namespace Generic_Sort
{
    public class Sortable<T> where T : IComparable<T>//My custom type is implementing Comaprable interface
    {
        public List<T> Items{get; private set;}

        /// <summary>
        /// Default Constructor
        /// </summary>
        public Sortable(List<T> inputList){
            Items = inputList;
        }

        /// <summary>
        /// **requires:** 1 element of type T
        /// **effects:** Adds item T to List
        /// **returns:** nothing
        /// </summary>
        public void Add(T item){
            Items.Add(item);
        }
        
        /// <summary>
        /// **requires:** 1 element of type T
        /// **effects:** Removes item T from List
        /// **returns:** nothing
        /// </summary>
        public void Remove(T item){
            Items.Remove(item);
        }
        
        /// <summary>
        /// **requires:** 2 elements of the same type T, must implement IComparable
        /// **effects:** compares 2 elements of the same type T
        /// **returns:** integer
        /// </summary>
         private int Compare(T x, T y)
        {
            return x.CompareTo(y); //IComparable defines this method behaviour
        }

        /// <summary>
        /// **requires:** nothing
        /// **effects:** sorts elements in 'Items' in ascending order, using Insertion Sort algorithm
        /// **returns:** nothing
        /// </summary>
        public void Sort() //Insertion Sort
        {
            for (int i = 0; i < Items.Count; i++)
            {
                var item = Items[i];
                var currentIndex = i;

                while (currentIndex > 0 && Compare(Items[currentIndex - 1], item) > 0)//Items  [currentIndex - 1] > item)
                {
                    Items[currentIndex] = Items [currentIndex - 1];
                    currentIndex--;
                }

                Items[currentIndex] = item;
            }
        }
    }
}