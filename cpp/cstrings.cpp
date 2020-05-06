// string simulation, changable dimensions

#include <iostream>
#include <stdlib.h> 			// dunno yet
#include <cmath>				// presumably...
#include <cstdlib> 				// for random
#include <vector>				// for use of vector object
#include <algorithm>    		// std::sort
#include <time.h>					// clock time stuff

using namespace std;

using std::cin;         using std::endl;		
using std::cout;		using std::string;

// global variables
const float pi = 3.14159265358979f;		// pi

// functions 

void phaseSetup(int meshRes, vector<int>& stringXY, vector<int>& stringYZ, vector<int>& stringZX);
int strCheck(float a, float b, float c, float d);
bool compare_abs(const int& a, const int& b);
bool compare_int(const int& a, const int& b);
int findNode(vector<int> stringVec, int nodeNum);
int stringCount(int meshRes, vector<int>& stringLength, vector<int>& stringXY, vector<int>& stringYZ, vector<int>& stringZX);
void eraseEntry(int which, int entryNum, vector<int>& stringXY, vector<int>& stringYZ, vector<int>& stringZX);
void nextCell(int& indexOld, int& indexNow, int& nodeNow, int nodeStart, int& phase, bool& closed, int& face, 
	int& faceOld, int faceStart, int meshRes, int mRS, vector<int> stringXY, vector<int> stringYZ, vector<int> stringZX);
bool checkNextFace(int node, int phase, vector<int> stringXYZ);

int main ( ) 
{
	clock_t	startTime = clock();					// clock
	int meshRes;									// mesh resolution
	vector<int> stringXY, stringYZ, stringZX;		// vectors holding +-nodeNumber for location-type of strings
	vector<int> stringLength, slBin, slCount;		// record string lengths here, slBin for sorting later
	srand (time(NULL));								// set this up

	cout << endl << " ... ::: ******************** ::: ..." << endl;
	cout << endl << " ... The 2013 C++ version of Cosmic String Phase Transition Simulation " << endl;
	cout << endl << " ... Please enter mesh resolution desired, integer expected: " << endl;

	
	while (1) {					// get input of simulation dimension
		if (cin >> meshRes) {
			// valid number
			break;
		} else {
			// not a valid number
			cout << " ... *** Invalid Input! Please input an integer value. *** " << endl;
			cin.clear();
			while (cin.get() != '\n') ; // empty loop
	  	}
	}							// done getting input

	cout << endl << " ... ::: Value of integer to be used: " << meshRes << endl;

	// phaseSetup to obtain phases at nodes and add strings
	phaseSetup(meshRes, stringXY, stringYZ, stringZX);

	cout << endl << " ... now onto analysis ... " << endl;

	// vectors somewhat unsorted, fix
	sort(stringXY.begin(), stringXY.end(), compare_abs);
	sort(stringYZ.begin(), stringYZ.end(), compare_abs);
	sort(stringZX.begin(), stringZX.end(), compare_abs);

	cout << endl << " ... vector size sanitychecks: " << stringXY.size() << " " 
			<< stringYZ.size() << " " << stringZX.size() << endl;

	// into the void...

	cout << " ... starting string count... " << endl;

	int q = 0;
	while (q == 0) {	
		q = stringCount(meshRes, stringLength, stringXY, stringYZ, stringZX);
		//if (q == 0) {cout << " ... ::: string found, length = " << stringLength[stringLength.size() - 1] << " " << endl;}
	}

	// string analysis
	
	cout << endl << " ... ::: final numbers - total string count = " << stringLength.size() << endl;
	sort(stringLength.begin(), stringLength.end(), compare_int);
	slBin.push_back(stringLength[0]);
	slCount.push_back(1);
	int lastSLC = 0;
	for (int q = 1; q < stringLength.size(); q++) {
		if (stringLength[q] == stringLength[q-1]) { slCount[lastSLC]++;}
		else { slBin.push_back(stringLength[q]); slCount.push_back(1); lastSLC++;}
	}

	int smallCount = 0;
	bool doneSC = 0;
	for (int q = 0; q < slBin.size(); q++) {
		if (slBin[q] < 100) { smallCount = smallCount + slCount[q]; }			// bin small strings
		else {
			if (!doneSC) { 			// not printed small ones out, so do that
				cout << " ... ::: - for string length < 100, " << smallCount << " strings were found." << endl;
				doneSC =! doneSC;
			}
			// and do other string
			if (slCount[q] == 1) { cout << " ... ::: - for string length = " << slBin[q] << ", " << slCount[q] << " string was found." << endl; }
			else { cout << " ... ::: - for string length = " << slBin[q] << ", " << slCount[q] << " strings were found." << endl; }
		}
	}

	cout << endl << " ... ::: cstring took ";
	cout << double( clock() - startTime ) / (double)CLOCKS_PER_SEC<< " seconds to run this time." << endl;

	cout << endl << " ... all done, bye! " << endl;
	cout << endl << " ... ::: ******************** ::: ..." << endl;

	return 0;

}

