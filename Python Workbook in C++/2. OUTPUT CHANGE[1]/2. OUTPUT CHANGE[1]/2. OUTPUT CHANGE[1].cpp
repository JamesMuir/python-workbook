// 2. OUTPUT CHANGE[1].cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	int varOne = 5;
	int varTwo = 2;
	int varThree = 7;

	cout << varOne << endl;
	cout << varTwo << endl;
	cout << varThree << endl;

	varOne = 12;
	varTwo = 22;
	varOne = 77;

	cout << varOne << endl;
	cout << varTwo << endl;
	cout << varThree << endl;

    return 0;
}

