#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>
#include <regex.h>
#include <math.h>
#include <time.h>
#include <err.h>
#include "struct.h"


#define PI 3.141592
#define MAXC  1024
#define ROWS 32
#define COLS 32
#define DELIM ","


/*------------------------------------------------------------------------------------*/
/*               CIE.c //  EMZ_load.c // RI_load.c // spectrum_load.c                 */
/*------------------------------------------------------------------------------------*/
double** CIE(double** spectrum, double* angle, int a_lgth, double* wavelength,double WL_step, int w_lgth);
double** EMZ_load(emil* structure, double thick_EML, int no_of_EMzone, int EML_number);
double** RI_load(Save* structure, double lambda_init, double lambda_final, double lambda_step, int layer_num);
double** spectrum_load(emil* EML, double lambda_init, double lambda_final, double lambda_step, int EML_number);

/*------------------------------------------------------------------------------------*/
/*                                   innerfunc.c                                      */
/*------------------------------------------------------------------------------------*/
int find(double* a, double b, int len);

double sum(double* a, int len);
double trapz(double* x, double* y, int start, int last);
double* linspace(double i, double f, int num);
double* arrjoin(double* a, double* b, int lenga, int lengb);
double* zeros(int x);
double* zeros_0(int x);
double** zeros2(int x, int y);
double** zeros2_0(int x, int y);
double*** zeros3(int x, int y, int z);
double*** zeros3_0(int x, int y, int z);
double**** zeros4(int x, int y, int z, int w);
double**** zeros4_0(int x, int y, int z, int w);
double**** zeros4_1(int x);
double**** zeros4_2(int x, int y);

void arrsum(double** a, double** b, int x, int y);
void arrsum_new(double** a, double** b, int x, int y, double** res);
void free2d(double** a);
void free3d(double*** a);
void free4d(double**** a);
void free2c(Complex** a);
void free3c(Complex*** a);
void free4c(Complex**** a);

Complex comsqrt(Complex a);
Complex compow2(Complex a);
Complex comdiv(Complex a, Complex b);
Complex comprod(Complex a, Complex b);
Complex commin(Complex a, Complex b);
Complex comsum(Complex a, Complex b);
Complex comxreal(Complex a, double b);
Complex inversecom(Complex a);
Complex compabs2(Complex a);
Complex comp(double a);
Complex* comparr(int x);
Complex** comparr2(int x, int y);
Complex*** comparr3(int x, int y, int z);
Complex*** comparr3_1(int x);
static Complex ONE = { 1 , 0 };


/*------------------------------------------------------------------------------------*/
/*                                    multiply.c                                      */
/*------------------------------------------------------------------------------------*/
void multiply_1(Complex** main, Complex* vec1, Complex** mat1, Complex* vec2, Complex** mat2, int x, int y, Complex** Res);
void multiply_2(Complex** main, Complex** mat1, Complex** mat2, int x, int y, Complex** Res);
void multiply_p_1(Complex* vec1, Complex** mat1, Complex** mat2, Complex** mat3, double* inpv, Complex** mat4, int x, int y, double** res);
void multiply_p_2(Complex* vec1, Complex** mat1, Complex** mat2, Complex** mat3, double* inpv, Complex** mat4, int x, int y, double** res);
void multiply_p_3(Complex* vec1, Complex** mat1, Complex** mat2, Complex** mat3, double* inpv, Complex** mat4, int x, int y, double** res);
void multiply_3_1(Complex* vec1, double** mat1, Complex** mat2, double* inpv, Complex** mat3, int x, int y, double** res);
void multiply_3_2(Complex* vec1, double** mat1, Complex** mat2, double* inpv, Complex** mat3, int x, int y, double** res);
void multiply_3_3(Complex* vec1, double** mat1, Complex** mat2, double* inpv, Complex** mat3, int x, int y, double** res);
void multiply_4_1(double** mat1, Complex* vec1, double weight, int x, int y, double** res);
void multiply_4_2(double** mat1, double*** spec, int no_EML, double weight, int x, int y, double** res);
void multiply_5_1_1(Complex* vec1, double** mat1, Complex** mat2, Complex** inpv, Complex** mat3, Complex* vec2, Complex** mat4, Complex* vec3, int x, int y, double** res);
void multiply_5_1_2(Complex* vec1, double** mat1, Complex** mat2, Complex** inpv, Complex** mat3, Complex* vec2, Complex** mat4, Complex* vec3, int x, int y, double** res);
void multiply_5_1_3(Complex* vec1, double** mat1, Complex** mat2, Complex** mat3, Complex* vec2, Complex** mat4, Complex* vec3, int x, int y, double** res);
void multiply_5_2(double** mat1, Complex** mat2, Complex* vec1, Complex** mat3, Complex* vec2, Complex** mat4, int x, int y, double** res);


/*------------------------------------------------------------------------------------*/
/*                                    output.c                                        */
/*------------------------------------------------------------------------------------*/
void output(char* directory, char* name, double output);
void output1(char* directory, char* name, double* output, int x);
void output2(char* directory, char* name, double** output, int x, int y);
void outputEL(char* directory, char* name, double** output, int x, int y);
void output3(char* directory, char* name, double*** output, int x, int y, int z);
void outputDS(char* directory, char* name, double**** output, int x, int y, int z, int w);

/*------------------------------------------------------------------------------------*/
/*                                    Reflec.c                                        */
/*------------------------------------------------------------------------------------*/
void Reflec(double distance, Complex** r, Complex* n_ordinary, Complex** L_1, double* inplane_vector, int inplane_vector_length, double* lambda, int lambda_length, Complex** Res);
void Reflec_2(double distance, Complex** r_1, Complex** r_2, Complex* n_ordinary, Complex** L_1, double* inplane_vector, int inplane_vector_length, double* lambda, int lambda_length, Complex** Res);
void Reflec_w(double distance, Complex** r, Complex* n_ordinary, Complex** L_1, int inplane_vector_length, double lambda, int lambdanum, Complex* Res);
void Reflec_2_w(double distance, Complex** r_1, Complex** r_2, Complex* n_ordinary, Complex** L_1, int inplane_vector_length, double lambda, int lambdanum, Complex* Res);


/*------------------------------------------------------------------------------------*/
/*                              TMM_anisotropy_coeff.c                                */
/*------------------------------------------------------------------------------------*/
Complex*** TMM_anisotropy_coeffs(double**** index, int no_EML, double** thick, double* inplane_vector, int ipv, int l_length, double* wavelength, int wl);
Complex** TMM_anisotropy_coeffs_compinpv_w(double**** index, int no_EML, double** thick, Complex* inplane_vector, int ipv, int l_length, double wavelength, int i);


/*------------------------------------------------------------------------------------*/
/*                                      hannah.c                                      */
/*------------------------------------------------------------------------------------*/
void fatalx(const char *str, size_t n);
double ***alloc_3d(double **data, int levels, int rows, int cols);
void print_3d(double ***a3d, int levels, int rows, int cols);
void *reshape_2d_3d(size_t id1, size_t id2, int iar[][id2], size_t od1, size_t od2, size_t od3);
void *xrealloc_dp (void **p, size_t *n);
void *xrealloc_sp (void *p, size_t sz, size_t *n);
void *xcalloc (size_t n, size_t s);
double xstrtod (char *str, char **ep);
const char* getfield(char* line, int num);
const char *getfield2 (char *buf, size_t field);
char *my_realpath(const char *path);
char* concat(const char *s1, const char *s2);


