//#include <stdio.h>
//int* sort(int* n, int size) {
//	int* a;
//	a = (int*)malloc(size * sizeof(int));
//	for (int i = 0; i < size; i++) {
//		*(a + i) = *(n + i);
//	}
//	for (int i = 0; i < size; i++) {
//		for (int j = 0; j < size-i-1; j++) {
//			if (a[j] > a[j+1]) {
//				int temp = 0;
//				temp = a[j];
//				a[j] = a[j+1];
//				a[j+1] = temp;
//			}
//		}
//	}
//	return a;
//}
//int main() {
//	int size;
//	int* n;
//	int* a;
//	scanf("%d", &size);
//	n = (int*)malloc(size * sizeof(int));
//	for (int i = 0; i < size; i++)
//		scanf("%d", (n + i));
//	a = sort(n, size);
//	for (int i = 0; i < size; i++)
//		printf("%d", a[i]);
//	return 0;
//}