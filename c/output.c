#include<stdio.h>


void output(char* directory, char* name, double output)
{
	char Fold[1024];
	sprintf(Fold, "%s\\%s.txt", directory, name);
	FILE* file = fopen(Fold, "wt");
	if (file == NULL)
	{
		printf("Error\n");
		return;
	}
	fprintf(file, "%8.6g	", output);
	fclose(file);
	return;
}


void output1(char* directory, char* name, double* output, int x)
{
	int i;
	char Fold[1024];
	sprintf(Fold, "%s\\%s.txt", directory, name);
	FILE* file = fopen(Fold, "wt");
	if (file == NULL)
	{
		printf("Error\n");
		return;
	}
	for (i = 0; i < x; i++)
	{
		fprintf(file, "%8.6g	", output[i]);
	}
	fclose(file);
	return;
}


void output2(char* directory, char* name, double** output, int x, int y)
{
	int i, j;
	char Fold[1024];
	sprintf(Fold, "%s\\%s.txt", directory, name);
	FILE* file = fopen(Fold, "wt");
	if (file == NULL)
	{
		printf("Error\n");
		return;
	}
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			fprintf(file, "%8.6g	", output[i][j]);
		}fprintf(file, "\n");
	}
	fclose(file);
	return;
}


void outputEL(char* directory, char* name, double** output, int x, int y)
{
	int i, j;
	char Fold[1024];
	sprintf(Fold, "%s\\%s.txt", directory, name);
	FILE* file = fopen(Fold, "wt");
	if (file == NULL)
	{
		printf("Error\n");
		return;
	}
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			fprintf(file, "%8.6g	", output[j][i]);
		}fprintf(file, "\n");
	}
	fclose(file);
	return;
}


void output3(char* directory, char* name, double*** output, int x, int y, int z)
{
	int i, j, k;
	char Fold[1024];
	sprintf(Fold, "%s\\%s.txt", directory, name);
	FILE* file = fopen(Fold, "wt");
	if (file == NULL)
	{
		printf("Error\n");
		return;
	}
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			for (k = 0; k < z; k++)
			{
				fprintf(file, "%8.6g	", output[i][j][k]);
			}fprintf(file, "\n");
		}fprintf(file, "\n");

	}
	fclose(file);
	return;
}


void outputDS(char* directory, char* name, double**** output, int x, int y, int z, int w)
{
	int i, j, k, l;
	char Fold[1024];
	sprintf(Fold, "%s\\%s.txt", directory, name);
	FILE* file = fopen(Fold, "wt");
	if (file == NULL)
	{
		printf("Error\n");
		return;
	}
	for (i = 0; i < x; i++)
	{
		for (j = 0; j < y; j++)
		{
			for (k = 0; k < z; k++)
			{
				for (l = 0; l < w; l++)
				{
					fprintf(file, "%8.6g	", output[k][l][j][i]);
				}fprintf(file, "\n");
			}fprintf(file, "\n");
		}fprintf(file, "\n");
	}
	fclose(file);
	return;
}
