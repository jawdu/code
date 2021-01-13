/*      

    C++WavLab. Try stuff out. output stuff from soundfw.cpp 

    idea: xenakis/noise/clusters  -take (1) bits from ruby (2) some high-freq stuff (microsound)
    and try to make complex arrangements in (L-R)+time. & little 'string' fragments. stray beats?

    start: work on waveforms. try make 'electroacoustics' that slowly evolves.

*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib> 				
#include <string>
#include <sstream>
#include <vector>
using namespace std;

namespace littleEndian
{
    template <typename Word>
    std::ostream& writeWord( std::ostream& outs, Word value, unsigned size = sizeof( Word ) )
    {
        for (; size; --size, value >>= 8)
            outs.put( static_cast <char> (value & 0xFF) );
        return outs;
    }
}
using namespace littleEndian;

void writeWav(string fileName, int N, vector<double> lChannel, vector<double> rChannel);
double randDouble(double min, double max);
vector<double> makeF(int nF);
vector<double> makeA(int nF);
double maxF(int nF, vector<double> a);

int main()
{
    vector<double> lChannel, rChannel;
    
    double hz = 44100;                       // samples per second
    double seconds  = 50.0;               // time *** don't know how this will work once I make it looser
    int N = hz * seconds;                     // total number of samples

    std::stringstream ss;                                                               // setup filename with timestamp
    ss << time(0);  
    std::string fileName = "test" + ss.str() + ".wav";
  
    int nF = 60; // NOTE makeF fixed for use of 60
    vector<double> a = makeA(nF);
    vector<double> f = makeF(nF);
    double aF = maxF(nF, a) * nF;

    for (int n = 0; n < N; n++)                                         
    {
        double v = 0.0;
        for (int p = 0; p < nF; p++)
        {
            v = v + a[p]*cos(6.28*f[p]*n/44100.0);
        }

        // try aF not nF
        lChannel.push_back(v/(double)aF);
        rChannel.push_back(v/(double)aF);

    }

    writeWav(fileName, N, lChannel, rChannel);                          // write .wav and finish
    cout << endl << "done, filename: " << fileName << endl;
 
    return 0;
}

// functions

static bool abs_compare(double a, double b)
{
    return (std::abs(a) < std::abs(b));
}

vector<double> makeF(int nF)
{
    vector<double> f;

    for (int p = 0; p < 10; p++)
    {
        double f1 = randDouble(20.0, 600.0);
        for (int q = 0; q < 6; q++)
        {
            // 5 and 2, who knows
            f.push_back((5+q)*f1 / (2+q));
        }
    }
    return f;
}

vector<double> makeA(int nF)
{
    vector<double> a;
    
    for (int p = 0; p < nF; p++)
    {
        a.push_back(randDouble(0.2, 0.8));
    }
    return a;
}

double maxF(int nF, vector<double> a)
{
    double aF = 0.0;
    
    for (int p = 0; p < nF; p++)
    {
        aF = aF + *max_element(a.begin(), a.end(), abs_compare);
    }
    aF = aF / nF;

    // cout << endl << aF << endl;

    return aF;
}

double randDouble(double min, double max)
{
    // random double between min and max
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
}

void writeWav(string fileName, int N, vector<double> lChannel, vector<double> rChannel)              
{
    ofstream stream;
    stream.open(fileName.c_str(), ios::out | ios::binary);

     // Write the file headers
    stream << "RIFF----WAVEfmt ";     // (chunk size to be filled in later)
    writeWord( stream,     16, 4 );        // no extension data
    writeWord( stream,      1, 2 );         // PCM - integer samples
    writeWord( stream,      2, 2 );         // two channels (stereo file)
    writeWord( stream,  44100, 4 );     // samples per second (Hz)
    writeWord( stream, 176400, 4 );    // (Sample Rate * BitsPerSample * Channels) / 8
    writeWord( stream,      4, 2 );         // data block size (size of two integer samples, one for each channel, in bytes)
    writeWord( stream,     16, 2 );        // number of bits per sample (use a multiple of 8)

    // Write the data chunk header
    size_t dataChunkPos = stream.tellp();
    stream << "data----";                    // (chunk size to be filled in later)

    double maxAmp = 32760;          // "volume" 

    // write stuff to wavs. note: setting up so that lChannel, rChannel in range [-1, 1].

    for (int n = 0; n < N; n++)
    {
        writeWord( stream, (int)(lChannel[n] * maxAmp), 2 );
        writeWord( stream, (int)(rChannel[n] * maxAmp), 2 );
    }

    // (We'll need the final file size to fix the chunk sizes above)
    size_t fileLength = stream.tellp();

    // Fix the data chunk header to contain the data size
    stream.seekp( dataChunkPos + 4 );
    writeWord( stream, fileLength - dataChunkPos + 8 );

    // Fix the file header to contain the proper RIFF chunk size, which is (file size - 8) bytes
    stream.seekp( 0 + 4 );
    writeWord( stream, fileLength - 8, 4 ); 

}




