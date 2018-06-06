#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

double get_time()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec * 1e-6;
}

double Mul(n)
{
    double* a = (double*)malloc(n * n * sizeof(double)); // Matrix A
    double* b = (double*)malloc(n * n * sizeof(double)); // Matrix B
    double* c = (double*)malloc(n * n * sizeof(double)); // Matrix C

    // Initialize the matrices to some values.
    int i, j, k;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            a[i * n + j] = i * n + j; // A[i][j]
            b[i * n + j] = j * n + i; // B[i][j]
            c[i * n + j] = 0; // C[i][j]
        }
    }

    double begin = get_time();

    //Calculate C = A * B.
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            for (k = 0; k < n; k++) {
                c[i * n + j] += a[i * n + k] * b[k * n + j];
            }
        }
    }

    double end = get_time();
    free(a);
    free(b);
    free(c);
    printf("time: %.6lf sec\n", end - begin);
    return end-begin;
}

int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);

    FILE *fp = fopen(argv[2], "w");
    if(fp==NULL)
    {
        return 0;
    }

    int i = 1;
    for(i=1; i<=n; i++)
    {
        fprintf(fp, "%lf", Mul(i));
        fprintf(fp, "\n");
    }


    return 0;
}
