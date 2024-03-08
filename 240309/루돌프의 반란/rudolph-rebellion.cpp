#include <iostream>
#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;
struct set {
    int index;
    int SR, SC, score;

    bool operator<(const set& d) const {
        return index < d.index;
    }
};

int map[51][51];
int visit[51][51]; // 산타가 존재하는 곳
int N, M, P, C, D;
int Rr, Rc;       // 루돌프 위치
vector<set> S; // 산타 위치
int FailSanta = 0;
int dx[8] = { 1, 0, -1, 0, 1, -1, 1, -1 };
int dy[8] = { 0, 1, 0, -1, 1, -1, -1, 1 };
int dx2[4] = { 0, 1, 0, -1 }; //상, 우, 하, 좌
int dy2[4] = { -1, 0, 1, 0 };

pair<bool, int>S_flag[31];

void Interface(int x, int y, int DX, int DY) {
    int X = x; int Y = y;
    if (visit[Y][X] != 0) {
        if (S[visit[Y][X] - 1].SR == 0 && S[visit[Y][X] - 1].SC == 0) return;
        X = X + DX;  Y = Y + DY;
        if (X < 1 || Y < 1 || X > N || Y > N) {
            S[visit[Y - DY][X - DX] - 1].SC = 0; S[visit[Y - DY][X - DX] - 1].SR = 0;
            FailSanta++;
            if (FailSanta == P) return;
            return;
        }
        S[visit[Y - DY][X - DX] - 1].SR += DY;
        S[visit[Y - DY][X - DX] - 1].SC += DX;
        visit[Y][X] = S[visit[Y - DY][X - DX] - 1].index;
        if (visit[Y][X] != 0 && visit[Y][X] != visit[Y - DY][X - DX]) {
            Interface(X, Y, DX, DY);
        }
    }
}

void Start(int m) {
    if (FailSanta == P) return;
    //기절 풀기
    if (m > 1) {
        for (int i = 0; i < S.size(); i++) {
            if (S[i].SC == 0 && S[i].SR == 0) { continue; } // 탈락한 산타
            else {
                S[i].score++;
            }
            if (S_flag[i].first && m >= S_flag[i].second + 2) {
                S_flag[i].first = false;
                S_flag[i].second = 0;
            }

        }
    }
    if (m > M) return;


    int Min = 2501; // 거리 최소
    int Sr = 0; int Sc = 0;
    int Rdx = 0; int Rdy = 0; // 루돌푸 이동 방향

    for (int i = 0; i < S.size(); i++) {
        if (S[i].SC == 0 && S[i].SR == 0) continue; // 탈락한 산타
        int temp = pow((S[i].SR - Rr), 2) + pow((S[i].SC - Rc), 2);
        if (temp <= Min) {
            Min = temp;
        }
    }

    for (int i = 0; i < S.size(); i++) {
        int temp = pow((S[i].SR - Rr), 2) + pow((S[i].SC - Rc), 2);
        if (Min == temp) {
            if (Sr < S[i].SR) {
                Sr = S[i].SR;
                Sc = S[i].SC;
                //Rdx = dx[k]; Rdy = dy[k];
            }
            else if (Sr == S[i].SR) {
                if (Sc < S[i].SC) {
                    Sr = S[i].SR;
                    Sc = S[i].SC;
                    //Rdx = dx[k]; Rdy = dy[k];
                }
            }
        }
    }

    Min = 2501;
    for (int k = 0; k < 8; k++) {
        int X = Rc + dx[k]; int Y = Rr + dy[k];
        int temp = pow((Sr - Y), 2) + pow((Sc - X), 2);
        if (temp < Min) {
            Min = temp;
            Rdx = dx[k]; Rdy = dy[k];
        }
    }

    Rr += Rdy; Rc += Rdx; // 루돌푸 이동

    for (int i = 0; i < S.size(); i++) {
        if (S[i].SC == 0 && S[i].SR == 0) continue; // 탈락한 산타
        if (Rr == S[i].SR && Rc == S[i].SC) { // 루돌푸 -> 산타 충돌
            S[i].score += C;
            int X = S[i].SC + (Rdx * C); int Y = S[i].SR + (Rdy * C);
            if (X < 1 || Y < 1 || X > N || Y > N) { // 탈락
                visit[S[i].SR][S[i].SC] = 0;
                S[i].SC = 0; S[i].SR = 0;
                FailSanta++;
                if (FailSanta == P) return;
            }
            else { // 기절
                
                Interface(X, Y, Rdx, Rdy);
                visit[S[i].SR][S[i].SC] = 0;
                S[i].SC = X; S[i].SR = Y;
                visit[S[i].SR][S[i].SC] = S[i].index;

                S_flag[i].first = true;
                S_flag[i].second = m;
            }
        }
    }

    //============= 산타 이동 ====================

    for (int i = 0; i < S.size(); i++) {
        if (S[i].SC == 0 && S[i].SR == 0) continue;
        if (S_flag[i].first) continue;
        Min = pow((Rr - S[i].SR), 2) + pow((Rc - S[i].SC), 2); // 원래 산타와 루돌푸 거리
        int Sdx = 0; int Sdy = 0;
        for (int k = 0; k < 4; k++) {
            int X = S[i].SC + dx2[k]; int Y = S[i].SR + dy2[k];
            if (visit[Y][X] != 0) continue;
            if (X < 1 || Y < 1 || X > N || Y > N) continue;
            int temp = pow((Rr - Y), 2) + pow((Rc - X), 2);
            if (temp < Min) {
                Min = temp;
                Sdx = dx2[k]; Sdy = dy2[k];
            }
        }
        //산타 이동
        visit[S[i].SR][S[i].SC] = 0;
        S[i].SR += Sdy; S[i].SC += Sdx;
        visit[S[i].SR][S[i].SC] = S[i].index;

        if (Rr == S[i].SR && Rc == S[i].SC) { // 산타 -> 루돌푸 충돌
            S[i].score += D;
            int X = S[i].SC - (Sdx * D); int Y = S[i].SR - (Sdy * D);
            if (X < 1 || Y < 1 || X > N || Y > N) { // 탈락
                visit[S[i].SR][S[i].SC] = 0;
                S[i].SC = 0; S[i].SR = 0;
                FailSanta++;
                if (FailSanta == P) return;
            }
            else { // 기절
                //visit[S[i].SR][S[i].SC] = 0;
                Interface(X, Y, -Sdx, -Sdy);
                visit[S[i].SR][S[i].SC] = 0;
                S[i].SC = X; S[i].SR = Y;
                visit[S[i].SR][S[i].SC] = S[i].index;

                S_flag[i].first = true;
                S_flag[i].second = m;
            }
        }
    }
    Start(m + 1); // 다음 판 시작
}

int main() {
    //freopen("input.txt", "r", stdin);
    cin >> N >> M >> P >> C >> D;
    cin >> Rr >> Rc;

    for (int i = 1; i <= P; i++) {
        int index, SR, SC;
        cin >> index >> SR >> SC;
        visit[SR][SC] = index;
        S.push_back({ index, SR, SC, 0 });
    }
    sort(S.begin(), S.end());
    Start(1);

    for (int i = 0; i < S.size(); i++) {
        cout << S[i].score << " ";
    }

    return 0;
}