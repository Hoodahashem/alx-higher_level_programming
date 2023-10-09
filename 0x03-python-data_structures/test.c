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
    while(curr->next != NULL)
    {
        curr = curr->next;
    }
    curr->next = new_node;
}

void dalloc(struction **node)
{
    struction *curr = *node;
    while(curr != NULL)
    {
        struction *aux = curr;
        curr = curr->next;
        free(aux);
    }
    *node = NULL;
}

void insert_at_the_beginning(struction **node, int value)
{
    struction *new_node = malloc(sizeof(struction));
    new_node->x = value;
    new_node->next = *node;
    *node = new_node;
}

void insert_after_node(struction *node, int value)
{
    struction *new_node = malloc(sizeof(struction));
    new_node->x = value;
    new_node->next = node->next;
    node->next = new_node;
}

int main(void)
{
    struction *node = NULL;

    insert_at_the_end(&node, 20);
    insert_at_the_end(&node, 30);
    insert_at_the_end(&node, 80);
    insert_at_the_beginning(&node, 10);
    insert_after_node(node,700);
    struction *curr = node;
    while (curr!=NULL) {
        printf("nums in the linked list is: %d\n", curr->x);
        curr = curr->next;
    }

    dalloc(&node);
    return 0;
}
