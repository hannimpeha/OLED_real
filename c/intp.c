#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int findx(double** Z);
int findy(double** Z);
double** zeros2(int x, int y);
void interp1(double* x, int x_tam, double* y, double* xx, int xx_tam, double* yy);
double** intp3(double** Z, double li, double lf)
{
	int i;	//	for 구문용 i 초기화
	int a = findy(Z);	//	주어진 이차배열의 행의 갯수 측정 0을 발견하기 직전까지!
	int b = findx(Z);	//	주어진 이차배열의 열의 갯수 측정 0직전까지
	int len_new = (int)(lf - li) + 1;	//	새로 만들 배열의 행의 갯수 선언
	double** res = zeros2(len_new, 5);
	if (b == 3)
	{
		double* x = (double*)malloc(a * sizeof(double));  // 열이 3개일경우를 기본으로 함 동적할당들
		double* y1 = (double*)malloc(a * sizeof(double));
		double* y2 = (double*)malloc(a * sizeof(double));
		double* new_x = (double*)malloc(len_new * sizeof(double));
		double* new_y1 = (double*)malloc(len_new * sizeof(double));
		double* new_y2 = (double*)malloc(len_new * sizeof(double));
		if (x == NULL || y1 == NULL || y2 == NULL || new_x == NULL || new_y1 == NULL || new_y2 == NULL)
			return false;
		for (i = 0; i < a; i++)	//	입력받은 이차배열을 일차배열로 분리
		{
			x[i] = Z[i][0];
			y1[i] = Z[i][1];
			y2[i] = Z[i][2];
		}
		for (i = 0; i < len_new; i++)	//	새로운 배열에 index값 부여
		{
			new_x[i] = li + i;
		}
		interp1(x, a, y1, new_x, len_new, new_y1);	//	interpolation!
		interp1(x, a, y2, new_x, len_new, new_y2);
		for (i = 0; i < len_new; i++)
		{
			res[i][0] = new_x[i];	//	결과값에 대응
			res[i][1] = new_y1[i];
			res[i][2] = new_y2[i];
		}
		free(x), free(y1), free(y2), free(new_x), free(new_y1), free(new_y2);
	}
	if (b == 5)  // 열이 3개가 아닐경우
	{
		double* x = (double*)malloc(a * sizeof(double));  // 열이 3개일경우를 기본으로 함
		double* y1 = (double*)malloc(a * sizeof(double));
		double* y2 = (double*)malloc(a * sizeof(double));
		double* y3 = (double*)malloc(a * sizeof(double));
		double* y4 = (double*)malloc(a * sizeof(double));
		double* new_x = (double*)malloc(len_new * sizeof(double));
		double* new_y1 = (double*)malloc(len_new * sizeof(double));
		double* new_y2 = (double*)malloc(len_new * sizeof(double));
		double* new_y3 = (double*)malloc(len_new * sizeof(double));
		double* new_y4 = (double*)malloc(len_new * sizeof(double));
		if (x == NULL || y1 == NULL || y2 == NULL || y3 == NULL || y4 == NULL || new_x == NULL || new_y1 == NULL || new_y2 == NULL || new_y3 == NULL || new_y4 == NULL)
			return false;
		for (i = 0; i < a; i++)
		{
			*(x + i) = Z[i][0];
			*(y1 + i) = Z[i][1];
			*(y2 + i) = Z[i][2];

			*(y3 + i) = Z[i][3];
			*(y4 + i) = Z[i][4];
		}
		for (i = 0; i < len_new; i++)
		{
			new_x[i] = li + i;
		}
		interp1(x, a, y1, new_x, len_new, new_y1);
		interp1(x, a, y2, new_x, len_new, new_y2);
		interp1(x, a, y3, new_x, len_new, new_y3);
		interp1(x, a, y4, new_x, len_new, new_y4);
		for (i = 0; i < len_new; i++)
		{
			res[i][0] = new_x[i];
			res[i][1] = new_y1[i];
			res[i][2] = new_y2[i];
			res[i][3] = new_y3[i];
			res[i][4] = new_y4[i];
		}
		free(x), free(y1), free(y2), free(y3), free(y4), free(new_x), free(new_y1), free(new_y2), free(new_y3), free(new_y4);
	}
	return res;
}
double** intp4(double** Z, double li, double lf, double ls)
{
	int i;	//	for 구문용 i 초기화
	int a = findy(Z);	//	주어진 이차배열의 행의 갯수 측정 0을 발견하기 직전까지!
	int b = findx(Z);	//	주어진 이차배열의 열의 갯수 측정 0 전까지
	int len_new = (int)((lf - li) / ls) + 1;	//	새로 만들 배열의 행의 갯수 선언
	double** res = zeros2(len_new, 5);
	if (b == 3)
	{
		double* x = (double*)malloc(a * sizeof(double));  // 열이 3개일경우를 기본으로 함 동적할당들
		double* y1 = (double*)malloc(a * sizeof(double));
		double* y2 = (double*)malloc(a * sizeof(double));
		double* new_x = (double*)malloc(len_new * sizeof(double));
		double* new_y1 = (double*)malloc(len_new * sizeof(double));
		double* new_y2 = (double*)malloc(len_new * sizeof(double));
		if (x == NULL || y1 == NULL || y2 == NULL || new_x == NULL || new_y1 == NULL || new_y2 == NULL)
			return false;
		for (i = 0; i < a; i++)	//	입력받은 이차배열을 일차배열로 분리
		{
			x[i] = Z[i][0];
			y1[i] = Z[i][1];
			y2[i] = Z[i][2];
		}
		for (i = 0; i < len_new; i++)	//	새로운 배열에 index값 부여
		{
			new_x[i] = li + ls * i;
		}
		interp1(x, a, y1, new_x, len_new, new_y1);	//	interpolation!
		interp1(x, a, y2, new_x, len_new, new_y2);
		for (i = 0; i < len_new; i++)
		{
			res[i][0] = new_x[i];	//	결과값에 대응
			res[i][1] = new_y1[i];
			res[i][2] = new_y2[i];
		}
		free(x), free(y1), free(y2), free(new_x), free(new_y1), free(new_y2);
	}
	if (b == 5)  // 열이 3개가 아닐경우
	{
		double* x = (double*)malloc(a * sizeof(double));  // 열이 3개일경우를 기본으로 함
		double* y1 = (double*)malloc(a * sizeof(double));
		double* y2 = (double*)malloc(a * sizeof(double));
		double* y3 = (double*)malloc(a * sizeof(double));
		double* y4 = (double*)malloc(a * sizeof(double));
		double* new_x = (double*)malloc(len_new * sizeof(double));
		double* new_y1 = (double*)malloc(len_new * sizeof(double));
		double* new_y2 = (double*)malloc(len_new * sizeof(double));
		double* new_y3 = (double*)malloc(len_new * sizeof(double));
		double* new_y4 = (double*)malloc(len_new * sizeof(double));
		if (x == NULL || y1 == NULL || y2 == NULL || y3 == NULL || y4 == NULL || new_x == NULL || new_y1 == NULL || new_y2 == NULL || new_y3 == NULL || new_y4 == NULL)
			return false;
		for (i = 0; i < a; i++)
		{
			*(x + i) = Z[i][0];
			*(y1 + i) = Z[i][1];
			*(y2 + i) = Z[i][2];

			*(y3 + i) = Z[i][3];
			*(y4 + i) = Z[i][4];
		}
		for (i = 0; i < len_new; i++)
		{
			*(new_x + i) = li + ls * i;
		}
		interp1(x, a, y1, new_x, len_new, new_y1);
		interp1(x, a, y2, new_x, len_new, new_y2);
		interp1(x, a, y3, new_x, len_new, new_y3);
		interp1(x, a, y4, new_x, len_new, new_y4);
		for (i = 0; i < len_new; i++)
		{
			res[i][0] = new_x[i];
			res[i][1] = new_y1[i];
			res[i][2] = new_y2[i];
			res[i][3] = new_y3[i];
			res[i][4] = new_y4[i];
		}
		free(x), free(y1), free(y2), free(y3), free(y4), free(new_x), free(new_y1), free(new_y2), free(new_y3), free(new_y4);
	}

	return res;
}