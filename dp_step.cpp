#include<iostream>
#include<stdlib.h>
using namespace std;
//d(k, j) = d(k-1, (j-1+n)%n) + d(k-1, (j+1)%n);
int addStep(int k)
{
	int arr[2][10] = { 0 };
	int flag = 1, i = 0, j = 0;
	arr[0][0] = 1;
	for (i = 1; i<10; i++){
		arr[0][i] = 0;
	}
	// j is the current step
	for (j = 1; j <= k; j++){
		for (i = 0; i<10; i++){
			arr[flag][i] = arr[!flag][(i - 1 + 10) % 10] + arr[!flag][(i + 1) % 10];
		}
		flag = !flag;
	}
	return arr[!flag][0];
}
int main()
{
	int k;
	cout << "Please input the step k:" << endl;
	cin>>k;
	cout << get_step_num(k)<<endl;
	system("pause");
	return 0;
}
