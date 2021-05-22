#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *agent1;
	listint_t *agent2;
	if (list == NULL)
	{
		return (0);
	}
	agent1 = list;
	agent2 = list;
	while(agent1 && agent2 && agent2->next)
	{
		agent1 = agent1->next;
		agent2 = agent2->next->next;
		if (agent1 == agent2)
		{
			return (1);
		}

	}
	return (0);
}