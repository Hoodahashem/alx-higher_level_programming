#include <stdio.h>
#include <stdlib.h>
typedef struct struction
{
    int x;
    struct struction *next;
}struction;

void insert_at_the_end(struction **node, int value)
{
    struction *new_node = malloc(sizeof(struction));
    new_node->x = value;
    new_node->next = NULL;
    if (*node == NULL)
    {
        *node = new_node;
        return;
    }

    struction *curr = *node;
    while(curr->next)
    {
        curr = curr->next;
    }
    curr->next = new_node;
}
int main(void)
{
    struction *node = NULL;

    insert_at_the_end(&node, 3);
    insert_at_the_end(&node, 5);
    insert_at_the_end(&node, 8);

    for(struction *curr = node; curr != NULL; curr = curr->next) {
        printf("then num in the node is: %d\n", curr->x);
    }
}