void phaseSetup(int meshRes, vector<int>& stringXY, vector<int>& stringYZ, vector<int>& stringZX)
// set up phases; later, write stuff or something...
{
	bool reversed = 0;		    // reversed order for node arrays. 
								// this will control which get written to, etc.

	float prevNodes[meshRes*meshRes], nextNodes[meshRes*meshRes];			// node arrays
	int a, b, c, d, nodeNum;		// nodes
	int mRS = meshRes * meshRes;			// easier
	int stringRes; int faceCount = 0; int stringCount = 0; int netStringCount = 0;

	cout << endl << " ... going into phaseSetup with mesh resolution = " << meshRes << endl;

	// initalise first array so we can check for strings in loop without clauses
	for (int ifa = 0; ifa < (mRS); ifa++) { prevNodes[ifa] = 0; }

	for (int z = 1; z < meshRes; z++) {		// Z LOOP start at 1 to allow checking for strings in-loop
											// also as z = 0 are all 0...
	
		if (!reversed) {					// write to nextNodes
			for (int y = 0; y < meshRes; y++) {
				for (int x = 0; x < meshRes; x++) {
					if (y == 0 || x == 0 || y == (meshRes-1) || x == (meshRes-1) || z == (meshRes-1)) {
					nextNodes[(y * meshRes) + x] = 0;
					} else {
					nextNodes[(y * meshRes) + x] = 2 * pi * ((float) rand() / (RAND_MAX));
					}
				}
			}
		} else {							// write to prevNodes
			for (int y = 0; y < meshRes; y++) {
				for (int x = 0; x < meshRes; x++) {
					if (y == 0 || x == 0 || y == (meshRes-1) || x == (meshRes-1) || z == (meshRes-1)) {
					prevNodes[(y * meshRes) + x] = 0;
					} else {
					prevNodes[(y * meshRes) + x] = 2 * pi * ((float) rand() / (RAND_MAX));
					}
				}
			}
		}									// end of if-else for write phases
	
		// Now check for strings and write to the 2 vectors for this
		// check 3 faces / node looped over (not all looped over, obv!)

		for (int y = 0; y < (meshRes - 1); y++) {		
			for (int x = 0; x < (meshRes - 1); x++) {
				// get node #s 
				nodeNum = y + (x * meshRes) + ((z - 1) * mRS);	// for indexing
				// a - d 'local' numbers w.r.t. x, y only					
				a = y + (x * meshRes);
				b = a + meshRes; c = a + 1 + meshRes; d = a + 1;
				// e = a but for other array; f = b; g = d;					
					
				if (z != 1) {
					faceCount++;
					// XY face pass (a, b, c, d)
					if (!reversed) {						// prevNodes is previous
						stringRes = strCheck(prevNodes[a], prevNodes[b], prevNodes[c], prevNodes[d]);
					} else {
						stringRes = strCheck(nextNodes[a], nextNodes[b], nextNodes[c], nextNodes[d]);
					}
					stringCount = stringCount + abs(stringRes);
					netStringCount = netStringCount + stringRes;
					// if string found
					if (stringRes != 0) {
						stringXY.push_back(stringRes*nodeNum);
					}
				}

				if (x != 0) {
					faceCount++;
					// YZ face pass (a, d, g, e)
					// reversed makes a difference of direction, so this or *-1
					if (!reversed) {
						stringRes = strCheck(prevNodes[a], prevNodes[d], nextNodes[d], nextNodes[a]);
					} else {
						stringRes = strCheck(nextNodes[a], nextNodes[d], prevNodes[d], prevNodes[a]);
					}
					stringCount = stringCount + abs(stringRes);	
					netStringCount = netStringCount + stringRes;
					// if string found
					if (stringRes != 0) {
						stringYZ.push_back(stringRes*nodeNum);
					}

				}					

				if (y != 0) {
					faceCount++;
					// ZX face pass (a, e, f, b)
					// reversed makes a difference of direction, so this or *-1
					if (!reversed) {
						stringRes = strCheck(prevNodes[a], nextNodes[a], nextNodes[b], prevNodes[b]);
					} else {
						stringRes = strCheck(nextNodes[a], prevNodes[a], prevNodes[b], nextNodes[b]);
					}
					stringCount = stringCount + abs(stringRes);					
					netStringCount = netStringCount + stringRes;
					// if string found
					if (stringRes != 0) {
						stringZX.push_back(stringRes*nodeNum);
					}
				}

			}
		}

		reversed = !reversed;				// flip bool reversed other way
	} 										// Z LOOP end

	cout << endl << " ... sanity checks: faceCount = " << faceCount << ", stringCount = " 
			<< stringCount << ", net string count = " << netStringCount << endl;

	cout << endl << " ... all done with phaseSetup!" << endl;

}


