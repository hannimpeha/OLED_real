typedef struct
{
	char name[20];
	double thick;
	char file_location[50];
}Save;
typedef struct
{
	int number;
	char spectrum_name[15];
	char spectrum_file_location[50];
	char EMZ_name[15];
	char EMZ_file_location[50];
	double QY;
	double HDR;
	double Exciton_prop;
}emil;
#ifndef COM
#define COM
typedef struct
{
	double A;	//	실수부
	double B;	//	허수부
}Complex;
#endif
