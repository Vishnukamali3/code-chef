#include <stdio.h>
int freekick(int x, int y)
{
    scanf("%d %d",&x,&y);
    if(x>y)
    {
        printf("FREEKICK");
    }
    else
    {
        printf("PENALTY");
    }
}

int main() 
{
    int x,y;
    scanf("%d %d",&x,&y);
	// your code goes here
    freekick(x,y);
}