//--------------------------------------------------------------------------------------//
//                                                                                      //
//                       OLED Optical Simulation Main Program                           //
//                                                                                      //
//--------------------------------------------------------------------------------------//
int main() {
    printf("//--------------------------------------------------------------------------------------//\n");
    printf("//                                                                                      //\n");
    printf("//                       OLED Optical Simulation Main Program                           //\n");
    printf("//                                                                                      //\n");
    printf("//--------------------------------------------------------------------------------------//\n");
    clock_t start, end;
    start = clock();
    double t_result;

    int i, j, k, l;
    //index and abbreviation
    /*
        % l: layer, w: WL, v: inplane vector, e: emisslve layer, z: emission zone,
        % a: angle, lgth: length, inpv: inplane vector
        % no: the number of ..,
        % EML: emissive layer, EMZ: emission zone, WL: WL, EXC: exciton
        % HDR: horizontal dipole ratio, QY: quantum yield, RI: refractive index
        % TM: transverse magnetic wave (p-polarization),
        % TE: transverse electric wave (s-polarization)
        % ordi: ordinari, extraordinary: extra, ext: external, sub: substrate
        % WG: waveguided, SPP: surface palsmon polaritons, ABS: absorption
        % SUBS: substrate guided, NR: non-radiative*/

    // administrator options
    printf("administrator options start\n");
    int maximum_layer_number = 16;
    int maximum_EML_number = 4;

    Save *structure = (Save *) malloc(sizeof(Save) * maximum_layer_number);//
    Save *structure_temp = (Save *) malloc(sizeof(Save) * maximum_layer_number);//
    emil *EML = (emil *) malloc(sizeof(emil) * maximum_EML_number);//
    // administrator options end
    printf("administrator options end\n\n");


    //calculation condition
    printf("calculation condition start\n");
    int v_number = 1000;       //	the number of in-plane vector
    int multiple = 25;        //	end of the in-planevector
    double *inpva = linspace(0, 1.49, v_number);
    double *inpvb = linspace(1.49 + 0.0001, multiple, 100);  //	normalized in-plane wavevector
    double *inpv = arrjoin(inpva, inpvb, v_number, 100);
    free(inpva), free(inpvb);
    int v_lgth = v_number + 100;

    char line[1024] = {0};
    char *p, *ep;
    size_t row = 0, col = 0, nrows = 0;
    size_t rmax = ROWS, cmax = COLS;

    int ind = 0;

    double WL_init, WL_final, WL_step;
    int w_lgth;

    double angle_init, angle_final, angle_step;
    int a_lgth;

    char *absolute_path;
    absolute_path = my_realpath("../resources/text_p.csv");
    FILE *file = fopen(absolute_path, "r");
    while (fgets(line, sizeof line, file)) {
        ind++;
        p = ep = line;

        char *tmp = strchr(line, '\n');
        if (tmp) *tmp = '\t';   // remove the '\n'
        tmp = strdup(line);

        if (ind==1){
            WL_init = atof(getfield2(tmp, 1));
            WL_final = atof(getfield2(tmp, 2));
            WL_step = atof(getfield2(tmp, 3));
            w_lgth = ((int) WL_final - (int) WL_init) / (int) WL_step + 1;
            printf("We are calculating WaveLength from %lf to %lf by %lf\n", WL_init, WL_final, WL_step);
        }
        if (ind==2){
            angle_init = atof(getfield2(tmp, 1));
            angle_final = atof(getfield2(tmp,2));
            angle_step = atof(getfield2(tmp, 3));
            a_lgth = ((int) angle_final - (int) angle_init) / (int) angle_step + 1;
            printf("We are calculating Angle from %lf to %lf by %lf\n", angle_init, angle_final, angle_step);
        }
    }
    //calculation condition end
    printf("calculation condition end\n\n");


    //input parameter
    printf("input parameter start\n");
    //structure inputinplane_vector_ext_TM
    char strFolderPath[] = {*my_realpath("")};
    char *External_Env = "air";

    absolute_path = my_realpath("../resources/text.csv");
    int u, nf, erc;
    int nfield = 6;
    regex_t reg;
    const char fmt[] = "([^,]*)[,\n]";
    char *regex = calloc(nfield, 1 + strlen(fmt));

    for (u = 0; u < nfield; u++) {
        strcat(regex, fmt);
    }

    int cflags = REG_EXTENDED;
    char errbuf[128];
    size_t len = sizeof(errbuf);
    const char *truncated = "";

    if ((erc = regcomp(&reg, regex, cflags)) != 0) {
        if ((len = regerror(erc, &reg, errbuf, len)) > sizeof(errbuf))
            truncated = "(truncated)";
        errx(EXIT_FAILURE, "%s %s", errbuf, truncated);
    }

    FILE *stream = fopen(absolute_path, "r");
    int no_l=0;         // the number of layers

    while (fgets(line, sizeof line, stream)) {
        strcpy(structure->name, getfield2(line, 2));
        structure->thick = atof(getfield2(line, 5));
        printf("Importing Structure Name: %s\n", structure->name);
        printf("Importing Structure Thickness: %f\n\n", structure->thick);
        no_l++;
    }
    fclose(stream);


    int no_EML = 0;    // the number of EML
    absolute_path = my_realpath("../resources/text_em.csv");
    FILE *fstream = fopen(absolute_path, "r");

    int ncol = 6;
    for (no_EML = 0; no_EML < maximum_EML_number && NULL!= fgets(line, sizeof(line), fstream); no_EML++) {
        regmatch_t matches[1 + ncol];

        EML[no_EML].number = atoi(getfield2(line,1));
        strcpy(EML[no_EML].spectrum_name, getfield2(line,3));
        EML[no_EML].Exciton_prop = atof(getfield2(line, 4));
        EML[no_EML].QY = atof(getfield2(line, 5));
        EML[no_EML].HDR = atof(getfield2(line,6));
        strcpy(EML[no_EML].EMZ_name, getfield2(line, 7));

//        if ((erc = regexec(&reg, line, 1 + nfield, matches, eflags)) != 0) {
//            if ((len = regerror(erc, &reg, errbuf, len)) > sizeof(errbuf))
//                truncated = "(truncated)";
//            errx(EXIT_FAILURE, "regex error: %s %s", errbuf, truncated);
//        }
//
//        for (nf = 1; nf < nfield + 1 && matches[nf].rm_so != -1; nf++) {
//            assert(matches[nf].rm_so <= matches[nf].rm_eo);
//            strcpy(&mat[h][nf],line + matches[nf].rm_so);
//            printf("%4d: %.*s\n",
//                   nf,
//                   (int) (matches[nf].rm_eo - matches[nf].rm_so),
//                   line + matches[nf].rm_so);
//        }
        printf("Importing EML number: %d\n", EML[no_EML].number);
        printf("Importing EML spectrum_name: %s\n", EML[no_EML].spectrum_name);
        printf("Importing EML Exciton_prop: %lf\n", EML[no_EML].Exciton_prop);
        printf("Importing EML Quantum Yield: %lf\n", EML[no_EML].QY);
        printf("Importing EML Horizontal Dipole Ratio: %lf\n", EML[no_EML].HDR);
        printf("Importing EML Emission Zone Name: %s\n", EML[no_EML].EMZ_name);
    }
    fclose(fstream);

    int no_EMZ = 31; // the number of EMZ
    //input parameter end
    printf("input parameter end\n\n");


    //Input organization and preallocations
    printf("Input organization and preallocations start\n");
    double *WL = linspace(WL_init, WL_final, ((int) WL_final - (int) WL_init) / (int) WL_step + 1);
    double *angle = linspace(angle_init, angle_final, ((int) angle_final - (int) angle_init) / (int) angle_step + 1);

    double **Temp = zeros2(w_lgth, v_lgth);
    double **index_temp;
    double **spectrum_temp;

    double ***index = zeros3(no_l + 1, 5, w_lgth);
    double ****index_up = zeros4(no_l + 1, 5, w_lgth, maximum_EML_number);
    double ****index_low = zeros4(no_l + 1, 5, w_lgth, maximum_EML_number);
    double **thick_up = zeros2(no_l + 1, maximum_EML_number);
    double **thick_low = zeros2(no_l + 1, maximum_EML_number);

    Complex *n_ordi = comparr(w_lgth);
    Complex *n_extra = comparr(w_lgth);
    Complex *n_2 = comparr(w_lgth);
    Complex *n_3 = comparr(w_lgth);

    Complex **L_1 = comparr2(v_lgth, w_lgth);
    Complex **L_2_TM = comparr2(v_lgth, w_lgth);
    Complex **L_2_TE = comparr2(v_lgth, w_lgth);
    Complex **L_3_TM = comparr2(v_lgth, w_lgth);
    Complex **L_3_TE = comparr2(v_lgth, w_lgth);

    Complex ****rt_up = (Complex ****) malloc(sizeof(Complex) * no_EML);
    if (rt_up == NULL)
        return false;
    Complex ****rt_low = (Complex ****) malloc(sizeof(Complex) * no_EML);
    if (rt_low == NULL)
        return false;

    double *thick = zeros(no_l + 1);
    int *no_up_layer = (int *) malloc(sizeof(int) * no_EML);
    if (no_up_layer == NULL)
        return false;
    int *no_low_layer = (int *) malloc(sizeof(int) * no_EML);
    if (no_low_layer == NULL)
        return false;

    double **thick_sub_ext = zeros2_0(2, 1);    //have to be a zero matrix
    int no_of_layer_sub_ext = 2;

    double ***spectrum = zeros3(w_lgth, 2, no_EML);

    Complex *P0_v = comparr(w_lgth);
    Complex *P0_h = comparr(w_lgth);
    Complex *P0 = comparr(w_lgth);

    //double s;
    //double d;

    double thick_EML;
    double ***EMZ = zeros3(no_EMZ, 2, no_EML);

    Complex **r_12_TE = comparr2(v_lgth, w_lgth); // TE = s - polarization
    Complex **t_12_TE = comparr2(v_lgth, w_lgth); // TM = p - polarization
    Complex **r_12_TM = comparr2(v_lgth, w_lgth);
    Complex **t_12_TM = comparr2(v_lgth, w_lgth);

    Complex **r_13_TE = comparr2(v_lgth, w_lgth);
    Complex **t_13_TE = comparr2(v_lgth, w_lgth);
    Complex **r_13_TM = comparr2(v_lgth, w_lgth);
    Complex **t_13_TM = comparr2(v_lgth, w_lgth);

    Complex **T_12_TM = comparr2(v_lgth, w_lgth);
    Complex **T_13_TM = comparr2(v_lgth, w_lgth);
    Complex **T_12_TE = comparr2(v_lgth, w_lgth);
    Complex **T_13_TE = comparr2(v_lgth, w_lgth);

    Complex *prefactor_v_TM = comparr(w_lgth);
    Complex *prefactor_h_TM = comparr(w_lgth);
    Complex *prefactor_h_TE = comparr(w_lgth);

    Complex **R_12_TE = comparr2(v_lgth, w_lgth);
    Complex **R_13_TE = comparr2(v_lgth, w_lgth);
    Complex **R_1213_TE = comparr2(v_lgth, w_lgth);
    Complex **R_12_TM = comparr2(v_lgth, w_lgth);
    Complex **R_13_TM = comparr2(v_lgth, w_lgth);
    Complex **R_1213_TM = comparr2(v_lgth, w_lgth);

    double **p_v_TM = zeros2(v_lgth, w_lgth);
    double **p_h_TM = zeros2(v_lgth, w_lgth);
    double **p_h_TE = zeros2(v_lgth, w_lgth);

    double **Abs_R_v_TM_12 = zeros2(v_lgth, w_lgth);
    double **Abs_R_v_TM_13 = zeros2(v_lgth, w_lgth);
    double **Abs_R_h_TM_12 = zeros2(v_lgth, w_lgth);
    double **Abs_R_h_TM_13 = zeros2(v_lgth, w_lgth);
    double **Abs_R_h_TE_12 = zeros2(v_lgth, w_lgth);
    double **Abs_R_h_TE_13 = zeros2(v_lgth, w_lgth);

    double **p_out_12_v_TM = zeros2(v_lgth, w_lgth);
    double **p_out_13_v_TM = zeros2(v_lgth, w_lgth);
    double **p_out_12_h_TM = zeros2(v_lgth, w_lgth);
    double **p_out_13_h_TM = zeros2(v_lgth, w_lgth);
    double **p_out_12_h_TE = zeros2(v_lgth, w_lgth);
    double **p_out_13_h_TE = zeros2(v_lgth, w_lgth);

    double ****p_total_TM = zeros4(no_EML, no_EMZ, w_lgth, v_lgth);
    double ****p_total_TE = zeros4(no_EML, no_EMZ, w_lgth, v_lgth);
    double ****p_total = zeros4(no_EML, no_EMZ, w_lgth, v_lgth);

    double **p_total_out_12_TM = zeros2(w_lgth, v_lgth);
    double **p_total_out_12_TE = zeros2(w_lgth, v_lgth);
    double **p_total_out_12 = zeros2(w_lgth, v_lgth);
    double **p_total_out_13_TM = zeros2(w_lgth, v_lgth);
    double **p_total_out_13_TE = zeros2(w_lgth, v_lgth);
    double **p_total_out_13 = zeros2(w_lgth, v_lgth);

    double *inpv_cut_ext_TM = zeros(w_lgth);
    double *inpv_cut_ext_TE = zeros(w_lgth);
    double *inpv_cut_sub_TM = zeros(w_lgth);
    double *inpv_cut_sub_TE = zeros(w_lgth);

    Complex **inpv_ext_TM = comparr2(w_lgth, a_lgth);
    Complex **inpv_ext_TE = comparr2(w_lgth, a_lgth);
    Complex **inpv_sub_TM = comparr2(w_lgth, a_lgth);
    Complex **inpv_sub_TE = comparr2(w_lgth, a_lgth);

    Complex **L_1_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **L_1_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **L_1_sub_TM = comparr2(a_lgth, w_lgth);
    Complex **L_1_sub_TE = comparr2(a_lgth, w_lgth);

    Complex **L_2_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **L_2_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **L_2_sub_TM = comparr2(a_lgth, w_lgth);
    Complex **L_2_sub_TE = comparr2(a_lgth, w_lgth);

    Complex **L_3_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **L_3_ext_TE = comparr2(a_lgth, w_lgth);

    Complex **inpv_sub_ext_TM = comparr2(w_lgth, a_lgth);
    Complex **inpv_sub_ext_TE = comparr2(w_lgth, a_lgth);

    double ****index_sub_ext = zeros4(2, 5, w_lgth, no_EML);

    Complex **L_1_sub_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **L_1_sub_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **L_2_sub_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **L_2_sub_ext_TE = comparr2(a_lgth, w_lgth);

    Complex ***rt_up_ext_TM = comparr3_1(w_lgth);
    Complex ***rt_up_ext_TE = comparr3_1(w_lgth);
    Complex ***rt_up_sub_TM = comparr3_1(w_lgth);
    Complex ***rt_up_sub_TE = comparr3_1(w_lgth);

    Complex ***rt_low_ext_TM = comparr3_1(w_lgth);
    Complex ***rt_low_ext_TE = comparr3_1(w_lgth);
    Complex ***rt_low_sub_TM = comparr3_1(w_lgth);
    Complex ***rt_low_sub_TE = comparr3_1(w_lgth);

    Complex ***rt_sub_ext_TM = comparr3_1(w_lgth);
    Complex ***rt_sub_ext_TE = comparr3_1(w_lgth);

    Complex **r_12_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **t_12_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **r_12_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **t_12_ext_TE = comparr2(a_lgth, w_lgth);

    Complex **r_12_sub_TM = comparr2(a_lgth, w_lgth);
    Complex **t_12_sub_TM = comparr2(a_lgth, w_lgth);
    Complex **r_12_sub_TE = comparr2(a_lgth, w_lgth);
    Complex **t_12_sub_TE = comparr2(a_lgth, w_lgth);

    Complex **r_13_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **t_13_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **r_13_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **t_13_ext_TE = comparr2(a_lgth, w_lgth);

    Complex **r_13_sub_TM = comparr2(a_lgth, w_lgth);
    Complex **r_13_sub_TE = comparr2(a_lgth, w_lgth);

    Complex **t_sub_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **t_sub_ext_TE = comparr2(a_lgth, w_lgth);

    Complex **T_12_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **T_13_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **T_12_sub_TM = comparr2(a_lgth, w_lgth);

    Complex **T_12_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **T_13_ext_TE = comparr2(a_lgth, w_lgth);
    Complex **T_12_sub_TE = comparr2(a_lgth, w_lgth);

    Complex **T_sub_ext_TM = comparr2(a_lgth, w_lgth);
    Complex **T_sub_ext_TE = comparr2(a_lgth, w_lgth);

    Complex **R_12_ext_TM = comparr2(w_lgth, a_lgth);
    Complex **R_13_ext_TM = comparr2(w_lgth, a_lgth);
    Complex **R_1213_ext_TM = comparr2(w_lgth, a_lgth);
    Complex **R_12_ext_TE = comparr2(w_lgth, a_lgth);
    Complex **R_13_ext_TE = comparr2(w_lgth, a_lgth);
    Complex **R_1213_ext_TE = comparr2(w_lgth, a_lgth);
    Complex **R_13_sub_TM = comparr2(w_lgth, a_lgth);
    Complex **R_1213_sub_TM = comparr2(w_lgth, a_lgth);
    Complex **R_13_sub_TE = comparr2(w_lgth, a_lgth);
    Complex **R_1213_sub_TE = comparr2(w_lgth, a_lgth);

    double **Abs_R_v_TM_12_ext = zeros2(a_lgth, w_lgth);
    double **Abs_R_v_TM_13_ext = zeros2(a_lgth, w_lgth);
    double **Abs_R_v_TM_12_sub = zeros2(a_lgth, w_lgth);
    double **Abs_R_h_TM_12_ext = zeros2(a_lgth, w_lgth);
    double **Abs_R_h_TM_13_ext = zeros2(a_lgth, w_lgth);
    double **Abs_R_h_TM_12_sub = zeros2(a_lgth, w_lgth);
    double **Abs_R_h_TE_12_ext = zeros2(a_lgth, w_lgth);
    double **Abs_R_h_TE_13_ext = zeros2(a_lgth, w_lgth);
    double **Abs_R_h_TE_12_sub = zeros2(a_lgth, w_lgth);

    double **p_out_12_v_ext_TM = zeros2(a_lgth, w_lgth);
    double **p_out_12_v_ext_TM_intf = zeros2(a_lgth, w_lgth);
    double **p_out_13_v_ext_TM = zeros2(a_lgth, w_lgth);
    double **p_out_12_v_sub_TM = zeros2(a_lgth, w_lgth);
    double **p_out_12_h_ext_TM = zeros2(a_lgth, w_lgth);
    double **p_out_12_h_ext_TM_intf = zeros2(a_lgth, w_lgth);
    double **p_out_13_h_ext_TM = zeros2(a_lgth, w_lgth);
    double **p_out_12_h_sub_TM = zeros2(a_lgth, w_lgth);
    double **p_out_12_h_ext_TE = zeros2(a_lgth, w_lgth);
    double **p_out_12_h_ext_TE_intf = zeros2(a_lgth, w_lgth);
    double **p_out_13_h_ext_TE = zeros2(a_lgth, w_lgth);
    double **p_out_12_h_sub_TE = zeros2(a_lgth, w_lgth);

    double ****p_out_12_ext_TM_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_ext_TE_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_ext_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_13_ext_TM_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_13_ext_TE_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_13_ext_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_sub_TM_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_sub_TE_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_sub_EMZ = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);

    double ****p_out_12_ext_TM_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_ext_TE_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_ext_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);

    double ****p_out_13_ext_TM_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_13_ext_TE_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_13_ext_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);

    double ****p_out_12_sub_TM_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_sub_TE_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);
    double ****p_out_12_sub_spec = zeros4(no_EML, no_EMZ, w_lgth, a_lgth);

    int *ext_number_TM = (int *) malloc(sizeof(int) * w_lgth);
    if (ext_number_TM == NULL)
        return false;
    int *ext_number_TE = (int *) malloc(sizeof(int) * w_lgth);
    if (ext_number_TE == NULL)
        return false;
    int *subs_number_TM = (int *) malloc(sizeof(int) * w_lgth);
    if (subs_number_TM == NULL)
        return false;
    int *subs_number_TE = (int *) malloc(sizeof(int) * w_lgth);
    if (subs_number_TE == NULL)
        return false;
    int *WG_number_TM = (int *) malloc(sizeof(int) * w_lgth);
    if (WG_number_TM == NULL)
        return false;
    int *WG_number_TE = (int *) malloc(sizeof(int) * w_lgth);
    if (WG_number_TE == NULL)
        return false;


    double **p_abs_TM_tailored = zeros2_0(w_lgth, v_lgth); // have to be a zero matrix
    double **p_abs_TE_tailored = zeros2_0(w_lgth, v_lgth); // have to be a zero matrix

    double ***P = zeros3(no_EML, no_EMZ, w_lgth);
    double ***OC = zeros3(no_EML, no_EMZ, w_lgth);
    double ***OC_back = zeros3(no_EML, no_EMZ, w_lgth);
    double ***ABS = zeros3(no_EML, no_EMZ, w_lgth);
    double ***SUBS = zeros3(no_EML, no_EMZ, w_lgth);
    double ***WG = zeros3(no_EML, no_EMZ, w_lgth);
    double ***SPPs = zeros3(no_EML, no_EMZ, w_lgth);

    double ***P_EMZ = zeros3(no_EML, no_EMZ, w_lgth);
    double ***OC_EMZ = zeros3(no_EML, no_EMZ, w_lgth);
    double ***OC_back_EMZ = zeros3(no_EML, no_EMZ, w_lgth);
    double ***ABS_EMZ = zeros3(no_EML, no_EMZ, w_lgth);
    double ***SUBS_EMZ = zeros3(no_EML, no_EMZ, w_lgth);
    double ***WG_EMZ = zeros3(no_EML, no_EMZ, w_lgth);
    double ***SPPs_EMZ = zeros3(no_EML, no_EMZ, w_lgth);

    double ***Purcell = zeros3(w_lgth, no_EML, no_EMZ);

    double **P_EML = zeros2_0(w_lgth, no_EML);
    double **OC_EML = zeros2_0(w_lgth, no_EML);
    double **OC_back_EML = zeros2_0(w_lgth, no_EML);
    double **ABS_EML = zeros2_0(w_lgth, no_EML);
    double **SUBS_EML = zeros2_0(w_lgth, no_EML);
    double **WG_EML = zeros2_0(w_lgth, no_EML);
    double **SPPs_EML = zeros2_0(w_lgth, no_EML);

    double ***q_eff = zeros3(w_lgth, no_EML, no_EMZ);
    double ***OC_eff = zeros3(w_lgth, no_EML, no_EMZ);
    double ***OC_back_eff = zeros3(w_lgth, no_EML, no_EMZ);
