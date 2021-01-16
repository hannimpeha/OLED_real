#include <stdlib.h>
#include <math.h>
#include "struct.h"
#include <time.h>
#include <float.h> 
#include <stdbool.h>


double* linspace(double i, double f, int num)	//matlab linspace �Լ�
{
	int a;
	double* arr = (double*)malloc(sizeof(double) * (num));
	if (arr == NULL)
		return false;
	for (a = 0; a < num; a++)
	{
		*(arr + a) = i + (double)a * (f - i) / ((double)num - (double)1);
	}
	return arr;
}


double* arrjoin(double* a, double* b, int lenga, int lengb)	//	�ΰ��� �Ǽ� �迭�� �ϳ��� �迭�� �մ� �Լ�
{
	int i, tot = lenga + lengb;
	double* arr = (double*)malloc(sizeof(double) * tot);
	if (arr == NULL)
		return false;
	for (i = 0; i < lenga; i++)
		for (i = 0; i < lenga; i++)
			* (arr + i) = a[i];
	for (i = lenga; i < lenga + lengb; i++)
		* (arr + i) = b[i - lenga];

	return arr;
}

double* zeros(int x)
{
	double* arr = (double*)malloc(sizeof(double) * x);
	if (arr == NULL)
		return false;
	return arr;
}


double* zeros_0(int x)
{
	double* arr = (double*)calloc(x,sizeof(double));
	if (arr == NULL)
		return false;
	return arr;
}


double** zeros2(int x, int y) //		2���� �迭 �����Ҵ�
{
	int i;
	double** arr = (double**)malloc(sizeof(double*) * x);
	if (arr == NULL)
		return false;
	arr[0] = (double*)malloc(sizeof(double) * x * y);
	if (arr[0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i-1)+y;
	}
	return arr;
}


double*** zeros3(int x, int y, int z) //	3���� �迭 �����Ҵ�
{
	int i, j;
	double*** arr = (double***)malloc(sizeof(double**) * x);
	if (arr == NULL)
		return false;
	arr[0] = (double**)malloc(sizeof(double*) * x * y);
	if (arr[0] == NULL)
		return false;
	arr[0][0] = (double*)malloc(sizeof(double) * x * y * z);
	if (arr[0][0] == NULL)
		return false;	
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr + i - 1) + y;
	}
	i = 0;
	for (j = 1; j < y; j++)
	{
		*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
	}
	for (i = 1; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
		}
	}
	return arr;
}


double**** zeros4(int x, int y, int z, int w)	//	4���� �迭 �����Ҵ�
{
	int i, j, k;
	double**** arr = (double****)malloc(sizeof(double***) * x);
	if (arr == NULL)
		return false;
	arr[0] = (double***)malloc(sizeof(double**) * x * y);
	if (arr[0] == NULL)
		return false;
	arr[0][0] = (double**)malloc(sizeof(double*) * x * y * z);
	if (arr[0][0] == NULL)
		return false;
	arr[0][0][0] = (double*)malloc(sizeof(double) * x * y * z * w);
	if (arr[0][0][0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr + i - 1) + y;
	}
	i = 0;
	for (j = 1; j < y; j++)
	{
		*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
	}
	for (i = 1; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
		}
	}
	i = 0, j = 0;
	for (k = 1; k < z; k++)
	{
		*(*(*(arr + i) + j) + k) = *(*(*(arr + i) + j) + k - 1) + w;
	}
	for (j = 1; j < y; j++)
	{
		for (k = 0; k < z; k++)
		{
			*(*(*(arr + i) + j) + k) = *(*(*(arr + i) + j) + k - 1) + w;
		}
	}
	for (i = 1; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			for (k = 0; k < z; k++)
			{
				*(*(*(arr + i) + j) + k) = *(*(*(arr + i) + j) + k - 1) + w;
			}
		}
	}
	return arr;
}


double**** zeros4_1(int x)	//	4���� �� 1���� �迭 �����Ҵ�
{
	double**** arr = (double****)malloc(sizeof(double***) * x);
	if (arr == NULL)
		return false;
	return arr;
}


double**** zeros4_2(int x, int y)	//	4���� �� 1, 2 ���� �迭 �����Ҵ�
{
	int i;
	double**** arr = (double****)malloc(sizeof(double***) * x);
	if (arr == NULL)
		return false;
	arr[0] = (double***)malloc(sizeof(double**) * x * y);
	if (arr[0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i-1)+y;
	}
	return arr;
}


double** zeros2_0(int x, int y) //	2���� zeros �Լ�
{
	int i;
	double** arr = (double**)malloc(x * sizeof(double*));
	if (arr == NULL)
		return false;
	arr[0] = (double*)calloc(x * y, sizeof(double));
	if (arr[0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i-1)+y;
	}
	return arr;
}


