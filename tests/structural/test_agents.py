"""Tests for agent structure."""

from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / "agents"


def _is_agent_file(path: Path) -> bool:
    """An agent .md file starts with YAML frontmatter (---). Plain docs do not."""
    try:
        return path.read_text(encoding="utf-8").startswith("---")
    except OSError:
        return False


def test_agent_count():
    """Total agent count matches expected value (frontmatter-bearing files only)."""
    agent_files = []
    if AGENTS_DIR.is_dir():
        for subdir in AGENTS_DIR.iterdir():
            if subdir.is_dir():
                agent_files.extend(
                    sorted(p for p in subdir.glob("*.md") if _is_agent_file(p))
                )
            elif subdir.suffix == ".md" and subdir.name != "README.md" and _is_agent_file(subdir):
                agent_files.append(subdir)
    # Also check .claude/agents/ for Claude subagents
    claude_agents = Path(__file__).resolve().parent.parent.parent / ".claude" / "agents"
    if claude_agents.is_dir():
        agent_files.extend(
            sorted(p for p in claude_agents.glob("*.md") if _is_agent_file(p))
        )
    assert len(agent_files) == 1, (
        f"Expected 1 agents, found {len(agent_files)}: {[f.name for f in agent_files]}"
    )