/*
	double** OC_EML_spec = zeros2_0(w_lgth, no_EML);		//
	double** OC_back_EML_spec = zeros2_0(w_lgth, no_EML);	//
	double** ABS_EML_spec= zeros2_0(w_lgth, no_EML);		//
	double** SUBS_EML_spec = zeros2_0(w_lgth, no_EML);		//
	double** WG_EML_spec = zeros2_0(w_lgth, no_EML);		//
	double** SPPs_EML_spec = zeros2_0(w_lgth, no_EML);		//
*/
    double ***p_out_12_ext_TM_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);    // have to be a zero matrix
    double ***p_out_12_ext_TE_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);    // have to be a zero matrix
    double ***p_out_12_ext_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);        // have to be a zero matrix

    double ***p_out_13_ext_TM_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);    // have to be a zero matrix
    double ***p_out_13_ext_TE_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);    // have to be a zero matrix
    double ***p_out_13_ext_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);        // have to be a zero matrix

    double ***p_out_12_sub_TM_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);    // have to be a zero matrix
    double ***p_out_12_sub_TE_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);    // have to be a zero matrix
    double ***p_out_12_sub_spec_EML = zeros3_0(a_lgth, w_lgth, no_EMZ);        // have to be a zero matrix

    double *OC_eff_integrated = zeros_0(no_EML);
    double *OC_back_eff_integrated = zeros_0(no_EML);
    double *ABS_eff_integrated = zeros_0(no_EML);
    double *SUBS_eff_integrated = zeros_0(no_EML);
    double *WG_eff_integrated = zeros_0(no_EML);
    double *SPPs_eff_integrated = zeros_0(no_EML);
    //double* NR_loss_integrated  = zeros_0(no_EML);

    double **p_out_12_ext_TM_final = zeros2_0(a_lgth, w_lgth);    // have to be a zero matrix
    double **p_out_12_ext_TE_final = zeros2_0(a_lgth, w_lgth);    // have to be a zero matrix
    double **p_out_12_ext_final = zeros2_0(a_lgth, w_lgth);        // have to be a zero matrix
    double **p_out_13_ext_TM_final = zeros2_0(a_lgth, w_lgth);    // have to be a zero matrix
    double **p_out_13_ext_TE_final = zeros2_0(a_lgth, w_lgth);    // have to be a zero matrix
    double **p_out_13_ext_final = zeros2_0(a_lgth, w_lgth);        // have to be a zero matrix
    double **p_out_12_sub_TM_final = zeros2_0(a_lgth, w_lgth);    // have to be a zero matrix
    double **p_out_12_sub_TE_final = zeros2_0(a_lgth, w_lgth);    // have to be a zero matrix
    double **p_out_12_sub_final = zeros2_0(a_lgth, w_lgth);        // have to be a zero matrix
    //	Input organization and preallocations end
    printf("Input organization and preallocations end\n\n");


    //	pre-processes
    printf("pre-process start\n");
    //	inserting external layers
    printf("inserting external layers start\n");
    strcpy(structure_temp[0].name, External_Env);
    structure_temp[0].thick = 0;

    for (i = 0; i < no_l; i++) {
        strcpy(structure_temp[i + 1].name, structure[i].name);
        structure_temp[i + 1].thick = structure[i].thick;
    }
    free(structure);

    int new_no_l = no_l + 1;
    //inserting external layers end
    printf("inserting external layers end\n\n");

    char* real_name;
    real_name = concat("../c/data/Refractive_index/", structure_temp[i].name);
    absolute_path = my_realpath(concat(real_name, ".ri"));

    //loading refractive index & thickness
    printf("loading refractive index & thickness start\n");
    for (i = 0; i < new_no_l; i++) {
        strcpy(structure_temp[i].file_location, absolute_path);
        index_temp = RI_load(structure_temp, WL_init, WL_final, WL_step, i);
        index = alloc_3d(index_temp, new_no_l, new_no_l, 4);
        //print_3d(index, 7, 5, 7);
//        for (k = 0; k < 12; k++) {
//            for (j = 0; j < w_lgth; j++) {
//                printf("\t%lf\n", index_temp[j][k]);
//                printf("%d", new_no_l);
//                index[i][k][j] = index_temp[j][k];
//            }
//        }
        free2d(index_temp);
        *(thick + i) = structure_temp[i].thick;
    }  // loading refractive index & thickness end
    printf("loading refractive index & thickness end\n\n");

    double *EXC = zeros(no_EML);
    double *EXC_prop = zeros(no_EML);

    //	EML processing
    printf("EML processing start\n");
    for (i = 0; i < no_EML; i++) {
        EXC[i] = EML[i].Exciton_prop;

        no_up_layer[i] = EML[i].number + 1;
        no_low_layer[i] = no_l + 1 - no_up_layer[i] + 1;

        for (j = 0; j < no_up_layer[i]; j++) {
            for (k = 0; k < 5; k++) {
                for (l = 0; l < w_lgth; l++) {
                    index_up[j][k][l][i] = index[EML[i].number + 1 - j - 1][k][l];
                }
            }
            thick_up[j][i] = thick[EML[i].number + 1 - j - 1];
        }
        //	SECTION TITLE
        //	DESCRIPTIVE TEXT
        for (j = 0; j < w_lgth; j++) {
            index_up[0][2][j][i] = 0;    //	no imaginary part
            index_up[0][4][j][i] = 0;    //	no imaginary part
        }
        for (j = 0; j < no_low_layer[i]; j++) {
            for (k = 0; k < 5; k++) {
                for (l = 0; l < w_lgth; l++) {
                    index_low[j][k][l][i] = index[EML[i].number - 1 + j + 1][k][l];
                }
            }
            thick_low[j][i] = thick[EML[i].number - 1 + j + 1];
        }
        for (j = 0; j < w_lgth; j++) {
            index_low[0][2][j][i] = 0;    //	no imaginary part
            index_low[0][4][j][i] = 0;    //	no imaginary part
        }

        real_name = concat("../c/data/spectrum/", EML[i].spectrum_name);
        absolute_path = my_realpath(concat(real_name, ".spec"));
        strcpy(EML[i].spectrum_file_location, absolute_path);
        //double **spectrum_temp = spectrum_load(EML, WL_init, WL_final, WL_step, i);
        spectrum_temp = spectrum_load(EML, WL_init, WL_final, WL_step, i);
        spectrum[i] = spectrum_temp;

//        for (j = 0; j < w_lgth; j++) {
//            //spectrum[j][0][i] = spectrum_temp[j][0];
//            //spectrum[j][1][i] = spectrum_temp[j][1];
//        }
//        free2d(spectrum_temp);

        real_name = concat("../c/data/Emission_zone/", EML[i].EMZ_name);
        absolute_path = my_realpath(concat(real_name, ".emz"));
        strcpy(EML[i].EMZ_file_location, absolute_path);
//        double **EMZ_temp = EMZ_load(EML, thick_up[0][i], no_EMZ, i);
//
//
//        // THIS IS THE TROUBLESOME PART //
//        for (j = 0; j < no_EMZ; j++) {
//            //printf("%lf\n", thick_up[1][i]);
//            //EMZ[j] = EMZ_load(EML, thick_up[0][i], no_EMZ, i);
//            //EMZ[j][0][i] = EMZ_temp[j][0];
//            EMZ[j][0][i] = EMZ_temp[j][0];
//            EMZ[j][1][i] = EMZ_temp[j][1];
//        }
//        free2d(EMZ_temp);
    }

    free3d(index);
    free(structure_temp);
    free(thick);


    double sum_EXC = 0;
    for (i = 0; i < no_EML; i++) {
        sum_EXC += EXC[i];
    }

    for (i = 0; i < no_EML; i++) {
        EXC_prop[i] = EXC[i] / sum_EXC;
    } // EML processing end
    printf("EML processing end\n\n");
    free(EXC);


    //	Transfer matrix
    printf("Transfer matrix start\n");
    for (i = 0; i < no_EML; i++) {
        //	TMM_anisotropy_coeffs : function
        //	row1: r_TE, row2: t_TE, row3: r_TM, row4: t_TM
        *(rt_up + i) = TMM_anisotropy_coeffs(index_up, i, thick_up, inpv, v_lgth, no_up_layer[i], WL, w_lgth);
        *(rt_low + i) = TMM_anisotropy_coeffs(index_low, i, thick_low, inpv, v_lgth, no_low_layer[i], WL, w_lgth);
    }
    //	Transfer matrix end
    printf("Transfer matrix end\n");
    //	pre-processes end
    printf("pre-processes end\n\n");



    /*------------------------------------------------------------------------------------*/
    /*                              Main Cacluations                                      */
    /*------------------------------------------------------------------------------------*/
    //	main calculations
    printf("/*------------------------------------------------------------------------------------*/\n");
    printf("/*                              Main Cacluations                                      */\n");
    printf("/*------------------------------------------------------------------------------------*/\n");
    double Const = 1;    //	Complex** arrsum_new(Complex** a, Complex** b, int x, int y)


    for (i = 0; i < no_EML; i++) {
        for (j = 0; j < w_lgth; j++) {
            //	common process
            printf("common process\n");
            n_ordi[j].A = index_up[0][1][j][i];
            n_ordi[j].B = index_up[0][2][j][i];
            n_extra[j].A = index_up[0][3][j][i];
            n_extra[j].B = index_up[0][4][j][i];

            //	2: low direction, 3: up direction
            n_2[j].A = index_low[no_low_layer[i] - 1][1][j][i];
            n_2[j].B = index_low[no_low_layer[i] - 1][2][j][i];
            n_3[j].A = index_up[no_up_layer[i] - 1][1][j][i];
            n_3[j].B = index_up[no_up_layer[i] - 1][2][j][i];

            thick_EML = thick_up[0][i];
            //	common process end
            printf("common process end\n\n");


            /*------------------------------------------------------------------------------------*/
            /*                                 Mode Analysis                                      */
            /*------------------------------------------------------------------------------------*/
            printf("Mode Analysis\n");
            //	for mode analysis 	reflection and transmission coeffs for eq(8-10)
            printf("reflection and transmission coeffs for eq(8-10) start\n");
            for (k = 0; k < v_lgth; k++) {
                L_1[k][j] = comsqrt(comp(1 - pow(inpv[k], 2)));
                L_2_TM[k][j] = comsqrt(
                        commin(comprod(compow2(n_2[j]), inversecom(compow2(n_extra[j]))), comp(pow(inpv[k], 2))));
                L_2_TE[k][j] = comsqrt(
                        commin(comprod(compow2(n_2[j]), inversecom(compow2(n_ordi[j]))), comp(pow(inpv[k], 2))));
                L_3_TM[k][j] = comsqrt(
                        commin(comprod(compow2(n_3[j]), inversecom(compow2(n_extra[j]))), comp(pow(inpv[k], 2))));
                L_3_TE[k][j] = comsqrt(
                        commin(comprod(compow2(n_3[j]), inversecom(compow2(n_ordi[j]))), comp(pow(inpv[k], 2))));

                r_12_TM[k][j] = rt_low[i][2][k][j];
                t_12_TM[k][j] = rt_low[i][3][k][j];
                r_12_TE[k][j] = rt_low[i][0][k][j];
                t_12_TE[k][j] = rt_low[i][1][k][j];

                r_13_TM[k][j] = rt_up[i][2][k][j];
                t_13_TM[k][j] = rt_up[i][3][k][j];
                r_13_TE[k][j] = rt_up[i][0][k][j];
                t_13_TE[k][j] = rt_up[i][1][k][j];
            }

            //	eq(1)
            P0_v[j] = comxreal(n_extra[j], Const);
            //	eq(2)
            P0_h[j] = comxreal(comprod(n_ordi[j], comprod(comsum(comxreal(compow2(n_ordi[j]), 3), compow2(n_extra[j])),
                                                          inversecom(comxreal(compow2(n_ordi[j]), 4)))), Const);
            //	eq(3)
            P0[j] = comsum(comxreal(P0_v[j], 1 - EML[i].HDR), comxreal(P0_h[j], EML[i].HDR));

        }
        //	reflection and transmission coeffs for eq (8-10) end
        printf("reflection and transmission coeffs for eq (8-10) end\n");
    }

    printf("\ttransmittance for eq (16-18) start\n");
    for (i = 0; i < no_EML; i++) {
        //	transmittance for eq (16-18)
        multiply_1(t_12_TM, n_extra, L_2_TM, n_ordi, L_1, v_lgth, w_lgth, T_12_TM);
        multiply_1(t_13_TM, n_extra, L_3_TM, n_ordi, L_1, v_lgth, w_lgth, T_13_TM);
        multiply_2(t_12_TE, L_2_TE, L_1, v_lgth, w_lgth, T_12_TE);
        multiply_2(t_13_TE, L_3_TE, L_1, v_lgth, w_lgth, T_13_TE);
        //	transmittance for eq(16-18) end
        printf("\ttransmittance for eq(16-18) end\n");
        printf("\t\tprefactors for eq (8-10, 16-18) start\n");
        for (j = 0; j < w_lgth; j++) {
            //	prefactors for eq (8-10, 16-18)
            *(prefactor_v_TM + j) = comxreal(comprod(n_extra[j], inversecom(n_ordi[j])), (double) 3 / 2);
            *(prefactor_h_TM + j) = comprod(comprod(comxreal(compow2(n_ordi[j]), 3), inversecom(
                    comsum(comxreal(compow2(n_ordi[j]), 3), compow2(n_extra[j])))),
                                            comprod(compow2(n_extra[j]), inversecom(compow2(n_ordi[j]))));
            *(prefactor_h_TE + j) = comprod(comxreal(compow2(n_ordi[j]), 3),
                                            inversecom(comsum(comxreal(compow2(n_ordi[j]), 3), compow2(n_extra[j]))));
        }
        //	prefactors for eq (8-10, 16-18) end
        printf("\t\tprefactors for eq (8-10, 16-18) end\n");
        //	mode analysis end
        printf("mode analysis end\n\n");
    }

    /*------------------------------------------------------------------------------------*/
    /*                               Far Field Emission                                   */
    /*------------------------------------------------------------------------------------*/
    printf("/*------------------------------------------------------------------------------------*/\n");
    printf("/*                               Far Field Emission                                   */\n");
    printf("/*------------------------------------------------------------------------------------*/\n");

    for (i = 0; i < no_EML; i++) {
        //	for far_field emission, re-determining the inplane wavevector and do the same process
        for (j = 0; j < w_lgth; j++) {
            for (k = 0; k < a_lgth; k++) {
                inpv_ext_TM[j][k] = comxreal(comprod(n_3[j], inversecom(n_extra[j])),
                                             sin(angle[k] * PI / (double) 180));
                inpv_ext_TE[j][k] = comxreal(comprod(n_3[j], inversecom(n_ordi[j])), sin(angle[k] * PI / (double) 180));

                inpv_sub_TM[j][k] = comxreal(comprod(n_2[j], inversecom(n_extra[j])),
                                             sin(angle[k] * PI / (double) 180));
                inpv_sub_TE[j][k] = comxreal(comprod(n_2[j], inversecom(n_ordi[j])), sin(angle[k] * PI / (double) 180));

                L_1_ext_TM[k][j] = comsqrt(commin(ONE, compow2(inpv_ext_TM[j][k])));
                L_1_ext_TE[k][j] = comsqrt(commin(ONE, compow2(inpv_ext_TE[j][k])));
                L_1_sub_TM[k][j] = comsqrt(commin(ONE, compow2(inpv_sub_TM[j][k])));
                L_1_sub_TE[k][j] = comsqrt(commin(ONE, compow2(inpv_sub_TE[j][k])));

                L_2_ext_TM[k][j] = comsqrt(
                        commin(comprod(compow2(n_2[j]), inversecom(compow2(n_extra[j]))), compow2(inpv_ext_TM[j][k])));
                L_2_ext_TE[k][j] = comsqrt(
                        commin(comprod(compow2(n_2[j]), inversecom(compow2(n_ordi[j]))), compow2(inpv_ext_TE[j][k])));
                L_2_sub_TM[k][j] = comsqrt(
                        commin(comprod(compow2(n_2[j]), inversecom(compow2(n_extra[j]))), compow2(inpv_sub_TM[j][k])));
                L_2_sub_TE[k][j] = comsqrt(
                        commin(comprod(compow2(n_2[j]), inversecom(compow2(n_ordi[j]))), compow2(inpv_sub_TE[j][k])));

                L_3_ext_TM[k][j] = comsqrt(
                        commin(comprod(compow2(n_3[j]), inversecom(compow2(n_extra[j]))), compow2(inpv_ext_TM[j][k])));
                L_3_ext_TE[k][j] = comsqrt(
                        commin(comprod(compow2(n_3[j]), inversecom(compow2(n_ordi[j]))), compow2(inpv_ext_TE[j][k])));

                for (l = 0; l < 5; l++) {
                    index_sub_ext[0][l][j][i] = index_low[no_low_layer[i] - 1][l][j][i];
                    index_sub_ext[1][l][j][i] = index_up[no_up_layer[i] - 1][l][j][i];
                }

                inpv_sub_ext_TM[j][k] = comprod(comprod(inpv_ext_TM[j][k], n_extra[j]), inversecom(n_2[j]));
                inpv_sub_ext_TE[j][k] = comprod(comprod(inpv_ext_TE[j][k], n_ordi[j]), inversecom(n_2[j]));
                L_1_sub_ext_TM[k][j] = comsqrt(commin(ONE, compow2(inpv_sub_ext_TM[j][k])));
                L_1_sub_ext_TE[k][j] = comsqrt(commin(ONE, compow2(inpv_sub_ext_TE[j][k])));

                L_2_sub_ext_TM[k][j] = comsqrt(
                        commin(comprod(compow2(n_3[j]), inversecom(compow2(n_2[j]))), compow2(inpv_sub_ext_TM[j][k])));
                L_2_sub_ext_TE[k][j] = comsqrt(
                        commin(comprod(compow2(n_3[j]), inversecom(compow2(n_2[j]))), compow2(inpv_sub_ext_TE[j][k])));
            }
            *(rt_up_ext_TM + j) = TMM_anisotropy_coeffs_compinpv_w(index_up, i, thick_up, *(inpv_ext_TM + j), a_lgth,
                                                                   no_up_layer[i], WL[j], j);
            *(rt_up_ext_TE + j) = TMM_anisotropy_coeffs_compinpv_w(index_up, i, thick_up, *(inpv_ext_TE + j), a_lgth,
                                                                   no_up_layer[i], WL[j], j);
            *(rt_up_sub_TM + j) = TMM_anisotropy_coeffs_compinpv_w(index_up, i, thick_up, *(inpv_sub_TM + j), a_lgth,
                                                                   no_up_layer[i], WL[j], j);
            *(rt_up_sub_TE + j) = TMM_anisotropy_coeffs_compinpv_w(index_up, i, thick_up, *(inpv_sub_TE + j), a_lgth,
                                                                   no_up_layer[i], WL[j], j);

            *(rt_low_ext_TM + j) = TMM_anisotropy_coeffs_compinpv_w(index_low, i, thick_low, *(inpv_ext_TM + j), a_lgth,
                                                                    no_low_layer[i], WL[j], j);
            *(rt_low_ext_TE + j) = TMM_anisotropy_coeffs_compinpv_w(index_low, i, thick_low, *(inpv_ext_TE + j), a_lgth,
                                                                    no_low_layer[i], WL[j], j);
            *(rt_low_sub_TM + j) = TMM_anisotropy_coeffs_compinpv_w(index_low, i, thick_low, *(inpv_sub_TM + j), a_lgth,
                                                                    no_low_layer[i], WL[j], j);
            *(rt_low_sub_TE + j) = TMM_anisotropy_coeffs_compinpv_w(index_low, i, thick_low, *(inpv_sub_TE + j), a_lgth,
                                                                    no_low_layer[i], WL[j], j);

            *(rt_sub_ext_TM + j) = TMM_anisotropy_coeffs_compinpv_w(index_sub_ext, i, thick_sub_ext,
                                                                    *(inpv_sub_ext_TM + j), a_lgth, no_of_layer_sub_ext,
                                                                    WL[j], j);
            *(rt_sub_ext_TE + j) = TMM_anisotropy_coeffs_compinpv_w(index_sub_ext, i, thick_sub_ext,
                                                                    *(inpv_sub_ext_TE + j), a_lgth, no_of_layer_sub_ext,
                                                                    WL[j], j);
        }   //	wavelength�� loop
    }


    /*-------------------------Reflection & Transmission Coeff----------------------------*/
    printf("/*-------------------------Reflection & Transmission Coeff----------------------------*/\n");
    for (i = 0; i < no_EML; i++) {
        //	reflection & transmission coeffs
        printf("reflection & transmission coeffs start\n");
        for (j = 0; j < w_lgth; j++) {
            for (k = 0; k < a_lgth; k++) {
                r_12_ext_TM[k][j] = rt_low_ext_TM[j][2][k];
                t_12_ext_TM[k][j] = rt_low_ext_TM[j][3][k];
                r_12_ext_TE[k][j] = rt_low_ext_TE[j][0][k];
                t_12_ext_TE[k][j] = rt_low_ext_TE[j][1][k];

                r_12_sub_TM[k][j] = rt_low_sub_TM[j][2][k];
                t_12_sub_TM[k][j] = rt_low_sub_TM[j][3][k];
                r_12_sub_TE[k][j] = rt_low_sub_TE[j][0][k];
                t_12_sub_TE[k][j] = rt_low_sub_TE[j][1][k];

                r_13_ext_TM[k][j] = rt_up_ext_TM[j][2][k];
                t_13_ext_TM[k][j] = rt_up_ext_TM[j][3][k];
                r_13_ext_TE[k][j] = rt_up_ext_TE[j][0][k];
                t_13_ext_TE[k][j] = rt_up_ext_TE[j][1][k];

                r_13_sub_TM[k][j] = rt_up_sub_TM[j][2][k];
                r_13_sub_TE[k][j] = rt_up_sub_TE[j][0][k];

                t_sub_ext_TM[k][j] = rt_sub_ext_TM[j][3][k];
                t_sub_ext_TE[k][j] = rt_sub_ext_TE[j][1][k];
            }
        }    //	reflection and transmission coeffs end
        printf("reflection and transmission coeffs end\n");
    }



        /*---------------------------------Transmittance------------------------------------*/
        printf("/*---------------------------------Transmittance------------------------------------*/\n");
    for (i = 0; i < no_EML; i++) {
        //	transmittance
        printf("transmittance start\n");
        multiply_1(t_12_ext_TM, n_extra, L_2_ext_TM, n_ordi, L_1_ext_TM, a_lgth, w_lgth, T_12_ext_TM);
        multiply_1(t_13_ext_TM, n_extra, L_3_ext_TM, n_ordi, L_1_ext_TM, a_lgth, w_lgth, T_13_ext_TM);
        multiply_1(t_12_sub_TM, n_extra, L_2_sub_TM, n_ordi, L_1_sub_TM, a_lgth, w_lgth, T_12_sub_TM);

        multiply_2(t_12_ext_TE, L_2_ext_TE, L_1_ext_TE, a_lgth, w_lgth, T_12_ext_TE);
        multiply_2(t_13_ext_TE, L_3_ext_TE, L_1_ext_TE, a_lgth, w_lgth, T_13_ext_TE);
        multiply_2(t_12_sub_TE, L_2_sub_TE, L_1_sub_TE, a_lgth, w_lgth, T_12_sub_TE);

        multiply_2(t_sub_ext_TM, L_2_sub_ext_TM, L_1_sub_ext_TM, a_lgth, w_lgth, T_sub_ext_TM);
        multiply_2(t_sub_ext_TE, L_2_sub_ext_TE, L_1_sub_ext_TE, a_lgth, w_lgth, T_sub_ext_TE);
        // transmittance end
        printf("transmittance end\n");
        // far_field emission end
        printf("far_field emission end\n\n");


        //	determination of the boarder
        for (k = 0; k < w_lgth; k++) {
            inpv_cut_ext_TM[k] = comprod(n_3[k], inversecom(n_extra[k])).A;
            inpv_cut_ext_TE[k] = comprod(n_3[k], inversecom(n_ordi[k])).A;
            inpv_cut_sub_TM[k] = comprod(n_2[k], inversecom(n_extra[k])).A;
            inpv_cut_sub_TE[k] = comprod(n_2[k], inversecom(n_ordi[k])).A;
        }
    }


    double d;
    double g;
    double s;

        /*------------------------------------------------------------------------------------*/
        /*                                 Mode Analysis                                      */
        /*------------------------------------------------------------------------------------*/
        printf("/*------------------------------------------------------------------------------------*/\n");
        printf("/*                                 Mode Analysis                                      */\n");
        printf("/*------------------------------------------------------------------------------------*/\n");
    for (i = 0; i < no_EML; i++) {
        for (j = 0; j < no_EMZ; j++) {
            //common process
            printf("common process\n");
            //for eq (8-10)

            //double d = EMZ_load(EML, thick_up[0][i], no_EMZ, i)[j][i];

            d = EMZ_load(EML, thick_EML, no_EMZ, i)[j][0];
            g = EMZ_load(EML, thick_EML, no_EMZ, i)[j][1];
            s = thick_EML - d;

//            double d = EMZ[j][0][i];
//            double s = thick_EML - EMZ[j][0][i];
//	        // common process end
            printf("common process end\n\n");

            //	for mode analyesis
            //	Reflec: function
            Reflec(d, r_12_TM, n_ordi, L_1, inpv, v_lgth, WL, w_lgth, R_12_TM);
            Reflec(s, r_13_TM, n_ordi, L_1, inpv, v_lgth, WL, w_lgth, R_13_TM);
            Reflec_2(thick_EML, r_12_TM, r_13_TM, n_ordi, L_1, inpv, v_lgth, WL, w_lgth, R_1213_TM);
            Reflec(d, r_12_TE, n_ordi, L_1, inpv, v_lgth, WL, w_lgth, R_12_TE);
            Reflec(s, r_13_TE, n_ordi, L_1, inpv, v_lgth, WL, w_lgth, R_13_TE);
            Reflec_2(thick_EML, r_12_TE, r_13_TE, n_ordi, L_1, inpv, v_lgth, WL, w_lgth, R_1213_TE);


            //	multiply: function
            //	eq (8)
            multiply_p_1(prefactor_v_TM, R_12_TM, R_13_TM, R_1213_TM, inpv, L_1, v_lgth, w_lgth, p_v_TM);
            //	eq (9)
            multiply_p_2(prefactor_h_TM, R_12_TM, R_13_TM, R_1213_TM, inpv, L_1, v_lgth, w_lgth, p_h_TM);
            //	eq (10)
            multiply_p_3(prefactor_h_TE, R_12_TE, R_13_TE, R_1213_TE, inpv, L_1, v_lgth, w_lgth, p_h_TE);


            //	for eq (16-18)
            for (k = 0; k < v_lgth; k++) {
                for (l = 0; l < w_lgth; l++) {
                    Abs_R_v_TM_12[k][l] = compabs2(comdiv(commin(ONE, R_13_TM[k][l]), commin(ONE, R_1213_TM[k][l]))).A;
                    Abs_R_v_TM_13[k][l] = compabs2(comdiv(commin(ONE, R_12_TM[k][l]), commin(ONE, R_1213_TM[k][l]))).A;
                    Abs_R_h_TM_12[k][l] = compabs2(comdiv(comsum(ONE, R_13_TM[k][l]), commin(ONE, R_1213_TM[k][l]))).A;
                    Abs_R_h_TM_13[k][l] = compabs2(comdiv(comsum(ONE, R_12_TM[k][l]), commin(ONE, R_1213_TM[k][l]))).A;
                    Abs_R_h_TE_12[k][l] = compabs2(comdiv(comsum(ONE, R_13_TE[k][l]), commin(ONE, R_1213_TE[k][l]))).A;
                    Abs_R_h_TE_13[k][l] = compabs2(comdiv(comsum(ONE, R_12_TE[k][l]), commin(ONE, R_1213_TE[k][l]))).A;
                }
            }


            //eq(16)
            multiply_3_1(prefactor_v_TM, Abs_R_v_TM_12, T_12_TM, inpv, L_1, v_lgth, w_lgth, p_out_12_v_TM);
            multiply_3_1(prefactor_v_TM, Abs_R_v_TM_13, T_13_TM, inpv, L_1, v_lgth, w_lgth, p_out_13_v_TM);

            //	eq (17)
            multiply_3_2(prefactor_h_TM, Abs_R_h_TM_12, T_12_TM, inpv, L_1, v_lgth, w_lgth, p_out_12_h_TM);
            multiply_3_2(prefactor_h_TM, Abs_R_h_TM_13, T_13_TM, inpv, L_1, v_lgth, w_lgth, p_out_13_h_TM);

            //	eq(18)
            multiply_3_3(prefactor_h_TE, Abs_R_h_TE_12, T_12_TE, inpv, L_1, v_lgth, w_lgth, p_out_12_h_TE);
            multiply_3_3(prefactor_h_TE, Abs_R_h_TE_13, T_13_TE, inpv, L_1, v_lgth, w_lgth, p_out_13_h_TE);

            //	eq(7)
            multiply_4_1(p_v_TM, P0_v, 1 - EML[i].HDR, v_lgth, w_lgth, p_total_TM[i][j]);
            multiply_4_1(p_h_TM, P0_v, EML[i].HDR, v_lgth, w_lgth, Temp);
            arrsum(p_total_TM[i][j], Temp, w_lgth, v_lgth);
            multiply_4_1(p_h_TE, P0_v, EML[i].HDR, v_lgth, w_lgth, p_total_TE[i][j]);
            arrsum_new(p_total_TM[i][j], p_total_TE[i][j], w_lgth, v_lgth, p_total[i][j]);

            //	eq(19)
            multiply_4_1(p_out_12_v_TM, P0_v, 1 - EML[i].HDR, v_lgth, w_lgth, p_total_out_12_TM);
            multiply_4_1(p_out_12_h_TM, P0_v, EML[i].HDR, v_lgth, w_lgth, Temp);
            arrsum(p_total_out_12_TM, Temp, w_lgth, v_lgth);
            multiply_4_1(p_out_12_h_TE, P0_v, EML[i].HDR, v_lgth, w_lgth, p_total_out_12_TE);
            arrsum_new(p_total_out_12_TM, p_total_out_12_TE, w_lgth, v_lgth, p_total_out_12);

            //	eq(19) opposite direction
            multiply_4_1(p_out_13_v_TM, P0_v, 1 - EML[i].HDR, v_lgth, w_lgth, p_total_out_13_TM);
            multiply_4_1(p_out_13_h_TM, P0_v, EML[i].HDR, v_lgth, w_lgth, Temp);
            arrsum(p_total_out_13_TM, Temp, w_lgth, v_lgth);
            multiply_4_1(p_out_13_h_TE, P0_v, EML[i].HDR, v_lgth, w_lgth, p_total_out_13_TE);
            arrsum_new(p_total_out_13_TM, p_total_out_13_TE, w_lgth, v_lgth, p_total_out_13);


            for (k = 0; k < w_lgth; k++) {
                if (j == 0) {
                    //	dviding optical modes
                    ext_number_TM[k] = find(inpv, inpv_cut_ext_TM[k], v_lgth);
                    ext_number_TE[k] = find(inpv, inpv_cut_ext_TE[k], v_lgth);
                    subs_number_TM[k] = find(inpv, inpv_cut_sub_TM[k], v_lgth);
                    subs_number_TE[k] = find(inpv, inpv_cut_sub_TE[k], v_lgth);
                    WG_number_TM[k] = find(inpv, 1, v_lgth);
                    WG_number_TE[k] = find(inpv, 1, v_lgth);
                }


                for (l = 0; l < ext_number_TM[k]; l++) {
                    p_abs_TM_tailored[k][l] =
                            p_total_TM[i][j][k][l] - p_total_out_12_TM[k][l] - p_total_out_13_TM[k][l];
                    p_abs_TE_tailored[k][l] =
                            p_total_TE[i][j][k][l] - p_total_out_12_TE[k][l] - p_total_out_13_TE[k][l];
                }


                //	integration in eq (7)
                P[i][j][k] = trapz(inpv, p_total[i][j][k], 1, v_lgth);
                OC[i][j][k] = trapz(inpv, p_total_out_12_TM[k], 1, ext_number_TM[k]) +
                              trapz(inpv, p_total_out_12_TE[k], 1, ext_number_TE[k]);
                OC_back[i][j][k] = trapz(inpv, p_total_out_13_TM[k], 1, ext_number_TM[k]) +
                                   trapz(inpv, p_total_out_13_TE[k], 1, ext_number_TE[k]);
                ABS[i][j][k] = trapz(inpv, p_abs_TM_tailored[k], 1, ext_number_TM[k]) +
                               trapz(inpv, p_abs_TE_tailored[k], 1, ext_number_TE[k]);
                SUBS[i][j][k] = trapz(inpv, p_total_TM[i][j][k], ext_number_TM[k], subs_number_TM[k]) +
                                trapz(inpv, p_total_TE[i][j][k], ext_number_TE[k], subs_number_TE[k]);
                WG[i][j][k] = trapz(inpv, p_total_TM[i][j][k], subs_number_TM[k], WG_number_TM[k]) +
                              trapz(inpv, p_total_TE[i][j][k], subs_number_TE[k], WG_number_TE[k]);
                SPPs[i][j][k] = trapz(inpv, p_total_TM[i][j][k], WG_number_TM[k], v_lgth) +
                                trapz(inpv, p_total_TE[i][j][k], WG_number_TE[k], v_lgth);

                //	eq (21) WL, EMzone, EML matrix
                q_eff[k][i][j] = EML[i].QY * P[i][j][k] / (1 - EML[i].QY + EML[i].QY * P[i][j][k]);

                //	eq (22)
                OC_eff[k][i][j] = OC[i][j][k] / P[i][j][k];
                OC_back_eff[k][i][j] = OC_back[i][j][k] / P[i][j][k];

                P_EMZ[i][j][k] = P[i][j][k] * g;
                OC_EMZ[i][j][k] = OC[i][j][k] * g;
                OC_back_EMZ[i][j][k] = OC_back[i][j][k] * g;
                ABS_EMZ[i][j][k] = ABS[i][j][k] * g;
                SUBS_EMZ[i][j][k] = SUBS[i][j][k] * g;
                WG_EMZ[i][j][k] = WG[i][j][k] * g;
                SPPs_EMZ[i][j][k] = SPPs[i][j][k] * g;
            }    //	w_lgth loop
            // mode anlysis end
            printf("mode anlysis end\n\n");
        }
    }


            /*------------------------------------------------------------------------------------*/
            /*                               Far Field Emission                                   */
            /*------------------------------------------------------------------------------------*/
            printf("/*------------------------------------------------------------------------------------*/\n");
            printf("/*                               Far Field Emission                                   */\n");
            printf("/*------------------------------------------------------------------------------------*/\n");
    for (i = 0; i < no_EML; i++) {
        for (j = 0; j < no_EMZ; j++) {

            d = EMZ_load(EML, thick_EML, no_EMZ, i)[j][0];
            g = EMZ_load(EML, thick_EML, no_EMZ, i)[j][1];
            s = thick_EML - d;


            //	for far-field emission
            for (k = 0; k < w_lgth; k++) {
                Reflec_w(d, r_12_ext_TM, n_ordi, L_1_ext_TM, a_lgth, WL[k], k, R_12_ext_TM[k]);
                Reflec_w(d, r_13_ext_TM, n_ordi, L_1_ext_TM, a_lgth, WL[k], k, R_13_ext_TM[k]);
                Reflec_2_w(thick_EML, r_12_ext_TM, r_13_ext_TM, n_ordi, L_1_ext_TM, a_lgth, WL[k], k, R_1213_ext_TM[k]);

                Reflec_w(d, r_12_ext_TE, n_ordi, L_1_ext_TE, a_lgth, WL[k], k, R_12_ext_TE[k]);
                Reflec_w(d, r_13_ext_TE, n_ordi, L_1_ext_TE, a_lgth, WL[k], k, R_13_ext_TE[k]);
                Reflec_2_w(thick_EML, r_12_ext_TE, r_13_ext_TE, n_ordi, L_1_ext_TE, a_lgth, WL[k], k, R_1213_ext_TE[k]);

                Reflec_w(d, r_13_sub_TM, n_ordi, L_1_sub_TM, a_lgth, WL[k], k, R_13_sub_TM[k]);
                Reflec_2_w(thick_EML, r_12_sub_TM, r_13_sub_TM, n_ordi, L_1_sub_TM, a_lgth, WL[k], k, R_1213_sub_TM[k]);

                Reflec_w(d, r_13_sub_TE, n_ordi, L_1_sub_TM, a_lgth, WL[k], k, R_13_sub_TE[k]);
                Reflec_2_w(thick_EML, r_12_sub_TE, r_13_sub_TE, n_ordi, L_1_sub_TE, a_lgth, WL[k], k, R_1213_sub_TE[k]);
            }


            for (k = 0; k < w_lgth; k++) {
                for (l = 0; l < a_lgth; l++) {
                    Abs_R_v_TM_12_ext[l][k] = compabs2(
                            comprod(commin(ONE, R_13_ext_TM[k][l]), inversecom(commin(ONE, R_1213_ext_TM[k][l])))).A;
                    Abs_R_v_TM_13_ext[l][k] = compabs2(
                            comprod(commin(ONE, R_12_ext_TM[k][l]), inversecom(commin(ONE, R_1213_ext_TM[k][l])))).A;
                    Abs_R_v_TM_12_sub[l][k] = compabs2(
                            comprod(commin(ONE, R_13_sub_TM[k][l]), inversecom(commin(ONE, R_1213_sub_TM[k][l])))).A;

                    Abs_R_h_TM_12_ext[l][k] = compabs2(
                            comprod(comsum(ONE, R_13_ext_TM[k][l]), inversecom(commin(ONE, R_1213_ext_TM[k][l])))).A;
                    Abs_R_h_TM_13_ext[l][k] = compabs2(
                            comprod(comsum(ONE, R_12_ext_TM[k][l]), inversecom(commin(ONE, R_1213_ext_TM[k][l])))).A;
                    Abs_R_h_TM_12_sub[l][k] = compabs2(
                            comprod(comsum(ONE, R_13_sub_TM[k][l]), inversecom(commin(ONE, R_1213_sub_TM[k][l])))).A;
                    Abs_R_h_TE_12_ext[l][k] = compabs2(
                            comprod(comsum(ONE, R_13_ext_TE[k][l]), inversecom(commin(ONE, R_1213_ext_TE[k][l])))).A;
                    Abs_R_h_TE_13_ext[l][k] = compabs2(
                            comprod(comsum(ONE, R_12_ext_TE[k][l]), inversecom(commin(ONE, R_1213_ext_TE[k][l])))).A;
                    Abs_R_h_TE_12_sub[l][k] = compabs2(
                            comprod(comsum(ONE, R_13_sub_TE[k][l]), inversecom(commin(ONE, R_1213_sub_TE[k][l])))).A;
                }
            }


            //	eq (25)
            multiply_5_1_1(prefactor_v_TM, Abs_R_v_TM_12_ext, T_12_ext_TM, inpv_ext_TM, L_1_ext_TM, n_2, L_2_ext_TM,
                           n_extra, a_lgth, w_lgth, p_out_12_v_ext_TM);
            multiply_5_2(p_out_12_v_ext_TM, T_sub_ext_TM, n_3, L_2_sub_ext_TM, n_2, L_1_sub_ext_TM, a_lgth, w_lgth,
                         p_out_12_v_ext_TM_intf);
            multiply_5_1_1(prefactor_v_TM, Abs_R_v_TM_13_ext, T_13_ext_TM, inpv_ext_TM, L_1_ext_TM, n_3, L_3_ext_TM,
                           n_extra, a_lgth, w_lgth, p_out_13_v_ext_TM);
            multiply_5_1_1(prefactor_v_TM, Abs_R_v_TM_12_sub, T_12_sub_TM, inpv_sub_TM, L_1_sub_TM, n_2, L_2_sub_TM,
                           n_extra, a_lgth, w_lgth, p_out_12_v_sub_TM);

            multiply_5_1_2(prefactor_h_TM, Abs_R_h_TM_12_ext, T_12_ext_TM, inpv_ext_TM, L_1_ext_TM, n_2, L_2_ext_TM,
                           n_extra, a_lgth, w_lgth, p_out_12_h_ext_TM);
            multiply_5_2(p_out_12_h_ext_TM, T_sub_ext_TM, n_3, L_2_sub_ext_TM, n_2, L_1_sub_ext_TM, a_lgth, w_lgth,
                         p_out_12_h_ext_TM_intf);
            multiply_5_1_2(prefactor_h_TM, Abs_R_h_TM_13_ext, T_13_ext_TM, inpv_ext_TM, L_1_ext_TM, n_3, L_3_ext_TM,
                           n_extra, a_lgth, w_lgth, p_out_13_h_ext_TM);
            multiply_5_1_2(prefactor_h_TM, Abs_R_h_TM_12_sub, T_12_sub_TM, inpv_sub_TM, L_1_sub_TM, n_2, L_2_sub_TM,
                           n_extra, a_lgth, w_lgth, p_out_12_h_sub_TM);


            //	eq (26)
            multiply_5_1_3(prefactor_h_TE, Abs_R_h_TE_12_ext, T_12_ext_TE, L_1_ext_TE, n_2, L_2_ext_TE, n_extra, a_lgth,
                           w_lgth, p_out_12_h_ext_TE);
            multiply_5_2(p_out_12_h_ext_TE, T_sub_ext_TE, n_3, L_2_sub_ext_TE, n_2, L_1_sub_ext_TE, a_lgth, w_lgth,
                         p_out_12_h_ext_TE_intf);
            multiply_5_1_3(prefactor_h_TE, Abs_R_h_TE_13_ext, T_13_ext_TE, L_1_ext_TE, n_3, L_3_ext_TE, n_extra, a_lgth,
                           w_lgth, p_out_13_h_ext_TE);
            multiply_5_1_3(prefactor_h_TE, Abs_R_h_TE_12_sub, T_12_sub_TE, L_1_sub_TE, n_2, L_2_sub_TE, n_extra, a_lgth,
                           w_lgth, p_out_12_h_sub_TE);
            multiply_4_1(p_out_12_v_ext_TM_intf, P0_v, EML[i].QY * (1 - EML[i].HDR), a_lgth, w_lgth,
                         p_out_12_ext_TM_EMZ[i][j]);
            multiply_4_1(p_out_12_h_ext_TM_intf, P0_v, EML[i].QY * EML[i].HDR, a_lgth, w_lgth, Temp);
            arrsum(p_out_12_ext_TM_EMZ[i][j], Temp, w_lgth, a_lgth);
            multiply_4_1(p_out_12_h_ext_TE_intf, P0_v, EML[i].QY * EML[i].HDR, a_lgth, w_lgth,
                         p_out_12_ext_TE_EMZ[i][j]);
            arrsum_new(p_out_12_ext_TM_EMZ[i][j], p_out_12_ext_TE_EMZ[i][j], w_lgth, a_lgth, p_out_12_ext_EMZ[i][j]);
            multiply_4_1(p_out_13_v_ext_TM, P0_v, EML[i].QY * (1 - EML[i].HDR), a_lgth, w_lgth,
                         p_out_13_ext_TM_EMZ[i][j]);
            multiply_4_1(p_out_13_h_ext_TM, P0_v, EML[i].QY * EML[i].HDR, a_lgth, w_lgth, Temp);
            arrsum(p_out_13_ext_TM_EMZ[i][j], Temp, w_lgth, a_lgth);
            multiply_4_1(p_out_13_h_ext_TE, P0_v, EML[i].QY * EML[i].HDR, a_lgth, w_lgth, p_out_13_ext_TE_EMZ[i][j]);
            arrsum_new(p_out_13_ext_TM_EMZ[i][j], p_out_13_ext_TE_EMZ[i][j], w_lgth, a_lgth, p_out_13_ext_EMZ[i][j]);

            multiply_4_1(p_out_12_v_sub_TM, P0_v, EML[i].QY * (1 - EML[i].HDR), a_lgth, w_lgth,
                         p_out_12_sub_TM_EMZ[i][j]);
            multiply_4_1(p_out_12_h_sub_TM, P0_v, EML[i].QY * EML[i].HDR, a_lgth, w_lgth, Temp);
            arrsum(p_out_12_sub_TM_EMZ[i][j], Temp, w_lgth, a_lgth);
            multiply_4_1(p_out_12_h_sub_TE, P0_v, EML[i].QY * EML[i].HDR, a_lgth, w_lgth, p_out_12_sub_TE_EMZ[i][j]);
            arrsum_new(p_out_12_sub_TM_EMZ[i][j], p_out_12_sub_TE_EMZ[i][j], w_lgth, a_lgth, p_out_12_sub_EMZ[i][j]);



            //	eq (27)
            multiply_4_2(p_out_12_ext_TM_EMZ[i][j], spectrum, i, g, a_lgth, w_lgth,
                         p_out_12_ext_TM_spec[i][j]);
            multiply_4_2(p_out_12_ext_TE_EMZ[i][j], spectrum, i, g, a_lgth, w_lgth,
                         p_out_12_ext_TE_spec[i][j]);
            arrsum_new(p_out_12_ext_TM_spec[i][j], p_out_12_ext_TE_spec[i][j], w_lgth, a_lgth, p_out_12_ext_spec[i][j]);

            multiply_4_2(p_out_13_ext_TM_EMZ[i][j], spectrum, i, g, a_lgth, w_lgth,
                         p_out_13_ext_TM_spec[i][j]);
            multiply_4_2(p_out_13_ext_TE_EMZ[i][j], spectrum, i, g, a_lgth, w_lgth,
                         p_out_13_ext_TE_spec[i][j]);
            arrsum_new(p_out_13_ext_TM_spec[i][j], p_out_13_ext_TE_spec[i][j], w_lgth, a_lgth, p_out_13_ext_spec[i][j]);

            multiply_4_2(p_out_12_sub_TM_EMZ[i][j], spectrum, i, g, a_lgth, w_lgth,
                         p_out_12_sub_TM_spec[i][j]);
            multiply_4_2(p_out_12_sub_TE_EMZ[i][j], spectrum, i, g, a_lgth, w_lgth,
                         p_out_12_sub_TE_spec[i][j]);
            arrsum_new(p_out_12_sub_TM_spec[i][j], p_out_12_sub_TE_spec[i][j], w_lgth, a_lgth, p_out_12_sub_spec[i][j]);

        } // far_field emission end
        printf("far_field emission end\n\n");
    }


    for (i = 0; i < no_EML; i++) {
        for (j = 0; j < no_EMZ; j++) {
            for (k = 0; k < w_lgth; k++) {
                P_EML[k][i] += P_EMZ[i][j][k];
                OC_EML[k][i] += OC_EMZ[i][j][k];
                OC_back_EML[k][i] += OC_back_EMZ[i][j][k];
                ABS_EML[k][i] += ABS_EMZ[i][j][k];
                SUBS_EML[k][i] += SUBS_EMZ[i][j][k];
                WG_EML[k][i] += WG_EMZ[i][j][k];
                SPPs_EML[k][i] += SPPs_EMZ[i][j][k];

                Purcell[k][i][j] = P[i][j][k] / P0[k].A;
            }
        }    //	EMZ loop
    }



    for (i = 0; i < no_EML; i++) {
        for (j = 0; j < w_lgth; j++) {
            OC_eff_integrated[i] +=
                    (spectrum[j][1][i] * EML[i].QY * OC_EML[j][i]) / (1 - EML[i].QY + EML[i].QY * P_EML[j][i]);
            OC_back_eff_integrated[i] +=
                    (spectrum[j][1][i] * EML[i].QY * OC_back_EML[j][i]) / (1 - EML[i].QY + EML[i].QY * P_EML[j][i]);
            ABS_eff_integrated[i] +=
                    (spectrum[j][1][i] * EML[i].QY * ABS_EML[j][i]) / (1 - EML[i].QY + EML[i].QY * P_EML[j][i]);
            SUBS_eff_integrated[i] +=
                    (spectrum[j][1][i] * EML[i].QY * SUBS_EML[j][i]) / (1 - EML[i].QY + EML[i].QY * P_EML[j][i]);
            WG_eff_integrated[i] +=
                    (spectrum[j][1][i] * EML[i].QY * WG_EML[j][i]) / (1 - EML[i].QY + EML[i].QY * P_EML[j][i]);
            SPPs_eff_integrated[i] +=
                    (spectrum[j][1][i] * EML[i].QY * SPPs_EML[j][i]) / (1 - EML[i].QY + EML[i].QY * P_EML[j][i]);
        }

        OC_eff_integrated[i] *= EXC_prop[i];
        OC_back_eff_integrated[i] *= EXC_prop[i];
        ABS_eff_integrated[i] *= EXC_prop[i];
        SUBS_eff_integrated[i] *= EXC_prop[i];
        WG_eff_integrated[i] *= EXC_prop[i];
        SPPs_eff_integrated[i] *= EXC_prop[i];
        //	mode analysis end
        printf("mode analysis end\n\n");
    }


    for (i = 0; i < no_EML; i++) {
        //	for far-field emission
        for (j = 0; j < no_EMZ; j++) {
            for (k = 0; k < a_lgth; k++) {
                for (l = 0; l < w_lgth; l++) {
                    p_out_12_ext_TM_spec_EML[k][l][i] += EXC_prop[i] * p_out_12_ext_TM_spec[i][j][l][k];
                    p_out_12_ext_TE_spec_EML[k][l][i] += EXC_prop[i] * p_out_12_ext_TE_spec[i][j][l][k];
                    p_out_12_ext_spec_EML[k][l][i] += EXC_prop[i] * p_out_12_ext_spec[i][j][l][k];

                    p_out_13_ext_TM_spec_EML[k][l][i] += EXC_prop[i] * p_out_13_ext_TM_spec[i][j][l][k];
                    p_out_13_ext_TE_spec_EML[k][l][i] += EXC_prop[i] * p_out_13_ext_TE_spec[i][j][l][k];
                    p_out_13_ext_spec_EML[k][l][i] += EXC_prop[i] * p_out_13_ext_spec[i][j][l][k];

                    p_out_12_sub_TM_spec_EML[k][l][i] += EXC_prop[i] * p_out_12_sub_TM_spec[i][j][l][k];
                    p_out_12_sub_TE_spec_EML[k][l][i] += EXC_prop[i] * p_out_12_sub_TE_spec[i][j][l][k];
                    p_out_12_sub_spec_EML[k][l][i] += EXC_prop[i] * p_out_12_sub_spec[i][j][l][k];
                }
            }
        }    //	no_EMZ loop //	far-field emission end
        printf("far-field emission end\n\n");
    }    // no_EML loop  //	main calculations end
    printf("main calculations end\n\n");


    printf("free start\n");
    free(ext_number_TM); free(ext_number_TE); free(subs_number_TM); free(subs_number_TE);
    free(WG_number_TM); free(WG_number_TE); free2d(p_abs_TM_tailored); free2d(p_abs_TE_tailored);
    free2d(Temp); free(EML); free(EXC_prop); free(n_ordi); free(n_extra); free(n_2); free(n_3);
    free(P0_v); free(P0_h); free2d(thick_up); free2d(thick_low); free2d(thick_sub_ext); free2c(L_1);
    free2c(L_2_TE); free2c(L_2_TM); free2c(L_3_TE); free2c(L_3_TM); free4c(rt_up); free4c(rt_low);
    free4d(index_up); free4d(index_low); free(no_up_layer); free(no_low_layer); free3d(EMZ);
    free2c(r_12_TE); free2c(t_12_TE); free2c(r_13_TE); free2c(t_13_TE); free2c(r_12_TM);
    free2c(t_12_TM); free2c(r_13_TM); free2c(t_13_TM); free(prefactor_h_TE);
    free(prefactor_h_TM); free(prefactor_v_TM); free2d(Abs_R_v_TM_12); free2d(Abs_R_h_TM_12);
    free2d(Abs_R_h_TE_12); free2d(Abs_R_v_TM_13); free2d(Abs_R_h_TM_13); free2d(Abs_R_h_TE_13);
    free2c(T_12_TM); free2c(T_13_TM); free2c(T_12_TE); free2c(T_13_TE); free2c(R_12_TM);
    free2c(R_13_TM); free2c(R_1213_TM); free2c(R_12_TE); free2c(R_13_TE); free2c(R_1213_TE);
    free2d(p_v_TM); free2d(p_h_TM); free2d(p_h_TE); free2d(p_out_12_v_TM); free2d(p_out_12_h_TM);
    free2d(p_out_12_h_TE); free2d(p_out_13_v_TM); free2d(p_out_13_h_TM); free2d(p_out_13_h_TE);
    free2d(p_total_out_12_TM); free2d(p_total_out_12_TE); free2d(p_total_out_12); free2d(p_total_out_13_TM);
    free2d(p_total_out_13_TE); free2d(p_total_out_13); free(inpv_cut_ext_TM); free(inpv_cut_sub_TM);
    free(inpv_cut_ext_TE); free(inpv_cut_sub_TE); free2c(inpv_ext_TM); free2c(inpv_ext_TE);
    free2c(inpv_sub_TM); free2c(inpv_sub_TE); free2c(L_1_ext_TM); free2c(L_1_ext_TE); free2c(L_1_sub_TM);
    free2c(L_1_sub_TE); free2c(L_2_ext_TM); free2c(L_2_ext_TE); free2c(L_2_sub_TM); free2c(L_2_sub_TE);
    free2c(L_3_ext_TM); free2c(L_3_ext_TE); free2c(inpv_sub_ext_TM); free2c(inpv_sub_ext_TE);
    free4d(index_sub_ext); free2c(L_1_sub_ext_TM); free2c(L_1_sub_ext_TE); free2c(L_2_sub_ext_TM);
    free2c(L_2_sub_ext_TE); free3c(rt_up_ext_TM); free3c(rt_up_ext_TE); free3c(rt_up_sub_TM);
    free3c(rt_up_sub_TE); free3c(rt_low_ext_TM); free3c(rt_low_ext_TE); free3c(rt_low_sub_TM);
    free3c(rt_low_sub_TE); free3c(rt_sub_ext_TM); free3c(rt_sub_ext_TE); free2c(r_12_ext_TM);
    free2c(t_12_ext_TM); free2c(r_12_sub_TM); free2c(t_12_sub_TM); free2c(r_12_ext_TE);
    free2c(t_12_ext_TE); free2c(r_12_sub_TE); free2c(t_12_sub_TE); free2c(r_13_ext_TM);
    free2c(t_13_ext_TM); free2c(r_13_ext_TE); free2c(t_13_ext_TE); free2c(r_13_sub_TM);
    free2c(r_13_sub_TE); free2c(t_sub_ext_TM); free2c(t_sub_ext_TE); free2c(T_12_ext_TM);
    free2c(T_13_ext_TM); free2c(T_12_sub_TM); free2c(T_sub_ext_TM); free2c(T_12_ext_TE);
    free2c(T_13_ext_TE); free2c(T_12_sub_TE); free2c(T_sub_ext_TE); free2c(R_12_ext_TM);
    free2c(R_13_ext_TM); free2c(R_1213_ext_TM); free2c(R_13_sub_TM);  free2c(R_1213_sub_TM);
    free2c(R_12_ext_TE); free2c(R_13_ext_TE); free2c(R_1213_ext_TE); free2c(R_13_sub_TE);
    free2c(R_1213_sub_TE); free2d(Abs_R_v_TM_12_ext); free2d(Abs_R_v_TM_13_ext); free2d(Abs_R_v_TM_12_sub);
    free2d(Abs_R_h_TM_12_ext); free2d(Abs_R_h_TM_13_ext); free2d(Abs_R_h_TM_12_sub); free2d(Abs_R_h_TE_12_ext);
    free2d(Abs_R_h_TE_13_ext); free2d(Abs_R_h_TE_12_sub); free2d(p_out_12_v_ext_TM); free2d(p_out_12_v_ext_TM_intf);
    free2d(p_out_13_v_ext_TM); free2d(p_out_12_v_sub_TM); free2d(p_out_12_h_ext_TE); free2d(p_out_12_h_ext_TE_intf); free2d(p_out_13_h_ext_TE);
    free2d(p_out_12_h_sub_TE);free2d(p_out_12_h_ext_TM);free2d(p_out_12_h_ext_TM_intf);free2d(p_out_13_h_ext_TM);
    free2d(p_out_12_h_sub_TM);free3d(OC);free3d(OC_back);free3d(ABS);
    free3d(SUBS);free3d(WG);free3d(SPPs);free2d(P_EML);free2d(OC_EML);free2d(OC_back_EML);
    free2d(ABS_EML);free2d(SUBS_EML);free2d(WG_EML);free2d(SPPs_EML);
