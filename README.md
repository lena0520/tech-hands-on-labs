# Tech Hands-on Labs

Companion notebooks and scripts for the "Hands-on" blog series on
https://www.lena-nadir.dev/blog.

This repository is intentionally vendor-agnostic and topic-agnostic:
each cloud vendor / technology gets its own top-level folder, and each
certification or theme within it gets its own subfolder. New tracks can
be added at any level without restructuring existing content.

## Structure

```
tech-hands-on-labs/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── shared/                  # helpers shared across tracks (grouped by vendor)
│   └── client.py            # Azure AI Foundry client setup
│
├── azure/
│   ├── ai-103/               # AI-103: Azure AI Apps and Agents Developer
│   │   ├── README.md
│   │   ├── episode-01-agent-basics/
│   │   ├── episode-02-file-search-rag/
│   │   ├── episode-03-structured-output/
│   │   └── episode-04-responsible-ai/
│   ├── ai-300/               # (future series)
│   └── ai-900-901/           # (future series)
│
├── aws/                      # (future) AWS certification series
│   └── README.md
│
└── gcp/                      # (future) GCP certification series
    └── README.md
```

## Setup

```bash
git clone <this-repo>
cd tech-hands-on-labs
pip install -r requirements.txt
cp .env.example .env   # fill in the values relevant to the track you're using
az login               # only needed for azure/ tracks
```

## Tracks

| Vendor | Track | Status |
|--------|-------|--------|
| Azure | [ai-103](./azure/ai-103) | in progress |
| Azure | ai-300 | not started |
| Azure | ai-900-901 | not started |
| AWS | - | not started |
| GCP | - | not started |

## Adding a new track

1. If it's a new vendor, create a top-level folder (e.g. `aws/`)
2. Inside the vendor folder, create a folder for the certification/theme
   (e.g. `aws/saa-c03/`)
3. Add a `README.md` describing the series
4. Add one folder per episode (`episode-01-...`, `episode-02-...`)
5. If the vendor needs its own client-setup helper, add it under
   `shared/` (e.g. `shared/aws_client.py`) so notebooks stay consistent
