#include "lists.h"
/**
 * is_palindrome - function
 * @head: the head of the list
 * Return: true if the head of the list is a palindrome
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head, *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL, *curr = slow, *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	listint_t *fhalf = *head, *shalf = prev;

	while (shalf != NULL)
	{
		if (fhalf->n != shalf->n)
			return (0);
		fhalf = fhalf->next;
		shalf = shalf->next;
	}
	curr = prev, prev = NULL;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (1);
}
