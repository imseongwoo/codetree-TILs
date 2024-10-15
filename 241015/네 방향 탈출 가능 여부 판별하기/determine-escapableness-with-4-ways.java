import java.util.*;

public class Main {
    static int n, m;
    static int[][] arr;
    static int[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt();
        m = sc.nextInt();
        arr = new int[n][m];
        visited = new int[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        
        if (bfs()) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
    
    public static boolean bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0});
        visited[0][0] = 1;
        
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m 
                    && visited[nx][ny] == 0 && arr[nx][ny] == 1) {
                    q.add(new int[]{nx, ny});
                    visited[nx][ny] = 1;
                }
            }
        }
        
        return visited[n - 1][m - 1] == 1;
    }
}