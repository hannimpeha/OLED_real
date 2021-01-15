#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "struct.h"
#include <stdbool.h>
int findx(double** Z);
void free2d(double** a);
double** zeros2_0(int x, int y);
double** intp4(double** Z, double li, double lf, double ls);
double** RI_load(Save* structure_temp, double lambda_init, double lambda_final, double lambda_step, int layer_num)
//	�־��� ����ü�� �־��� Refractive Index ������ �о �԰ݿ� �´� �迭�� �ű� �� intp4�Լ��� �̿��Ͽ� ���ϴ� ���·� �����迭�� ������ϴ� �Լ�
{
	int i = 0, j;
	int w_lgth = (int)((lambda_final - lambda_init) / lambda_step)+1;
	char temp[100];
	char* temp1 = temp;
	char* temp2;
	double result;
	double** arr = zeros2_0(2000, 6);
	FILE* road = fopen(structure_temp[layer_num].file_location, "rt");
	if (road == NULL)
	{
		printf("Welcome To RI Load\n");
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
			*(*(arr + i) + j) = result;
			j++;
		}
		i++;
	}
	fclose(road);
	int a = findx(arr);
	double** index_temp_interpolated = intp4(arr, lambda_init, lambda_final, lambda_step);
	if (a == 3)
	{
		for (i = 0; i < w_lgth; i++)
		{
			index_temp_interpolated[i][3] = index_temp_interpolated[i][1];
			index_temp_interpolated[i][4] = index_temp_interpolated[i][2];
		}
	}
	free2d(arr);
	return	index_temp_interpolated;
}