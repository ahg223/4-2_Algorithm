#include<iostream>
#include<vector>

using namespace std;

long long answer, m;
int n, p[10];

void iter(int, int, int, vector<int>);

int main(void){
	cin >> n >> m;
    for(int i = 0; i < n; i++) cin >> p[i];
    
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            vector<int> v;
            v.push_back(j);
            iter(1, j, i, v);
            v.pop_back();
        }
    }
    cout << answer;
}

void iter(int Qsize, int start, int size, vector<int> v){
    if(Qsize == size){
    	if(size % 2){
            long long temp = 1;
            for(int i = 0; i < size ; i++)temp *= p[v[i] - 1];
            answer += m / temp;
        }
        else{
            long long temp = 1;
            for(int i =0; i < size; i++) temp *= p[v[i] - 1];
            answer -= m / temp;
        }
        return;
    }
    for(int i = start + 1; i <= n; i++){
        v.push_back(i);
        iter(Qsize + 1,i,size,v);
        v.pop_back();
    }
}