double*** zeros3_0(int x, int y, int z) //	3���� zeros �Լ�
{
	int i, j;
	double*** arr = (double***)malloc(sizeof(double**) * x);
	if (arr == NULL)
		return false;
	arr[0] = (double**)malloc(sizeof(double*) * x * y);
	if (arr[0] == NULL)
		return false;
	arr[0][0] = (double*)calloc(x * y * z,sizeof(double));
	if (arr[0][0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i - 1) + y;
	}
	i = 0;
	for (j = 1; j < y; j++)
	{
		*(*(arr + i) + j) = *(*(arr+i)+j - 1) + z;
	}
	for (i = 1; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr+i)+j - 1) + z;
		}
	}
	return arr;
}


double**** zeros4_0(int x, int y, int z, int w)	//	4���� zeros �Լ�
{
	int i, j, k;
	double**** arr = (double****)malloc(sizeof(double***) * x);
	if (arr == NULL)
		return false;
	arr[0] = (double***)malloc(sizeof(double**) * x * y);
	if (arr[0] == NULL)
		return false;
	arr[0][0] = (double**)malloc(sizeof(double*) * x * y * z);
	if (arr[0][0] == NULL)
		return false;
	arr[0][0][0] = (double*)calloc(x * y * z * w,sizeof(double));
	if (arr[0][0][0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i - 1) + y;
	}
	i = 0;
	for (j = 1; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr+i)+j - 1) + z;
		}
	for (i = 1; i < x; i++)
		{
		for (j = 0; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr+i)+j - 1) + z;
		}		
	}
	i = 0, j = 0;
	for (k = 1; k < z; k++)
	{
		*(*(*(arr + i) + j) + k) = *(*(*(arr+i)+j)+k - 1) + w;
	}
	for(j=1;j<y;j++)
	{
		for (k = 0; k < z; k++)
		{
			*(*(*(arr + i) + j) + k) = *(*(*(arr+i)+j)+k - 1) + w;
		}
	}
	for(i=1;i<x;i++)
	{
		for (j = 0; j < y; j++)
		{
			for (k = 0; k < z; k++)
			{
				*(*(*(arr + i) + j) + k) = *(*(*(arr+i)+j)+k - 1) + w;
			}
		}
	}
	return arr;
}


int findx(double** Z)	//	���� 6��¥�� �迭�� ������ 0�� ù��°���� ���Ͽ�, �迭�� ũ�⸦ Ư���ϴ� �Լ�
{
	int a = 3;
	while (1)
	{
		if (*(*(Z + 0) + a) == 0)
			break;
		a++;
	}
	return a;
}


int findy(double** Z)	//	���� 6�� �迭���� �� ������ 0�� ù���� ���� ���Ͽ�, �迭�� ũ�⸦ Ư���ϴ� �Լ�
{
	int a = 1;
	while (1)
	{
		if (*(*(Z + a) + 0) == 0)
			break;
		a++;
	}
	return a;
}


int findNearestNeighbourIndex(double value, double* x, int len)	//	���ο� x��ǥ�鿡�� x��ǥ���� ������ ���� ū ���� ������ ���� ã�� �Լ�
{
	double dist;
	int idx;
	int i;

	idx = -1;
	dist = DBL_MAX;
	for (i = 0; i < len; i++) {
		double newDist = value - x[i];
		if (newDist >= 0 && newDist < dist) {
			dist = newDist;
			idx = i;
		}
	}
	return idx;
}


void interp1(double* x, int x_tam, double* y, double* xx, int xx_tam, double* yy) // ���� findNearestNeighbourindex �Լ����� ���� ���� ����, ���������� linear interpolation �� ������ ���ϴ� �Լ�
{
	double dx, dy, * slope, * intercept;
	int i, indiceEnVector;

	slope = (double*)calloc(x_tam, sizeof(double));
	if (slope == NULL)
		return;
	intercept = (double*)calloc(x_tam, sizeof(double));
	if (intercept == NULL)
		return;

	for (i = 0; i < x_tam; i++) {
		if (i < x_tam - 1) {
			dx = x[i + 1] - x[i];
			dy = y[i + 1] - y[i];
			slope[i] = dy / dx;
			intercept[i] = y[i] - x[i] * slope[i];
		}
		else {
			slope[i] = slope[i - 1];
			intercept[i] = intercept[i - 1];
		}
	}
	for (i = 0; i < xx_tam; i++) {
		indiceEnVector = findNearestNeighbourIndex(xx[i], x, x_tam);
		if (indiceEnVector != -1)
			yy[i] = slope[indiceEnVector] * xx[i] + intercept[indiceEnVector];
		else
			yy[i] = DBL_MAX;
	}
	free(slope);
	free(intercept);
}


