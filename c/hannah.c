//
// Created by Hannah Lee on 2021/01/16.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>
#include <errno.h>
#include <math.h>
#include <time.h>
#include <err.h>

#define ZALLOC(item, n, type) if ((item = (type *)calloc((n), sizeof(type))) == NULL) \
                                  fatalx("Unable to allocate %d unit(s) for item\n", n)
#define ALLOC(p, n) do {                                \
    if (!((p) = calloc((n), sizeof(*(p))))) {           \
        fprintf(stderr, "Memory allocation failure\n"); \
        exit(1);                                        \
    }                                                   \
} while (0)

void fatalx(const char *str, size_t n)
{
    fprintf(stderr, "%s: %zu\n", str, n);
    exit(1);
}


double ***alloc_3d(double **data, int levels, int rows, int cols)
{
    int count = 0;
    double ***array_3d;
    ZALLOC(array_3d, levels, double **);
    for (int i = 0; i < levels; i++)
    {
        //int **data;
        ZALLOC(data, rows, double *);
        array_3d[i] = data;
        for (int j = 0; j < rows; j++)
        {
            double *entries;
            ZALLOC(entries, cols, double);
            array_3d[i][j] = entries;
            for (int k = 0; k < cols; k++)
            {
                array_3d[i][j][k] = count++;
            }
        }
    }
    return array_3d;
}


void print_3d(double ***a3d, int levels, int rows, int cols)
{
    for (int i = 0; i < levels; i++)
    {
        printf("%d:\n", i);
        for (int j = 0; j < rows; j++)
        {
            printf("   %d:  ", j);
            for (int k = 0; k < cols; k++)
                printf(" %3lf", a3d[i][j][k]);
            putchar('\n');
        }
    }
}


static void free_3d(int ***a3d, int levels, int rows)
{
    for (int i = 0; i < levels; i++)
    {
        for (int j = 0; j < rows; j++)
            free(a3d[i][j]);
        free(a3d[i]);
    }
    free(a3d);
}


void *reshape_2d_3d(size_t id1, size_t id2, int iar[][id2],
                    size_t od1, size_t od2, size_t od3) {
    // oar is a pointer to a multidimensional array; in this case, it will
    // point to the first element of an array of arrays (of arrays).
    int (*oar)[od2][od3];
    size_t size1 = id1 * id2;
    size_t size2 = od1 * od2 * od3;
    size_t min_size = (size1 <= size2) ? size1 : size2;

    ALLOC(oar, od1);

    // A loop nest could be used here, too, but I find this simpler for
    // tracking the correspondence of array elements.  It also better
    // accommodates the case where the reshaped result has different overall
    // size from the original.
    for (size_t i = 0; i < min_size; i++) {
        oar[i / (od2 * od3)][(i / od3) % od2][i % od3] = iar[i / id2][i % id2];
    }

    return oar;
}

void *xrealloc_dp (void **p, size_t *n)
{
    void *tmp = realloc (p, 2 * *n * sizeof tmp);
#ifdef DEBUG
    printf ("\n  reallocating %zu to %zu\n", *n, *n * 2);
#endif
    if (!tmp) {
        fprintf (stderr, "%s() error: virtual memory exhausted.\n", __func__);
        exit (EXIT_FAILURE);
    }
    p = tmp;
    memset (p + *n, 0, *n * sizeof tmp); /* set new pointers NULL */
    *n *= 2;

    return p;
}


void *xrealloc_sp (void *p, size_t sz, size_t *n)
{
    void *tmp = realloc (p, 2 * *n * sz);
#ifdef DEBUG
    printf ("\n  reallocating '%zu' to '%zu', size '%zu'\n", *n, *n * 2, sz);
#endif
    if (!tmp) {
        fprintf (stderr, "%s() error: virtual memory exhausted.\n", __func__);
        exit (EXIT_FAILURE);
    }
    p = tmp;
    memset (p + *n * sz, 0, *n * sz); /* zero new memory */
    *n *= 2;

    return p;
}


void *xcalloc (size_t n, size_t s)
{
    register void *memptr = calloc (n, s);
    if (memptr == 0)
    {
        fprintf (stderr, "%s() error: virtual memory exhausted.\n", __func__);
        exit (EXIT_FAILURE);
    }

    return memptr;
}


double xstrtod (char *str, char **ep)
{
    errno = 0;

    double val = strtod (str, ep);

    /* Check for various possible errors */
    if ((errno == ERANGE && (val == HUGE_VAL || val == HUGE_VALL)) ||
        (errno != 0 && val == 0)) {
        perror ("strtod");
        exit (EXIT_FAILURE);
    }

    if (*ep == str) {
        fprintf (stderr, "No digits were found\n");
        exit (EXIT_FAILURE);
    }

    return val;
}


const char* getfield(char* line, int num)
{
    const char* tok;
    for (tok = strtok(line, ",");
         tok && *tok;
         tok = strtok(NULL, ",\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}


const char *getfield2 (char *buf, size_t field)
{
    size_t len = strlen(buf);       /* size of input string */
    char *cpy = malloc (len + 1),   /* allocate for copy */
    *p,                         /* pointer to use with strsep */
    *tok = NULL;                /* token for requested field */

    if (!cpy)                       /* validate allocation */
        return NULL;

    memcpy (cpy, buf, len + 1);     /* copy buf to cpy */
    p = cpy;                        /* pointer to cpy, preserves cpy address */

    while (field-- && (tok = strsep (&p, ","))) {}  /* get field field */

    /* copy tok to cpy and return cpy on success or NULL on failure */
    return tok ? memmove (cpy, tok, strlen(tok) + 1) : NULL;
}