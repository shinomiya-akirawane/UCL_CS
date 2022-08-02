//#include <stdio.h>
//char s[1005];
//int top = 0;
//char num[1005];
//void pop() {
//	top--;
//}
//
//void push(char n) {
//	top++;
//	s[top] = n;
//}
//
//char check() {
//	return s[top];
//}
//
//int palin(int a) {
//	int cnt = 1;
//	int i = 1;
//	while (a != 0) {
//		char dig = 0;
//		dig = a % 10;
//		num[cnt] = dig + 48;
//		a = a / 10;
//		cnt++;
//	}
//	while (num[i] != '/') {
//		push(num[i]);
//		i++;
//	}
//	int len = i - 1;
//	i = i - 2;
//	while (i > 0) {
//		if (check() == num[len-i]) {
//			pop();
//		}
//		i--;
//	}
//	if (top == 1)
//		printf("Palin!\n");
//	else
//		printf("No Palin!\n");
//}
//int main() {
//	int n;
//	memset(s, '/', sizeof(s));
//	memset(num, '/', sizeof(num));
//	scanf("%d", &n);
//	palin(n);
//	return 0;
//}