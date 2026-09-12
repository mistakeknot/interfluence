# hooks

No hooks are registered. `hooks.json` declares an empty map on purpose.

## Why the PostToolUse:Edit hook is off

interfluence is deprecated in favour of [intervox](https://github.com/mistakeknot/intervox) (by way of the interim intervoice). `learn-from-edits.sh` logged edit diffs to `.interfluence/learnings-raw.log` for voice-profile learning; intervox does the same job against its own store. Leaving both registered double-logs every edit for anyone who still has both plugins installed, so this one stays disabled.

The script is kept in the tree for reference and for anyone reconstructing the old pipeline from `.interfluence/` data.

## Why the note is here and not in hooks.json

It used to live in `hooks.json` under `_deprecated` and `_original_hooks` keys. JSON has no comments, and Claude Code validates plugin manifests against a closed schema, so both keys were reported on every session start:

```
interfluence: hooks.json: unknown keys "_deprecated", "_original_hooks" ignored
```

The registration those keys preserved was:

```json
{
  "PostToolUse": [
    {
      "matcher": "Edit",
      "hooks": [
        {
          "type": "command",
          "command": "${CLAUDE_PLUGIN_ROOT}/hooks/learn-from-edits.sh",
          "timeout": 5
        }
      ]
    }
  ]
}
```
