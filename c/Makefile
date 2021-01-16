hannimpeha.so: CIE.o EMZ_load.o innerfunc.o intp.o multiply.o OLED_main.o output.o Reflec.o RI_load.o spectrum_load.o TMM_anisotropy_coeff.o hannah.o
	gcc -shared -o hannimpeha.so CIE.o EMZ_load.o  innerfunc.o intp.o multiply.o OLED_main.o output.o Reflec.o RI_load.o spectrum_load.o TMM_anisotropy_coeff.o hannah.o

CIE.o: CIE.c
	gcc -Wall -c -o CIE.o CIE.c -fPIC

EMZ_load.o: EMZ_load.c
	gcc -Wall -c -o EMZ_load.o EMZ_load.c -fPIC

innerfunc.o: innerfunc.c
	gcc -Wall -c -o innerfunc.o innerfunc.c -fPIC

intp.o: intp.c
	gcc -Wall -c -o intp.o intp.c -fPIC

multiply.o: multiply.c
	gcc -Wall -c -o multiply.o multiply.c -fPIC

OLED_main.o: OLED_main.c
	gcc -Wall -c -o OLED_main.o OLED_main.c -fPIC

output.o: output.c
	gcc -Wall -c -o output.o output.c -fPIC

Reflec.o: Reflec.c
	gcc -Wall -c -o Reflec.o Reflec.c -fPIC

RI_load.o: RI_load.c
	gcc -Wall -c -o RI_load.o RI_load.c -fPIC

spectrum_load.o: spectrum_load.c
	gcc -Wall -c -o spectrum_load.o spectrum_load.c -fPIC

TMM_anistropy_coeff.o: TMM_anisotropy_coeff.c
	gcc -Wall -c -o TMM_anistropy_coeff.o TMM_anisotropy_coeff.c -fPIC

hannah.o: hannah.c
	gcc -Wall -c -o hannah.o hannah.c -fPIC

clean:
	rm *.o test.so