Complex* comparr(int x)
{
	Complex* output = (Complex*)malloc(sizeof(Complex) * x);
	if (output == NULL)
		return false;
	return output;
}


Complex** comparr2(int x, int y)	//	���Ҽ� ǥ���� ���� 2���� ����ü�� �����Ҵ��ϴ� �Լ�
{
	int i;
	Complex** arr = (Complex**)malloc(sizeof(Complex*) * x);
	if (arr == NULL)
		return false;
	arr[0] = (Complex*)malloc(sizeof(Complex) * x * y);
	if (arr[0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i - 1) + y;
	}
	return arr;
}


Complex** comparr2_0(int x, int y)	//	���Ҽ� ǥ���� ���� 3���� ����ü�� �����Ҵ��ϴ� �Լ�
{
	int i, j;
	Complex O;
	O.A = 0, O.B = 0;
	Complex** arr = (Complex * *)malloc(sizeof(Complex*) * x);
	if (arr == NULL)
		return false;
	arr[0] = (Complex*)malloc(sizeof(Complex) * x * y);
	if (arr[0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr+i - 1) + y;
	}
	for (i = 0; i < x; i++)
		for (j = 0; j < y; j++)
			* (*(arr + i) + j) = O;
	return arr;
}


Complex*** comparr3(int x, int y, int z)	//	���Ҽ� ǥ���� ���� 3���� ����ü�� �����Ҵ��ϴ� �Լ�
{
	int i, j;
	Complex*** arr = (Complex***)malloc(sizeof(Complex**) * x);
	if (arr == NULL)
		return false;
	arr[0] = (Complex**)malloc(sizeof(Complex*) * x * y);
	if (arr[0] == NULL)
		return false;
	arr[0][0] = (Complex*)malloc(sizeof(Complex) * x * y * z);
	if (arr[0][0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr + i - 1) + y;
	}
	i = 0;
	for (j = 1; j < y; j++)
	{
		*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
	}
	for (i = 1; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
		}
	}
	return arr;
}


Complex*** comparr3_1(int x)	//	���Ҽ� ǥ���� ���� 3���� ����ü�� �����Ҵ��ϴ� �Լ�
{
	Complex*** output = (Complex * **)malloc(sizeof(Complex) * x);
	if (output == NULL)
		return false;
	return output;
}


Complex*** comparr3_0(int x, int y, int z)	//	���Ҽ� ǥ���� ���� 3���� ����ü�� �����Ҵ��ϴ� �Լ�
{
	int i, j, k;
	Complex O;
	O.A = 0, O.B = 0;
	Complex*** arr = (Complex * **)malloc(sizeof(Complex * *) * x);
	if (arr == NULL)
		return false;
	arr[0] = (Complex * *)malloc(sizeof(Complex*) * x * y);
	if (arr[0] == NULL)
		return false;
	arr[0][0] = (Complex*)malloc(sizeof(Complex) * x * y * z);
	if (arr[0][0] == NULL)
		return false;
	for (i = 1; i < x; i++)
	{
		*(arr + i) = *(arr + i - 1) + y;
	}
	i = 0;
	for (j = 1; j < y; j++)
	{
		*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
	}
	for (i = 1; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			*(*(arr + i) + j) = *(*(arr + i) + j - 1) + z;
		}
	}
	for (i = 0; i < x; i++)
		for (j = 0; j < y; j++)
			for (k = 0; k < z; k++)
				* (*(*(arr + i) + j) + k) = O;
	return arr;
}
//���Ҽ� ����


Complex comprod(Complex a, Complex b)	//	���Ҽ� ����
{
	Complex res;
	res.A = a.A * b.A - a.B * b.B;
	res.B = a.B * b.A + a.A * b.B;
	return res;
}


Complex comsum(Complex a, Complex b)	//	���Ҽ� ����
{
	Complex res;
	res.A = a.A + b.A;
	res.B = a.B + b.B;
	return res;
}


Complex commin(Complex a, Complex b)	//	���Ҽ� �E��
{
	Complex res;
	res.A = a.A - b.A;
	res.B = a.B - b.B;
	return res;
}


Complex comsqrt(Complex a)	//	���Ҽ� ������
{
	Complex res;
	res.A = sqrt((a.A + sqrt(pow(a.A, (double)2) + pow(a.B, (double)2))) / 2);
	res.B = sqrt((sqrt(pow(a.A, (double)2) + pow(a.B, (double)2)) - a.A) / 2);
	return res;
}


Complex comsqrtsimple(Complex a)	//	���Ҽ� ������
{
	Complex res;
	if (a.A > 0)
	{
		res.B = 0;
		res.A = sqrt(a.A);
	}
	else if (a.A < 0)
	{
		res.B = sqrt(-a.A);
		res.A = 0;
	}
	else
	{
		res.B = 0;
		res.A = 0;
	}
	return res;
}


