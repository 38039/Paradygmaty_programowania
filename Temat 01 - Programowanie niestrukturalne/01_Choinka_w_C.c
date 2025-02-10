// TEMAT   1:  PROGRAMOWANIE NIESTRUKTURALNE
// ZADANIE 1:  CHOINKA W C
//
// WYMAGANIA:
// Maksymalna liczba plików: 1
// Rodzaj pracy: Praca indywidualna
//
// TREŚĆ:
// Napisz w języku C program rysujący "choinki"
// Liczba poziomów powinna być pobierana z klawiatury.
// Choinka o parzystej liczbie poziomów powinna zostać "wyrysowana" gwiazdkami, a o nieparzystej - hashami (#).
// Po wyrysowaniu choinki program ma ponownie pobrać liczbę poziomów i wyrysować nową choinkę.
// Rysowanie choinek ma być powtarzane wielokrotnie aż do wyrysowania choinki o wysokości 7.
//
// UWAGA: Program należy napisać NIESTRUKTURALNIE -
// to znaczy nie wolno używać "struktur sterujących" -
// pętli, else, sekwencji (czyli nie można użyć wyrażeń przecinkowych ani nawiasów { oraz }
// poza rozpoczynającym i kończącym maina - innymi słowy w programie może wystąpić tylko jedna para nawiasów {}).
// Za to można (a nawet trzeba) używać goto.

#include <stdio.h>

int main(void) {
    int levels, actual_level, num_of_stars, iterator;

start_program:
    scanf("%d", &levels);
    iterator = 1;

start_drawing:
    if (iterator > levels) goto next_step;
    actual_level = levels - iterator;

draw_one_space:
    if (actual_level <= 0) goto calculate_stars;
    printf(" ");
    actual_level--;
    goto draw_one_space;

calculate_stars:
    num_of_stars = 2 * iterator - 1;

draw_one_star:
    if (num_of_stars <= 0) goto end_current_line;
    printf(levels % 2 == 0 ? "*" : "#");
    num_of_stars--;
    goto draw_one_star;

end_current_line:
    printf("\n");
    iterator++;
    goto start_drawing;

next_step:
    if (levels == 7) goto kill_program;
    goto start_program;

kill_program:
    return 0;
}