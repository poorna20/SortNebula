# SortNebula
  I took the given example as an already defined array and did the coding. I can make it user friendly by asking user to enter the values too.
  Explanation to each code:
	1. Cocktail sort: It is a variation of bubble sort in which the sort traverses through the array in both directions alternatively
	   Each iteration occurs in 2 steps:
	   1) The first step loops the array from left to right and adjacent items are compared, if the key on the left is greater than the value on the right,
	      the keys are swapped. Thus, the largest key value and its corresponding value resides at the end.Incase both the keys are equal, it compares the 
	      theirs values and swaps accordingly.
	   2)Second step loops the array in the opposite direction- starting from key before the recently sorted key, and moving back to the start of the array
	     Adjacent keys are compared and swapped first, and if the keys are equal values are checked.


	2. Gnome Sort: It is based on the concept of a Garden Gnome sorting his flower pots. That is, It checks the element adjacent to the current one, if they
	   in the right order it goes one element forward, otherwise it swaps and moves one element backwards. And if there is no previous element, it goes 
	   forward; if there is no pot to its right, its done sorting.
	   Algorithm: 1) If the pointer is at the start of the array, It goes to the right element. ie, from a[0] to a[1].
		      2) If the current element is larger than or equal to the previous elememnt, then go one step right (i++)
		      3) If the current element is smaller than the previous element then swap the two and go one index backwards. (i--)
		      4) Repeat the steps until the pointer ie, i reaches the end of the array. And if end is reached, stop.

	3. Quick Sort: Based on divide and conquer algorithm, It picks an element (Last element in mine) as pivot and partitions the given array around the pivot.
	   In the partition function, Given the last element of the array as the pivot, it puts the pivot element at its right position in sorted array and arrange
	   all smaller elements than the pivot to its left and all greater elements to its right and accordingly changes its value too along with changing of keys.
	   In case, both the keys are equal the values are compared for positioning.
	   It traverses throught the array and checks each element from the start with the pivot, if the element is smaller than the pivot index gets incremented
	   by 1 (i++) and swap takes place of the pair. If the keys are equal, Values are checked and similar steps takes place. After comparing all the elements,
	   pivot is swapped with the (i+1)th element ie, it goes to its proper position in the sorted array.The functiong returns the position of the partition
	   which is then used to run the other statements of the quicksort function ie, running the partition function from the first element to the partition and 
	   the second one from the element to the end and the procedure is followed for each partition until sorted array is reached.
