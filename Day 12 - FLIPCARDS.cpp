#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,x;
	    cin>>n>>x;
	    if( x == 0)
	    {
	        cout<<0<<endl;
	    }
	    else if( x == n)
	    {
	        cout<<0<<endl;
	    }
	    else
	    {
	        if(n/2 >= x)
	        {
	            cout<<x<<endl;
	        }
	        else
	        {
	            cout<<n-x<<endl;
	        }
	    }
	}
	return 0;
}
