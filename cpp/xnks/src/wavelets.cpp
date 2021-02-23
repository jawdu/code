// wavelet functions

#include "wavelets.h"
#include <cmath>

double morlet(double t, double omega)
{           // return morlet wavelet value for a t, omega
    // IMPORTANT: the t passed here should be converted from int and also to suitable range about 0
    double tn = 1.0 * t;            
    double pi = 0.7511255;
    double ct = 1.0 + exp(-0.1*omega*omega) - 2*exp(-0.75*omega*omega);
    double co = pow(ct, -0.5);
    double ko = exp(-0.5*omega*omega);
    double val = co * pi * exp(-0.5*t*t) * (cos(omega*t) - ko);
    return val;
}
