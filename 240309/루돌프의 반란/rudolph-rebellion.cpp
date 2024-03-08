#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>

int dy[8] = { 0,0,1,-1,1,1,-1,-1 };
int dx[8] = { 1,-1,0,0,1,-1,1,-1 };

int sdy[4] = {-1,0,1,0};
int sdx[4] = {0,1,0,-1};


using namespace std;

struct santa {
    int num;
    int y;
    int x;
    int state;
    int score;
};
vector<santa> santas;

bool cmp(santa a, santa b)
{
    return a.num < b.num;
}

int score[31];

int map_[50][50];
int N, M, P, C, D;
int sy, sx;

//move((mindir + 2) % 4, ry, rx, santas[i].num);
                    

void move(int dir, int y, int x,int sannum,int type) //산타 재귀로 움직이기
{
   
    int temp = sannum;
    int ny, nx;
    if (type == 1)
    {
         ny = y + sdy[dir];
         nx = x + sdx[dir];
    }
    else
    {
         ny = y + dy[dir];
         nx = x + dx[dir];
    }

    

    if (ny<0 || nx<0 || nx>N - 1 || ny>N - 1) //장외
    {
        
        for (int i = 0; i < santas.size(); i++)
        {
            if (santas[i].num == map_[y][x])
            {
                score[santas[i].num] = santas[i].score;
                santas.erase(santas.begin() + i);
            }
        }
    }
    else
    {
        if (map_[ny][nx] > 0) //상호작용 일어날경우
        {
            move(dir, ny, nx, map_[y][x],type);
        }
        else //상호작용 안일어날경우
        {
            map_[ny][nx] = map_[y][x];
        }
    }

    for (int i = 0; i < santas.size(); i++)
    {
        if (santas[i].num == map_[y][x])
        {
            santas[i].y = ny;
            santas[i].x = nx;
        }
    }

    map_[y][x] = sannum;

}


