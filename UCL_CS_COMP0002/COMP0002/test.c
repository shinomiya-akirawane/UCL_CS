//#include <stdio.h>
//int fun(int x) {
//	return x;
//}
//
//void pointer_basic() {
//	int (*n)(int, int);//����ֵΪint��������int�Ĳ����ĺ���
//	int(*p)(int);
//	p = fun;
//	int c = (*p)(1, 2);
//	printf("%d", c);
//	int var = 20;
//	int* ip;
//	ip = &var;
//	printf("�����ĵ�ַ %p", &var);
//	printf("ip�����洢�ĵ�ַ %p", ip);
//	printf("ip������ֵ %d", *ip);
//}
//void pointer_example() {
//	int i1, i2;
//	int* p1, * p2;
//	i1 = 5;
//	p1 = &i1;
//	i2 = *p1 / 2 + 10;
//	p2 = p1;
//	printf("i1=%i,i2=%i,*p1=%i,*p2=%i\n", i1, i2, *p1, *p2);
//}
//void pointer_array() {
//	int num[10];
//	int* p = num;
//	*p = 10;
//	*(p + 1) = 20;
//	for (int i = 0; i <= 1; i++) {
//		printf("%i ", *p);
//		p++;
//	}
//}
//void pointer_dynamic_array() {
//	int* p;
//	int n = 0;
//	scanf("%d", &n);
//	p = (int*)malloc(sizeof(int) * n);
//	*p = 10;
//	*(p + 1) = 20;
//	for (int i = 0; i <= 1; i++) {
//		printf("%i ", *p);
//		p++;
//	}
//}
//int main() {
//	return 0;
//}