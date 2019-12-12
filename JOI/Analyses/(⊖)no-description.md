# 4.数学 (Mathematics)

## 4.1 算術および幾何 (Arithmetics and Geometry)
  
⊖ ピタゴラスの定理 (Pythagorean theorem)     

## 4.2 離散構造 (Discrete Structures) (DS)   

### DS1. 関数・関係・集合 (Functions, relations, and sets) 

### DS2. 基礎的な論理 (Basic logic)   

⊖ **モーダスポネンス** (単純な論証) (modus ponens), **モーダストレンス** (対偶による証明) (modus tollens)    

### DS3. 証明の技法 (Proof techniques)

⊖ **直接の証明** (direct proofs), 反例・対偶・矛盾による証明 (proofs by: counterexample, contrapo-
sition, contradiction)    
⊖ 数学的帰納法 (mathematical induction)    
⊖ 強帰納法 (strong induction) (完全帰納法ともいう (also known as complete induction))    

### DS4. 数え上げの基礎 (Basics of counting)

⊖ **包除原理** (inclusion-exclusion principle)   
⊖ **鳩ノ巣原理** (pigeonhole principle)   
⊖ **パスカルの恒等式** (Pascal’s identity), **二項定理** (binomial theorem)   
   
### DS5. グラフ・木 (Graphs and trees)
<details>
<summary>なぜか△がはいってた(無視してもいいです)</summary>
△ 木 (Trees) とその基本性質 (and their basic properties), 根付き木 (rooted trees)   
△ 無向グラフ (undirected graphs)   
- 次数 (degree)   
- 道 (path)   
- 閉路 (cycle)
- 連結性 (connectedness)   
- オイラー路・オイラー閉路   
- ハミルトン路・ハミルトン閉路 (Euler/Hamilton path/cycle)   
- 握手 補題 (handshaking lemma))   

△ 有向グラフ (directed graphs)   
- 入次数 (in-degree)   
- 出次数 (out-degree)   
- 有向路・有向閉路 (directed path/cycle)   
- オイラー路・オイラー閉路   
- ハミルトン路・ハミルトン閉路 (Euler/Hamil-ton path/cycle)   

△ 全域木 (spanning trees)   
△ 走査戦略 (traversal strategies)   
△ 辺や頂点がラベル・重さ・色などで「装飾」されたグラフ (‘decorated’ graphs with edge/node
labels, weights, colors)   
△ 多重グラフ (multigraphs), 自己ループを含むグラフ (graphs with self-loops)   
△ 二部グラフ (bipartite graphs)   
</details>

# 5.計算機科学 (Computing Science)   

## 5.1 プログラミングの原理 (Programming Fundamentals)   

### PF1. プログラミング構造の基礎 (Fundamental programming constructs) (for abstract machines)  
 
⊖ **構造化された分割** (structured decomposition)   

### PF2. アルゴリズム・問題解決 (Algorithms and problem-solving)
⊖ **問題解決戦略** (Problem-solving strategies {
- 理解して–計画して–実行して–確認せよ(understand–plan–do–check),
- 関連事項の分離 (separation of concerns),
- 一般化 (generalization), 
- 特殊化(specialization), 
- 場合分け, 
- 逆向きに考える (working backwards), etc.
}    

⊖ **問題解決過程におけるアルゴリズムの役割** (the role of algorithms in the problem-solving process)  
⊖ **アルゴリズム実装の戦略** (implementation strategies for algorithms) (§6 SE1 を参照 (also see §6 SE1))  
⊖ **デバッグ戦略** (debugging strategies) (§6 SE1 を参照 (also see §6 SE3))

### PF3. データ構造の基礎 (Fundamental data structures)

### PF4. 再帰 (Recursion)   

⊖ 分割統治法 (divide-and-conquer strategies)   
⊖ 再帰の実装 (implementation of recursion)   
⊖ 再帰的バックトラック (recursive backtracking)   

## 5.2 アルゴリズム・計算量 (Algorithms and Complexity)

### AL1. アルゴリズム解析の基礎 (Basic algorithmic analysis)

⊖ 計算量上界の漸近解析 (Asymptotic analysis of upper complexity bounds)    
  (できれば非公式に (informally if possible))   
⊖ 大きい O 記法 (Big O notation)   
⊖ 標準的な計算量クラス (Standard complexity classes) (定数 (constant), 対数 (logarithmic), 線形
(linear), O(n log n), 二乗 (quadratic), 三乗 (cubic), 指数 )   
⊖ アルゴリズムにおける時間計算量・空間計算量のトレードオフ (time and space tradeoffs in algorithms)   

### AL2. アルゴリズム的戦略 (Algorithmic strategies)

⊖ 単純なループ設計戦略 (simple loop design strategies)   
⊖ 力ずくのアルゴリズム (brute-force algorithms) (全数探索 (exhaustive search))   
⊖ 貪欲法 (greedy algorithms)   
⊖ 分割統治法 (divide-and-conquer)   
⊖ バックトラック法 (backtracking) (再帰的・非再帰的なもの (recursive and non-recursive)), 分
枝限定法 (branch-and-bound)   
⊖ パターンマッチング，文字列・テキストアルゴリズム (pattern matching and string/text algo-
rithms)   
⊖ 動的計画法 (dynamic programming)   

### AL3a. アルゴリズム (Algorithms)

⊖ 整数に対する単純な数論アルゴリズム (simple number theory algorithms involving integers):
基数変換 (radix conversion), ユークリッドのアルゴリズム (Euclid’s algorithm), 素数判定, エラトステネスの篩 (Sieve of Eratosthenes), 素因数分解 (除法の試行または篩), 効率の良いベキ乗 (efficient exponentiation)   
⊖ 任意精度の単純な整数演算(加法・減法および単純な乗法 (addition, subtraction, simple multiplication))　　

⊖ 単純な配列操作

- (充填 (filling)   
- 移動 (shifting)   
- 回転 (rotating)   
- 反転 (reversal)   
- サイズ変更 (resizing)   
- 最小値・最大値 (minimum/maximum)   
- 接頭部和 (prefixsums)   
- ヒストグラム (histogram)   
- バケットソート (bucket sort))   

⊖ 逐次 (sequential) 処理・探索 (processing/search)，二分探索 (and binary search)   
⊖ 二次ソートアルゴリズム (Quadratic sorting algorithms) (選択 (selection), 挿入 (insertion))   
⊖ ピボットによる配列分割 (Partitioning an array according to a pivot), クイックソート (Quick-sort), クイックセレクト (Quickselect) (k 番目に小さい元の探索 (to find the k-th smallest element))   
⊖ 最悪計算量が O(n log n) となる ソートアルゴリズム (sorting algorithms)   

- ヒープソート (heap sort)
- マージソート (merge sort))   

