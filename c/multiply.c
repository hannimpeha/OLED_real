#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "struct.h"
double real(Complex a);
double** zeros2(int x, int y);
Complex comsum(Complex a, Complex b);
Complex commin(Complex a, Complex b);
Complex comprod(Complex a, Complex b);
Complex compabs2(Complex a);
Complex inversecom(Complex a);
Complex comxreal(Complex a, double b);
Complex compow2(Complex a);
Complex comdiv(Complex a, Complex b);
Complex** comparr2(int x, int y);
static Complex ONE = { 1, 0 };
void multiply_1(Complex** main, Complex* vec1, Complex** mat1, Complex* vec2, Complex** mat2, int x, int y, Complex** Res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			Res[i][j] = comprod(compabs2(main[i][j]), comprod(comdiv(vec1[j], vec2[j]), comdiv(mat1[i][j], mat2[i][j])));

		}
	}
	return;
}
void multiply_2(Complex** main, Complex** mat1, Complex** mat2, int x, int y, Complex** Res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			Res[i][j] = comprod(compabs2(main[i][j]), comdiv(mat1[i][j],mat2[i][j]));
		}
	}
	return;
}
void multiply_p_1(Complex* vec1, Complex** mat1, Complex** mat2, Complex** mat3, double* inpv, Complex** mat4, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] =comdiv(comdiv(comxreal(comprod(comprod(vec1[j],commin(ONE,mat1[i][j])),commin(ONE,mat2[i][j])),pow(inpv[i],3)),mat4[i][j]),commin(ONE,mat3[i][j])).A;
		}
	}
	return;
}
void multiply_p_2(Complex* vec1, Complex** mat1, Complex** mat2, Complex** mat3, double* inpv, Complex** mat4, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = comxreal(comprod(comprod(vec1[j], comsum(ONE, mat1[i][j])), comprod(comprod(comsum(ONE, mat2[i][j]), inversecom(commin(ONE, mat3[i][j]))), inversecom(mat4[i][j]))), ((double)1 - pow(inpv[i], 2)) * inpv[i]).A;
		}
	}
	return;
}
void multiply_p_3(Complex* vec1, Complex** mat1, Complex** mat2, Complex** mat3, double* inpv, Complex** mat4, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = comprod(comxreal(comprod(comprod(vec1[j], comsum(ONE, mat1[i][j])), comprod(comsum(ONE, mat2[i][j]), inversecom(commin(ONE, mat3[i][j])))), inpv[i]), inversecom(mat4[i][j])).A;
		}
	}
	return;
}
void multiply_3_1(Complex* vec1, double** mat1, Complex** mat2, double* inpv, Complex** mat3, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = 0.5 * mat1[i][j] * pow(inpv[i], 3) * comdiv(comprod(vec1[j], mat2[i][j]), mat3[i][j]).A;
		}
	}
	return;
}
void multiply_3_2(Complex* vec1, double** mat1, Complex** mat2, double* inpv, Complex** mat3, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = 0.5 * inpv[i] * ((double)1 - pow(inpv[i], 2)) * mat1[i][j] * comdiv(comprod(vec1[j], mat2[i][j]), mat3[i][j]).A;
		}
	}
	return;
}

void multiply_3_3(Complex* vec1, double** mat1, Complex** mat2, double* inpv, Complex** mat3, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = 0.5 * inpv[i] * mat1[i][j] * comdiv(comprod(vec1[j], mat2[i][j]), mat3[i][j]).A;
		}
	}
	return;
}
void multiply_4_1(double** mat1, Complex* vec1, double weight, int x, int y, double** res)
{	//	������ ���Ǹ� ���� w_lgth�� ���� �ǵ��� ��ȯ
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[j][i] = comxreal(vec1[j], weight * mat1[i][j]).A;
		}
	}
	return;
}
void multiply_4_2(double** mat1, double*** spec, int no_EML, double weight, int x, int y, double** res)
{	//	������ ���Ǹ� ���� w_lgth�� ���� �ǵ��� ��ȯ
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[j][i] = weight * spec[j][1][no_EML] * mat1[j][i];	//	�޴� ���	����
		}
	}
	return;
}
void multiply_5_1_1(Complex* vec1, double** mat1, Complex** mat2, Complex** inpv, Complex** mat3, Complex* vec2, Complex** mat4, Complex* vec3, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = 0.5 * mat1[i][j] * comprod(comprod(comprod(vec1[j], mat2[i][j]), comdiv(compow2(inpv[j][i]), mat3[i][j])), comdiv(comprod(vec2[j], mat4[i][j]), vec3[j])).A;
		}
	}
	return;
}
void multiply_5_1_2(Complex* vec1, double** mat1, Complex** mat2, Complex** inpv, Complex** mat3, Complex* vec2, Complex** mat4, Complex* vec3, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = 0.5 * mat1[i][j] * comprod(comprod(comprod(vec1[j], mat2[i][j]), comdiv(commin(ONE, compow2(inpv[j][i])), mat3[i][j])), comdiv(comprod(vec2[j], mat4[i][j]), vec3[j])).A;
		}
	}
	return;
}
void multiply_5_1_3(Complex* vec1, double** mat1, Complex** mat2, Complex** mat3, Complex* vec2, Complex** mat4, Complex* vec3, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = 0.5 * mat1[i][j] * comprod(comdiv(comprod(vec1[j], mat2[i][j]), mat3[i][j]), comdiv(comprod(vec2[j], mat4[i][j]), vec3[j])).A;
		}
	}
	return;
}
void multiply_5_2(double** mat1, Complex** mat2, Complex* vec1, Complex** mat3, Complex* vec2, Complex** mat4, int x, int y, double** res)
{
	int i, j;
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			res[i][j] = mat1[i][j] * comdiv(comprod(comprod(mat2[i][j], vec1[j]), comdiv(mat3[i][j], vec2[j])), mat4[i][j]).A;
		}
	}
	return;
}
