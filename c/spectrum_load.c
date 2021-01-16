#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "struct.h"
void free2d(double** a);
double** zeros2_0(int x, int y);
double** intp4(double** Z, double li, double lf, double ls);


double** spectrum_load(emil* EML, double lambda_init, double lambda_final, double lambda_step, int EML_number)
{
	int i = 0, j, col = 0;
	char temp[100];
	char* temp1 = temp;
	char* temp2;
	double result;
	double** arr = zeros2_0(500, 6);
	FILE* road = fopen(EML[EML_number].spectrum_file_location, "rt");
	if (road == NULL)
	{
		printf("Welcome To Spectrum Load\nThis May Take A While...\n");
		return false;
	}
	while (1)
	{
		j = 0;
		if (feof(road))
			break;
		temp1 = fgets(temp1, 100, road);
		temp2 = strtok(temp1, "	");
		while (temp2 != NULL)
		{
			result = atof(temp2);
			temp2 = strtok(NULL, "	");
			arr[i][j] = result;
			j++;
		}
		i++;
	}
	fclose(road);
	double** spectrum_interpolated = intp4(arr, lambda_init, lambda_final, lambda_step);
	free2d(arr);
	double spectrum_sum = 0;
	for (i = 0; i < ((int)(lambda_final - lambda_init) / lambda_step) + 1; i++)
	{
		spectrum_sum += spectrum_interpolated[i][1];
	}
	for (i = 0; i < ((int)(lambda_final - lambda_init) / lambda_step) + 1; i++)
	{
		spectrum_interpolated[i][1] = spectrum_interpolated[i][1] / spectrum_sum;
	}
	return spectrum_interpolated;
}
