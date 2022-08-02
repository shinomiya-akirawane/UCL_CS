//#include <stdio.h>
//int getLength(char*s) {
//	int length = 0;
//	while (1) {
//		if (*(s + length) == '\0') {
//			break;
//		}
//		length++;
//	}
//	return length;
//}
//int strend(char* s, char* t) {
//	int length_s = getLength(s);
//	int length_t = getLength(t);
//	int length = 0;
//	int temp = length_t-1;
//	for (int i = length_s-1; i >= 0; i--) {
//		if (*(s + i) == *(t + temp))
//			length++;
//		temp--;
//	}
//	if (length == length_t)
//		return 1;
//	else
//		return 0;
//}
//int main() {
//	char* s=(char*)malloc(10*sizeof(char));
//	char* t = (char*)malloc(10 * sizeof(char));
//	scanf("%s", s);
//	scanf("%s", t);
//	printf("%d",strend(s, t));
//	return 0;
//}