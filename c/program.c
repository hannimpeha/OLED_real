//
// Created by Hannah Lee on 2021/01/11.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int number;
    char* layer;
    char* material;
    char* refractive;
    int weight;
    char* measure;
} Owner;

Owner owners[100];

int load(char* filename)
{
    char buffer[200];
    //char token[50];
    Owner* owner;
    int owners_size = 0;
    FILE* file = fopen(filename, "r");

    char *token = strtok(buffer, ",");
    while(token)
    {
        owner = (Owner*)malloc(sizeof(Owner));
        owner->number = atoi(strtok(buffer, ","));
        owner->layer = strtok(NULL, ",");
        owner->material = strtok(NULL, ",");
        owner->refractive = strtok(NULL, ",");
        owner->weight = atoi(strtok(buffer, ","));
        owner->measure = strtok(NULL, ",");
        owners[owners_size++] = *owner;
    }

    fclose(file);
    return owners_size;
}


const char* getfield(char* line, int num)
{
    const char* tok;
    for (tok = strtok(line, ",");
         tok && *tok;
         tok = strtok(NULL, ",\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}

int main()
{
//    int choise, owners_size, index;
//    char* owners_filename = "/Users/hannahlee/HANNIMPEHA/OLED/example/text.csv";
//
//    owners_size = load(owners_filename);
//
//    if(owners_size)
//    {
//        for(index = 0; index < owners_size; index++)
//            printf("%d, %s %s %s %s %d %s\n",
//                   owners[index].number, owners[index].layer,
//                   owners[index].material, owners[index].refractive,
//                   owners[index].refractive, owners[index].weight,
//                   owners[index].measure);
//    }

    FILE* stream = fopen("/Users/hannahlee/HANNIMPEHA/OLED/example/text.csv", "r");

    char line[1024];
    while (fgets(line, 1024, stream))
    {
        char* tmp = strdup(line);
        printf("Field 3 would be %s\n", getfield(tmp, 3));
        //printf(tmp);
        // NOTE strtok clobbers tmp
        free(tmp);
    }
}