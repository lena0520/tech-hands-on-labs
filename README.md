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
├── shared/
│ └── client.py # Azure AI Foundry client setup
│
└── azure/
├── ai-103/ # AI-103: Azure AI Apps and Agents Developer
│ ├── README.md
│ ├── episode-01-agent-basics/
│ ├── episode-02-file-search-rag/
│ ├── episode-03-structured-output/
│ └── episode-04-responsible-ai/
├── ai-300/
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


## Adding a new track

1. If it's a new vendor (e.g. AWS, GCP), create a top-level folder for it first
2. Inside the vendor folder, create a folder for the certification/theme
   (e.g. `aws/saa-c03/`)
3. Add a `README.md` describing the series
4. Add one folder per episode (`episode-01-...`, `episode-02-...`)
