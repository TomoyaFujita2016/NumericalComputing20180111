#include <stdio.h>
#include <string.h>

#define FILE_PATH "./input.txt"
#define IH_LIMIT 256
#define IV_LIMIT 256

void displayWords();
void inputText();
void splitLine(char*);
void wordChecker(char*);
void sort();

char words[IV_LIMIT][IH_LIMIT];
int wordFreq[IV_LIMIT];
int wordCnt = 0;

int main(void){
    inputText();
    sort();
    displayWords();
    return 0;
}

void displayWords(){
    for(int i = 0; i < wordCnt; i ++){
        printf("[ %s ] :[ %d ]\n", words[i], wordFreq[i]);
    }
}

void inputText(){
    FILE* fp;
    char line[IH_LIMIT];
    if ((fp=fopen(FILE_PATH,"r")) != NULL){
        while(fgets(line, IV_LIMIT, fp) != NULL){
            splitLine(line);
        }
    }else{
        printf("I can't read this file : %s", FILE_PATH);
    }
    fclose(fp);
}

void splitLine(char* line){
    char* word = strtok(line, " \n");
    wordChecker(word);
    while(word != NULL) {
        word = strtok(NULL, " \n");
        if(word != NULL) {
            wordChecker(word);   
        }
    }
}

void wordChecker(char* word){
    for(int i = 0; i < wordCnt; i ++){
        if(strcmp(word, words[i]) == 0){
            wordFreq[i] ++;
            return;
        }
    }
    strcpy(words[wordCnt], word);
    wordFreq[wordCnt] ++;
    wordCnt ++;
    return;
}

void sort(){
    char tmpStr[IH_LIMIT];
    int tmpInt;
    for(int i=0; i < wordCnt; i ++){
        for(int n=wordCnt-1; n > i; n --){
            if(wordFreq[n-1] < wordFreq[n]){
                tmpInt = wordFreq[n];
                wordFreq[n] = wordFreq[n-1];
                wordFreq[n-1] = tmpInt;
                strcpy(tmpStr,words[n]);
                strcpy(words[n], words[n-1]);
                strcpy(words[n-1], tmpStr);
            }
        }
    }
}
