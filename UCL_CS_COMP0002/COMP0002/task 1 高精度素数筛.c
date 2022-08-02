#include <stdio.h>
int num[105];
int flag = 0;

int mod_s(int num[105],int i) {
	int cnt;
	for (int i = 0; i <= 105; i++) {
		cnt=num[i] % i;
		cnt += num[i + 1] * 10;
	}
	return cnt;
}
int main() {
	for (int i = 0; i <= 100; i++)
		scanf("%d", &num[i]);
	printf("%d", mod_s(num[105], 3));
}
/*int main(void) {
	for (int i = 0; i <= 100; i++)
		scanf("%d", &num[i]);
	int i = 2;
	for (i = 2; i < num; i++) {
		if (mod_s(num[105],i)== 0) {
			int flag = 1;
			printf("NO!\n");
			break;
		}
	}
	if (flag == 0)
		printf("YES!\n");
	return 0;
}*/
