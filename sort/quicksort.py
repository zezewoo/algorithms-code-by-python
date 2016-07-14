#! /usr/bin/python


def quicksort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quicksort(A, p, q-1)
		quicksort(A, q+1, p)
	return A


def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in xrange(p, r-1):
		if A[j]<=x:
			i = i + 1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[r] = A[r],A[i+1]
	return i+1