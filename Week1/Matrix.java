/**
 * Created by cathy on 2018/06/03.
 */
import java.io.FileWriter;
import java.io.Writer;
import java.util.*;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

class Matrix {
    public static long multiply(int n) {
//        if (args.length != 1) {
//            System.out.println("usage: java Matrix N");
//            return;
//        }
//        int n = Integer.parseInt(args[0]);

        double[][] a = new double[n][n]; // Matrix A
        double[][] b = new double[n][n]; // Matrix B
        double[][] c = new double[n][n]; // Matrix C

        // Initialize the matrices to some values.
        int i, j, k;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                a[i][j] = i * n + j;
                b[i][j] = j * n + i;
                c[i][j] = 0;
            }
        }

        long begin = System.currentTimeMillis();

        /**************************************/
    /* Write code to calculate C = A * B. */

        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                for (k = 0; k < n; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        /**************************************/

        long end = System.currentTimeMillis();
        long time = end - begin;
//        System.out.printf("time: %.6f sec\n", time / 1000.0);

        // Print C for debugging. Comment out the print before measuring the execution time.
//        double sum = 0;
//        for (i = 0; i < n; i++) {
//            for (j = 0; j < n; j++) {
//                sum += c[i][j];
//                // System.out.printf("c[%d][%d]=%f\n", i, j, c[i][j]);
//            }
//        }
        // Print out the sum of all values in C.
        // This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
//        System.out.printf("sum: %.6f\n", sum);
        return time;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("please input a integer number: ");
        int n = in.nextInt();

        File f = new File("matrix_java.txt");
        Writer out = null;
        try {
            out = new FileWriter(f);
        } catch (IOException e) {
            e.printStackTrace();
        }

        for (int i = 1; i <= n; i++) {
            long time = multiply(i);
//            System.out.print(time);
//            System.out.printf("time: %.6f sec\n", time / 1000.0);
            try{
                out.write(String.valueOf((time/1000.0)));
                out.write("\n");
            }catch (IOException e1){
                e1.printStackTrace();
            }
        }
        try {
            out.close();
        }catch (IOException e2){
            e2.printStackTrace();
        }


        }
    }