double conj(Complex a)	//	�ӷ����Ҽ����� ���� ���ϴ� �Լ�
{
	double res;
	res = pow(a.A, 2) + pow(a.B, 2);
	return res;
}


Complex inversecom(Complex a)	//	���Ҽ��� ����
{
	Complex res;
	double con = conj(a);
	res.A = a.A / con;
	res.B = -a.B / con;
	return res;
}


Complex comdiv(Complex a, Complex b)
{
	Complex res;
	double con = conj(b);
	res.A = (a.A * b.A + a.B * b.B) / con;
	res.B = (a.B * b.A - a.A * b.B) / con;
	return res;
}


Complex comxreal(Complex a, double b)	//	���Ҽ��� �Ǽ���
{
	Complex res;
	res.A = a.A * b;
	res.B = a.B * b;
	return res;
}


void matxmat(Complex(*a)[2], Complex(*b)[2])	//	4x4 ���Ҽ���� ������ �Լ�
{
	int i, j, k;
	Complex res[4][2] = { 0 };
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 2; j++)
		{
			for (k = 0; k < 2; k++)
			{
				res[j][k] = comsum(res[j][k], comprod(a[j][i], b[i][k]));
			}
		}
	}
	for (i = 0; i < 2; i++)
	{
		for (j = 2; j < 4; j++)
		{
			for (k = 0; k < 2; k++)
			{
				res[j][k] = comsum(res[j][k], comprod(a[j][i], b[2+i][k]));
			}
		}
	}
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			a[i][j] = res[i][j];
		}
	}
	return;
}


Complex compow2(Complex a)	//	���Ҽ��� ������ ���ϴ� �Լ�
{
	Complex res;
	res.A = a.A * a.A - a.B * a.B;
	res.B = 2 * a.A * a.B;
	return res;
}


Complex comp(double a)	//	double������ �Ǽ����� ���Ҽ� ���·� ��ȯ
{
	Complex res;
	res.A = a;
	res.B = 0;
	return res;
}


Complex compabs2(Complex a)	//	���Ҽ��� ���밪�� ������ ���ϴ� �Լ�
{
	Complex res;
	res.A = pow(a.A, 2) + pow(a.B, 2);
	res.B = 0;
	return res;
}


Complex realtocomp_im(double a)
{
	Complex res;
	res.A = 0;
	res.B = a;
	return res;
}


Complex realtocomp_re(double a)
{
	Complex res;
	res.B = 0;
	res.A = a;
	return res;
}


Complex tricomp(Complex a)	//	exp(ik)�� cos(k)+i*sin(k)�÷� �ٲٴ� �Լ�
{
	Complex res;
	res.A = exp(-a.B) * cos(a.A);
	res.B = exp(-a.B) * sin(a.A);
	return res;
}


double real(Complex a)
{
	double res;
	res = a.A;
	return res;
}


void arrsum(double** a, double** b, int x, int y)	//	�� �����迭�� ���г��� �����ִ� �Լ�
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			a[i][j] = a[i][j] + b[i][j];
		}
	}
	return;
}


void arrsum_new(double** a, double** b, int x, int y, double** res)	//	�� �����迭�� ���г��� �����ִ� �Լ�
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = a[i][j] + b[i][j];
		}
	}
	return;
}


void arrxreal(double** a, double b, int x, int y)	//	�������迭�� �Ǽ��� ���ִ� �Լ�
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			a[i][j] = b * a[i][j];
		}
	}
	return;
}


void free2c(Complex** a)
{
	free(a[0]);
	free(a);
	return;
}


void free3c(Complex*** a)
{
	free(a[0][0]);
	free(a[0]);
	free(a);
	return;
}


void free4c(Complex**** a)
{
	free(a[0][0][0]);
	free(a[0][0]);
	free(a[0]);
	free(a);
	return;
}


void free2d(double** a)
{
	free(a[0]);
	free(a);
	return;
}


void free3d(double*** a)
{
	free(a[0][0]);
	free(a[0]);
	free(a);
	return;
}


void free4d(double**** a)
{
	free(a[0][0][0]);
	free(a[0][0]);
	free(a[0]);
	free(a);
	return;
}


int find(double* a, double b, int len)
{
	int i;
	for (i = 0; i < len; i++)
		if (b >= a[len - i - 1])
			break;
	return len - i;
}


double sum(double* a, int len)
{
	int i;
	double res = 0;
	for (i = 0; i < len; i++)
	{
		res += a[i];
	}
	return res;
}


double trapz(double* x, double* y, int start, int last)	// ��ٸ����� ����
{
	int i;
	double res = 0;
	for (i = start - 1; i < last - 1; i++)
	{
		res += (x[i + 1] - x[i]) * (y[i + 1] + y[i]) / 2;
	}
	return res;
}