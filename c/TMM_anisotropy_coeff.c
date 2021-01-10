#include "struct.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#define PI 3.141592
void free2c(Complex * *a);
void free3c(Complex*** a);
Complex comsum(Complex a, Complex b);
Complex comprod(Complex a, Complex b);
Complex comsqrt(Complex a);
Complex comsqrtsimple(Complex a);
Complex commin(Complex a, Complex b);
Complex inversecom(Complex a);
Complex comxreal(Complex a, double b);
Complex*** comparr3(int x, int y, int z);
Complex*** comparr3_0(int x, int y, int z);
Complex** comparr2(int x, int y);
Complex** comparr2_0(int x, int y);
Complex** matxmat(Complex(*a)[2], Complex(*b)[2]);
double** zeros2(int x, int y);
double*** zeros3(int x, int y, int z);
double*** zeros3_0(int x, int y, int z);
Complex*** TMM_anisotropy_coeffs(double**** index, int no_EML, double** thick, double* inplane_vector, int ipv, int l_length, double* wavelength, int wl)
{
	//	Matrix에서 0인값을 지우고 4 x 2꼴로 바꿈
	//	input & output
	//	index : l*5*w matrix, refractive index
	//	thick : l vector, thickness of the layer
	//	inplane_vector : v vector
	//	wavelength : w vector
	//	l_length : scalar, the numbere of layer

	//	output 4*v*w matrix

	int i, j, k, l, m;
	Complex temp;
	Complex*** index_complex = comparr3(l_length, 2, wl);
	Complex*** L_TM = comparr3(l_length, ipv, wl);
	Complex*** L_TE = comparr3(l_length, ipv, wl);
	Complex interface_M[4][2];
	Complex phase_M[4][2];
	Complex Mat[4][2];
	Complex C;
	C.A = 1, C.B = 0;
	Complex D;
	D.A = 0, D.B = 0;

	double* n_ordi = (double*)malloc(sizeof(double) * wl);
	if (n_ordi == NULL)
		return false;
	double* n_extra = (double*)malloc(sizeof(double) * wl);
	if (n_extra == NULL)
		return false;

	Complex*** output = comparr3(4, ipv, wl);

	for (i = 0; i < wl; i++)
	{
		index_complex[0][0][i].A = index[0][1][i][no_EML];
		index_complex[0][1][i].A = index[0][3][i][no_EML];
		index_complex[0][0][i].B = (double)0;
		index_complex[0][1][i].B = (double)0;


		*(n_ordi + i) = index_complex[0][0][i].A;
		*(n_extra + i) = index_complex[0][1][i].A;

		for (j = 0; j < ipv; j++)
		{
			if ((double)1 - pow(inplane_vector[j], 2) < 0)
			{
				L_TM[0][j][i].B = sqrt(pow(inplane_vector[j], 2) - 1);
				L_TE[0][j][i].B = sqrt(pow(inplane_vector[j], 2) - 1);
				L_TM[0][j][i].A = (double)0;
				L_TE[0][j][i].A = (double)0;
			}
			else
			{
				L_TM[0][j][i].A = sqrt(1 - pow(inplane_vector[j], 2));
				L_TE[0][j][i].A = sqrt(1 - pow(inplane_vector[j], 2));
				L_TM[0][j][i].B = (double)0;
				L_TE[0][j][i].B = (double)0;
			}
		}
		for (j = 1; j < l_length; j++)
		{
			index_complex[j][0][i].A = ((double)2 / 3) * index[j][1][i][no_EML] + ((double)1 / 3) * index[j][3][i][no_EML];
			index_complex[j][0][i].B = ((double)2 / 3) * index[j][2][i][no_EML] + ((double)1 / 3) * index[j][4][i][no_EML];
			index_complex[j][1][i].A = index_complex[j][0][i].A;
			index_complex[j][1][i].B = index_complex[j][0][i].B;
			for (k = 0; k < ipv; k++)
			{
				C.A = -pow(inplane_vector[k], (double)2);
				temp = comxreal(comprod(index_complex[j][0][i], index_complex[j][0][i]), ((double)1 / pow(*(n_extra + i), (double)2)));
				L_TM[j][k][i] = comsqrt(comsum(temp, C));
				temp = comxreal(comprod(index_complex[j][0][i], index_complex[j][0][i]), ((double)1 / pow(*(n_ordi + i), (double)2)));
				L_TE[j][k][i] = comsqrt(comsum(temp, C));
			}
		}
	}
	double* k0 = (double*)malloc(sizeof(double) * wl);
	if (k0 == NULL)
		return false;
	for (i = 0; i < wl; i++)
	{
		*(k0 + i) = 2 * PI / wavelength[i];
	}
	//	calculation
	C.A = 1, C.B = 0;
	Complex*** Matrix = comparr3_0(8 * (l_length - 1),wl, 2 * ipv);
	Complex m11, m12, m21, m22, m33, m34, m43, m44;
	Complex param_TE, param_TM, phi_TM, phi_TE;
	for (i = 0; i < wl; i++)
	{
		for (j = 0; j < ipv; j++)
		{
			for (k = 1; k < l_length; k++)
			{
				//	interface matrix
				m11 = comsum(L_TE[k - 1][j][i], L_TE[k][j][i]);
				m12 = commin(L_TE[k - 1][j][i], L_TE[k][j][i]);
				m21 = commin(L_TE[k - 1][j][i], L_TE[k][j][i]);
				m22 = comsum(L_TE[k - 1][j][i], L_TE[k][j][i]);

				m33 = comsum(comprod(comprod(index_complex[k - 1][0][i], index_complex[k - 1][1][i]), L_TM[k][j][i]), comprod(comprod(index_complex[k][0][i], index_complex[k][1][i]), L_TM[k - 1][j][i]));
				m34 = commin(comprod(comprod(index_complex[k - 1][0][i], index_complex[k - 1][1][i]), L_TM[k][j][i]), comprod(comprod(index_complex[k][0][i], index_complex[k][1][i]), L_TM[k - 1][j][i]));
				m43 = commin(comprod(comprod(index_complex[k - 1][0][i], index_complex[k - 1][1][i]), L_TM[k][j][i]), comprod(comprod(index_complex[k][0][i], index_complex[k][1][i]), L_TM[k - 1][j][i]));
				m44 = comsum(comprod(comprod(index_complex[k - 1][0][i], index_complex[k - 1][1][i]), L_TM[k][j][i]), comprod(comprod(index_complex[k][0][i], index_complex[k][1][i]), L_TM[k - 1][j][i]));

				param_TE = inversecom(comxreal(L_TE[k - 1][j][i], 2));
				param_TM = inversecom(comprod(comprod(comxreal(L_TM[k - 1][j][i], 2), index_complex[k][0][i]), index_complex[k - 1][0][i]));

				Matrix[8 * (k - 1)][i][2 * j] = comprod(param_TE, m11);
				Matrix[8 * (k - 1)][i][2 * j + 1] = comprod(param_TE, m12);
				Matrix[8 * (k - 1) + 1][i][2 * j] = comprod(param_TE, m21);
				Matrix[8 * (k - 1) + 1][i][2 * j + 1] = comprod(param_TE, m22);

				Matrix[8 * (k - 1) + 2][i][2 * j] = comprod(param_TM, m33);
				Matrix[8 * (k - 1) + 2][i][2 * j + 1] = comprod(param_TM, m34);
				Matrix[8 * (k - 1) + 3][i][2 * j] = comprod(param_TM, m43);
				Matrix[8 * (k - 1) + 3][i][2 * j + 1] = comprod(param_TM, m44);

				//	phase matrix
				phi_TM.A = exp(comxreal(L_TM[k][j][i], k0[i] * *(n_extra + i) * thick[k][no_EML]).B) * cos(comxreal(L_TM[k][j][i], -1 * k0[i] * *(n_extra + i) * thick[k][no_EML]).A);
				phi_TM.B = exp(comxreal(L_TM[k][j][i], k0[i] * *(n_extra + i) * thick[k][no_EML]).B) * sin(comxreal(L_TM[k][j][i], -1 * k0[i] * *(n_extra + i) * thick[k][no_EML]).A);
				phi_TE.A = exp(comxreal(L_TE[k][j][i], k0[i] * *(n_ordi + i) * thick[k][no_EML]).B) * cos(comxreal(L_TE[k][j][i], -1 * k0[i] * *(n_ordi + i) * thick[k][no_EML]).A);
				phi_TE.B = exp(comxreal(L_TE[k][j][i], k0[i] * *(n_ordi + i) * thick[k][no_EML]).B) * sin(comxreal(L_TE[k][j][i], -1 * k0[i] * *(n_ordi + i) * thick[k][no_EML]).A);

				Matrix[8 * (k - 1) + 4][i][2 * j] = phi_TE;
				Matrix[8 * (k - 1) + 5][i][2 * j + 1] = inversecom(phi_TE);
				Matrix[8 * (k - 1) + 6][i][2 * j] = phi_TM;
				Matrix[8 * (k - 1) + 7][i][2 * j + 1] = inversecom(phi_TM);
			}
		}
	}
	free(k0);
	free(n_ordi);
	free(n_extra);
	free3c(index_complex);
	free3c(L_TM);
	free3c(L_TE);

	for (i = 0; i < wl; i++)
	{
		for (j = 0; j < ipv; j++)
		{
			Mat[0][0] = Mat[1][1] = Mat[2][0] = Mat[3][1] = C;
			Mat[0][1] = Mat[1][0] = Mat[2][1] = Mat[3][0] = D;
			for (k = 1; k < l_length; k++)
			{
				for (l = 0; l < 4; l++)
				{
					for (m = 0; m < 2; m++)
					{
						interface_M[l][m] = Matrix[8 * (k - 1) + l][i][2 * j + m];
						phase_M[l][m] = Matrix[8 * (k - 1) + 4 + l][i][2 * j + m];
					}
				}
				matxmat(Mat, interface_M);
				matxmat(Mat, phase_M);
			}
			output[0][j][i] = comprod(Mat[1][0], inversecom(Mat[0][0]));	//	r_TE
			output[1][j][i] = inversecom(Mat[0][0]);	//	t_TE
			output[2][j][i] = comprod(Mat[3][0], inversecom(Mat[2][0]));	//	r_TM
			output[3][j][i] = inversecom(Mat[2][0]);	//	t_TM
		}
	}
	free3c(Matrix);
	return output;
}
Complex** TMM_anisotropy_coeffs_compinpv_w(double**** index, int no_EML, double** thick, Complex* inplane_vector, int ipv, int l_length, double wavelength, int i)	//	복소수 형태 inplane vector에 파장별 값을 출력
{
	//	input & output
	//	index : l*5*w matrix, refractive index
	//	thick : l vector, thickness of the layer
	//	inplane_vector : v vector
	//	wavelength : w vector
	//	l_length : scalar, the numbere of layer

	//	output 4*v*w matrix

	int j, k, l, m;
	Complex temp;
	Complex** index_complex = comparr2(l_length, 2);
	Complex** L_TM = comparr2(l_length, ipv);
	Complex** L_TE = comparr2(l_length, ipv);
	Complex interface_M[4][2];
	Complex phase_M[4][2];
	Complex Mat[4][2];
	Complex C;
	C.A = 1, C.B = 0;
	Complex D;
	D.A = 0, D.B = 0;

	double n_ordi;
	double n_extra;

	Complex** output = comparr2(4, ipv);

	index_complex[0][0].A = index[0][1][i][no_EML];
	index_complex[0][1].A = index[0][3][i][no_EML];
	index_complex[0][0].B = (double)0;
	index_complex[0][1].B = (double)0;

	n_ordi = index_complex[0][0].A;
	n_extra = index_complex[0][1].A;

	for (j = 0; j < ipv; j++)
	{
		if ((double)1 - pow(inplane_vector[j].A, 2) < 0)
		{
			L_TM[0][j].B = sqrt(pow(inplane_vector[j].A, 2) - 1);
			L_TE[0][j].B = sqrt(pow(inplane_vector[j].A, 2) - 1);
			L_TM[0][j].A = (double)0;
			L_TE[0][j].A = (double)0;
		}
		else
		{
			L_TM[0][j].A = sqrt(1 - pow(inplane_vector[j].A, 2));
			L_TE[0][j].A = sqrt(1 - pow(inplane_vector[j].A, 2));
			L_TM[0][j].B = (double)0;
			L_TE[0][j].B = (double)0;
		}
	}
	for (j = 1; j < l_length; j++)
	{
		index_complex[j][0].A = ((double)2 / 3) * index[j][1][i][no_EML] + ((double)1 / 3) * index[j][3][i][no_EML];
		index_complex[j][0].B = ((double)2 / 3) * index[j][2][i][no_EML] + ((double)1 / 3) * index[j][4][i][no_EML];
		index_complex[j][1].A = index_complex[j][0].A;
		index_complex[j][1].B = index_complex[j][0].B;
		for (k = 0; k < ipv; k++)
		{
			C.A = -pow(inplane_vector[k].A, (double)2);
			temp = comxreal(comprod(index_complex[j][0], index_complex[j][0]), ((double)1 / pow(n_extra, (double)2)));
			L_TM[j][k] = comsqrt(comsum(temp, C));
			temp = comxreal(comprod(index_complex[j][0], index_complex[j][0]), ((double)1 / pow(n_ordi, (double)2)));
			L_TE[j][k] = comsqrt(comsum(temp, C));
		}
	}

	double k0;
	k0 = 2 * PI / wavelength;

	//	calculation
	C.A = 1, C.B = 0;
	Complex** Matrix = comparr2_0(8 * (l_length - 1), 2 * ipv);
	Complex m11, m12, m21, m22, m33, m34, m43, m44;
	Complex param_TE, param_TM, phi_TM, phi_TE;
	for (j = 0; j < ipv; j++)
	{
		for (k = 1; k < l_length; k++)
		{
			//	interface matrix
			m11 = comsum(L_TE[k - 1][j], L_TE[k][j]);
			m12 = commin(L_TE[k - 1][j], L_TE[k][j]);
			m21 = commin(L_TE[k - 1][j], L_TE[k][j]);
			m22 = comsum(L_TE[k - 1][j], L_TE[k][j]);

			m33 = comsum(comprod(comprod(index_complex[k - 1][0], index_complex[k - 1][1]), L_TM[k][j]), comprod(comprod(index_complex[k][0], index_complex[k][1]), L_TM[k - 1][j]));
			m34 = commin(comprod(comprod(index_complex[k - 1][0], index_complex[k - 1][1]), L_TM[k][j]), comprod(comprod(index_complex[k][0], index_complex[k][1]), L_TM[k - 1][j]));
			m43 = commin(comprod(comprod(index_complex[k - 1][0], index_complex[k - 1][1]), L_TM[k][j]), comprod(comprod(index_complex[k][0], index_complex[k][1]), L_TM[k - 1][j]));
			m44 = comsum(comprod(comprod(index_complex[k - 1][0], index_complex[k - 1][1]), L_TM[k][j]), comprod(comprod(index_complex[k][0], index_complex[k][1]), L_TM[k - 1][j]));

			param_TE = inversecom(comxreal(L_TE[k - 1][j], 2));
			param_TM = inversecom(comprod(comprod(comxreal(L_TM[k - 1][j], 2), index_complex[k][0]), index_complex[k - 1][0]));

			Matrix[8 * (k - 1)][2 * j] = comprod(param_TE, m11);
			Matrix[8 * (k - 1)][2 * j + 1] = comprod(param_TE, m12);
			Matrix[8 * (k - 1) + 1][2 * j] = comprod(param_TE, m21);
			Matrix[8 * (k - 1) + 1][2 * j + 1] = comprod(param_TE, m22);

			Matrix[8 * (k - 1) + 2][2 * j] = comprod(param_TM, m33);
			Matrix[8 * (k - 1) + 2][2 * j + 1] = comprod(param_TM, m34);
			Matrix[8 * (k - 1) + 3][2 * j] = comprod(param_TM, m43);
			Matrix[8 * (k - 1) + 3][2 * j + 1] = comprod(param_TM, m44);

			//	phase matrix
			phi_TM.A = exp(comxreal(L_TM[k][j], k0 * n_extra * thick[k][no_EML]).B) * cos(comxreal(L_TM[k][j], -1 * k0 * n_extra * thick[k][no_EML]).A);
			phi_TM.B = exp(comxreal(L_TM[k][j], k0 * n_extra * thick[k][no_EML]).B) * sin(comxreal(L_TM[k][j], -1 * k0 * n_extra * thick[k][no_EML]).A);
			phi_TE.A = exp(comxreal(L_TE[k][j], k0 * n_ordi * thick[k][no_EML]).B) * cos(comxreal(L_TE[k][j], -1 * k0 * n_ordi * thick[k][no_EML]).A);
			phi_TE.B = exp(comxreal(L_TE[k][j], k0 * n_ordi * thick[k][no_EML]).B) * sin(comxreal(L_TE[k][j], -1 * k0 * n_ordi * thick[k][no_EML]).A);

			Matrix[8 * (k - 1) + 4][2 * j] = phi_TE;
			Matrix[8 * (k - 1) + 5][2 * j + 1] = inversecom(phi_TE);
			Matrix[8 * (k - 1) + 6][2 * j]  = phi_TM;
			Matrix[8 * (k - 1) + 7][2 * j + 1] = inversecom(phi_TM);
		}
	}
	free2c(index_complex);
	free2c(L_TM);
	free2c(L_TE);
	for (j = 0; j < ipv; j++)
	{
		Mat[0][0] = Mat[1][1] = Mat[2][0] = Mat[3][1] = C;
		Mat[0][1] = Mat[1][0] = Mat[2][1] = Mat[3][0] = D;
		for (k = 1; k < l_length; k++)
		{
			for (l = 0; l < 4; l++)
			{
				for (m = 0; m < 2; m++)
				{
					interface_M[l][m] = Matrix[8 * (k - 1) + l][2 * j + m];
					phase_M[l][m] = Matrix[8 * (k - 1) + 4 + l][2 * j + m];
				}
			}
			matxmat(Mat, interface_M);
			matxmat(Mat, phase_M);
		}
		output[0][j] = comprod(Mat[1][0], inversecom(Mat[0][0]));	//	r_TE
		output[1][j] = inversecom(Mat[0][0]);	//	t_TE
		output[2][j] = comprod(Mat[3][0], inversecom(Mat[2][0]));	//	r_TM
		output[3][j] = inversecom(Mat[2][0]);	//	t_TM
	}


	free2c(Matrix);
	return output;
}