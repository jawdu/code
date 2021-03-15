// wavelet functions
#include "utils.h"
#include "wavelets.h"

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

double gabor(double t, double omega)
{       // return gabor wavelet imaginary component. assume x0 = 0. range still [-5, 5]
    double tn = 1.0 * t;
    double a = 2.0 * 2.0;             // controls rate of exponential drop off. only a^2 term used.
    double val = exp(-1.0 * t * t / a) * -1.0 * sin(omega * t);
    return val;
}

double shannon(double t)
{
    return (2*sinc(2.0*t) - sinc(1.0*t));
    //return (2*sinc(2.0*t*omega) - sinc(1.0*t*omega));
}