⊖ 有向木の走査 (traversals of ordered trees) (前順・間順・後順 (pre-, in-, and post-order))   
⊖ グラフの**深さ優先探索・幅優先探索** (Depth- and breadth-first traversals of graphs), 無向グラフの連結成分の決定 (determining connected components of an undirected graph)   
⊖ **最短路アルゴリズム** (shortest-path algorithms) (**ダイクストラ法** (Dijkstra), **ベルマン-フォード法** (Bellman-Ford), **フロイド-ワーシャル法** (Floyd-Warshall))   
⊖ **推移閉包** (transitive closure) (フロイドのアルゴリズム (Floyd’s algorithm))   
⊖ **最小全域木** (minimum spanning tree) (ヤルニーク-プリム法，クラスカル法 (Jarn ́ık-Prim and
Kruskal algorithms))   
⊖ **トポロジカルソート** (topological sort)   
⊖ オイラー路・オイラー閉路(の存在)を判定するアルゴリズム (algorithms to determine the (existence of an) Euler path/cycle)   
### AL3b  データ構造 (Data structures)

⊖ 二分ヒープデータ構造 (binary heap data structure)  
⊖ **二分探索木** (Binary search trees) (バランスの取れていないもの (unbalanced))  
⊖ 抽象データ型との関係 (interaction with abstract data types): 優先度付きキュー (priorityqueues); 順序付き集合・順序無し集合・写像 (ordered and unordered sets and maps)  
⊖ 区間木 (interval trees), フェンウィック木 (and Fenwick trees)  
⊖ **グラフの表現** (representations of graphs) (**隣接リスト** (adjacency lists), **隣接行列** (adjacency matrix))  
⊖ 素集合の表現 (representation of disjoint sets): Union-Find データ構造 (the Union-Find data structure)

### AL7 オートマトン・文法 (Automata and grammars)   
<details><summary>△です。話題のE問題です。</summary>
△ バッカス-ナウア記法による単純な文法の理解 (Understanding a simple grammar in Backus-Naur form)
</details>

### AL8. 高度なアルゴリズム解析 (Advanced algorithmic analysis)
⊖ 組み合わせゲーム理論の基礎 (basics of combinatorial game theory), 勝利・敗北ポジション (winning and losing positions), 最適ゲームのミニマックスアルゴリズム (minimax algorithm for optimal game playing)

### AL10. 幾何アルゴリズム (Geometric algorithms) (2 次元の場合. 整数座標が望ましい (in two dimensions, preferably with integer coordinates))   


⊖ 点の表現 (representing points)   
- ベクトル (vectors)   
- 直線 (lines)   
- 線分 (line segments)   

⊖ 同一直線上の点の判定 (checking for colinear points), 平行・直交ベクトル (parallel/orthogonal
vectors), 時計回りの回転 (clockwise turns)   
⊖ 2 直線の交点 (intersection of two lines)   
⊖ 多角形 (polygons): 面積および重心の計算 (computing area and center of mass)   
⊖ (一般の・凸)多角形がある点を含むことの判定 (checking whether a (general/convex) polygon contains a point)   
⊖ 座標圧縮 (coordinates compression)   
⊖ **凸包計算アルゴリズム** (convex hull finding algorithms)   
⊖ 平面走査法 (sweeping line method)   
