# Processed Things Decisions

This file records processed Things source decisions that do not belong directly in a skill reference.

## Decisions

### Ungerade Header für Homepage

- Things ID(s): `YQiZqUHVqc9WrQzMzRi2TW`
- Source: <https://css-tricks.com/creating-non-rectangular-headers/>
- Decision: `ignored`
- Target: `css-layout-responsive`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Ignored for skill work: old decorative non-rectangular header trend/implementation source; if CSS shapes or masking become relevant, use newer shape/mask/clip-path sources instead of preserving this as a direct reference.

### Claude Code overview - Anthropic

- Things ID(s): `BmogJdzzdNtTyusnTJ1Q8m`
- Source: <https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview?ref=labnotes.org>
- Decision: `secondary`
- Target: `agent-knowledge-workflows`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://code.claude.com/docs?ref=labnotes.org
- Guidance: Secondary for agent-knowledge-workflows: official Claude Code overview is useful background for agentic coding workflow comparison and tool-specific caveats, but it is not design-system material and should not directly shape UI/frontend skills.

### Databases For Front-End Developers: The Rise Of Serverless Databases

- Things ID(s): `WJZHvbNT4mrzUtGYpQi7op`
- Source: <https://www.smashingmagazine.com/2022/08/databases-frontend-developers-rise-serverless-databases/?ck_subscriber_id=1697729046>
- Decision: `ignored`
- Target: `data-architecture`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Ignored after second-pass: older serverless database primer, not relevant enough for current skill structure and no clear reusable rule/reference target.

### Node.js Security Best Practices | Node.js

- Things ID(s): `4t5jMvm6ttKsjk3SWN2AYv`
- Source: <https://nodejs.org/en/docs/guides/security/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23124%3A+FLIP%2C+Lifecycle%2C+Next.js%2C+TypeScript%2C+Vanilla-Extract%2C+LiveView%2C+Remix%2C+GitHub%2C+Race+Conditions%2C+Fontpie%2C+Remotion...%20-%209416696>
- Decision: `ignored`
- Target: `processed-decision`
- URL recheck: 2026-06-13, HTTP 404
- Guidance: Rejected for this archive pass: Node.js security best practices is not motion interaction or current frontend skill material.

### Here’s how I use LLMs to help me write code

- Things ID(s): `2s9CgbhTEusPBnW7aQuvuW`
- Source: <https://simonwillison.net/2025/Mar/11/using-llms-for-code/>
- Decision: `ignored`
- Target: `processed-decision`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Deferred/rejected for design-system work: LLM coding workflow source belongs to agent workflow research, not UI design-system guidance.

### https://developers.openai.com/api/docs/guides/prompt-guidance/

- Things ID(s): `WdF3S4Egk3rDJNUTeiD95N`
- Source: <https://developers.openai.com/api/docs/guides/prompt-guidance/>
- Decision: `ignored`
- Target: `processed-decision`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://developers.openai.com/api/docs/guides/prompt-guidance
- Guidance: Deferred for OpenAI-specific prompting docs; do not fold into UI design-system references.

### https://developers.openai.com/codex/app-server

- Things ID(s): `9aJpJAKmPr21rxGQxKvmBx`
- Source: <https://developers.openai.com/codex/app-server>
- Decision: `ignored`
- Target: `processed-decision`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Deferred for OpenAI/Codex app-server docs; not design-system source material.

### I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5

- Things ID(s): `PGZDquw6VMTgtZmoUv7ChL`
- Source: <https://simonwillison.net/2025/Dec/15/porting-justhtml/?ref=labnotes.org>
- Decision: `ignored`
- Target: `processed-decision`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Deferred for agent/Codex workflow research; not frontend-testing skill material.
