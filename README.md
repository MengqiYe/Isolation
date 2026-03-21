# Isolation Game 🎮

3x2 Isolation 棋盘游戏 - 人工智能博弈项目，实现 Minimax 算法和 Alpha-Beta 剪枝。

## 🎯 项目简介

Isolation 是一个双人零和博弈游戏：
- 在 3x2 棋盘上进行
- 玩家轮流移动，每次移动后当前位置变为不可达
- 无法移动的玩家输掉游戏

## 📂 项目结构

```
Isolation/
├── game_agent.py        # 游戏代理核心实现
├── competition_agent.py # 竞赛代理
├── sample_players.py    # 示例玩家
├── minimax.py           # Minimax 算法实现
├── minimax_helpers.py   # Minimax 辅助函数
├── gamestate.py         # 游戏状态管理
├── tournament.py        # 锦标赛模式
├── agent_test.py        # 代理测试
├── isolation/           # 游戏核心逻辑
├── isoviz/              # 可视化模块
└── tests/               # 单元测试
```

## 🧠 核心算法

### Minimax 算法
```
minimax(state, depth):
    if terminal(state) or depth == 0:
        return evaluation(state)
    if max_player:
        return max(minimax(child) for child in successors)
    else:
        return min(minimax(child) for child in successors)
```

### Alpha-Beta 剪枝
优化搜索效率，减少不必要的节点展开：
- **Alpha**: 最大玩家已找到的最佳值
- **Beta**: 最小玩家已找到的最佳值

### 评估函数
- 可用移动数量
- 位置控制
- 对手移动限制

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/MengqiYe/Isolation.git

# 运行测试
python -m pytest tests/

# 运行锦标赛
python tournament.py

# 测试自定义代理
python agent_test.py
```

## 🎮 游戏规则

1. **初始状态**: 两个玩家位于棋盘两端
2. **移动规则**: 每次可向相邻空格移动（上下左右及对角线）
3. **阻塞规则**: 移动后原位置变为障碍，不可再次进入
4. **胜负判定**: 无法移动的玩家输掉游戏

## 📊 项目来源

Udacity Artificial Intelligence Nanodegree 项目

## 👤 作者

MengqiYe

## 📄 许可证

MIT License
