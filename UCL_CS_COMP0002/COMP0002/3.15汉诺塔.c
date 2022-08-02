//#include <stdio.h>
//int cnt;
//void move(int disk, char n, char m) {
//	cnt++;
//	printf("No.%d move: Move %d disk from %c to %c\n", 
//		cnt, disk, n, m);
//}
//void hanoi(int n,char a,char b,char c) {
//	if (n == 1)
//		move(1, a, c);
//	else {
//		hanoi(n - 1, a, c, b);
//		move(n, a, c);
//		hanoi(n - 1, b, a, c);
//	}
//}
//
//int main() {
//	char a = 'A';
//	char b = 'B';
//	char c = 'C';
//	int num;
//	printf("Please enter the number of plates: ");
//	scanf("%d", &num);
//	hanoi(num, a, b, c);
//	printf("Total move time is: %d", cnt);
//	return 0;
//}