int main()
{
    cin >> N >> M >> P >> C >> D;

    cin >> sy >> sx;


    sy--;
    sx--;
    int ssy = sy;
    int ssx = sx;
    map_[sy][sx] = -1;

    int num, y, x;
    for (int i = 0; i < P; i++)
    {
        scanf("%d %d %d", &num, &y, &x);
        y--;
        x--;
        santas.push_back({ num,y,x });
        map_[y][x] = num;
    }

    sort(santas.begin(), santas.end(), cmp);

    //반복 시작 //santas size가 0이거나 m번 반복하면 종료

    for (int qwe = 0; qwe < M; qwe++)
    {
        if (santas.size() == 0) break;
        for (int i = 0; i < santas.size(); i++)
        {
            if (santas[i].state > 0) santas[i].state--;
        }




        //루돌프 최소 거리 찾기
        int mindis = 987654321;
        santa minsanta;
        int tempdis;
        for (int i = 0; i < santas.size(); i++)
        {
            tempdis = (sx - santas[i].x) * (sx - santas[i].x) + (sy - santas[i].y) * (sy - santas[i].y);
            if (mindis > tempdis)
            {
                mindis = tempdis;
                minsanta = santas[i];
            }
            else if (mindis == tempdis)
            {

                if (santas[i].y > minsanta.y)
                {
                    mindis = tempdis;
                    minsanta = santas[i];
                }
                else if (santas[i].y == minsanta.y)
                {
                    if (santas[i].x > minsanta.x)
                    {
                        mindis = tempdis;
                        minsanta = santas[i];
                    }
                }
            }
        }
        printf("\n");
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                printf("%d ", map_[i][j]);
            }
            printf("\n");
        }
        
        //루돌프 이동

        map_[sy][sx] = 0;
        
        mindis = 987654321;
        int mindir;
        for (int i = 0; i < 8; i++)
        {

            int ny = sy + dy[i];
            int nx = sx + dx[i];
            if (ny<0 || nx<0 || nx>N - 1 || ny>N - 1) continue;

            tempdis = (nx - minsanta.x) * (nx - minsanta.x) + (ny - minsanta.y) * (ny - minsanta.y);
            if (mindis > tempdis)
            {
                mindis = tempdis;
                mindir = i;
            }

        }
        sy = sy + dy[mindir];
        sx = sx + dx[mindir];

        //cout << mindir << sy << sx << endl;
        int ry;
        int rx;
        int sannum;
        if (map_[sy][sx] > 0) // 루돌프가 산타에 충돌
        {

            sannum = map_[sy][sx];
            ry = sy + dy[mindir] * C;
            rx = sx + dx[mindir] * C;

            for (int i = 0; i < santas.size(); i++)
            {
                if (santas[i].num == sannum)
                {
                    santas[i].score += C;
                    santas[i].state = 2;
                }
            }

            if (ry<0 || rx<0 || rx>N - 1 || ry>N - 1) //장외
            {
                //sannum-1지우기

                for (int i = 0; i < santas.size(); i++)
                {
                    if (santas[i].num == sannum) {
                        score[santas[i].num] = santas[i].score;
                        santas.erase(santas.begin() + i);
                    }

                }

            }
            else
            {
                for (int i = 0; i < santas.size(); i++)
                {
                    if (santas[i].num == sannum)
                    {
                        santas[i].y = ry;
                        santas[i].x = rx;
                    }
                }
                if (map_[ry][rx] > 0) //상호작용 일어날경우
                {
                    
                    move(mindir, ry, rx, sannum,0);
                }
                else //상호작용 안일어날경우
                {
                    
                    map_[ry][rx] = sannum;
                }
            }
        }
        map_[sy][sx] = -1;
        /*
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                printf("%d ", map_[i][j]);
            }
            printf("\n");
        }

        for (int i = 0; i < santas.size(); i++)
        {
            printf("%d %d", santas[i].num, santas[i].state);
        }*/

        //map_[sy][sx] == 1;

        //cout << sy << sx << endl;
        //산타가 루돌프에 가기 시작

        for (int i = 0; i < santas.size(); i++)
        {
            mindis = 987654321;

            if (santas[i].state > 0) continue;

            for (int j = 0; j < 4; j++)
            {
                int ny = santas[i].y + sdy[j];
                int nx = santas[i].x + sdx[j];

                if (ny<0 || nx<0 || nx>N - 1 || ny>N - 1) continue;

                if (map_[ny][nx] > 0) continue;
                int nowdis= (santas[i].x - sx) * (santas[i].x - sx) + (santas[i].y - sy) * (santas[i].y - sy);
                tempdis = (nx - sx) * (nx - sx) + (ny - sy) * (ny - sy);

                if (nowdis < tempdis) continue;

                if (mindis > tempdis)
                {
                    mindis = tempdis;
                    mindir = j;
                }
            }
            /*
            printf("\n");
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    printf("%d ", map_[i][j]);
                }
                printf("\n");
            }
            printf("\n");
            */
            if (mindis == 987654321) continue;
            else if (sy == santas[i].y + sdy[mindir] && sx == santas[i].x + sdx[mindir]) //루돌프 만날경우
            {
                

                ry = sy + sdy[(mindir + 2) % 4] * D;
                rx = sx + sdx[(mindir + 2) % 4] * D;
                santas[i].state = 2;
                santas[i].score += D;
                map_[santas[i].y][santas[i].x] = 0;

                if (ry<0 || rx<0 || rx>N - 1 || ry>N - 1) //장외
                {
                    //sannum-1지우기

                    score[santas[i].num] = santas[i].score;
                    santas.erase(santas.begin() + i);
                    i--;
                }
                else
                {

                    if (map_[ry][rx] > 0) //상호작용 일어날경우
                    {
                        santas[i].y = ry;
                        santas[i].x = rx;
                        

                        move((mindir + 2) % 4, ry, rx, santas[i].num,1);
                    }
                    else //상호작용 안일어날경우
                    {

                        santas[i].y = ry;
                        santas[i].x = rx;
                        map_[ry][rx] = santas[i].num;
                    }
                }
            }
            else //루돌프 안만날경우
            {

                map_[santas[i].y][santas[i].x] = 0;
                santas[i].y = santas[i].y + sdy[mindir];
                santas[i].x = santas[i].x + sdx[mindir];
                map_[santas[i].y][santas[i].x] = santas[i].num;


            }

        }
        
        printf("\n");
        printf("final");
        printf("\n");
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                printf("%d ", map_[i][j]);
            }
            printf("\n");
        }
        
        for (int i = 0; i < santas.size(); i++)
        {
            santas[i].score++;
            printf("%d %d %d %d\n", santas[i].num, santas[i].y, santas[i].x, santas[i].score);

        }
        
    }

    for (int i = 0; i < santas.size(); i++)
    {
        score[santas[i].num] = santas[i].score;
    }
    //printf("\n");
    for (int i = 1; i <= P; i++)
    {
        cout << score[i] << " ";
    }

}