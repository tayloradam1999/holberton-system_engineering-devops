#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wctype.h>
#include <setjmp.h>

/**
 * infinite_while - Infinite while loop
 * Return: 0
 */

int infinite_while(void)
{
while (1)
sleep(1);
return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: 0
 */

int main(void)
{
pid_t zombo;
int x = 0;

for (; x < 5; x++)
{
zombo = fork();
if (zombo == 0)
exit(0);
printf("Zombie process created, PID: %d\n", zombo);
}
infinite_while();
return (0);
}
