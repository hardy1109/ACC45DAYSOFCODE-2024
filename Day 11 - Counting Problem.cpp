#include <iostream>
#include <vector>

using namespace std;
int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector<long long> arr; 
        for (int i = 0; i < N; i++) {
            long long x;
            cin >> x;
            arr.push_back(x); 
        }
        int odd_count = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] % 2 != 0) {
                odd_count++;
            }
        }
        if (odd_count >= 2) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
