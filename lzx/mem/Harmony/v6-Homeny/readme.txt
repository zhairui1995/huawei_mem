README.md
中文说明文档。介绍 v6 的用途、hdc 采集流程、PowerShell/Bash 用法、参数和常见问题。

mem_analyze-v6.c
核心 C 源码。真正做内存分析的程序：写 /proc/<pid>/clear_refs 清空访问标记，读取 /proc/<pid>/smaps，统计 Referenced/Rss/Pss/Swap，生成 Markdown 报告。

mem_analyze-v6-ohos
用 OpenHarmony native clang 交叉编译出来的鸿蒙设备侧可执行文件。collect_hdc_v6.ps1/sh 会把它推到设备上运行。

collect_hdc_v6.ps1
Windows PowerShell 主入口。负责：编译 mem_analyze-v6.c、通过 hdc 推送到鸿蒙设备、执行 clear_refs、等待操作、采样 smaps、拉回报告。你现在主要用这个。

collect_hdc_v6.sh
Bash 版本入口。功能和 collect_hdc_v6.ps1 对齐，适合 Git Bash、WSL 或类 Unix 环境。
