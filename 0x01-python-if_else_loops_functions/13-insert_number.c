#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *aux;
	int node_index;
	/* create the new node */
	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	current = *head;
	if (current  == NULL)
	{
		return (NULL);
	}
	node_index = 0;
	while (current->next != NULL)
	{
		if (current->n > number && node_index == 0)
		{
			/*add the node just befor*/
			aux = current;
			new->next = aux;
			current = new;
			return (new);
		}
		if (current->next->n > number && node_index > 0)
		{
			/*add the node just befor*/
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
		node_index++;
	}
	if (current->n < number && current->next == NULL)
	{
		new = add_nodeint_end(head, number);
		return (new);
	}
	return (*head);
}