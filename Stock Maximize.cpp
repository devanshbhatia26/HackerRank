#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        ll arr[n];
        for(ll i=0;i<n;i++) cin>>arr[i];
        ll profit=0;
        ll max = 0;
        for(ll i=n-1;i>=0;i--){
            if(max<=arr[i]) max = arr[i];
            profit += max-arr[i];
        }
        cout<<profit<<endl;
    }
    return 0;
}

