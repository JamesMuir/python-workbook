// 3. IRRATATING PARROT[1].cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string name, question;
	unsigned int age;
	while (true) {
		cout << "Please enter name: ";
		cin >> name;
		cout << "Your name is " << name << endl;

		cout << "Please enter age: ";
		cin >> age;
		cout << "Your age is " << age << endl;

		cout << "Please enter the correct word to brake out of the never ending loop: ";
		cin >> question;
		
		if (question == "word") {
			break;
		}
		else {
			cout << "You are a failure." << endl;
		}
	}
    return 0;
}

