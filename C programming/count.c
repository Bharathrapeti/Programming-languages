#include <stdio.h>
#include <ctype.h>

int main()
{
    char ch;
    int vowels = 0, consonants = 0, digits = 0, spaces = 0;

    printf("Enter a string: ");

    while ((ch = getchar()) != '\n' )
    {
        if (ch == ' ')
            spaces++;
        else if (isdigit(ch))
            digits++;
        else if (isalpha(ch))
        {
            ch = tolower(ch);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                vowels++;
            else
                consonants++;
        }
    }

    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
    printf("Digits: %d\n", digits);
    printf("Spaces: %d\n", spaces);

    return 0;
}