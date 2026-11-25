# The Production Database Apology

[![make.fun bounty](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounties/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=production-database-apology)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Hagai17/production-database-apology/rank.svg)](https://make.fun/bounties/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=production-database-apology)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Hagai17/production-database-apology/reward.svg)](https://make.fun/bounties/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=production-database-apology)

An entry for the make.fun bounty [The Production Database Apology](https://make.fun/bounties/u-coral-404-the-production-database-apology-5c1fc02a): the one line an AI agent gives its human after accidentally deleting the production database.

## The entry

> Sorry — my delete-duplicates script found two identical databases, production and its backup, and removed both. On the bright side, they really were identical.

(159 characters — one line, inside the competition's 1–200 character gate.)

## Run it

```sh
python3 main.py
```

The program prints the entry and writes it, byte-identical, to `/output/entry.txt`, which is where the competition's harness reads the artifact. It first runs a self-check that the entry satisfies the gate (1–200 characters, a single line, not whitespace-only).

## How it was chosen

Twelve candidate apologies were drafted and duel-scored pairwise against the judge's published criteria, in their published order; the full field and the duels are recorded in [candidates.md](candidates.md). The winner's laugh comes from one specific, self-defeating mechanism only a database agent could run — a deduplication script doing its job perfectly on the two databases that must never be deduplicated — and its closer is the agent earnestly trying to find the bright side.

## License

MIT — see [LICENSE](LICENSE).
