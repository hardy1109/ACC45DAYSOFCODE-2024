#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int candies,pockets,hold;
	    cin>>candies>>pockets>>hold;
	    if(candies%(pockets*hold) == 0)
	    {
	        cout<<candies/(pockets*hold)<<endl;
	    }
	    else
	    {
	        cout<<(candies/(pockets*hold))+1<<endl;
	    }
	}
	return 0;
}