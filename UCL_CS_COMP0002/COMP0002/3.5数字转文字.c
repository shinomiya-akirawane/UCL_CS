//#include <stdio.h>
//void oneDigits(int num) {
//	char* name[] = { "zero","one","two","three","four",
//		"five","six","seven","eight","nine" };
//	for (int i = 0; i <= 9; i++) 
//		if (num == i)
//			printf("%s", name[i]);
//}
//void twoDigits(int num) {
//	switch (num) {
//	case 10:
//		printf("ten");
//		return;
//	case 11:
//		printf("eleven");
//		return;
//	case 12:
//		printf("twelve");
//		return;
//	case 13:
//		printf("thirdteen");
//		return;
//	case 14:
//		printf("fourteen");
//		return;
//	case 15:
//		printf("fifteen");
//		return;
//	case 16:
//		printf("sixteen");
//		return;
//	case 17:
//		printf("seventeen");
//		return;
//	case 18:
//		printf("eighteen");
//		return;
//	case 19:
//		printf("nineteen");
//		return;
//	}
//	int firstDigit = num % 10;
//	num = num / 10;
//	char* name[] = { " "," ","twenty","thirty","fourty",
//		"fifty","sixty","seventy","eighty","ninty" };
//	for (int i = 0; i <= 9; i++)
//		if (num == i)
//			printf("%s", name[i]);
//	for (int i = 0; i <= 9; i++)
//		if (firstDigit == i) {
//			printf("-");
//			oneDigits(i);
//		}
//}
//void threeDigits(int num) {
//	int firstDigit = num % 100;
//	num = num / 100;
//	oneDigits(num);
//	printf(" hundreds and ");
//	twoDigits(firstDigit);
//}
//
//int main() {
//	int num;
//	scanf("%d", &num);
//	threeDigits(num);
//	return 0;
//}