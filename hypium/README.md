# 斗鱼 Hypium 自动化

安装项目环境：

```bash
bash scripts/setup_hypium_env.sh
```

运行首个用户操作序列：

```bash
bash scripts/run_douyu_hypium.sh
```

默认流程：

```text
启动斗鱼 -> 返回搜索页 -> 搜索 pubg -> 进入新直播间
-> 切换视频/聊天 -> 暂停并恢复播放
-> 前后台切换 3 次 -> 关闭斗鱼
```

可调参数：

```bash
DOUYU_BACKGROUND_CYCLES=5 \
DOUYU_ACTION_WAIT=3 \
DOUYU_SEARCH_TERM=pubg \
bash scripts/run_douyu_hypium.sh
```

报告保存在 `hypium/reports/`，运行时数据保存在项目内 `.hypium-home/`。
