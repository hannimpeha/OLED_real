typedef struct
{
	char name[20];
	double thick;
	char file_location[1024];
}Save;


typedef struct
{
	int number;
	char spectrum_name[20];
	char spectrum_file_location[1024];
	char EMZ_name[20];
	char EMZ_file_location[1024];
	double QY;
	double HDR;
	double Exciton_prop;
}emil;


#ifndef COM
#define COM
typedef struct
{
	double A;	//	real
	double B;	//	imagine
}Complex;
#endif
