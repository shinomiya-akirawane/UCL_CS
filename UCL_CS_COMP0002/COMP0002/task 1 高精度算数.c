//#include <stdio.h>
//#include <string.h>
//char num_s1[105], num_s2[105];
//int num_1_Len, num_2_Len;
//int num_1[105], num_2[105],ans[1000],tag;
///*�߾��ӷ�*/
//void add(char num_s1[105], char num_s2[105]) {
//	num_1_Len = strlen(num_s1);
//	num_2_Len = strlen(num_s2);
//
//	//��������
//	for (int i = num_1_Len; i >= 0; i--) {
//		num_1[num_1_Len - i] = num_s1[i] - '0';
//	}
//	for (int i = num_2_Len; i >= 0; i--) {
//		num_2[num_2_Len - i] = num_s2[i] - '0';
//	}
//
//	//��λ�ӷ�
//	for (int i = 0; i <= 105; i++) {
//		ans[i] = num_1[i] + num_2[i];
//		if (ans[i] >= 10) {
//			tag = ans[i] / 10;
//			ans[i] = ans[i] % 10;
//			num_1[i + 1] += tag;
//		}
//	}
//
//	//���������
//	for (int i = 99; i >= 1; i--) {
//		if (ans[i] != 0)
//			printf("%d ", ans[i]);
//	}
//};
//
///*�߾�����*/
//void minus(char num_s1[105], char num_s2[105]) {
//	num_1_Len = strlen(num_s1);
//	num_2_Len = strlen(num_s2);
//	
//	//��������
//	for (int i = num_1_Len; i >= 0; i--) {
//		num_1[num_1_Len - i] = num_s1[i] - 48;
//	}
//	for (int i = num_2_Len; i >= 0; i--) {
//		num_2[num_2_Len - i] = num_s2[i] - 48;
//	}
//
//	for (int i = 0; i <= num_1_Len; i++)
//		printf("%d", num_1[i]);
//	for (int i = 0; i <= num_2_Len; i++)
//		printf("%d", num_2[i]);
//	//��λ����
//	for (int i = 0; i <= 105; i++) {
//		if (num_1[i] < num_2[i]) {
//			num_1[i + 1]--;
//			num_1[i] = num_1[i]+10;
//			ans[i] = num_1[i] - num_2[i];
//		}
//	}
//
//	//���������
//	for (int i = 99; i > 0; i--)
//		if(ans[i]!=0)
//		printf("%d", ans[i]);
//};
//
///*�߾��ȳ˷�*/
//void mul(char num_s1[105],char num_s2[105]) {
//	num_1_Len = strlen(num_s1);
//	num_2_Len = strlen(num_s2);
//
//	//��������
//	for (int i = num_1_Len; i >= 0; i--) {
//		num_1[num_1_Len - i] = num_s1[i] - 48;
//	}
//	for (int i = num_2_Len; i >= 0; i--) {
//		num_2[num_2_Len - i] = num_s2[i] - 48;
//	}
//	//�߾��ȳ˷�
//	for (int i = 1; i <= num_1_Len; i++) {
//		for (int j = 1; j <= num_2_Len; j++) {
//			ans[i + j - 1] += num_1[i] * num_2[j];
//			ans[i + j] += ans[i + j - 1] / 10;
//			ans[i + j - 1] %= 10;
//		}
//	}
//
//	//���������
//	for (int i = 99; i > 0; i--)
//		if (ans[i] != 0)
//			printf("%d\n", ans[i]);
//}
//int main() {
//	//��ʼ������
//	memset(num_1, 0, sizeof(num_1));
//	memset(num_2, 0, sizeof(num_2));
//	memset(num_s1, 0, sizeof(num_s1));
//	memset(num_s2, 0, sizeof(num_s2));
//	memset(ans, 0, sizeof(ans));
//
//	//�������
//	scanf_s("%s", &num_s1,sizeof(num_s1));
//	scanf_s("%s", &num_s2,sizeof(num_s2));
//
//	mul(num_s1, num_s2);
//
//	return 0;
//};
