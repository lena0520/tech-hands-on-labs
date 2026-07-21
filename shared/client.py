"""Shared helper for creating an authenticated AIProjectClient + OpenAI client
for Azure AI Foundry tracks (azure/ai-103, azure/ai-300, ...).

Usage:
    from shared.client import get_clients
    project, openai = get_clients()
"""
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


def get_clients():
    endpoint = os.environ["PROJECT_ENDPOINT"]
    project = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )
    openai = project.get_openai_client()
    return project, openai
