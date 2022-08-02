//#include <stdio.h>
//char sign[15];
//char list[10000][15];
//char signs[3] = { 47,43,45 };
//int c;
//
//void buildSignList(int line,int cnt) {
//	if (cnt == 8) {
//		for (int i = 1; i <= 8; i++)
//			list[c][i] = sign[i];
//		c++;
//		return;
//	}
//	for (int i = 0; i <= 2; i++) {
//		sign[cnt++] = signs[i];
//		buildSignList(c, cnt);
//		cnt--;
//	}
//}
//int main() {
//	buildSignList(1, 0);
//	for (int i = 1; i <= 7000; i++) {
//		int num[15] = { 0,1,2,3,4,5,6,7,8,9 };
//		int ans = 0;
//		for (int j = 1; j <= 8; j++) {
//			if (list[i][j] == 47) {
//				num[j + 1] = num[j] * 10 + num[j + 1];
//				num[j] = 0;
//			}
//			if (list[i][j] == 45) {
//				num[j + 1] = -1 * num[j + 1];
//			}
//			ans += num[j];
//		}
//		if (ans == 100) {
//			for (int k = 1; k <= 8; k++)
//				printf("%d ", num[k]);
//		}
//	}
//	return 0;
//}