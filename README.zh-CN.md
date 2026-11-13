# Daily Astrology｜每日西方占星运势 Skill

一个面向 AI Agent 的每日西方占星 Skill：先用计算引擎获取真实天象和本命盘行运数据，再由模型进行克制、具体、可验证的象征性解读。

**计算交给引擎，解释交给模型；不编造星体位置，不把占星包装成科学预测。**

## 当前版本

v0.1 基础框架：Skill 工作流、解释规范、隐私配置约定、上游计算引擎安装脚本和 JSON 调用桥接。

## 安装

在支持 Agent Skills 的客户端中：

```bash
npx skills add LiliR-is-here/daily-astrology
```

本地开发：

```bash
git clone https://github.com/LiliR-is-here/daily-astrology.git
cd daily-astrology
bash scripts/setup.sh
```

要求 Python 3.10+ 和 Git。计算引擎单独安装在 `.deps/astro`，不复制进本仓库。

## 个人资料

参考 [references/profile.md](references/profile.md) 创建本地 JSON 出生资料。需要出生日期、出生地坐标和 IANA 时区；出生时间未知时请明确标记未知，不要猜测。

个人资料、私人报告不要提交到 Git。仓库已忽略常见 profile 文件和 reports 目录。

## 运行每日行运

```bash
python3 scripts/run_engine.py \
  --profile ~/.config/daily-astrology/profile.json \
  --date 2026-11-13
```

输出是带请求信息的 JSON。Agent 必须检查引擎实际返回的宫制、精度和数据字段；不能默认声称使用 Placidus。若引擎失败或数据不完整，应明确说明，不能凭空补齐。

## 每日解读结构

1. 今日天象：日期、时区、实际计算结果。
2. 今日主线：1–3 个最重要的主题。
3. 现实映射：可能出现在哪些普通生活场景。
4. 潜在张力：可观察的取舍，不做灾难化预测。
5. 一个小行动：低负担、可执行。
6. 一个观察问题：用现实体验验证是否共鸣。

## 设计原则

- 默认西方热带黄道。
- 宫制以计算引擎实际返回值为准；Placidus 未被确认支持时，不得宣称使用 Placidus。
- 行运按相关性、相位紧密度、持续时间和重复主题筛选，不机械罗列。
- 不使用幸运分数、百分比、幸运数字或颜色等虚假精确。
- 不预测疾病、死亡、关系结局、投资收益等高风险结果。
- 占星仅用于反思，不替代医疗、法律、财务或心理健康专业建议。

## 上游项目与许可证

- [aryaminus/astro](https://github.com/aryaminus/astro)：MIT，作为独立安装的计算引擎。
- [wvanderen/astrology-skill](https://github.com/wvanderen/astrology-skill)：MIT，其 retrieval-first 思路作为设计参考；未复制代码和参考资料。

本仓库原创内容采用 MIT，详见 [LICENSE](LICENSE) 与 [NOTICE.md](NOTICE.md)。
