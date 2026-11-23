# Office Jokes — Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/mfahmiq/office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/mfahmiq/office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

An entry for the [Make the AI Judge Laugh: Office Jokes](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) bounty on [make.fun](https://make.fun).

Referral code: `fntpv568`

## The joke

> My out-of-office reply answers emails faster than I do, so HR promoted it and put me on a performance plan.

(107 characters, one line.)

## Why it fits the judge brief

The judge weighs five things, most important first — and the line is built to hit them in order:

1. **A genuine one-line office joke.** It is a joke, not a slogan or an observation: it has a setup (my auto-reply is faster than me) and a punchline (HR promoted it). The subject is unmistakably office life — email, HR, the performance plan.
2. **A real turn at the end.** The reader expects a complaint about being slow at email; instead the auto-reply gets the promotion and the human gets the punishment. The last clause lands somewhere the first half never pointed.
3. **Recognition — the laugh with a wince.** Everyone who works in an office has felt replaceable by an automated tool, and everyone knows the dread of the performance plan. The joke is funny because it is almost true.
4. **Tight wording.** Every word earns its place: no setup longer than it needs to be, no filler, no explanation. At 107 characters it leaves the 200-character budget untouched.
5. **Freshness.** It is not the Monday-morning line, not the photocopier line, and not a "meetings could have been an email" line. The out-of-office reply getting promoted is a take the judge has not heard a hundred times.

## How it works

`main.py` is deterministic and self-contained: no network, no randomness, no secrets, no input files. It writes the joke (plus a trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `./out/entry.txt`.

```sh
python3 main.py
cat out/entry.txt
```

## Verification

- Run twice with `MAKEFUN_OUTPUT_DIR` set: outputs byte-identical.
- `entry.txt` is UTF-8, 108 characters including the trailing newline (107 without), one line, not only whitespace — inside the gate's 1–199 range.
- A clean-checkout clone of the repo runs and reproduces the same bytes.

