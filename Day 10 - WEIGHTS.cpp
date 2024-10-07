#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int w,a,b,c;
	    cin>>w>>a>>b>>c;
	    if(w == a || w == b|| w == c|| w == a+b|| w == b+c|| w == c+a || w == a+b+c)
	    {
	        cout<<"YES"<<endl;
	    }
	    else
	    {
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}