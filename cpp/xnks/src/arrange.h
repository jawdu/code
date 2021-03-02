#include <cmath>
#include <iostream>
#include <vector>
std::vector<int> mevents(int& N, double lambda, int nev);
std::vector<double> momegas(int nom);
void lcmorlet(int N, std::vector<int> mev, std::vector<double> mos, std::vector<double>& lChannel, std::vector<double>& rChannel);
void mtest(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel);
