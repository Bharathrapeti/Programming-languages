#include<stdio.h>
int main()
{
	double x;

	printf("Enter a number: ");
	if (scanf("%lf", &x) != 1) {
		fprintf(stderr, "Invalid input\n");
		return 1;
	}

	if (x < 0) x = -x;

	printf("Absolute value: %g\n", x);
	return 0;
}