#include <algorithm>
#include <cmath>
#include <random>
#include <vector>
double randDouble(double min, double max);
double maxF(int nF, std::vector<double> a);
double sinc(double x);
void addnoise(int N, std::vector<double>& lChannel, std::vector<double>& rChannel);
void normaliser(int N, double F, std::vector<double>& lChannel, std::vector<double>& rChannel);
