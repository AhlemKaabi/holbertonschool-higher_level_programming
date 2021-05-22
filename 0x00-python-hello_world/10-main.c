#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *current;
	listint_t *temp;
	listint_t *reset;
	int i;

	head = NULL;
	for (i = 0; i < 101; i++)
		add_nodeint(&head, i);

	print_listint(head);

	current = head;
	for (i = 0; i < 26; i++)
		current = current->next;
	temp = current;

	current = head;
	for (i = 0; i < 76; i++)
		current = current->next;
	reset = current->next;
	current->next = temp;

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 76; i++)
		current = current->next;
	current->next = reset;

	free_listint(head);

	return (0);
}