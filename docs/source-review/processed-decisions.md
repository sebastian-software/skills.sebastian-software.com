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

