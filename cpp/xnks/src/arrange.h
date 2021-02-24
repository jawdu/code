#include <vector>
std::vector<int> mevents(int& N);
std::vector<double> momegas(int nmev);
void lcmorlet(int N, std::vector<int> mev, std::vector<double> mos, std::vector<double>& lChannel, std::vector<double>& rChannel);
void mtest(int& N, std::vector<double>& lChannel, std::vector<double>& rChannel);
