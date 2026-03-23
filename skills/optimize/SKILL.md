---
name: optimize
description: "Optimize a voice profile for token efficiency — deduplicate rules, cut meta-commentary, convert atmosphere to directives, trim examples. Target 20%+ reduction."
---

# Voice Profile Optimization

Reduce token cost of voice profiles while preserving all constraints. Run after `/interfluence analyze` or on any existing profile.

**Announce:** "Optimizing voice profile for token efficiency."

## Prerequisites

Load the profile via MCP:
1. `profile_list(projectDir)` to discover available voices
2. `profile_get(projectDir)` for the base profile
3. `profile_get(projectDir, voice)` for each delta

If no profile exists, tell the user to run `/interfluence analyze` first.

## Step 1: Measure Baseline

Count the approximate token length of each profile (base + deltas). Report:
```
Base profile: ~X tokens (Y lines)
Delta "blog": ~X tokens (Y lines)
Total: ~X tokens
```

## Step 2: Deduplicate Rules

Scan all H2 sections for semantically equivalent constraints. Common duplications:

- Same avoidance in both "Vocabulary & Diction" and "Anti-Patterns"
- Same pattern described in "Sentence Structure" and "Structure Patterns"
- Same directive in base and a delta (delta should only contain differences)

For each duplicate found, keep the most specific version in the most appropriate section. Remove the other.

## Step 3: Cut Meta-Commentary

Remove sentences that describe the profile's own design rather than instructing the model:

- "The briefing voice inherits this but uses it structurally rather than lyrically"
- "This section captures the author's relationship with..."
- "Based on the corpus analysis, we observe that..."

These describe *how the profile was made*, not *what the voice sounds like*. Delete them.

## Step 4: Convert Atmosphere to Directives

Rewrite evocative but non-actionable prose into Do/Don't form:

**Before:** "Cultural References: Draws from a rich well of literary fiction, particularly Banks and Le Guin, creating an atmosphere of thoughtful science-fiction discourse."

**After:** "Cultural References: Reference Banks, Le Guin, and literary SF when illustrating points. Don't reference pop culture, Marvel, or mainstream tech influencers."

## Step 5: Trim Examples

Where both a long corpus quote AND a Do/Don't pair demonstrate the same pattern:
- Keep the Do/Don't pair (more token-efficient)
- Remove the long quote
- Preserve at least one corpus quote per section for authenticity

## Step 6: Merge Overlapping Sections

If two sections have heavy overlap after deduplication:
- **Anti-Patterns + AI-Tells** → merge into "Banned Patterns"
- Only merge if >50% content overlaps; otherwise keep separate

## Step 7: Verify Completeness

Before saving, verify:
- [ ] All 7 required H2 sections present (Overview, Sentence Structure, Vocabulary & Diction, Tone & Voice, Structure Patterns, Cultural References, Anti-Patterns/Banned Patterns)
- [ ] Every directive is actionable (do X / don't do Y)
- [ ] At least one corpus quote per section preserved
- [ ] No constraint was removed — only consolidated or reworded

## Step 8: Save and Report

Save optimized profiles via `profile_save`. Report:

```
Optimization complete:
- Base: X tokens → Y tokens (Z% reduction)
- Delta "blog": X → Y (Z%)
- Total: X → Y (Z%)

Changes:
- Deduplicated N rules across sections
- Cut N meta-commentary sentences
- Converted N atmospheric descriptions to directives
- Trimmed N redundant corpus quotes
- Merged N overlapping sections
```

If reduction is <10%, note that the profile was already well-optimized.
