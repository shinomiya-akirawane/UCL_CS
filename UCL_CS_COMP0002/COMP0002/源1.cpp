#include <iostream>
#include <string>
using namespace std;
bool ispalin(std::string s) {
    int len = size(s);
    int p1 = 0, p2 = len - 1;
    while (p2 > p1) {
        if (s[p1] != s[p2])
            return false;
        p1++;
        p2--;
    }
    return true;
}
char s1[20][1000];
string solution(string input) {
    int ord = 0;
    int posx = 0, posy = 0;
    int x1 = 0, y1 = 0;
    string e="";
    string ans="";
    int len_max = 0;
    for (int x = 0; x < size(input); x++) {
        ord = input[x];
        if ((ord >= 65 && ord <= 90) || (ord >= 97 && ord <= 122)) {
            s1[posx][posy] = input[x];
            posx++;
        }
        else {
            posx = 0;
            posy++;
        }
    }
    for (int y = 0; y <= 100; y++) {
        for (int x = 0; x <= 15; x++) {
            e+= s1[x][y];
        }
        if (ispalin(e) && size(e)>len_max) {
            len_max =e.length();
            ans = e;
        }
    }
    return ans;
}
int main() {
    using namespace std; 
    cout << solution("bob racecar")<<endl;
    return 0;
}