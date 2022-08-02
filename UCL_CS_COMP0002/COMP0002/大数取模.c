//#include <stdio.h>
//int num[105];
//int dig;
//
//int mod_s(int num[105], int i) {
//	int cnt=num[0];
//	for (int i = 0; i <= 105; i++) {
//		cnt = cnt % i;
//		cnt = cnt * 10 + num[i + 1];
//	}
//	return cnt;
//}
//int main() {
//	scanf("%d", &dig);
//	for (int i = 0; i <= dig; i++)
//		scanf("%d", &num[105]);
//	printf("%d", mod_s(num[100], 3));
//}
///*int main(void) {
//	for (int i = 0; i <= 100; i++)
//		scanf("%d", &num[i]);
//	int i = 2;
//	for (i = 2; i < num; i++) {
//		if (mod_s(num[105],i)== 0) {
//			int flag = 1;
//			printf("NO!\n");
//			break;
//		}
//	}
//	if (flag == 0)
//		printf("YES!\n");
//	return 0;
//}*/
