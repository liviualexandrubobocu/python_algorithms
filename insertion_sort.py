n = 4
A = [10, 3, 5, 4]
def insertionSort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            mid = A[j]
            A[j] = key
            A[j+1] = mid
            j -= 1
            key = A[j+1]

    return A

insertionSort(A, n);   

import unittest;

class TestInsertionSort(unittest.TestCase):
    
    def test_insertionSort(self):
        self.assertEqual(insertionSort([10, 3, 4, 5], 4), [3,4,5,10])
        self.assertEqual(insertionSort([40, 2, 0, -1, -1], 5), [-1, -1, 0, 2, 40])

if __name__ == '__main__':
    unittest.main()


