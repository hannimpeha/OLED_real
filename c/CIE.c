#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
void free2d(double** a);
double** zeros2_0(int x, int y);
double* zeros(int x);

double** CIE(double** spectrum, double* angle, int a_lgth, double* wavelength, double WL_step, int w_lgth)
{
	int i, j;
	double temp;
	double** temparr = zeros2_0(3, a_lgth);
	double** trures = zeros2_0(a_lgth, 3);
	double* color_X = zeros(w_lgth);
	double* color_Y = zeros(w_lgth);
	double* color_Z = zeros(w_lgth);
	FILE* cx = fopen("data\\color_X.dat", "rt");
	FILE* cy = fopen("data\\color_Y.dat", "rt");
	FILE* cz = fopen("data\\color_Z.dat", "rt");
	if (cx == NULL || cy == NULL || cz == NULL)
	{
		printf("Error\n");
		return false;
	}
	double color_x[902];
	for (i = 0; i < 902; i++)
	{
		fscanf(cx, "%lg", &color_x[i]);
	}
	fclose(cx);

	for (i = 0; i < w_lgth; i++)
	{
		color_X[i] = color_x[(int)WL_step * 2 * i + (int)wavelength[0] - 299];
	}
	for (i = 0; i < 902; i++)
	{
		fscanf(cy, "%lg", &color_x[i]);
	}
	fclose(cy);
	for (i = 0; i < w_lgth; i++)
	{
		color_Y[i] = color_x[(int)WL_step * 2 * i + (int)wavelength[0] - 299];
	}
	for (i = 0; i < 902; i++)
	{
		fscanf(cz, "%lg", &color_x[i]);
	}
	fclose(cz);

	for (i = 0; i < w_lgth; i++)
	{
		color_Z[i] = color_x[(int)WL_step * 2 * i + (int)wavelength[0] - 299];
	}
	for (i = 0; i < a_lgth; i++)
	{

		for (j = 0; j < w_lgth; j++)
		{
			temparr[0][i] += color_X[j] * spectrum[i][j];
			temparr[1][i] += color_Y[j] * spectrum[i][j];
			temparr[2][i] += color_Z[j] * spectrum[i][j];
		}
	}
	for (j = 0; j < a_lgth; j++)
	{
		temp = temparr[0][j] + temparr[1][j] + temparr[2][j];
		for (i = 0; i < 3; i++)
		{
			trures[j][i] = temparr[i][j] / temp;
		}
	}
	free2d(temparr);
	free(color_X); free(color_Y); free(color_Z);
	return trures;
}
