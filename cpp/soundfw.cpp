// get writing .wav for cpp sorted

/* more to do

https://stackoverflow.com/a/50916141 tog et filename with timestamp

*/


#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

// global variables
// function list

void writeWav(string fileName);

int main()
{

    // prepare date stamp next as well
    std::string fileName = "test.wav";
    cout << endl << "filename: " << fileName << endl;
    
    writeWav(fileName);
 
    return 0;

}

// functions

void writeWav(string fileName)
{
    // https://stackoverflow.com/a/31038528

    //https://www.reddit.com/r/cpp/comments/85uzkr/github_supersimple_intro_program_for_generating/
    //^ compare and contrast?


    ofstream stream;
    stream.open(fileName.c_str(), ios::out | ios::binary);

/*    double samplerate = 44100.00; // Sample rate
    double frequency = 200.00; // Frequency

    int bufferSize = (1/frequency)*samplerate; 
    stream.write("RIFF", 4);                    // RIFF chunk
    write<int>(stream, 36 + bufferSize*sizeof(int)); // RIFF chunk size in bytes
    stream.write("WAVE", 4);                    // WAVE chunk
    stream.write("fmt ", 4);                    // fmt chunk
    write32(stream, 16);                     // size of fmt chunk
    write16(stream, 1);                       // Format = PCM
    write16(stream, 1);                       // # of Channels
    write32(stream, samplerate);                // Sample Rate  
    write32(stream, samplerate*sizeof(int));    // Byte rate
    write16(stream, sizeof(int));             // Frame size
    write16(stream, 24);                      // Bits per sample
    stream.write("data", 4);                   // data chunk
    write32(stream, bufferSize*sizeof(int));   // data chunk size in bytes


    // Now that the header is out of the way, you'll just need to modify your loop to first convert the double (-1.0,1.0) samples into 32-bit signed int. Truncate the bottom 8-bits since you only want 24-bit and then write out the data. Just so you know, it is common practice to store 24-bit samples inside of a 32-bit word because it is much easier to stride through using native types.

    for (int i = 0; i < bufferSize; ++i) // 
    {
        double tmp = 0.0;  // what the osund is (or grab from array) so this is dummy val for now
        int intVal = (int)(tmp * 2147483647.0) & 0xffffff00;
        stream << intVal;
    }
*/
    return 0;

}










