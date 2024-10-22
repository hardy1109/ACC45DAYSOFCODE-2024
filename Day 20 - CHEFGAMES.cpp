#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int ball,count = 0;
	    for(int i =0; i<4; i++)
	    {
	        cin>>ball;
	        if(ball == 0)
	        {
	            count++;
	        }
	    }
	    if(count == 4)
	    {
	        cout<<"IN"<<endl;
	    }
	    else
	    {
	        cout<<"OUT"<<endl;
	    }
	}
	return 0;
}