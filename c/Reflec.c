#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "struct.h"
#define PI 3.141592
double* zeros(int x);
Complex realtocomp_im(double a);
Complex comprod(Complex a, Complex b);
Complex inversecom(Complex a);
Complex comxreal(Complex a, double b);
Complex tricomp(Complex a);
void Reflec(double distance, Complex** r, Complex* n_ordinary, Complex** L_1, double* inplane_vector, int inplane_vector_length, double* lambda, int lambda_length, Complex** Res)
{
	int i, j;	//	inplane_vector_length행 lambda_length열 크기를 갖는 행렬을 내뱉음
	double* k0 = zeros(lambda_length);
	for (i = 0; i < lambda_length; i++)
		* (k0 + i) = 2 * PI / lambda[i];
	for (i = 0; i < inplane_vector_length; i++)
	{
		for (j = 0; j < lambda_length; j++)
		{
			*(*(Res + i) + j) = comprod(r[i][j], tricomp(comprod(L_1[i][j], comxreal(n_ordinary[j], 2 * *(k0 + j) * distance))));
		}
	}
	free(k0);
	return;
}
void Reflec_2(double distance, Complex** r_1, Complex** r_2, Complex* n_ordinary, Complex** L_1, double* inplane_vector, int inplane_vector_length, double* lambda, int lambda_length, Complex** Res)
{
	int i, j;	//	inplane_vector_length행 lambda_length열 크기를 갖는 행렬을 내뱉음
	double* k0 = zeros(lambda_length);
	for (i = 0; i < lambda_length; i++)
		* (k0 + i) = 2 * PI / lambda[i];
	for (i = 0; i < inplane_vector_length; i++)
	{
		for (j = 0; j < lambda_length; j++)
		{
			*(*(Res + i) + j) = comprod(comprod(r_2[i][j], r_1[i][j]), tricomp(comxreal(comprod(L_1[i][j], n_ordinary[j]), 2 * *(k0+j) * distance)));
		}
	}
	free(k0);
	return;
}
void Reflec_w(double distance, Complex** r, Complex* n_ordinary, Complex** L_1, int inplane_vector_length, double lambda, int lambdanum, Complex* res)
{
	int i;
	double k0 = 2 * PI / lambda;
	for (i = 0; i < inplane_vector_length; i++)
	{
		*(res + i) = comprod(r[i][lambdanum], tricomp(comxreal(comprod(L_1[i][lambdanum], n_ordinary[lambdanum]), 2 * k0 * distance)));
	}
	return;
}
void Reflec_2_w(double distance, Complex** r_1, Complex** r_2, Complex* n_ordinary, Complex** L_1, int inplane_vector_length, double lambda, int lambdanum, Complex* res)
{
	int i;	
	double k0 = 2 * PI / lambda;
	for (i = 0; i < inplane_vector_length; i++)
	{
		*(res + i) = comprod(comprod(r_2[i][lambdanum], r_1[i][lambdanum]), tricomp(comxreal(comprod(L_1[i][lambdanum], n_ordinary[lambdanum]), 2 * k0 * distance)));
	}
	return;
}