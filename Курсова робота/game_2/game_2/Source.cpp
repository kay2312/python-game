#include <cstdlib>
#include <ctime>

extern "C" __declspec(dllexport) int Fire(int a, int b) { return a - b; }
extern "C" __declspec(dllexport) int RandomArsenal(int level) {
    srand(time(0));
    int arsenal, enemy;

    if (level == 1)
        arsenal = rand() % 5 + 3;       //від 3 до 7 (включно)

    if (level == 2)
        arsenal = rand() % 5 + 3;       //від 3 до 7 

    if (level == 3)
        arsenal = rand() % 4 + 5;       //від 5 до 8

    if (level == 4)
        arsenal = rand() % 3 + 6;       //від 6 до 8 

    if (level == 5)
        arsenal = rand() % 4 + 7;       //від 7 до 10 

    if (level == 6)
        arsenal = rand() % 4 + 9;       //від 9 до 12 

    if (level == 7)
        arsenal = rand() % 4 + 10;       //від 10 до 13 

    if (level == 8)
        arsenal = rand() % 5 + 14;       //від 14 до 18

    if (level == 9)
        arsenal = rand() % 6 + 20;      //від 20 до 25

    if (level >= 10)
        arsenal = rand() % 4 + 27;      //від 27 до 30

    return arsenal;
}
extern "C" __declspec(dllexport) int RandomEnemy(int level, int arsenal) {
    int enemy, number;
    if (level == 1)
        enemy = arsenal;

    if(level == 2)
        enemy = arsenal * 5;

    if (level == 3) {
        number = rand() % 3 + 1;
        arsenal = arsenal - number;
        enemy = number;
        enemy += arsenal * 5;
    }

    if (level == 4) {
        while (true) {
            int arsenal_copy = arsenal;
            number = rand() % 3 + 1;
            arsenal_copy = arsenal_copy - number;
            enemy = number;
            number = rand() % 3 + 2;
            arsenal_copy = arsenal_copy - number;
            enemy += number * 5;
            enemy += arsenal_copy * 10;
            if (enemy >= 35 && enemy <=70)
               break;
        }
    }

    if (level == 5) {
        while (true) {
            int arsenal_copy = arsenal;

            number = rand() % 4 + 1;        //від 1 до 4
            arsenal_copy = arsenal_copy - number;
            enemy = number;
            number = rand() % 3 + 1;        //від 1 до 3
            arsenal_copy = arsenal_copy - number;
            enemy += number * 5;
            enemy += arsenal_copy * 10;

            if (enemy >= 45 && enemy<=100)
                break;
        }
    }

    if (level == 6) {
        while (true) {
            int arsenal_copy = arsenal;

            number = rand() % 2 + 1;        //від 1 до 2
            arsenal_copy = arsenal_copy - number;
            enemy = number;

            number = rand() % 3 + 3;        //від 3 до 5
            arsenal_copy = arsenal_copy - number;
            enemy += number * 5;

            number = rand() % 3;            //від 1 до 2
            arsenal_copy = arsenal_copy - number;
            enemy += number * 50;

            enemy += arsenal_copy * 10;

            if (enemy >= 80)
                break;
        }
    }

    if (level == 7) {
       while (true) {
           int arsenal_copy = arsenal;

            number = rand() % 2 + 1;        //від 1 до 2
            arsenal_copy = arsenal_copy - number;
            enemy = number;

            number = rand() % 3 + 4;        //від 4 до 6
            arsenal_copy = arsenal_copy - number;
            enemy += number * 5;

            number = rand() % 3;            //від 0 до 2
            arsenal_copy = arsenal_copy - number;
            enemy += number * 10;

            enemy += arsenal_copy * 50;

            if (enemy >= 100)
               break;
        }
    }

    if (level == 8) {
        while (true) {
            int arsenal_copy = arsenal;

            number = rand() % 4;        //від 0 до 3
            arsenal_copy = arsenal_copy - number;
            enemy = number;

            number = rand() % 3 + 3;        //від 3 до 5
            arsenal_copy = arsenal_copy - number;
            enemy += number * 10;

            number = rand() % 3 + 3;         //від 3 до 5
            arsenal_copy = arsenal_copy - number;
            enemy += number * 50;

            enemy += arsenal_copy * 5;

            if (enemy >= 200 && enemy <=350)
                break;
        }
    }

    if (level == 9) {
        while (true) {
            int arsenal_copy = arsenal;

            number = rand() % 3 + 5;        //від 5 до 7
            arsenal_copy = arsenal_copy - number;
            enemy = number;

            number = rand() % 3 + 4;     //від 4 до 6
            arsenal_copy = arsenal_copy - number;
            enemy += number * 5;

            number = rand() % 3 + 4;         //від 4 до 6
            arsenal_copy = arsenal_copy - number;
            enemy += number * 50;

            enemy += arsenal_copy * 10;

            if (enemy >= 250 && enemy <= 500)
                break;
        }
    }

    if (level >= 10) {
        while (true) {
            int arsenal_copy = arsenal;

            number = rand() % 3 + 5;        //від 5 до 7
            arsenal_copy = arsenal_copy - number;
            enemy = number;

            number = rand() % 3 + 4;     //від 4 до 6
            arsenal_copy = arsenal_copy - number;
            enemy += number * 10;

            number = rand() % 3 + 8;         //від 8 до 10
            arsenal_copy = arsenal_copy - number;
            enemy += number * 50;

            enemy += arsenal_copy * 5;

            if (enemy >= 400 && enemy <= 700)
                break;
        }
    }

    return enemy;

}


extern "C" __declspec(dllexport) int Score(int score, int check, int level, int heart) {

    if (check == 1)
        score -= 10 + 5*(level-1);
    else
        score += 20 + 10*(level-1);

    if (heart == 3)
        score += 5 + 5 * (level - 1);

    return score;
}
