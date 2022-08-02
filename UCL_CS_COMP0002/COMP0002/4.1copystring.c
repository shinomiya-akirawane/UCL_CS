//#include <stdio.h>
//#include <string.h>
//int n;
//char* stringCopy(char* s) {
//	int length = 0;
//	while (1){
//		if (*(s + length) == '\0') {
//			break;
//		}
//		length++;
//	}
//	char* result = (char*)malloc(length * sizeof(char));
//	for (int i = 0; i < length; i++) {
//		*(result + i) = *(s + i);
//		/**result = *s;
//		result++;
//		s++;	指针位置被移动*/
//	}
//	*(result + length) = '\0';
//	return result;
//}
//
//int main() {
//	char* input = (char *) malloc(100 * sizeof(char));
//	scanf("%s", input);
//	
//	char* output = stringCopy(input);
//	printf("%s", output);
//	return 0;
//}