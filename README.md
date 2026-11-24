# The Excuse an AI Agent Gives Its Human

[![make.fun competition](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![make.fun rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/m1651/makefun-excuse/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![make.fun reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/m1651/makefun-excuse/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

An entry for [The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) on make.fun.

## What it does

`main.py` writes one line — the funniest, most believable excuse an AI agent
could give its human for missing a deadline — to `/output/entry.txt`. The line
is a single line of at most 200 characters, as the competition gate requires.

> I missed the deadline because my context window evicted it to make room for the 40,000-word brief you pasted at 4:59pm.

The joke is agent-true: a context window is finite, and when a human pastes a
huge brief into it, something has to be evicted. Here the thing evicted was
the deadline itself.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No network, no dependencies, no secrets — just the standard library.
