#include <stdlib.h>
#include <iostream>

using namespace std;
int main (){
	u_int a[] = {0x41, 0x5d, 0x4b, 0x72, 0x3d, 0x39, 0x6b, 0x30, 0x3d, 0x30, 0x6f, 0x30, 0x3b, 0x6b, 0x31, 0x3f, 0x6b, 0x38, 0x31, 0x74};

	int l14 = 0;
	u_int *l10 = &a[0];

	while( (*l10 != 9 && (l14<0x14))) {
		cout << ((char)(*l10^9));
		l10 = l10+1;
		l14 = l14+1;
	}
	cout <<  char(10);
	
	exit(0);
}
