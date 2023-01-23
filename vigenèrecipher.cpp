// Vigenère Cipher

#include <bits/stdc++.h>
using namespace std;

string generateKey(string str, string key) {
    int a = str.size();
 
    for (int i = 0; ; i++){
        if (a == i){
            i = 0;
        }
        
        if (key.size() == str.size()){
            break;
        }
        
        key.push_back(key[i]);
    }
    return key;
}

string cipherText(string str, string key){
    string cipher_text;
 
    for (int i = 0; i < str.size(); i++){
        char a = (str[i] + key[i]) %26;
        a += 'A';
        cipher_text.push_back(a);
    }
    
    return cipher_text;
}
 
string originalText(string cipher_text, string key){
    string orig_text;
 
    for (int i = 0 ; i < cipher_text.size(); i++){
        char a = (cipher_text[i] - key[i] + 26) %26;
        a += 'A';
        orig_text.push_back(a);
    }
    
    return orig_text;
}

int main(){
    string str = "HELLOWORLD";
    string keyword = "BYE";
 
    string key = generateKey(str, keyword);
    string cipher_text = cipherText(str, key);
 
    cout << "Ciphertext : " << cipher_text << "\n";
    cout << "Original/Decrypted Text : " << originalText(cipher_text, key);
    
    return 0;
}
