#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int cons=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='a'|| s[i]=='e' || s[i]=='i' || s[i]=='o' ||s[i]=='u')
            {
                cons=0;
              continue;
                
            }
            else
            {
                cons++;
                if(cons>=4)
                  break;
            }
              
             
        }
        if(cons>=4)
          cout<<"NO"<<endl;
        else 
          cout<<"YES"<<endl;
          
          
    }
    return 0;
}
