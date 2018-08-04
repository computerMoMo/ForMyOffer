#include "stdafx.h"
# include "quickSort.h"
# include <vector>
using namespace std;

int partition(vector<int> & array, int start, int end)
{
	int key = array[start];
	int low = start;
	int high = end;
	while (low < high)
	{
		while (low < high && array[high] >= key)
		{
			high -= 1;
		}
		array[low] = array[high];

		while (low < high && array[low] <= key)
		{
			low += 1;
		}
		array[high] = array[low];
	}
	array[low] = key;
	return low;
}

void quick_sort(vector <int> & array, int start, int end)
{
	if(start < end)
	{
		int pos = partition(array, start, end);
		quick_sort(array, start, pos - 1);
		quick_sort(array, pos + 1, end);
	}
	else
	{
		return;
	}
}