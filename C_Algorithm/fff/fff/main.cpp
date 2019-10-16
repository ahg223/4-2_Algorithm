//
//  main.cpp
//  fff
//
//  Created by AHG223 on 2019/09/30.
//  Copyright © 2019 None. All rights reserved.
//

#include <iostream>
//#include <bits/stdc++.h>

using namespace std;

class AHG {
    
public:
    int value = 0;
    void func0() {
        cout << "AHG func0" << endl;
        cout << value << endl;
    }
    virtual void func1() {
        cout << "AHG func1" << endl;
    }
    virtual void func2() = 0;
};

class Child : public AHG {
    
public:
    void setValue(int temp) {
        value = temp;
    }
    void func0() {
        cout << "Child func0" << endl;
    }
    void func1() override {
        cout << "Child func1" << endl;
    }
    void func2() override {
        cout << "Child func2" << endl;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    Child child;
    Child *pch = new Child();
    AHG* ptr = &child;
    
    child.setValue(1);
    ptr->func0();   // AHG func0 \n 1
    ptr->func1();   // Child func1
    
    return 0;
}