void eraseEntry(int which, int entryNum, vector<int>& stringXY, vector<int>& stringYZ, vector<int>& stringZX)
{
	if ((which == 1) && (entryNum < stringXY.size())) {
		//cout << "deleting from XY: " << entryNum << " size = " << stringXY.size() << endl;
		stringXY.erase(stringXY.begin()+entryNum);
	} else if ((which == 2) && (entryNum < stringYZ.size())){
		//cout << "deleting from YZ: " << entryNum << " size = " << stringYZ.size() <<  endl;
		stringYZ.erase(stringYZ.begin()+entryNum);
	} else if ((which == 3) && (entryNum < stringZX.size())){
		//cout << "deleting from ZX: " << entryNum << " size = " << stringZX.size() <<  endl;
		stringZX.erase(stringZX.begin()+entryNum);
	} else {
		cout << " ... ERROR eraseEntry .. " << endl;
    	exit (EXIT_FAILURE);
	}

}


int strCheck(float a, float b, float c, float d)
// check for string
{
	int s;
	float l[4];
	float lSum = 0;
	l[0] = b - a;
	l[1] = c - b;
	l[2] = d - c;
	l[3] = a - d;

	for (int k = 0; k < 4; k++) {
		if (l[k] > pi) { 
			l[k] = l[k] - 2*pi; 
		}
		else if (l[k] < -pi) { 
			l[k] = l[k] + 2*pi; 
		}
		lSum = lSum + l[k];
	}

	s = (int) rintf(lSum / (2*pi));

	return s;
}

bool compare_abs(const int& a, const int& b)
// for sorting by abs value
{
    return (abs(a) < abs(b));
}

bool compare_int(const int& a, const int& b)
// for sorting by int value
{
    return (a < b);
}

int findNode(vector<int> stringVec, int nodeNum)
{
	// loop escape - maximum number of halving from stringVec.size()
	int maxSteps = 1 + (int) ceil(log(stringVec.size()) / log(2));				
	int trialPos = (int) round(stringVec.size() / 2);
	int minPos = -1;		// or it won't pick up first entry
	int maxPos = stringVec.size(); 

	for (int p = 0; p < maxSteps; p++) {
		if (abs(stringVec[trialPos]) < nodeNum) {
			// trialPos too small
			minPos = trialPos;		
			trialPos = trialPos + (int) round(((maxPos - trialPos) / 2));
		}
		else if (abs(stringVec[trialPos]) > nodeNum) {
			// trialPos too big
			maxPos = trialPos;
			trialPos = trialPos - (int) round(((trialPos - minPos) / 2));
		}
		else
		{ 	// check for neighbours - can be + & -!
			// maybe doesn't matter - doubt either is favoured, so no bias.
			return (trialPos);
		}
	}

	return -1;			// if none found. return 0 is valid obviously!
}



