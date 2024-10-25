#include <iostream>
#include <string.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int count1 = 0, count2 = 0;
	    for(int i =0; i<n; i++)
	    {
	        string str;
	        cin>>str;
	        if(str == "START38")
	            count1++;
	        else
	            count2++;
	    }
	    cout<<count1<<" "<<count2<<endl;
	}
	return 0;
}