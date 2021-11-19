import os

PRECOMMIT_REPLACER_TEMPLATE = r"""
- search: /[/\\]{search_term}[/\\]/
  replacement: ./
"""


def rec_split(s):
    rest, tail = os.path.split(s)
    if rest in ("", os.path.sep):
        return (tail,)
    if rest == s:
        return (rest,)
    return rec_split(rest) + (tail,)


if __name__ == "__main__":

    git_repo = os.path.dirname(__file__)
    repo_split = rec_split(git_repo) + ("benchmarks",)
    search_term = r"[/\\]".join(repo_split)
    with open(".pre-commit-search-and-replace.yaml", "wt") as f:
        f.write(
            PRECOMMIT_REPLACER_TEMPLATE.format(
                search_term=search_term,
                pathsep=os.path.sep,
            )
        )
