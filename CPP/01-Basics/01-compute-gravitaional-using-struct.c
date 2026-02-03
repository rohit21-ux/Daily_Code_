// Including standard input - output header
#include<stdio.h>


// Defining a custom type ComputeGravotational
struct ComputeGravitational
{

    double m1;
    double m2;
    double r;

};

// Function Declaration
double ComputeGravitationalForce(struct ComputeGravitational * pData);

//Entry point Function
int main (void )
{
    // Variable Declaration
    struct ComputeGravitational sunEarth;
    struct ComputeGravitational sunJupitor;

    double forceBetweenSunEarth;
    double forceBetweenSunJupitor;

    //code
    sunEarth.m1 = 1.9891e30;
    sunEarth.m2 = 5.9722e24;
    sunEarth.r = 149597871000;

    forceBetweenSunEarth = ComputeGravitationalForce(&sunEarth);
    printf("Gravitaional Force Between the Sun and the Earth = (%lf) N\n",forceBetweenSunEarth);

    sunJupitor.m1 = 1.9891e30;
    sunJupitor.m2 = 1.89813e27;
    sunJupitor.r = 760070000000;

    forceBetweenSunJupitor = ComputeGravitationalForce(&sunJupitor);
    printf("Gravitational force Between the Sun and The Jupitor = (%lf) N\n",forceBetweenSunJupitor);
    return (0);

}


double ComputeGravitationalForce(struct ComputeGravitational * pData)

{

    double G =6.67 * (10e-11);
    double F;

    F= (G *pData->m1 * pData->m2) / (pData->r * pData->r);

    return (F);
}