int stringCount(int meshRes, vector<int>& stringLength, vector<int>& stringXY, vector<int>& stringYZ, vector<int>& stringZX)
{
// use variable f to record which face, (+-1 F_xy, +-2 F_yz, +-3 F_zx)
// now, control by when stringXYYZZX vectors become empty
                    
	int face, faceStart, faceOld;			// +-1 2 or 3. faceOld used for index to eraseEntry
	int phase;								// i.e. s from matlab code. +1 increasing F_ij, -1 decreasing F_ij
	int indexOld, indexNow;					// index of array.
	int nodeStart, nodeNow;					// starting node / current node
	int numSteps = 0;						// to record length
	int mRS = meshRes * meshRes;
	bool closed = 0;						//

	//cout << endl << " ... into stringCount *gulp* ... " << endl;

	// get starting face
	if (!stringXY.empty()) {
  		indexOld = rand() % stringXY.size();
		nodeStart = abs(stringXY[indexOld]);
		faceStart = stringXY[indexOld] / nodeStart;

	} else if (!stringYZ.empty()) {					//(stringYZ.size() > 0) {
  		indexOld = rand() % stringYZ.size();
		nodeStart = abs(stringYZ[indexOld]);
		faceStart = 2 * stringYZ[indexOld] / nodeStart;

	} else if (!stringZX.empty()) {					//(stringZX.size() > 0) {
  		indexOld = rand() % stringZX.size();
		nodeStart = abs(stringZX[indexOld]);
		faceStart = 3 * stringZX[indexOld] / nodeStart;

	} else { 
		cout << endl << " ... all vectors empty! ... " << endl;
		return 1;
	}

	nodeNow = nodeStart; face = faceStart; phase = faceStart / abs(faceStart); indexNow = indexOld;

	// start loop

	while (!closed) {

		//cout << endl << ":::::: Pre next cell number dump: indexOld " << indexOld << " indexNow " << indexNow << " nodeNow " << nodeNow
			//		<< " phase " << phase << " face " << face << " faceOld " << faceOld << " faceStart " << faceStart << endl;
		
		int yCur = ((nodeNow % mRS) % meshRes);
		int xCur = ((nodeNow - yCur) % mRS) / meshRes;
		int zCur = (nodeNow - yCur - (xCur * meshRes)) / mRS;
		//cout << " x, y, z: " << xCur << " " << yCur << " " << zCur << endl;

		nextCell(indexOld, indexNow, nodeNow, nodeStart, phase, closed, 
			face, faceOld, faceStart, meshRes, mRS, stringXY, stringYZ, stringZX);

		//cout << "::::: Post next cell number dump: indexOld " << indexOld << " indexNow " << indexNow << " nodeNow " << nodeNow
		//			<< " phase " << phase << " face " << face << " faceOld " << faceOld << endl;

		// after these, remove
		if (!closed) {
			//cout << " sizes alert: XY / YZ / ZX : " << stringXY.size() << " " << stringYZ.size() << " " << stringZX.size() << endl; 
			//cout << " .. numsteps now: " << numSteps << " and deleting from " << faceOld << " entry " << indexOld << endl;
			eraseEntry(abs(faceOld), indexOld, stringXY, stringYZ, stringZX);
			if ((indexNow > indexOld) && (abs(face) == abs(faceOld))) { indexNow--; } 		
		} // something not getting erased here

		numSteps++;
		
		if (closed) {
			// finished, delete last entry using indexNow		
			eraseEntry(abs(faceOld), indexNow, stringXY, stringYZ, stringZX);
			// add completed string to length vector
			stringLength.push_back(numSteps);
		}

		// infinity check
		if (numSteps > (mRS * meshRes)) { closed = !closed; }
	}

	// end loop

	return 0;	                // done :)
	
}

