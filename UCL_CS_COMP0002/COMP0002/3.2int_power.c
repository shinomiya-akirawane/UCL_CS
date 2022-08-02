//#include <stdio.h>
//int power_loop(int a, int b) {	//aµÄb´Î·½
//	for (int i = 1; i <= b/2; i++) {
//		a = a * a;
//	}
//	return a;
//}
//int power_rec(int a, int b) {
//	int temp;
//
//	if (b == 1)
//		return a;
//	else {
//
//		temp = power_rec(a, b / 2);
//
//		if (b % 2 == 0)
//			return temp * temp;
//		else
//			return temp * temp * a;
//	}
//}
//int main() {
//	int a, b;
//	scanf("%d %d", &a, &b);
//	printf("%d", power_rec(a, b));
//	return 0;
//}