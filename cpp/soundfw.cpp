/*      --- simple output wav framework for c++, to get working to use in future ---

    source:  https://www.cplusplus.com/forum/beginner/166954/#msg840873 

*/

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib> 				// for random
#include <string>
#include <sstream>
using namespace std;

// namespace littleEndian for .wavs to ensure file headers written correctly
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

void writeWav(string fileName);

int main()
{
    // date stamp

    std::stringstream ss;
    ss << time(0);  
    std::string ts = ss.str();
    std::string fileName = "test" + ts + ".wav";
    
    writeWav(fileName);

    cout << endl << "done, filename: " << fileName << endl;
 
    return 0;

}

// functions

void writeWav(string fileName)
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

    double maxAmp = 32760;  // "volume"
    double hz = 44100;                       // samples per second
    // double frequency = 261.626;      // middle C
    double seconds  = 1.0;                  // time
    
    int N = hz * seconds;                     // total number of samples

    // write stuff to wavs

    for (int n = 0; n < N; n++)
    {
        // white noise
        writeWord( stream, (int)((maxAmp * (rand() / ((double) RAND_MAX))) - 16000), 2 );
        writeWord( stream, (int)((maxAmp * (rand() / ((double) RAND_MAX))) - 16000), 2 );
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