void nextCell(int& indexOld, int& indexNow, int& nodeNow, int nodeStart, int& phase, bool& closed, int& face, 
		int& faceOld, int faceStart, int meshRes, int mRS, vector<int> stringXY, vector<int> stringYZ, vector<int> stringZX)
{
	faceOld = face; 				
	
	if (face == 1) {

		if ((((nodeNow + mRS) == nodeStart) && (faceStart == phase)) ||			// +xy (this and below 4 are checking for closure)
			((nodeNow == nodeStart) && (faceStart == -2 * phase)) ||			// -yz
		 	(((nodeNow + meshRes) == nodeStart) && (faceStart == 2 * phase)) || // +yz
			((nodeNow == nodeStart) && (faceStart == -3 * phase)) ||			// -zx
			(((nodeNow + 1) == nodeStart) && (faceStart == 3 * phase))) {		// +zx			
				// trigger end
				closed = !closed;
		}
											// now conditions for finding next non-closure face, corresponds to cases above
		
		else if (checkNextFace(nodeNow + mRS, phase, stringXY)) {
			indexOld = indexNow;								// moved on, indexOld will be deleted now
			nodeNow = nodeNow + mRS;							// have a node at (nodeNow + mRS), move there
			indexNow = findNode(stringXY, nodeNow);				// get array index value for (nodeNow + mRS)
			//faceOld = face;									// no change of face, face unchanged
		}
		else if (checkNextFace(nodeNow, -phase, stringYZ)) {
			indexOld = indexNow; 
			indexNow = findNode(stringYZ, nodeNow);
			face = -2; 
			phase = -phase;
		}
		else if (checkNextFace(nodeNow + meshRes, phase, stringYZ)) {
			indexOld = indexNow;
			nodeNow = nodeNow + meshRes;
			indexNow = findNode(stringYZ, nodeNow);
			face = 2;
		}
		else if (checkNextFace(nodeNow, -phase, stringZX)) {
			indexOld = indexNow;								
			indexNow = findNode(stringZX, nodeNow);			
			face = -3;
			phase = -phase;
		}
		else if (checkNextFace(nodeNow + 1, phase, stringZX)) {
			indexOld = indexNow;
			nodeNow = nodeNow + 1;
			indexNow = findNode(stringZX, nodeNow);
			face = 3;
		}

		//else { cout << endl << "error in next cell face 1" << endl; }
	}															// end of face = 1

	else if (face == -1) {

		if ((((nodeNow - mRS) == nodeStart) && (faceStart == phase)) || 			// -xy 
			(((nodeNow - mRS) == nodeStart) && (faceStart == 2 * phase)) ||			// -yz
		 	(((nodeNow + meshRes - mRS) == nodeStart) && (faceStart == -2 * phase)) || 	// +yz
			(((nodeNow - mRS) == nodeStart) && (faceStart == 3 * phase)) ||			// -zx
			(((nodeNow + 1 - mRS) == nodeStart) && (faceStart == -3 * phase))) {			// +zx			
				// trigger end
				closed = !closed;
		}

		else if (checkNextFace(nodeNow - mRS, phase, stringXY)) {
			indexOld = indexNow;
			nodeNow = nodeNow - mRS;
			indexNow = findNode(stringXY, nodeNow);
		}

		else if (checkNextFace(nodeNow - mRS, phase, stringYZ)) {
			indexOld = indexNow; 
			nodeNow = nodeNow - mRS;
			indexNow = findNode(stringYZ, nodeNow);
			face = -2; 
		}

		else if (checkNextFace(nodeNow + meshRes - mRS, -phase, stringYZ)) {
			indexOld = indexNow;
			nodeNow = nodeNow + meshRes - mRS;
			indexNow = findNode(stringYZ, nodeNow);
			face = 2; 
			phase = -phase;
		}

		else if (checkNextFace(nodeNow - mRS, phase, stringZX)) {
			indexOld = indexNow;
			nodeNow = nodeNow - mRS;
			indexNow = findNode(stringZX, nodeNow);
			face = -3; 
		}

		else if (checkNextFace(nodeNow + 1 - mRS, -phase, stringZX)) {
			indexOld = indexNow;
			nodeNow = nodeNow + 1 - mRS;
			indexNow = findNode(stringZX, nodeNow);
			face = 3; 
			phase = -phase;
		}

		//else { cout << endl << "error in next cell face -1" << endl; }
	}															// end of face = -1

	else if (face == 2) {

		if ((((nodeNow + meshRes) == nodeStart) && (faceStart == 2 * phase)) ||			// +yz 
			((nodeNow == nodeStart) && (faceStart == -3 * phase)) ||					// -zx
		 	(((nodeNow + 1) == nodeStart) && (faceStart == 3 * phase)) || 				// +zx
			((nodeNow == nodeStart) && (faceStart == -1 * phase)) ||					// -xy
			(((nodeNow + mRS) == nodeStart) && (faceStart == phase))) {					// +xy			
				// trigger end
				closed = !closed;
		}

		else if (checkNextFace(nodeNow + meshRes, phase, stringYZ)) {   
			indexOld = indexNow;
			nodeNow = nodeNow + meshRes;
			indexNow = findNode(stringYZ, nodeNow);
		}

		else if (checkNextFace(nodeNow, -phase, stringZX)) { 
			indexOld = indexNow; 
			indexNow = findNode(stringZX, nodeNow);
			face = -3;
			phase = -phase; 
		}

		else if (checkNextFace(nodeNow + 1, phase, stringZX)) {
			indexOld = indexNow;
			nodeNow = nodeNow + 1;
			indexNow = findNode(stringZX, nodeNow);
			face = 3; 
		}

		else if (checkNextFace(nodeNow, -phase, stringXY)) {  
			indexOld = indexNow;
			indexNow = findNode(stringXY, nodeNow);
			face = -1; 
			phase = -phase;
		}

		else if (checkNextFace(nodeNow + mRS, phase, stringXY)) { 
			indexOld = indexNow;
			nodeNow = nodeNow + mRS;
			indexNow = findNode(stringXY, nodeNow);
			face = 1; 
		}

		//else { cout << endl << "error in next cell face 2" << endl; }
	}															// end of face = 2

	else if (face == -2) {

		if ((((nodeNow - meshRes) == nodeStart) && (faceStart == 2 * phase)) ||		// -yz 
			(((nodeNow - meshRes) == nodeStart) && (faceStart == 3 * phase)) ||		// -zx
		 	(((nodeNow - meshRes + 1) == nodeStart) && (faceStart == -3 * phase)) || 	// +zx
			(((nodeNow - meshRes) == nodeStart) && (faceStart == phase)) ||		// -xy
			(((nodeNow - meshRes + mRS) == nodeStart) && (faceStart == -1 * phase))) {		// +xy			
				// trigger end
				closed = !closed;
		}

		else if (checkNextFace(nodeNow - meshRes, phase, stringYZ)) {   
			indexOld = indexNow;
			nodeNow = nodeNow - meshRes;
			indexNow = findNode(stringYZ, nodeNow);
		}

		else if (checkNextFace(nodeNow - meshRes, phase, stringZX)) { 
			indexOld = indexNow;
			nodeNow = nodeNow - meshRes;
			indexNow = findNode(stringZX, nodeNow);
			face = -3;
		}

		else if (checkNextFace(nodeNow - meshRes + 1, -phase, stringZX)) {
			indexOld = indexNow;
			nodeNow = nodeNow - meshRes + 1;
			indexNow = findNode(stringZX, nodeNow);
			face = 3; 
			phase = -phase; 
		}

		else if (checkNextFace(nodeNow - meshRes, phase, stringXY)) {  
			indexOld = indexNow;
			nodeNow = nodeNow - meshRes;
			indexNow = findNode(stringXY, nodeNow);
			face = -1; 
		}

		else if (checkNextFace(nodeNow - meshRes + mRS, -phase, stringXY)) { 
			indexOld = indexNow;
			nodeNow = nodeNow - meshRes + mRS;
			indexNow = findNode(stringXY, nodeNow);
			face = 1; 
			phase = -phase;
		}

		//else { cout << endl << "error in next cell face -2" << endl; }
	}															// end of face = -2

	else if (face == 3) {

		if ((((nodeNow + 1) == nodeStart) && (faceStart == 3 * phase)) ||			// zx 
			((nodeNow == nodeStart) && (faceStart == -1 * phase)) ||				// -xy
		 	(((nodeNow + mRS) == nodeStart) && (faceStart == phase)) ||		 		// +xy
			((nodeNow == nodeStart) && (faceStart == -2 * phase)) ||				// -yz
			(((nodeNow + meshRes) == nodeStart) && (faceStart == 2 * phase))) {		// +yz			
				// trigger end
				closed = !closed;
		}

		else if (checkNextFace(nodeNow + 1, phase, stringZX)) {   
			indexOld = indexNow;
			nodeNow = nodeNow + 1;
			indexNow = findNode(stringZX, nodeNow);
		}

		else if (checkNextFace(nodeNow, -phase, stringXY)) { 
			indexOld = indexNow;
			indexNow = findNode(stringXY, nodeNow);
			face = -1;
			phase = -phase; 
		}

		else if (checkNextFace(nodeNow + mRS, phase, stringXY)) {
			indexOld = indexNow;
			nodeNow = nodeNow + mRS;
			indexNow = findNode(stringXY, nodeNow);
			face = 1; 

		}

		else if (checkNextFace(nodeNow, -phase, stringYZ)) {  
			indexOld = indexNow;
			indexNow = findNode(stringYZ, nodeNow);
			face = -2;
			phase = -phase;
		}

		else if (checkNextFace(nodeNow + meshRes, phase, stringYZ)) { 
			indexOld = indexNow;
			nodeNow = nodeNow + meshRes;
			indexNow = findNode(stringYZ, nodeNow);
			face = 2; 
		}

		//else { cout << endl << "error in next cell face 3" << endl; }
	}															// end of face = 3

	else if (face == -3) {

		if ((((nodeNow - 1) == nodeStart) && (faceStart == 3 * phase)) ||				// zx 
			(((nodeNow - 1) == nodeStart) && (faceStart == phase)) ||				// -xy
		 	(((nodeNow - 1 + mRS) == nodeStart) && (faceStart == -1 * phase)) ||		 		// +xy
			(((nodeNow - 1) == nodeStart) && (faceStart == 2 * phase)) ||				// -yz
			(((nodeNow - 1 + meshRes) == nodeStart) && (faceStart == -2 * phase))) {		// +yz			
				// trigger end
				closed = !closed;
		}

		else if (checkNextFace(nodeNow - 1, phase, stringZX)) {   
			indexOld = indexNow;
			nodeNow = nodeNow - 1;
			indexNow = findNode(stringZX, nodeNow);
		}

		else if (checkNextFace(nodeNow - 1, phase, stringXY)) { 
			indexOld = indexNow;
			nodeNow = nodeNow - 1;
			indexNow = findNode(stringXY, nodeNow);
			face = -1;
		}

		else if (checkNextFace(nodeNow -1 + mRS, -phase, stringXY)) {
			indexOld = indexNow;
			nodeNow = nodeNow -1 + mRS;
			indexNow = findNode(stringXY, nodeNow);
			face = 1; 
			phase = -phase; 
		}

		else if (checkNextFace(nodeNow - 1, phase, stringYZ)) {  
			indexOld = indexNow;
			nodeNow = nodeNow - 1;
			indexNow = findNode(stringYZ, nodeNow);
			face = -2;
		}

		else if (checkNextFace(nodeNow - 1 + meshRes, -phase, stringYZ)) { 
			indexOld = indexNow;
			nodeNow = nodeNow - 1 + meshRes;
			indexNow = findNode(stringYZ, nodeNow);
			face = 2; 
			phase = -phase;
		}

		//else { cout << endl << "error in next cell face -3" << endl; }
	}															// end of face = -3

	else {
	// error somewhere
		cout << endl << " ... ERROR nextCell .. face = " << face << endl ;
		exit (EXIT_FAILURE);
	}

}


bool checkNextFace(int node, int phase, vector<int> stringXYZ)
{
	// first check if node invalid value
	if (node < 0) { cout << " FUCK THIS IS BAD " << endl;}
	// check for empty vector
	if (stringXYZ.size() == 0) { return 0; } 
	
	int k = findNode(stringXYZ, node);

	if ((k >= 0) && ((stringXYZ[k] / abs(stringXYZ[k])) == phase)) {
		//cout << " success in checkNextFace: k = " << k << ", stringxyz: " << stringXYZ[k] << " ::: *** ::: ___ ::: ########## " << endl;
		return 1; }
	else { return 0;}
}









