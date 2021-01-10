#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "struct.h"
#include <stdbool.h>
int findx(double** Z);
void free2d(double** a);
double** zeros2_0(int x, int y);
double** intp4(double** Z, double li, double lf, double ls);
double** RI_load(Save* structure, double lambda_init, double lambda_final, double lambda_step, int layer_num)
//	주어진 구조체로 주어진 Refractive Index 파일을 읽어서 규격에 맞는 배열로 옮긴 후 intp4함수를 이용하여 원하는 형태로 이차배열을 재생성하는 함수
{
	int i = 0, j;
	int w_lgth = (int)((lambda_final - lambda_init) / lambda_step)+1;
	char temp[100];
	char* temp1 = temp;
	char* temp2;
	double result;
	double** arr = zeros2_0(2000, 6);
	FILE* road = fopen(structure[layer_num].file_location, "rt");
	if (road == NULL)
	{
		printf("파일 로드 오류");
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