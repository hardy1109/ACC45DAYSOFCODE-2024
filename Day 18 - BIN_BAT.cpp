#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,a,b;
	    cin>>n>>a>>b;
	    int count = 0;
	    while(n>0)
	    {
	        count++;
	        n = n/2;
	    }
	    count = count-1;
        cout<<(count*(a+b))-b<<endl;
	}
	return 0;
}