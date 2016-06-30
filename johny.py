# https://www.codechef.com/problems/JOHNY

def solve(num_songs, songs, index):
    Uncle_Johny = songs[index-1]
    songs = sorted(songs)
    for i in range(num_songs):
        if songs[i] == Uncle_Johny:
            return i+1 

def johny():
    """
    1 <= T <= 1000
    1 <= K <= N <= 100
    1 <= Ai <= 109
    """
    T = int(raw_input())
    for i in range(T):
        num_songs = int(raw_input())
        songs = map(int, raw_input().split())
        index = int(raw_input())
        print solve(num_songs, songs, index)

if __name__ == '__main__':
    johny() 