/*	free2d(OC_EML_spec); free2d(OC_back_EML_spec); free2d(ABS_EML_spec);
	free2d(SUBS_EML_spec); free2d(WG_EML_spec); free2d(SPPs_EML_spec);*/
    free4d(p_out_12_ext_TM_spec);free4d(p_out_12_ext_TE_spec);free4d(p_out_12_ext_spec);free4d(p_out_13_ext_TM_spec);
    free4d(p_out_13_ext_TE_spec);free4d(p_out_13_ext_spec);free4d(p_out_12_sub_TM_spec);free4d(p_out_12_sub_TE_spec);
    free4d(p_out_12_sub_spec);free3d(P_EMZ);free3d(OC_EMZ);free3d(OC_back_EMZ);
    free3d(ABS_EMZ);free3d(SUBS_EMZ);free3d(WG_EMZ);free3d(SPPs_EMZ);
    free3d(P);free(P0);free3d(spectrum);free4d(p_out_12_ext_TM_EMZ);free4d(p_out_12_ext_TE_EMZ);
    free4d(p_out_12_ext_EMZ);free4d(p_out_13_ext_TM_EMZ);free4d(p_out_13_ext_TE_EMZ);free4d(p_out_13_ext_EMZ);
    free4d(p_out_12_sub_TM_EMZ);free4d(p_out_12_sub_TE_EMZ);free4d(p_out_12_sub_EMZ);
    //	free end
    printf("free end\n\n");


    //	printing output
    //	for mode analysis
    double OC_eff_final = sum(OC_eff_integrated, no_EML);
    double OC_back_eff_final = sum(OC_back_eff_integrated, no_EML);
    double ABS_eff_final = sum(ABS_eff_integrated, no_EML);
    double SUBS_eff_final = sum(SUBS_eff_integrated, no_EML);
    double WG_eff_final = sum(WG_eff_integrated, no_EML);
    double SPPs_eff_final = sum(SPPs_eff_integrated, no_EML);
    double NR_loss_final =
            1 - (OC_eff_final + OC_back_eff_final + ABS_eff_final + SUBS_eff_final + WG_eff_final + SPPs_eff_final);

    printf("/*------------------------------------------------------------------------------------*/\n");
    printf("OC:%g, OC_back:%g, Subs:%g, WG:%g, SPPs:%g,  Abs:%g, NR_loss:%g \n", OC_eff_final, OC_back_eff_final,
           SUBS_eff_final, WG_eff_final, SPPs_eff_final, ABS_eff_final,
           NR_loss_final);        //  NR_loss�� ABS��ġ �ٲ�Ͱ���	NR loss	�� 0??...
    printf("/*------------------------------------------------------------------------------------*/\n");
    //	mode analysis end
    printf("mode analysis end\n\n");


    free(OC_eff_integrated);free(OC_back_eff_integrated);
    free(ABS_eff_integrated);free(SUBS_eff_integrated);
    free(WG_eff_integrated);free(SPPs_eff_integrated);
    //for far_field emission


    for (i = 0; i < no_EML; i++) {
        for (j = 0; j < a_lgth; j++) {
            for (k = 0; k < w_lgth; k++) {
                p_out_12_ext_TM_final[j][k] += p_out_12_ext_TM_spec_EML[j][k][i];
                p_out_12_ext_TE_final[j][k] += p_out_12_ext_TE_spec_EML[j][k][i];
                p_out_12_ext_final[j][k] += p_out_12_ext_spec_EML[j][k][i];

                p_out_13_ext_TM_final[j][k] += p_out_13_ext_TM_spec_EML[j][k][i];
                p_out_13_ext_TE_final[j][k] += p_out_13_ext_TE_spec_EML[j][k][i];
                p_out_13_ext_final[j][k] += p_out_13_ext_spec_EML[j][k][i];

                p_out_12_sub_TM_final[j][k] += p_out_12_sub_TM_spec_EML[j][k][i];
                p_out_12_sub_TE_final[j][k] += p_out_12_sub_TE_spec_EML[j][k][i];
                p_out_12_sub_final[j][k] += p_out_12_sub_spec_EML[j][k][i];
            }
        }
    }  // EML loop


    free3d(p_out_12_ext_TM_spec_EML);free3d(p_out_12_ext_TE_spec_EML);
    free3d(p_out_12_ext_spec_EML);free3d(p_out_13_ext_TM_spec_EML);
    free3d(p_out_13_ext_TE_spec_EML);free3d(p_out_13_ext_spec_EML);
    free3d(p_out_12_sub_TM_spec_EML);free3d(p_out_12_sub_TE_spec_EML);free3d(p_out_12_sub_spec_EML);
    // far-field emission end
    printf("far-field emission end\n\n");


    //	output processing for n loops
    //	output: MOde, spectrum, PUrcell, qeff, CIE, Luminace
    //	output matrix
    //	angle * 1
    double *output_angular_intensity_bottom = zeros(a_lgth);
    double *output_angular_intensity_top = zeros(a_lgth);
    double *output_angular_intensity_sub = zeros(a_lgth);
    double *output_angular_intensity_bottom_TM = zeros(a_lgth);
    double *output_angular_intensity_top_TM = zeros(a_lgth);
    double *output_angular_intensity_sub_TM = zeros(a_lgth);
    double *output_angular_intensity_bottom_TE = zeros(a_lgth);
    double *output_angular_intensity_top_TE = zeros(a_lgth);
    double *output_angular_intensity_sub_TE = zeros(a_lgth);


    //	angle * 3
    double **output_CIE_bottom;
    double **output_CIE_top;
    double **output_CIE_sub;


    //	7 columns
    double output_mode[7] = {OC_eff_final, OC_back_eff_final, ABS_eff_final, SUBS_eff_final, WG_eff_final,
                             SPPs_eff_final, NR_loss_final};

    //	Candela per ampere part
    FILE *es = fopen(my_realpath("../c/data/eyesense.dat"), "rt");
    if (es == NULL) {
        printf("There is no data\n");
        return false;
    }
    char temp[20];
    char *temp1 = temp;
    char *temp2;
    double result;
    double **eyesense = zeros2_0(600, 3);
    while (1) {
        j = 0;
        if (feof(es))
            break;
        temp1 = fgets(temp1, 100, es);
        temp2 = strtok(temp1, "	");
        while (temp2 != NULL) {
            result = atof(temp2);
            temp2 = strtok(NULL, "	");
            *(*(eyesense + i) + j) = result;
            j++;
        }
        i++;
    }
    fclose(es);



    double *Temp2 = zeros_0(w_lgth);
    for (i = 0; i < w_lgth; i++)
        Temp2[i] = p_out_12_ext_final[0][i] * eyesense[(int) WL_init - 299 + (int) WL_step * i][1];
    double Cd_bottom = 683.002 * sum(Temp2, w_lgth) * WL_step;        //		Watt/mA/sr -> Cd/mA
    for (i = 0; i < w_lgth; i++)
        Temp2[i] = p_out_13_ext_final[0][i] * eyesense[(int) WL_init - 299 + (int) WL_step * i][1];
    double Cd_top = 683.002 * sum(Temp2, w_lgth) * WL_step;
    double Ampere = 1000;    //	1000mA, 1Coulomb/sec
    for (i = 0; i < w_lgth; i++)
        Temp2[i] = p_out_12_ext_final[0][i];
    double output_Watt_per_mA_sr_bottom = sum(Temp2, w_lgth) * WL_step;
    for (i = 0; i < w_lgth; i++)
        Temp2[i] = p_out_13_ext_final[0][i];
    double output_Watt_per_mA_sr_top = sum(Temp2, w_lgth) * WL_step;
    free(Temp2);
    double output_Cd_per_A_bottom = Cd_bottom / Ampere;
    double output_Cd_per_A_top = Cd_top / Ampere;


    //	angle * 1
    for (i = 0; i < a_lgth; i++) {
        output_angular_intensity_bottom[i] = sum(p_out_12_ext_final[i], w_lgth);
        output_angular_intensity_top[i] = sum(p_out_13_ext_final[i], w_lgth);
        output_angular_intensity_sub[i] = sum(p_out_12_sub_final[i], w_lgth);        //	matlab �ڵ� �̻�!
        output_angular_intensity_bottom_TM[i] = sum(p_out_12_ext_TM_final[i], w_lgth);
        output_angular_intensity_top_TM[i] = sum(p_out_13_ext_TM_final[i], w_lgth);
        output_angular_intensity_sub_TM[i] = sum(p_out_12_sub_TM_final[i], w_lgth);
        output_angular_intensity_bottom_TE[i] = sum(p_out_12_ext_TE_final[i], w_lgth);
        output_angular_intensity_top_TE[i] = sum(p_out_13_ext_TE_final[i], w_lgth);
        output_angular_intensity_sub_TE[i] = sum(p_out_12_sub_TE_final[i], w_lgth);
    }
    //	angle * 3
    output_CIE_bottom = CIE(p_out_12_ext_final, angle, a_lgth, WL, WL_step, w_lgth);
    output_CIE_top = CIE(p_out_13_ext_final, angle, a_lgth, WL, WL_step, w_lgth);
    output_CIE_sub = CIE(p_out_12_sub_final, angle, a_lgth, WL, WL_step, w_lgth);
    free(angle);
    free(WL);


    end = clock();
    double r_1;
    r_1 = t_result = ((double) end - (double) start) / CLOCKS_PER_SEC;
    printf("%lf is the Calculation Time\n", t_result);


	char strFolderPathCPA[100]={0};
	char strFolderPathEL[100]={0};
	char strFolderPathAI[100]={0};
	char strFolderPathCIE[100]={0};
	char strFolderPathEFF[100]={0};
	char strFolderPathDS[100]={0};


    strcpy(strFolderPath, my_realpath("../c/output/#1-1"));
    //mkdir(strFolderPath, 0700);
     //7 columns
    output1(strFolderPath, "output_mode", output_mode, 7);



    //Candela per ampere
    real_name = concat(strFolderPath, "/Candela_per_ampere");
    strcpy(strFolderPathCPA, real_name);
    //mkdir(strFolderPathCPA, 0700);
    output(strFolderPathCPA, "output_Watt_per_mA_sr_bottom", output_Watt_per_mA_sr_bottom);
    output(strFolderPathCPA, "output_Watt_per_mA_sr_top", output_Watt_per_mA_sr_top);
    output(strFolderPathCPA, "output_Cd_per_A_bottom", output_Cd_per_A_bottom);
    output(strFolderPathCPA, "output_Cd_per_A_top", output_Cd_per_A_top);



    //ELspectrum	% wavelegnth* angle
    real_name = concat(strFolderPath, "/ELspectrum");
    strcpy(strFolderPathEL, real_name);
    //mkdir(strFolderPathEL, 0700);
    outputEL(strFolderPathEL, "output_ELspectrum_bottom", p_out_12_ext_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_top", p_out_13_ext_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_sub", p_out_12_sub_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_bottom_TM", p_out_12_ext_TM_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_top_TM", p_out_13_ext_TM_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_sub_TM", p_out_12_sub_TM_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_bottom_TE", p_out_12_ext_TE_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_top_TE", p_out_13_ext_TE_final, w_lgth, a_lgth);
    outputEL(strFolderPathEL, "output_ELspectrum_sub_TE", p_out_12_sub_TE_final, w_lgth, a_lgth);



    //angular_intensity		% angle * 1
    real_name = concat(strFolderPath, "/angular_intensity");
    strcpy(strFolderPathAI, real_name);
    //mkdir(strFolderPathAI, 0700);
    output1(strFolderPathAI, "output_angular_intensity_bottom", output_angular_intensity_bottom, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_top", output_angular_intensity_top, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_sub", output_angular_intensity_sub, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_bottom_TM", output_angular_intensity_bottom_TM, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_top_TM", output_angular_intensity_top_TM, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_sub_TM", output_angular_intensity_sub_TM, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_bottom_TE", output_angular_intensity_bottom_TE, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_top_TE", output_angular_intensity_top_TE, a_lgth);
    output1(strFolderPathAI, "output_angular_intensity_sub_TE", output_angular_intensity_sub_TE, a_lgth);


    //CIE			% angle * 3
    real_name = concat(strFolderPath, "/CIE");
    strcpy(strFolderPathCIE, real_name);
    //mkdir(strFolderPathCIE, 0700);
    output2(strFolderPathCIE, "output_CIE_bottom", output_CIE_bottom, a_lgth, 3);
    output2(strFolderPathCIE, "output_CIE_top", output_CIE_top, a_lgth, 3);
    output2(strFolderPathCIE, "output_CIE_sub", output_CIE_sub, a_lgth, 3);


    //eff			% wavelegnth * EML * EMZ
    real_name = concat(strFolderPath, "/EFF");
    strcpy(strFolderPathEFF, real_name);
    //mkdir(strFolderPathEFF, 0700);
    output3(strFolderPathEFF, "output_OC_eff", OC_eff, w_lgth, no_EML, no_EMZ);
    output3(strFolderPathEFF, "output_OC_top_eff", OC_back_eff, w_lgth, no_EML, no_EMZ);
    output3(strFolderPathEFF, "output_Purcell", Purcell, w_lgth, no_EML, no_EMZ);
    output3(strFolderPathEFF, "output_effective_QY", q_eff, w_lgth, no_EML, no_EMZ);



    //dissipation	% inplane_wavevector * wavelength * EML * EMZ
    real_name = concat(strFolderPath, "/dissipation");
    strcpy(strFolderPathDS, real_name);
    //mkdir(strFolderPathDS, 0700);
    outputDS(strFolderPathDS, "output_power_dissipation", p_total, v_lgth, w_lgth, no_EML, no_EMZ);
    outputDS(strFolderPathDS, "output_power_dissipation_TM", p_total_TM, v_lgth, w_lgth, no_EML, no_EMZ);
    outputDS(strFolderPathDS, "output_power_dissipation_TE", p_total_TE, v_lgth, w_lgth, no_EML, no_EMZ);



    free4d(p_total); free4d(p_total_TM);free4d(p_total_TE);free2d(p_out_12_ext_final);
    free2d(p_out_13_ext_final);free2d(p_out_12_sub_final);free2d(p_out_12_ext_TM_final);free2d(p_out_13_ext_TM_final);
    free2d(p_out_12_sub_TM_final);free2d(p_out_12_ext_TE_final);free2d(p_out_13_ext_TE_final);free2d(p_out_12_sub_TE_final);
    free3d(OC_eff);free3d(OC_back_eff);free3d(Purcell);free3d(q_eff);
    free(output_angular_intensity_sub_TE);free(output_angular_intensity_top_TE);free(output_angular_intensity_bottom_TE);free(output_angular_intensity_sub_TM);
    free(output_angular_intensity_top_TM);free(output_angular_intensity_bottom_TM);free(output_angular_intensity_sub);free(output_angular_intensity_top);
    free(output_angular_intensity_bottom);free2d(output_CIE_bottom);free2d(output_CIE_top);free2d(output_CIE_sub);


    end = clock();
    t_result = ((double) end - (double) start) / CLOCKS_PER_SEC;
    printf("%lf is the Writing Time\n", t_result - r_1);

    return 0;
}