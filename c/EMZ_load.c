#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "struct.h"
#include <stdbool.h>
int findx(double** Z);
int findy(double** Z);
void free2d(double** a);
double** intp4(double** Z, double li, double lf, double ls);
double** zeros2_0(int x, int y);
double** EMZ_load(emil* structure, double thick_EML, int no_of_EMzone, int EML_number)
//	주어진 구조체로 주어진 EMZ file을 읽어서 2 x EMZ_length의 배열로 옮긴 후 출력한다.
{
	int i = 0, j, col, max_number, delta_number;
	char temp[100];
	char* temp1 = temp;
	char* temp2;
	double result, EMZ_sum = 0, EMZ_sum2 = 0, max, delta_location;
	double** arr = zeros2_0(105, 6);
	double** EMZ = zeros2_0(no_of_EMzone, 2);
	double delta_EMZ = (double)1 / (double)((double)no_of_EMzone - (double)1);
	FILE* road = fopen(structure[EML_number].EMZ_file_location, "rt");
	if (road == NULL)
	{
		printf("파일 로드 오류");
		return false;
	}
	while (1)
	{
		if (feof(road))
			break;
		j = 0;
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
	col = i;
	fclose(road);
	int a = findy(arr);
	double** EMZ_interpolated = intp4(arr, 0, 1, delta_EMZ);
	for (i = 0; i < no_of_EMzone; i++)
	{
		EMZ[i][0] = thick_EML * EMZ_interpolated[i][0];
	}
	for (i = 0; i < col; i++)
	{
		EMZ_sum += arr[i][1];
	}
	max = arr[0][1];
	for (i = 0; i < 101; i++)
	{
		if (arr[i][1] > max)
			max = arr[i][1];
	}
	if (EMZ_sum == max)	//	it is a delta function
	{
		j = 0;
		for (i = 0; i < a; i++)
		{
			if (arr[i][1] != EMZ_sum)
				j++;
			else
				break;
		}
		max_number = j;
		delta_location = thick_EML * arr[j][0];
		j = 0;
		for (i = 0; i < no_of_EMzone; i++)
		{
			if (delta_location != EMZ[i][0])
				j++;
			else
				break;
		}
		delta_number = j;
		EMZ[delta_number][0] = thick_EML * arr[max_number][0];
		EMZ[delta_number][1] = arr[max_number][1];
	}
	else
	{
		for (i = 0; i < no_of_EMzone; i++)
		{
			EMZ_sum2 += EMZ_interpolated[i][1];
		}
		for (i = 0; i < no_of_EMzone; i++)
		{
			EMZ[i][1] = EMZ_interpolated[i][1] / EMZ_sum2;
		}
	}
	free2d(arr);
	return	EMZ;
}