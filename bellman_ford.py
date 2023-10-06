#include <iostream>
#include <vector>
#include <climits>

using namespace std;

struct Edge {
    int u, v, w;
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    const int inf = INT_MAX;
    vector<int> dist(n + 1, inf);
    dist[1] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (const Edge& edge : edges) {
            int u = edge.u;
            int v = edge.v;
            int w = edge.w;
            if (dist[u] != inf && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    int no_path = 30000;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == inf) {
            dist[i] = no_path;
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;

    return 0;
}
