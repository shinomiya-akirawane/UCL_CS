//#include <stdio.h>
//int** twoDArray(int r_length, int c_length) {
//	int** array;
//	array = (int**)malloc(c_length * sizeof(int*));
//	for (int i = 0; i < r_length; i++)
//		array[i] = (int*)malloc(c_length * sizeof(int));
//	for (int i = 0; i < c_length; i++) {
//		for (int j = 0; j < r_length; j++) {
//			scanf("%d", &array[i][j]);
//		}
//	}
//	return array;
//}
//int main() {
//	int** array;
//	int r_length;
//	int c_length;
//	printf("Please enter column length and row length: ");
//	scanf("%d %d", &c_length, &r_length);
//	array = twoDArray(r_length, c_length);
//	for (int i = 0; i < c_length; i++) {
//		for (int j = 0; j < r_length; j++) {
//			printf("%d ", array[i][j]);
//		}
//		printf("\n");
//	}
//	return 0;
//}