#include<stdio.h>
#include<stdlib.h>

typedef struct sturction
{
    int x;
    struct sturction *next;
}NODE;

void insert_at_the_end(NODE **node, int value)
{
    NODE *new_node = malloc(sizeof(struct sturction));

    new_node->x = value;
    new_node->next = NULL;

    NODE *curr = *node;
    while(curr->next != NULL)
    {
        curr = curr->next;
    }
    curr->next = new_node;
}
int main(void)
{
    NODE *node = malloc(sizeof(struct sturction));

    node->x = 0;
    node->next = NULL;
    insert_at_the_end(&node, 5);
    insert_at_the_end(&node, 8);
    insert_at_the_end(&node, 4);
    for(NODE *curr = node; curr; curr = curr->next)
    {
        printf("int: %d\n", curr->x);
    } 
}
